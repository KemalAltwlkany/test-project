import numpy as np
import pandas as pd
import plotly.graph_objects as go
from test_project.plots.basic_plots import BasicPlot


class BluePlot(BasicPlot):

    def __init__(self):
        super().__init__(color='blue')
        self.title = 'A basic BLUE plot.'