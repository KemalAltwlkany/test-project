import numpy as np
import pandas as pd
import plotly.graph_objects as go

class BasicPlot:

    def __init__(self, color='black', symbol='x'):
        self.fig = go.Figure()
        self.title = 'A basic plot.'
        self.color = color
        self.symbol = symbol

    def plot(self):
        self.fig.add_trace(go.Scatter(x=np.arange(0, 10, 1), y=np.array([i**2 for i in range(10)]), mode='lines+markers', name='lines and markers', marker_color=self.color,
        marker=dict(
            size=15,
            symbol=self.symbol,
            )       
        ))
        self.fig.update_layout(title=self.title)
        self.fig.show()