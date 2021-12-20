import click

from ReportsCollection import ReportsCollection
from config import DEFAULT_OUTPUT_DIR


@click.command('diff')
@click.option('-r', '--reports', nargs=2, type=str, help='Two file paths to simulation report files')
@click.option('-o', '--output-dir', default=DEFAULT_OUTPUT_DIR, type=click.Path(exists=True), help='Output directory.',
              show_default=True)
def diff(reports,  output_dir):
    """Compare two generated simulation report files
    \f

    :param reports: paths to two simulation reports
    :param output_dir: output directory
    """

    reports_coll = ReportsCollection()
    stats_df = reports_coll.load_paths(reports).T

    a, b = stats_df.columns
    stats_df['diff'] = stats_df[a] - stats_df[b]
    stats_df['reldiff'] = stats_df['diff'] / stats_df[a]

    click.echo(stats_df)
