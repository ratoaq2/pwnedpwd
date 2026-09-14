import hashlib

import click
import requests


@click.command
@click.password_option(confirmation_prompt=False)
@click.pass_context
def pwnedpwd(ctx: click.core.Context, password: str) -> None:
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    sha1_prefix = sha1[:5]
    sha1_suffix = sha1[5:]

    headers = {"Add-Padding": "true"}
    r = requests.get(f"https://api.pwnedpasswords.com/range/{sha1_prefix}", headers=headers)
    r.raise_for_status()
    for line in r.text.splitlines():
        suffix, count = line.split(":")
        if suffix != sha1_suffix:
            continue

        pwned = int(count)
        if pwned:
            click.echo(
                f"{click.style('[BAD]', bold=True, fg='red')} Password appeared "
                f"{click.style(f'{pwned}', bold=True, fg='red')} times in data breaches. "
                f"(source https://haveibeenpwned.com/Passwords)"
            )
            ctx.exit(1)

    click.echo(
        f"{click.style('[GOOD]', bold=True, fg='green')} Password "
        f"{click.style('is not present', bold=True, fg='blue')} in any known data breach. "
        f"(source https://haveibeenpwned.com/Passwords)"
    )


if __name__ == "__main__":
    pwnedpwd()
