from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


inf = pd.read_excel('finf3.xlsx')
### This to make sure the file is correctly read ###
print(inf)

xo = [inf.ix[1, 'F1'], inf.ix[24, 'F1'], inf.ix[67, 'F1'], inf.ix[75, 'F1'], inf.ix[78, 'F1']]
yo = [inf.ix[1, 'F2'], inf.ix[24, 'F2'], inf.ix[67, 'F2'], inf.ix[75, 'F2'], inf.ix[78, 'F2']]

xa = [inf.ix[5, 'F1'], inf.ix[29, 'F1'], inf.ix[33, 'F1'], inf.ix[36, 'F1'], inf.ix[42, 'F1'], inf.ix[51, 'F1'], inf.ix[59, 'F1'], inf.ix[62, 'F1'], inf.ix[65, 'F1'], inf.ix[72, 'F1']]
ya = [inf.ix[5, 'F2'], inf.ix[29, 'F2'], inf.ix[33, 'F2'], inf.ix[36, 'F2'], inf.ix[42, 'F2'], inf.ix[51, 'F2'], inf.ix[59, 'F2'], inf.ix[62, 'F2'], inf.ix[65, 'F2'], inf.ix[72, 'F2']]

xe = [inf.ix[80, 'F1'], inf.ix[3, 'F1'], inf.ix[7, 'F1'], inf.ix[10, 'F1'], inf.ix[13, 'F1'], inf.ix[19, 'F1'], inf.ix[22, 'F1'], inf.ix[38, 'F1'], inf.ix[40, 'F1'], inf.ix[45, 'F1'], inf.ix[48, 'F1'], inf.ix[55, 'F1'], inf.ix[57, 'F1']]
ye = [inf.ix[80, 'F2'], inf.ix[3, 'F2'], inf.ix[7, 'F2'], inf.ix[10, 'F2'], inf.ix[13, 'F2'], inf.ix[19, 'F2'], inf.ix[22, 'F2'], inf.ix[38, 'F2'], inf.ix[40, 'F2'], inf.ix[45, 'F2'], inf.ix[48, 'F2'], inf.ix[55, 'F2'], inf.ix[57, 'F2']]

xi = [inf.ix[15, 'F1'], inf.ix[17, 'F1'], inf.ix[27, 'F1'], inf.ix[53, 'F1']]
yi = [inf.ix[15, 'F2'], inf.ix[17, 'F2'], inf.ix[27, 'F2'], inf.ix[53, 'F2']]

xu = [inf.ix[105, 'F1'], inf.ix[107, 'F1'], inf.ix[110, 'F1'], inf.ix[101, 'F1'], inf.ix[94, 'F1']]
yu = [inf.ix[105, 'F2'], inf.ix[107, 'F2'], inf.ix[110, 'F2'], inf.ix[101, 'F2'], inf.ix[94, 'F2']]

xs = [280, 360, 560, 800, 520, 420]

ys = [2240, 2040, 1840, 1280, 900, 800]

xs2 = [320, 400, 620, 920, 640, 400, 360]
ys2 = [2750, 2500, 2400, 1400, 1200, 920, 760]


plot1 = plt.gca()

xas = [inf.ix[84, 'F1'], inf.ix[26, 'F1'], inf.ix[6, 'F1'], inf.ix[8, 'F1'], inf.ix[16, 'F1'], inf.ix[18, 'F1'], inf.ix[25, 'F1'], inf.ix[28, 'F1'], inf.ix[54, 'F1'], inf.ix[58, 'F1'], inf.ix[69, 'F1'], inf.ix[72, 'F1'], inf.ix[50, 'F1'], inf.ix[41, 'F1'], inf.ix[32, 'F1']]
yas = [inf.ix[84, 'F2'], inf.ix[26, 'F2'], inf.ix[6, 'F2'], inf.ix[8, 'F2'], inf.ix[16, 'F2'], inf.ix[18, 'F2'], inf.ix[25, 'F2'], inf.ix[28, 'F2'], inf.ix[54, 'F2'], inf.ix[58, 'F2'], inf.ix[69, 'F2'], inf.ix[72, 'F2'], inf.ix[50, 'F2'], inf.ix[41, 'F2'], inf.ix[32, 'F2']]

xes = [inf.ix[76, 'F1'], inf.ix[4, 'F1'], inf.ix[79, 'F1'], inf.ix[16, 'F1'], inf.ix[31, 'F1'], inf.ix[43, 'F1'], inf.ix[56, 'F1'], inf.ix[71, 'F1']]
yes = [inf.ix[76, 'F2'], inf.ix[4, 'F2'], inf.ix[79, 'F2'], inf.ix[16, 'F2'], inf.ix[31, 'F2'], inf.ix[43, 'F2'], inf.ix[56, 'F2'], inf.ix[71, 'F2']]

xos = [inf.ix[66, 'F1'], inf.ix[64, 'F1'], inf.ix[63, 'F1'], inf.ix[11, 'F1'], inf.ix[14, 'F1'], inf.ix[18, 'F1'], inf.ix[20, 'F1'], inf.ix[23, 'F1'], inf.ix[61, 'F1'], inf.ix[64, 'F1'], inf.ix[66, 'F1'], inf.ix[68, 'F1'], inf.ix[73, 'F1']]
yos = [inf.ix[66, 'F2'], inf.ix[64, 'F2'], inf.ix[63, 'F2'], inf.ix[11, 'F2'], inf.ix[14, 'F2'], inf.ix[18, 'F2'], inf.ix[20, 'F2'], inf.ix[23, 'F2'], inf.ix[61, 'F2'], inf.ix[64, 'F2'], inf.ix[66, 'F2'], inf.ix[68, 'F2'], inf.ix[73, 'F2']]

xis = [inf.ix[53, 'F1'], inf.ix[9, 'F1'], inf.ix[12, 'F1'], inf.ix[21, 'F1'], inf.ix[30, 'F1'], inf.ix[47, 'F1']]
yis = [inf.ix[53, 'F2'], inf.ix[9, 'F2'], inf.ix[12, 'F2'], inf.ix[21, 'F2'], inf.ix[30, 'F2'], inf.ix[47, 'F2']]

xus = [inf.ix[92, 'F1']]
yus = [inf.ix[92, 'F2']]

plot1.scatter(yas, xas, facecolor='none', edgecolors='g')
plot1.scatter(yes, xes, facecolor='none', edgecolors='b')
plot1.scatter(yis, xis, facecolor='none', edgecolors='y')
plot1.scatter(yos, xos, facecolor='none', edgecolors='r')
plot1.scatter(yus, xus, facecolor='none', edgecolors='c')

plot1.scatter(ya, xa, s=50, color='g', alpha=0.5)
plot1.scatter(ye, xe, s=50, color='b', alpha=0.5)
plot1.scatter(yi, xi, s=50, color='y', alpha=0.5)
plot1.scatter(yo, xo, s=50, color='r', alpha=0.5)
plot1.scatter(yu, xu, s=50, color='c', alpha=0.5)


plot1.scatter(ys2, xs2, s=50, color='k')
plt.title('Female Informant 5')
plot1.invert_yaxis()
plot1.invert_xaxis()
plt.show()
