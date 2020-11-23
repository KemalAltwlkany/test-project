import sys as sys
sys.path.insert(0, '/home/kemal/Programming/Python2021/test_project/')

from test_project.plots.basic_plots import BasicPlot

basic = BasicPlot()
basic.plot()
print('Created a basic plot.')