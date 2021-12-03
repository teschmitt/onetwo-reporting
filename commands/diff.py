import click

from config import DEFAULT_OUTPUT_DIR
from utils import get_dataframe_from_file_list


@click.command('diff')
@click.option('-r', '--reports', nargs=2, type=str, help='Two file paths to simulation report files')
@click.option('-o', '--output-dir', default=DEFAULT_OUTPUT_DIR, type=click.Path(exists=True), help='Output directory.',
              show_default=True)
def diff(reports,  output_dir):
    """Get stats from the generated report files
    \f

    :param reports: paths to two simulation reports
    :param output_dir: output directory
    """

    stats_df = get_dataframe_from_file_list(reports).T
    a, b = stats_df.columns
    stats_df['diff'] = stats_df[a] - stats_df[b]
    stats_df['reldiff'] = stats_df['diff'] / stats_df[a]
    print(stats_df)
