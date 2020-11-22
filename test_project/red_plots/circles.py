import numpy as np
import pandas as pd  # required by plotly
import plotly.graph_objects as go

# tests numpy
print(np.array([1, 2, 3]))

fig = go.Figure(go.Scatter(x=np.arange(0, 10, 1), y=np.array([i**2 for i in range(10)]), mode='lines+markers', name='lines and markers', marker_color='red',
    marker=dict(
    size=15,
    symbol='circle',
)))
fig.update_layout(title='Circles')
fig.show()