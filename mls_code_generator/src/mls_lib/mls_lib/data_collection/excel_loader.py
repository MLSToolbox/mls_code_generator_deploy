""" Excel Loader """
import pandas as pd
from mls_lib.objects.data_frame import DataFrame
from mls_lib.orchestration.task import Task

class ExcelLoader(Task):
    """ Excel Loader """
    def __init__(self, path : str):
        super().__init__()
        self.path = path

    def execute(self):
        df = DataFrame()
        data = pd.read_excel(self.path)
        df.set_data(data)
        self._set_output("resulting_table", df)
