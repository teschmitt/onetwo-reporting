import click
import pandas as pd

from config import stat_options
from utils import get_file_list


@click.command('stats')
@click.option('-d', '--report-dir', default='./reports/', type=click.Path(exists=True), help='Report directory.')
@click.option('-f', '--output-format', default='PNG', type=click.Choice(['PNG', 'JPG'], case_sensitive=False))
@click.option('-g', '--glob', 'glob_string', default=['*'], multiple=True,
              help='Glob pattern to look for in reports directory.')
@click.option('-o', '--output-dir', default='./images/', type=click.Path(exists=True), help='Output directory.')
@click.option('-s', '--stat', default='sim_time', type=click.Choice(sorted(stat_options.keys())),
              help='Name of the statistics value that should be parsed from the report files')
def stats(report_dir, glob_string, output_format, output_dir, stat):
    """
    Get stats from the generated report files
    \f

    :param stat: name of the statistics value that should be parsed from the report files
    :param output_dir: output directory
    :param output_format: output format (deprecated)
    :param glob_string: glob string
    :param report_dir: report directory
    """
    file_list = get_file_list(glob_string, report_dir)

    file_handles = [open(fp, 'r') for fp in file_list]

    msg_stats = []
    for fh in file_handles:
        scenario = {'scenario': fh.readline().split(' ')[-1].strip()}
        for line in fh.readlines():
            elems = line.split(':')
            if len(elems) > 1:
                scenario[elems[0].strip()] = elems[1].strip()
        msg_stats.append(scenario)
        fh.close()

    stats_df = pd.DataFrame(msg_stats).set_index('scenario')

    for col in stats_df.columns:
        if col != 'scenario':
            stats_df[col] = pd.to_numeric(stats_df[col], errors='coerce')

    print(f'{file_list=}, {type(file_list)}')
    print(f'{output_format=}, {type(output_format)}')
    print(f'{output_dir}, {type(output_format)}')
    print(stats_df)
