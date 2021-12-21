import click

from config import stat_options, DEFAULT_GROUP, DEFAULT_OUTPUT_DIR, DEFAULT_REPORTS_DIR, DEFAULT_STAT
from ReportsGroup import ReportsGroup


@click.command('stats')
@click.option('-d', '--report-dir', default=DEFAULT_REPORTS_DIR, type=click.Path(exists=True), help='Report directory.',
              show_default=True)
@click.option('-g', '--group', default=DEFAULT_GROUP, multiple=True,
              help='Report groups. Each group is a tuple of a glob pattern and a name for this group of reports. '
                   'If more than one group is specified, reports matched by different patterns will be aggregated',
              show_default=True)
@click.option('-o', '--output-dir', default=DEFAULT_OUTPUT_DIR, type=click.Path(exists=True), help='Output directory.',
              show_default=True)
@click.option('-s', '--stat', default=DEFAULT_STAT, type=click.Choice(sorted(stat_options.keys())), multiple=True,
              help='Name of the statistics value(s) that should be parsed from the report files', show_default=True)
@click.option('-t', '--separate-tables', default=False, is_flag=True, help="Show all stats in separate tables")
def stats(report_dir, separate_tables, group, output_dir, stat):
    """Get stats from the generated report files
    \f

    :param separate_tables: true if all stats should be displayed in their own table, false otherwise
    :param stat: name of the statistics value that should be parsed from the report files
    :param output_dir: output directory
    :param group: list of tuples to split collections of reports into groups
    :param report_dir: report directory
    """

    report_groups = [ReportsGroup(g, report_dir) for g in group]
    df_list = [rg.df for rg in report_groups]

    display_all = '*' in stat

    if len(df_list) == 1:
        stats_df = df_list[0]

        cols = list(stats_df.columns) if display_all else list(stat)
        if separate_tables:
            for col in cols:
                click.echo(stats_df[[col]])
        else:
            click.echo(stats_df[cols])
