import numpy as np
import pandas as pd
import plotly.graph_objects as go
from test_project.plots.basic_plots import BasicPlot


class RedPlot(BasicPlot):

    def __init__(self):
        super().__init__(color='red')
        self.title = 'A basic RED plot.'