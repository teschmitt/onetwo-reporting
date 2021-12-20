from glob import glob
from pathlib import PurePath

import pandas as pd


class ReportsCollection:
    """
    Report series contain a certain collection of reports that can be either intrinsically compared or used for
    comparisons with other ReportSeries objects.


    """

    def __init__(self):
        self._file_list = []
        self._stats_df = pd.DataFrame()

    def load_glob(self, glob_string: str, reports_dir: str) -> pd.DataFrame:
        """
        Get a list of files in directory :param report_dir: with the glob pattern :param glob_string and load them into
        a Pandas dataframe

        :param glob_string: glob pattern to look for
        :param reports_dir: directory of the files
        """
        globs = [PurePath(reports_dir, g) for g in glob_string]
        file_lists = [glob(g.as_posix()) for g in globs]
        self._file_list = [i for sublist in file_lists for i in sublist]  # flatten a two-dimensional list

        self._load_data()
        return self._stats_df

    def load_paths(self, filepaths: list) -> pd.DataFrame:
        """
        Load a passed list of filepaths into a Pandas dataframe

        :param filepaths: Paths of the filoes to load
        """
        self._file_list = filepaths
        self._load_data()
        return self._stats_df

    @property
    def df(self):
        return self._stats_df

    @df.setter
    def df(self, df):
        self._stats_df = df

    def _load_data(self) -> None:
        """" Utility method to assist in loading all data from a collection of filepaths """

        if len(self._file_list) > 0:
            try:
                file_handles = [open(fp, 'r') for fp in self._file_list]
            except OSError as e:
                print(f'Something went terribly wrong opening a file. Please check your glob pattern or file list and '
                      f'try again. OS Error: {e}')
                file_handles = []

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

