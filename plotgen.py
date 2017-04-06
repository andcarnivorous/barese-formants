import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np




questA = pd.read_csv("questpython.csv")
del questA["Unnamed: 0"]

questA.index = np.arange(1, len(questA) + 1)

########################
####### WOMEN ##########
########################

plt.title('Women')

questA.Si_F.plot.bar(position=2, color="green", width=0.25)
questA.No_F.plot.bar(position=1, color="red", width=0.25)
questA.A_volte_F.plot.bar(position=0, color="yellow", width=0.25)
plt.axis([-1, 20, 0, 50])
### LEGEND ###
green_patch = mpatches.Patch(color="green", label="Si")

yellow_patch = mpatches.Patch(color="yellow", label="A volte")

red_patch = mpatches.Patch(color="red", label="No")
plt.legend(handles=[green_patch, yellow_patch, red_patch])

totalyesM = sum(questA['Si_M']) 
totalnoM = sum(questA['No_M'])

totalyesF = sum(questA['Si_F']) 
totalnoF = sum(questA['No_F'])

objects = ['M', 'F']
index = np.arange(len(objects))

plt.tight_layout()

plt.show()

########################
######## MEN ###########
########################

questA.Si_M.plot.bar(position=2, color="blue", width=0.25)
questA.No_M.plot.bar(position=1, color="black", width=0.25)
questA.A_volte_M.plot.bar(position=0, color="grey", width=0.25)
plt.axis([-1, 20, 0, 50])

### LEGEND ###
black_patch = mpatches.Patch(color="black", label="No")

blue_patch = mpatches.Patch(color="blue", label="Si")

grey_patch = mpatches.Patch(color="grey", label="A volte")
plt.legend(handles=[blue_patch, grey_patch, black_patch])

plt.tight_layout()
plt.title('Men')
plt.show()


plt.figure()

###############
#### TOTAL ####
###############

questA.Si_A.plot.bar(position=0, color="blue", rot=0, width=0.25)
questA.No_A.plot.bar(position=1, color="black", width=0.25)
questA.A_volte_A.plot.bar(position=2, color="grey", width=0.25)
plt.axis([-1, 20, 0, 97])
##### LEGEND ###
black_patch = mpatches.Patch(color="black", label="No")
##
blue_patch = mpatches.Patch(color="blue", label="Si")
##
grey_patch = mpatches.Patch(color="grey", label="A volte")
plt.legend(handles=[blue_patch, grey_patch, black_patch])

plt.title('Total')
plt.tight_layout()
plt.show()

##########################
##### HORIZONTAL BAR #####
##########################
plt.figure()

plt.subplot(121).invert_xaxis()
plt.title('Men')

questA.Si_M.plot.barh(position=0, color="blue", width=0.25)
questA.No_M.plot.barh(position=2, color="black", width=0.25)
questA.A_volte_M.plot.barh(position=1, color="c", width=0.25)
plt.tight_layout()
green_patch = mpatches.Patch(color="green", label="Si")

yellow_patch =mpatches.Patch(color="yellow", label="A volte")

red_patch = mpatches.Patch(color="red", label="No")

black_patch = mpatches.Patch(color="black", label="No")

blue_patch = mpatches.Patch(color="blue", label="Si")

grey_patch = mpatches.Patch(color="grey", label="A volte")
plt.legend(loc=9, bbox_to_anchor=(0.8, -0.05), ncol=6, handles=[blue_patch, grey_patch, black_patch, green_patch, yellow_patch, red_patch])


cur_axes = plt.gca()
cur_axes.axes.get_yaxis().set_visible(False)

plt.subplot(122)
plt.title('Women')
questA.Si_F.plot.barh(position=0, color="green", width=0.25)
questA.No_F.plot.barh(position=2, color="red", width=0.25)
questA.A_volte_F.plot.barh(position=1, color="orange", width=0.25)
plt.tight_layout()
#plt.axis([0, 50, -1, 20])
plt.subplots_adjust(wspace=0.10)


plt.show()



