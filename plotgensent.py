import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np



questA = pd.read_csv("questpython.csv")
del questA["Unnamed: 0"]
questA.index = np.arange(1, len(questA) + 1)

print(questA)

df4 = pd.DataFrame()

### Extract: From 1 to 9 / From 14 to 17 ###

siw1 = [questA.ix[1:9, 'Si_F'], questA.ix[14:20, 'Si_F']]
siw2 = [questA.ix[1:9, 'A_volte_F'], questA.ix[14:20, 'A_volte_F']]
siw3 = pd.concat(siw1)
siw4 = pd.concat(siw2)


sim1 = [questA.ix[1:9, 'Si_M'], questA.ix[14:20, 'Si_M']]
sim2 = [questA.ix[1:9, 'A_volte_M'], questA.ix[14:20, 'A_volte_M']]
sim3 = pd.concat(sim1)
sim4 = pd.concat(sim2)


### BUILD NEW DF from extracted rows ###

df4['SIW'] = siw3 + siw4
df4['SIM'] = sim3 + sim4

df4['NOWM'] = questA['No_M']
df4['NOWF'] = questA['No_F']

print(df4)

plt.figure(211)

plt.subplot(211)
plt.title('Women')
df4.SIW.plot.bar(width=0.25, position=1)
df4.NOWF.plot.bar(width=0.25, position=2, color='k')
plt.axis([-1, 16, 0, 50])


plt.subplot(212)
plt.title('Men')
df4.SIM.plot.bar(width=0.25, position=1)
df4.NOWM.plot.bar(width=0.25, position=2, color='k')
plt.axis([-1, 16, 0, 50])
plt.show()
