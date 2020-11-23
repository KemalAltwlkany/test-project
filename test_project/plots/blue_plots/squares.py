import numpy as np
import pandas as pd  # required by plotly
import plotly.graph_objects as go

from test_project.plots.blue_plots.blue_plot import BluePlot

class SquareBluePlot(BluePlot):

    def __init__(self):
        super().__init__()
        self.symbol = 'square'
        self.title = 'A SQUARE BLUE plot.'