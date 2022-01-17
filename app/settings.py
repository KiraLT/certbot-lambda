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


def read_env(name: str, required: bool = False, multi=False, default=None):
    value = getenv(name)

    if required and not name:
        raise ValueError(f"Environment variable {name} is required")

    if multi:
        if value:
            return [v.strip() for v in value.split(",")]
        return default if default else []

    if value:
        return value.strip()

    return default if default else value


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
)
