from boto3 import client
import json
from slugify import slugify

from .certbot import Cert


def upload_certs_as_secrets(
    certs: list[Cert], name: str, description: str = ""
) -> None:
    for cert in certs:
        name = name.format(domain=slugify(cert.domain))

        create_or_update_secret(
            name=name,
            data={f.name: f.content for f in cert.files},
            description=description,
        )


def create_or_update_secret(
    name: str,
    data: dict[str, str],
    description: str = "",
):
    secretsmanager = client("secretsmanager")

    try:
        secretsmanager.create_secret(
            Name=name,
            Description=description,
            SecretString=json.dumps(data),
        )
        print(f"Creating a new secret {name}")
    except secretsmanager.exceptions.ResourceExistsException:
        print(f"Updating secret {name} with new certs")

        secretsmanager.put_secret_value(SecretId=name, SecretString=json.dumps(data))
