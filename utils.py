from glob import glob
from pathlib import PurePath

import pandas as pd


def get_file_list(glob_string, report_dir):
    """Get a list of files in directory :param report_dir:
    with the glob pattern :param glob_string

    :param glob_string: glob pattern to look for
    :param report_dir: directory of the files
    :return: flat, unsorted list of files
    """
    globs = [PurePath(report_dir, g) for g in glob_string]
    file_lists = [glob(g.as_posix()) for g in globs]
    file_list = [i for sublist in file_lists for i in sublist]  # flatten a two-dimensional list
    return file_list


def get_dataframe_from_file_list(file_list):
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
    stats_df = pd.DataFrame(msg_stats).set_index('scenario').sort_index()
    for col in stats_df.columns:
        if col != 'scenario':
            stats_df[col] = pd.to_numeric(stats_df[col], errors='coerce')
    return stats_df
