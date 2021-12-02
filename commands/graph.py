import click

import seaborn as sns
import matplotlib.pyplot as plt

from config import seaborn_palettes, seaborn_styles, stat_options, seaborn_contexts, DEFAULT_GLOB, \
    DEFAULT_GRAPH_CONTEXT, DEFAULT_OUTPUT_DIR, DEFAULT_REPORTS_DIR, DEFAULT_GRAPH_OUTPUT_FMT, DEFAULT_GRAPH_STYLE, \
    DEFAULT_STAT, DEFAULT_GRAPH_PALETTE
from utils import get_file_list, get_dataframe_from_file_list


@click.command('graph')
@click.option('-d', '--report-dir', default=DEFAULT_REPORTS_DIR, type=click.Path(exists=True), help='Report directory.',
              show_default=True)
@click.option('-f', '--output-format', default=DEFAULT_GRAPH_OUTPUT_FMT,
              type=click.Choice(['PNG', 'JPG'], case_sensitive=False),
              show_default=True)
@click.option('-g', '--glob', 'glob_string', default=DEFAULT_GLOB, multiple=True,
              help='Glob pattern to look for in reports directory.', show_default=True)
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
def graph(report_dir, glob_string, output_format, output_dir, stat, style, context, palette):
    """Draw graphs based on the generated report files
    \f

    :param palette: Seaborn palette for the generated graphs
    :param context: Seaborn context for the generated graphs
    :param style: Seaborn style for the generated graphs
    :param stat: name of the statistics value that should be parsed from the report files
    :param output_dir: output directory
    :param output_format: output format
    :param glob_string: glob string
    :param report_dir: report directory
    """

    file_list = get_file_list(glob_string, report_dir)
    stats_df = get_dataframe_from_file_list(file_list)

    for i in range(len(stat)):
        st = stat[i]
        sns.set_theme(style=style, context=context)
        fig = sns.barplot(x=stats_df.index, y=stats_df[st], palette=palette)
        # ax.axhline(0, color="k", clip_on=False)
        fig.set_title(stat_options[st])
        fig.set_ylabel(stat_options[st])
        fig.set_xlabel("Scenario")

        # call this only between to plots, never at the end
        if i < len(stat) - 1:
            plt.figure()

    plt.show()
