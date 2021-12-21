import click

import seaborn as sns
import matplotlib.pyplot as plt

from ReportsGroup import ReportsGroup
from config import seaborn_palettes, seaborn_styles, stat_options, seaborn_contexts, DEFAULT_GROUP, \
    DEFAULT_GRAPH_CONTEXT, DEFAULT_OUTPUT_DIR, DEFAULT_REPORTS_DIR, DEFAULT_GRAPH_OUTPUT_FMT, DEFAULT_GRAPH_STYLE, \
    DEFAULT_STAT, DEFAULT_GRAPH_PALETTE


@click.command('graph')
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
@click.option('-s', '--stat', default=DEFAULT_STAT, type=click.Choice(sorted(stat_options.keys())), multiple=True,
              help='Name of the statistics value that should be parsed from the report files', show_default=True)
@click.option('-c', '--context', default=DEFAULT_GRAPH_CONTEXT, type=click.Choice(sorted(seaborn_contexts)),
              help='Seaborn context for the generated graphs', show_default=True)
@click.option('-p', '--palette', default=DEFAULT_GRAPH_PALETTE, type=click.Choice(sorted(seaborn_palettes)),
              help='Seaborn color palette for the generated graphs', show_default=True)
@click.option('-y', '--style', default=DEFAULT_GRAPH_STYLE, type=click.Choice(sorted(seaborn_styles)),
              help='Seaborn theme for the generated graphs', show_default=True)
@click.option('-0', '--ymin0', default=False, is_flag=True, help='Flag t start the y-axis at 0 no matter what')
def graph(report_dir, group, output_format, output_dir, stat, style, context, palette, ymin0):
    """Draw graphs based on the generated report files \f
    If only one group is passed, each bar represents one simulation. If multiple groups are defined, aggregate results
    are shown.

    :param ymin0: Start the y-axis at 0 no matter what
    :param palette: Seaborn palette for the generated graphs
    :param context: Seaborn context for the generated graphs
    :param style: Seaborn style for the generated graphs
    :param stat: name of the statistics value that should be parsed from the report files
    :param output_dir: output directory
    :param output_format: output format
    :param group: list of tuples to split collections of reports into groups
    :param report_dir: report directory
    """

    report_groups = [ReportsGroup(g, report_dir) for g in group]
    df_list = [rg.df for rg in report_groups]

    if len(df_list) == 1:
        stats_df = df_list[0]
        if '*' in stat:
            stat = stats_df.columns
        for i in range(len(stat)):
            st = stat[i]
            sns.set_theme(style=style, context=context)
            fig = sns.barplot(x=stats_df.index, y=stats_df[st], palette=palette)
            # ax.axhline(0, color="k", clip_on=False)
            fig.set_title(stat_options[st])
            fig.set_ylabel(stat_options[st])
            fig.set_xlabel("Scenario")

            if ymin0:
                fig.set_ylim(bottom=0)
            else:
                fig.set_ylim((stats_df[st].min() * 0.98, stats_df[st].max() * 1.005))

            # call this only between to plots, never at the end
            if i < len(stat) - 1:
                plt.figure()

        plt.show()
    else:
        click.echo(group)
        click.echo(report_groups)
