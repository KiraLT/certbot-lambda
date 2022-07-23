from pathlib import Path
from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv


@dataclass
class Settings:
    CERTBOT_EMAILS: list[str]
    CERTBOT_DOMAINS: list[str]
    CERTBOT_DNS_PLUGIN: str
    CERTBOT_SERVER: str
    CERTBOT_DIR: Path
    AWS_SECRET_NAME: str
    AWS_DEFAULT_REGION: str
    AWS_SECRET_DESCRIPTION: str
    CERTBOT_PREFERRED_CHAIN: str = None


def read_env(name: str, required: bool = False, multi=False, default=None, delimiter=","):
    value = getenv(name)

    if required and not name:
        raise ValueError(f"Environment variable {name} is required")

    if multi:
        if value:
            return [v.strip() for v in value.split(delimiter)]
        return default if default is not None else []

    if value:
        return value.strip()

    return default if default is not None else value


load_dotenv()

settings = Settings(
    CERTBOT_EMAILS=read_env("CERTBOT_EMAILS", required=True, multi=True),
    CERTBOT_DOMAINS=read_env("CERTBOT_DOMAINS", required=True, multi=True),
    CERTBOT_DNS_PLUGIN=read_env("CERTBOT_DNS_PLUGIN", required=True),
    CERTBOT_SERVER=read_env(
        "CERTBOT_SERVER", default="https://acme-v02.api.letsencrypt.org/directory"
    ),
    CERTBOT_DIR=Path(read_env("CERTBOT_DIR", default="/tmp/certbot")).resolve(),
    AWS_DEFAULT_REGION=read_env("AWS_DEFAULT_REGION", required=True),
    AWS_SECRET_NAME=read_env("AWS_SECRET_NAME", default="certbot-{domain}"),
    AWS_SECRET_DESCRIPTION=read_env("AWS_SECRET_DESCRIPTION", default="Auto generated SSL certificate by lambda-certbot"),
    CERTBOT_PREFERRED_CHAIN=read_env("CERTBOT_PREFERRED_CHAIN"),
    CERTBOT_EXTRA_ARGS=read_env("CERTBOT_EXTRA_ARGS", multi=True, delimiter=" "),
    CERTBOT_CREDENTIALS=read_env("CERTBOT_CREDENTIALS"),
    CERTBOT_PROPAGATION_SECONDS=read_env("CERTBOT_PROPAGATION_SECONDS")
)
