from unittest.mock import patch, MagicMock
import os
from tempfile import TemporaryDirectory
from pathlib import Path
import json

from app.handler import handler

secrets = {
    "fullchain.pem": "a" * 60,
    "chain.pem": "a" * 60,
    "privkey.pem": "a" * 60,
    "cert.pem": "a" * 60,
}

@patch("app.services.aws.client")
@patch("app.services.certbot.main.main")
def test_app(certbot, client):
    client.return_value.list_secrets.return_value = {"SecretList": []}

    with TemporaryDirectory() as tmpdir:
        path = Path(tmpdir).resolve()

        def certbot_side_effect(args: list[str]):
            for name, content in secrets.items():
                subpath = path.joinpath('live/domain.com', name)
                subpath.parent.mkdir(parents=True, exist_ok=True)

                with subpath.open("w") as f:
                    f.write(content)

        certbot.side_effect = certbot_side_effect

        with patch.dict(
            os.environ,
            {
                "CERTBOT_EMAILS": "test@gmail.com",
                "CERTBOT_DOMAINS": "*.domain.com",
                "CERTBOT_DNS_PLUGIN": "dns-cloudflare",
                "AWS_DEFAULT_REGION": "eu-east-1",
                "CERTBOT_DIR": str(path),
            },
            clear=True,
        ):
            handler(None, None)

        certbot.assert_called_once_with(
            [
                "--config-dir",
                str(path),
                "--work-dir",
                str(path),
                "--logs-dir",
                str(path),
                "certonly",
                "--non-interactive",
                "--agree-tos",
                "--email",
                "test@gmail.com",
                "--authenticator",
                "dns-cloudflare",
                "--preferred-challenges",
                "dns-01",
                "--server",
                "https://acme-v02.api.letsencrypt.org/directory",
                "--domains",
                "*.domain.com",
            ]
        )
        client.return_value.create_secret.assert_called_once_with(
            Name='certbot-domain-com',
            Description='Auto generated SSL certificate by lambda-certbot',
            SecretString=json.dumps(secrets)
        )
