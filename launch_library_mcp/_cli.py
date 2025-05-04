import logging
import click

from .mcp_llv2 import mcp_llv2

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


cli = click.Group()


@cli.command()
def run_llv2():
    mcp_llv2.run(transport="stdio")


if __name__ == "__main__":
    cli()
