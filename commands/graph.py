import click

from config import graph_theme_options, stat_options
from utils import get_file_list, get_dataframe_from_file_list


@click.command('graph')
@click.option('-d', '--report-dir', default='./reports/', type=click.Path(exists=True), help='Report directory.')
@click.option('-f', '--output-format', default='PNG', type=click.Choice(['PNG', 'JPG'], case_sensitive=False))
@click.option('-g', '--glob', 'glob_string', default=['*'], multiple=True,
              help='Glob pattern to look for in reports directory.')
@click.option('-o', '--output-dir', default='./images/', type=click.Path(exists=True), help='Output directory.')
@click.option('-s', '--stat', default='sim_time', type=click.Choice(sorted(stat_options.keys())),
              help='Name of the statistics value that should be parsed from the report files')
@click.option('-t', '--theme', type=click.Choice(sorted(graph_theme_options.keys())),
              help='Theme for the generated graphs')
def graph(report_dir, glob_string, output_format, output_dir, stat):
    """Draw graphs based on the generated report files
    \f

    :param stat: name of the statistics value that should be parsed from the report files
    :param output_dir: output directory
    :param output_format: output format
    :param glob_string: glob string
    :param report_dir: report directory
    """

    file_list = get_file_list(glob_string, report_dir)
    stats_df = get_dataframe_from_file_list(file_list)

    print(f'{file_list=}, {type(file_list)}')
    print(f'{output_format=}, {type(output_format)}')
    print(f'{output_dir=}, {type(output_dir)}')
    print(stats_df)
