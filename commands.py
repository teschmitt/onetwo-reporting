import click

from utils import get_file_list


@click.command('stats')
@click.option('-d', '--report-dir', default='./reports/', type=click.Path(exists=True), help='Report directory.')
@click.option('-f', '--output-format', default='PNG', type=click.Choice(['PNG', 'JPG'], case_sensitive=False))
@click.option('-g', '--glob', 'glob_string', default=['*'], multiple=True,
              help='Glob pattern to look for in reports directory.')
@click.option('-o', '--output-dir', default='./images/', type=click.Path(exists=True), help='Output directory.')
@click.option('-s', '--stat', default='delivery_prob',
              help='Name of the statistics value that should be parsed from the report files')
def stats(report_dir, glob_string, output_format, output_dir):
    """Get stats from the generated report files"""
    file_list = get_file_list(glob_string, report_dir)
    print(f'{file_list=}, {type(file_list)}')
    print(f'{output_format=}, {type(output_format)}')
    print(f'{output_dir}, {type(output_format)}')
