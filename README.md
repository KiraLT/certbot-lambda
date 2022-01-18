# certbot-lambda

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Deployment

Download latest version of `certbot-lambda.zip` from [releases](https://github.com/KiraLT/certbot-lambda/releases).

### Creating lambda

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

### Automatic rotation

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
| CERTBOT_EMAILS | Email used for registration and recovery contact. Use comma to register multiple emails, ex: u1@example.com,u2@example.com. | **required** |
| CERTBOT_DOMAINS | One or more domains that require certs generation. | **required** |
| CERTBOT_DNS_PLUGIN | DNS provider plugin name for acme challenge. E.g. `dns-cloudflare`, find plugin list [here](https://eff-certbot.readthedocs.io/en/stable/using.html#dns-plugins). | **required** |
| CERTBOT_SERVER | Letsencrypt API url. | `https://acme-v02.api.letsencrypt.org/directory` |
| CERTBOT_DIR | Temporary certbot directory where logs and generated certs will be stored. | `/tmp/certbot` |
| AWS_SECRET_NAME | AWS secret name template, {domain} will be replaced with domain name. | `certbot-{domain}` |

Each DNS challenge plugin requires different configuration, check [documentation](https://eff-certbot.readthedocs.io/en/stable/using.html#dns-plugins) for more information.
