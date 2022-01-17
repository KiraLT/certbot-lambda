# certbot-lambda

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### Environment variables

| Name | Description | Default value | Required |
|---|---|---|---|
| CERTBOT_EMAILS | Email used for registration and recovery contact. Use comma to register multiple emails, ex: u1@example.com,u2@example.com. |  | * |
| CERTBOT_DOMAINS | One or more domains that require certs generation. |  | * |
| CERTBOT_DNS_PLUGIN | DNS provider plugin name for acme challenge. E.g. `dns-cloudflare`, find plugin list [here](https://eff-certbot.readthedocs.io/en/stable/using.html#dns-plugins). |  | * |
| CERTBOT_SERVER | Letsencrypt API url. | https://acme-v02.api.letsencrypt.org/directory |  |
| CERTBOT_DIR | Temporary certbot directory where logs and generated certs will be stored. | /tmp/certbot |  |
| AWS_SECRET_NAME | AWS secret name template, {domain} will be replaced with domain name. | certbot- {domain} |  |

Each DNS challenge plugin requires different configuration, check [documentation](https://eff-certbot.readthedocs.io/en/stable/using.html#dns-plugins) for more information.

