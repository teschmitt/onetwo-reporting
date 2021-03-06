import click

from config import stat_options, DEFAULT_GLOB, DEFAULT_OUTPUT_DIR, DEFAULT_REPORTS_DIR, DEFAULT_STAT
from utils import get_file_list, get_dataframe_from_file_list


@click.command('stats')
@click.option('-d', '--report-dir', default=DEFAULT_REPORTS_DIR, type=click.Path(exists=True), help='Report directory.',
              show_default=True)
@click.option('-g', '--glob', 'glob_strings', default=DEFAULT_GLOB, multiple=True,
              help='Glob pattern(s) to look for in reports directory.', show_default=True)
@click.option('-o', '--output-dir', default=DEFAULT_OUTPUT_DIR, type=click.Path(exists=True), help='Output directory.',
              show_default=True)
@click.option('-s', '--stat', default=DEFAULT_STAT, type=click.Choice(sorted(stat_options.keys())), multiple=True,
              help='Name of the statistics value(s) that should be parsed from the report files', show_default=True)
@click.option('-t', '--separate-tables', default=False, is_flag=True, help="Show all stats in separate tables")
def stats(report_dir, separate_tables, glob_strings, output_dir, stat):
    """Get stats from the generated report files
    \f

    :param separate_tables: true if all stats should be displayed in their own table, false otherwise
    :param stat: name of the statistics value that should be parsed from the report files
    :param output_dir: output directory
    :param glob_strings: glob string
    :param report_dir: report directory
    """

    file_list = get_file_list(glob_strings, report_dir)
    stats_df = get_dataframe_from_file_list(file_list)

    display_all = '*' in stat

    cols = list(stats_df.columns) if display_all else list(stat)
    if separate_tables:
        for col in cols:
            click.echo(stats_df[[col]])
    else:
        click.echo(stats_df[cols])
