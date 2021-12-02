from glob import glob
from pathlib import PurePath


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
