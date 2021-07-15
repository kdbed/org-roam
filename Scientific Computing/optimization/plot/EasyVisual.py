from vpython import *


Plot1 = gcurve(color = color.white)

for x in arange(0., 8.1, 0.1):
    Plot1.plot( pos = (x, 5.*cos(2.*x)*exp(-0.4*x)))

graph1 = gdisplay( width = 600, height = 450, title = 'Visual 2D Plot', xtitle = 'x', ytitle = 'f(x)', foreground = color.black, background = color.white)

Plot2 = gdots(color = color.black)

for x in arange( -5., 5, 0.1):
    Plot2.plot(pos = (x, cos(x)))
