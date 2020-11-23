import sys as sys
sys.path.insert(0, '/home/kemal/Programming/Python2021/test_project/')

from test_project.plots.red_plots.circles import CircleRedPlot
from test_project.plots.blue_plots.circles import CircleBluePlot

blue = CircleBluePlot()
red = CircleRedPlot()
red.plot()
blue.plot()
print('Created two circle plots, one red and one blue.')