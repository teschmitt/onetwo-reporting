import click

from commands.graph import graph
from commands.stats import stats

__version__ = 0.1


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'Version {__version__}')
    ctx.exit()


@click.group()
@click.option('-v', '--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True,
              help='Show version and exit.')
def toolkit():
    pass


# noinspection PyTypeChecker
toolkit.add_command(stats)
# noinspection PyTypeChecker
toolkit.add_command(graph)

if __name__ == '__main__':
    toolkit()
