# Certbot Lambda

[![CodeQL](https://github.com/KiraLT/certbot-lambda/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/KiraLT/certbot-lambda/actions/workflows/codeql-analysis.yml)
[![codecov](https://codecov.io/gh/KiraLT/certbot-lambda/branch/main/graph/badge.svg?token=E599EPAOPM)](https://codecov.io/gh/KiraLT/certbot-lambda)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/relekang/python-semantic-release)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Running Certbot on AWS Lambda and upload certs to AWS Secrets Manager.

Inspired by [kingsoftgames/certbot-lambda](https://github.com/kingsoftgames/certbot-lambda) and [Deploying EFF's Certbot in AWS Lambda](https://arkadiyt.com/2018/01/26/deploying-effs-certbot-in-aws-lambda/).


## Features

- Supports wildcard certificates (Let's Encrypt ACME v2).
- Uploads certificates to [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).
- Runs on [AWS Lambda](https://aws.amazon.com/lambda/).
- Supports automatic rotation.
- Supports 14 [DNS providers](https://eff-certbot.readthedocs.io/en/stable/using.html#dns-plugins).

## Deployment

### AWS Lambda

Download latest version of `certbot-lambda.zip` from [releases](https://github.com/KiraLT/certbot-lambda/releases).

1. Create new lambda in AWS Dashboard with `Python 3.9` runtime.
1. Upload `certbot-lambda.zip` at `Code` > `Code source` > `Upload from` > `.zip file`.
1. Update handler to `lambdex_handler.handler` at `Code` > `Runtime settings` > `Handler`.
1. Create new `Execution role` at `Configuration` > `Execution role` > `Edit` > `Create a new role from AWS policy templates` with name `lambda-certbot`.
1. Go to created role by clicking on the name and `Attach policies`:
    * `SecretsManagerReadWrite`
    * `AmazonRoute53FullAccess`
1. Increase execution timeout in `Configuration` > `General configuration` to 10 minutes and memory limit to 150Mb.
1. Add ENV variables at `Configuration` > `Environment variables` (check bellow for required ENV variables).
1. Run lambda manually one time to create a secret by going to `Test` and executing `hello-wold` template.

#### Automatic rotation

AWS secret can run created lambda periodically to generate new certs, for example, every month. 

For that to work, update lambda and add new `Resource-based policy` at `Configuration` > `Permissions` -> `Add permissions`:
    * **AWS Service**: `Secrets Manager`
    * **Statement ID**: `SecretsManagerAccess`
    * **Principal**: `secretsmanager.amazonaws.com`
    * **Action**: `lambda:InvokeFunction`

Then go to AWS Secrets dashboard and create a rotation rule for created secrets - it should execute created lambda.

## Environment variables

| Name | Description | Default/required |
|---|---|---|
| CERTBOT_EMAILS | Email used for registration and recovery contact. Use comma to register multiple emails, eg: `u1@example.com,u2@example.com`. | **required** |
| CERTBOT_DOMAINS | One or more domains that require certs generation. | **required** |
| CERTBOT_DNS_PLUGIN | DNS provider plugin name for acme challenge. E.g. `dns-cloudflare`, find plugin list [here](https://eff-certbot.readthedocs.io/en/stable/using.html#dns-plugins). | **required** |
| CERTBOT_CREDENTIALS | Credentials file content depending on `CERTBOT_DNS_PLUGIN`. E. g. `{\n"type": "service_account",\n...}` for `dns-google` plugin. | **required** except for [route53](https://certbot-dns-route53.readthedocs.io/en/stable/#credentials) |
| CERTBOT_SERVER | Letsencrypt API url. | `https://acme-v02.api.letsencrypt.org/directory` |
| CERTBOT_DIR | Temporary certbot directory where logs and generated certs will be stored. | `/tmp/certbot` |
| CERTBOT_PREFERRED_CHAIN | Force to use specified cert chain, e.g. `ISRG Root X1` | |
| AWS_SECRET_NAME | AWS secret name template, {domain} will be replaced with domain name. | `certbot-{domain}` |
| AWS_SECRET_DESCRIPTION | AWS secret name description text. | `Auto generated SSL certificate by lambda-certbot` |
| CERTBOT_PROPAGATION_SECONDS | The number of seconds to wait for DNS to propagate before asking the ACME server to verify the DNS record. | Depends on dns plugin |
| CERTBOT_EXTRA_ARGS | Additional arguments that will be passed to [certbot](https://eff-certbot.readthedocs.io/en/stable/using.html#certbot-command-line-options). | |

Each DNS challenge plugin requires different configuration, check [documentation](https://eff-certbot.readthedocs.io/en/stable/using.html#dns-plugins) for more information.

## Letsencrypt

### 2021 September 30th Root CA X3 root certificate expired

Due to a bug in some versions of [OpenSSL (1.0.0 - 1.0.2)](https://community.letsencrypt.org/t/openssl-client-compatibility-changes-for-let-s-encrypt-certificates/143816), [GnuTLS (< 3.6.14)](https://lists.gnupg.org/pipermail/gnutls-help/2020-June/004648.html), [LibreSSL (< 3.2.0)](https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-3.2.0-relnotes.txt) and perhaps other TLS/SSL libraries as well, Let's Encrypt's certificates will be seen as invalid as a result of this invalid DST Root CA X3 certificate still being included.

To solve this issue, you can disable `Root CA X3` certificate that is still included due to legacy support (mostly Android) by providing `CERTBOT_PREFERRED_CHAIN=ISRG Root X1` environment variable.

_Source: [Laravel: Let's Encrypt Compatibility Changes](https://blog.laravel.com/forge-lets-encrypt-compatibility-changes)_

## Examples

### AWS Lambda to AWS Secrets using Route 53

#### Configuration

```
CERTBOT_EMAILS=name@example.com
CERTBOT_DOMAINS=*.example.com,example.com
CERTBOT_DNS_PLUGIN=dns-route53
```

| In the [lambda](https://aws.amazon.com/lambda/) aws credentials are provided by default. Make sure lambda role has access to AWS Secrets and Route 53. Or you can [configure them manually](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html).

### AWS Lambda to AWS Secrets using Cloudflare

#### Configuration

```
CERTBOT_EMAILS=name@example.com
CERTBOT_DOMAINS=*.example.com,example.com
CERTBOT_DNS_PLUGIN=dns-cloudflare
CERTBOT_CREDENTIALS="dns_cloudflare_api_token = 0123456789abcdef0123456789abcdef01234567"
```

| In the [lambda](https://aws.amazon.com/lambda/) aws credentials are provided by default. Make sure lambda role has access to AWS Secrets. Or you can [configure them manually](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html).