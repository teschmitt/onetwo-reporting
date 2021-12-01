import click
from glob import glob
from pathlib import PurePath

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


@toolkit.command('stats')
@click.option('-d', '--report-dir', default='./reports/', type=click.Path(exists=True), help='Report directory.')
@click.option('-f', '--output-format', default='PNG', type=click.Choice(['PNG', 'JPG'], case_sensitive=False))
@click.option('-g', '--glob', 'glob_string', default=['*'], multiple=True,
              help='Glob pattern to look for in reports directory.')
@click.option('-o', '--output-dir', default='./images/', type=click.Path(exists=True), help='Output directory.')
@click.option('-s', '--stat', default='delivery_prob',
              elp='Name of the statistics value that should be parsed from the report files')
def stats(report_dir, glob_string, output_format, output_dir):
    """Get stats from the generated report files"""
    file_list = get_file_list(glob_string, report_dir)
    print(f'{file_list=}, {type(file_list)}')
    print(f'{output_format=}, {type(output_format)}')
    print(f'{output_dir}, {type(output_format)}')


def get_file_list(glob_string, report_dir):
    globs = [PurePath(report_dir, g) for g in glob_string]
    file_lists = [glob(g.as_posix()) for g in globs]
    file_list = [i for sublist in file_lists for i in sublist]  # flatten a two-dimensional list
    return file_list


if __name__ == '__main__':
    toolkit()
