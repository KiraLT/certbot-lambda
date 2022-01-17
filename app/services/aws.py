from boto3 import client

from .certbot import Cert

secretsmanager = client('secretsmanager')


def list_secret_names() -> list[str]:
    return {
        v['Name']
        for v in client.list_secrets()['SecretList']
    }


def upload_certs_as_secrets(
    certs: list[Cert],
    name: str,
    secret_names: list[str] = None
) -> None:
    for cert in certs:
        name = name.format(domain=cert.domain)

        create_or_update_secret(
            name=name,
            data=json.dumps({
                f.name: f.content
                for f in cert.files
            }),
            secret_names=available_secrets
        )


def create_or_update_secret(
    name: str,
    data: dict[str, str],
    secret_names: list[str] = None
):
    secret_names = secret_names if secret_names is not None else list_secret_names()

    if name in secret_names:
        print(f'Updating secret {name} with new certs')

        secretsmanager.put_secret_value(
            SecretId=name,
            SecretString=json.dumps(data)
        )
    else:
        print(f'Creating a new secret {name}')

        secretsmanager.create_secret(
            Name=name,
            Description=f'Auto generated SSL certificate by certbot',
            SecretString=json.dumps(data)
        )
