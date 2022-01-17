from pathlib import Path
from dataclasses import dataclass


@dataclass
class CertFile:
    name: str
    content: str


@dataclass
class Cert:
    domain: str
    files: list[CertFile]


def obtain_certbot_certs(
    emails: list[str],
    domains: list[str],
    dns_plugin: str,
    certbot_dir: Path,
    certbot_server: str
) -> list[Cert]:
    certbot_args = [
        # Override directory paths so script doesn't have to be run as root
        '--config-dir', str(certbot_dir),
        '--work-dir', str(certbot_dir),
        '--logs-dir', str(certbot_dir),

        # Obtain a cert but don't install it
        'certonly',

        # Run in non-interactive mode
        '--non-interactive',

        # Agree to the terms of service
        '--agree-tos',

        # Email of domain administrators
        '--email', ','.join(emails),

        # Use dns challenge with dns plugin
        '--authenticator', dns_plugin,
        '--preferred-challenges', 'dns-01',

        # Use this server instead of default acme-v01
        '--server', certbot_server,

        # Domains to provision certs for (comma separated)
        '--domains', ','.join(domains)
    ]
    certbot.main.main(certbot_args)

    return [
        Cert(
            domain=v.name,
            files=[
                CertFile(
                    name=f.name,
                    content=f.read_text()
                )
                for f in v.iterdir()
                if f.suffix == '.pem'
            ]
        )
        for v in CERTBOT_DIR.joinpath('live').iterdir()
        if v.is_dir()
    ]
