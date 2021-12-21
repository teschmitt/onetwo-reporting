from glob import glob
from pathlib import PurePath
from typing import List, Any

import pandas as pd
from pandas import DataFrame


class ReportsGroup:
    """
    A reports-group contains a certain collection of reports that can be either intrinsically compared or used for
    comparisons with other ReportSeries objects.

    :param glob_string: glob pattern to look for
    :param reports_dir: directory of the files

    """

    def __init__(self, group: tuple, reports_dir: str):
        self._glob_string, self._group_name = group
        self._reports_dir = reports_dir
        self._file_list = []
        self._stats_df = DataFrame()
        self._file_list = glob(PurePath(self._reports_dir, self._glob_string).as_posix())

        self._load_data()

    @property
    def df(self) -> DataFrame:
        return self._stats_df

    @df.setter
    def df(self, df: DataFrame) -> None:
        self._stats_df = df

    @property
    def name(self):
        return self._group_name

    def statistics(self):
        return self._stats_df.describe()


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

            self._stats_df = DataFrame(msg_stats).set_index('scenario').sort_index()
            for col in self._stats_df.columns:
                if col != 'scenario':
                    self._stats_df[col] = pd.to_numeric(self._stats_df[col], errors='coerce')

    def __repr__(self):
        return f'ReportsGroup({self._glob_string}, {self._group_name})'
