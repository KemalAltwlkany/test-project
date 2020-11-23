import numpy as np
import pandas as pd  # required by plotly
import plotly.graph_objects as go

from test_project.plots.red_plots.red_plot import RedPlot

class CircleRedPlot(RedPlot):

    def __init__(self):
        super().__init__()
        self.symbol = 'circle'
        self.title = 'A CIRCLE RED plot.'