import click

import seaborn as sns
import matplotlib.pyplot as plt

from config import seaborn_themes, stat_options, seaborn_contexts
from utils import get_file_list, get_dataframe_from_file_list


@click.command('graph')
@click.option('-c', '--context', default='paper', type=click.Choice(sorted(seaborn_contexts)),
              help='Seaborn context for the generated graphs')
@click.option('-d', '--report-dir', default='./reports/', type=click.Path(exists=True), help='Report directory.')
@click.option('-f', '--output-format', default='PNG', type=click.Choice(['PNG', 'JPG'], case_sensitive=False))
@click.option('-g', '--glob', 'glob_string', default=['*MessageStats*.txt'], multiple=True,
              help='Glob pattern to look for in reports directory.')
@click.option('-o', '--output-dir', default='./images/', type=click.Path(exists=True), help='Output directory.')
@click.option('-s', '--stat', default='delivery_prob', type=click.Choice(sorted(stat_options.keys())),
              help='Name of the statistics value that should be parsed from the report files')
@click.option('-t', '--theme', default='whitegrid', type=click.Choice(sorted(seaborn_themes)),
              help='Seaborn theme for the generated graphs')
def graph(report_dir, glob_string, output_format, output_dir, stat, theme, context):
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

    sns.set_theme(style="whitegrid", context="paper")
    ax = sns.barplot(x=stats_df.index, y=stats_df[stat], palette="deep")
    ax.axhline(0, color="k", clip_on=False)
    ax.set_ylabel(stat_options[stat])
    ax.set_xlabel("Scenario")
    plt.show()
