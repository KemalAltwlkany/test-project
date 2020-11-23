import sys as sys
sys.path.insert(0, '/home/kemal/Programming/Python2021/test_project/')

from test_project.plots.red_plots.squares import SquareRedPlot
from test_project.plots.blue_plots.squares import SquareBluePlot

red = SquareRedPlot()
blue = SquareBluePlot()
red.plot()
blue.plot()
print('Created two square plots, one red and one blue.')