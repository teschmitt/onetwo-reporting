import click

from ReportsGroup import ReportsGroup
from config import DEFAULT_GROUP, DEFAULT_OUTPUT_DIR, DEFAULT_REPORTS_DIR, DEFAULT_GRAPH_OUTPUT_FMT


@click.command('diff')
@click.option('-d', '--report-dir', default=DEFAULT_REPORTS_DIR, type=click.Path(exists=True), help='Report directory.',
              show_default=True)
@click.option('-f', '--output-format', default=DEFAULT_GRAPH_OUTPUT_FMT,
              type=click.Choice(['PNG', 'JPG'], case_sensitive=False),
              show_default=True)
@click.option('-g', '--group', default=DEFAULT_GROUP, multiple=True,
              help='Report groups. Each group is a tuple of a glob pattern and a name for this group of reports. '
                   'If more than one group is specified, reports matched by different patterns will be aggregated',
              show_default=True)
@click.option('-o', '--output-dir', default=DEFAULT_OUTPUT_DIR, type=click.Path(exists=True), help='Output directory.',
              show_default=True)
def diff(report_dir, group, output_dir, output_format):
    """Compare two generated simulation report files. If more than two groups are defined, only the first two will be
    considered.
    \f

    :param report_dir: report directory
    :param output_dir: output directory
    :param output_format: output format
    :param group: list of tuples to split collections of reports into groups
    :param output_dir: output directory
    """

    report_groups = [ReportsGroup(g, report_dir) for g in group]
    df_list = [rg.df for rg in report_groups]

    try:
        # get the first two tables of reporting data and join them
        stats_a = df_list[0].median()
        stats_b = df_list[1].median()
        stats_df = stats_a.to_frame(report_groups[0].name).join(stats_b.to_frame(report_groups[1].name))

        stats_df['diff'] = stats_a - stats_b
        stats_df['reldiff'] = stats_df['diff'] / stats_a

        click.echo(stats_df)
    except IndexError as e:
        click.echo(f'You must pass two groups when calling diff. {e}')


