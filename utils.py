from glob import glob
from pathlib import PurePath


def get_file_list(glob_string, report_dir):
    globs = [PurePath(report_dir, g) for g in glob_string]
    file_lists = [glob(g.as_posix()) for g in globs]
    file_list = [i for sublist in file_lists for i in sublist]  # flatten a two-dimensional list
    return file_list
