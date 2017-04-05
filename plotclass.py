import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


def superplot():
    df3 = pd.read_csv('questclass1.csv')
    df3.index = np.arange(1, len(df3) + 1)

    ### First Bar Figure ###

    plt.figure()

    plt.subplot(232)
    plt.title('Middle Class Women')
    (df3.Si_M_F * 100 / df3.ix[2, 'Tot_M_F']).plot.bar(width=0.25, position=1)
    (df3.Maybe_M_F * 100 / df3.ix[2, 'Tot_M_F']).plot.bar(width=0.25, position=2, color='y')
    (df3.No_M_F * 100 / df3.ix[2, 'Tot_M_F']).plot.bar(width=0.25, position=3, color='r')
    plt.tick_params(labelsize=8)

    plt.subplot(235)
    plt.title('Middle Class Men')
    (df3.Si_M_M * 100 / df3.ix[2, 'Tot_M_M']).plot.bar(width=0.25, position=1)
    (df3.Maybe_M_M * 100 / df3.ix[2, 'Tot_M_M']).plot.bar(width=0.25, position=2, color='y')
    (df3.No_M_M * 100 / df3.ix[2, 'Tot_M_M']).plot.bar(width=0.25, position=3, color='r')
    plt.tick_params(labelsize=8)

    plt.subplot(234)
    plt.title('Working Class Men')
    (df3.Si_W_M * 100 / df3.ix[2, 'Total_W_M']).plot.bar(width=0.25, position=1)
    (df3.Maybe_W_M * 100 / df3.ix[2, 'Total_W_M']).plot.bar(width=0.25, position=2, color='y')
    (df3.No_W_M * 100 / df3.ix[2, 'Total_W_M']).plot.bar(width=0.25, position=3, color='r')
    plt.tick_params(labelsize=8)

    plt.subplot(231)
    plt.title('Working Class Women')
    (df3.Si_W_F * 100 / df3.ix[2, 'Total_W_F']).plot.bar(width=0.25, position=1)
    (df3.Maybe_W_F * 100 / df3.ix[2, 'Total_W_F']).plot.bar(width=0.25, position=2, color='y')
    (df3.No_W_F * 100 / df3.ix[2, 'Total_W_F']).plot.bar(width=0.25, position=3, color='r')
    plt.tick_params(labelsize=8)

    plt.subplot(236)
    plt.title('Upper Class Men')
    (df3.Si_U_M * 100 / df3.ix[2, 'Tot_U_M']).plot.bar(width=0.25, position=1)
    (df3.Maybe_U_M * 100 / df3.ix[2, 'Tot_U_M']).plot.bar(width=0.25, position=2, color='y')
    (df3.No_U_M * 100 / df3.ix[2, 'Tot_U_M']).plot.bar(width=0.25, position=3, color='r')
    plt.tick_params(labelsize=8)

    plt.subplot(233)
    plt.title('Upper Class Women')
    (df3.Si_U_F * 100 / df3.ix[2, 'Tot_U_F']).plot.bar(width=0.25, position=1)
    (df3.Maybe_U_F * 100 / df3.ix[2, 'Tot_U_F']).plot.bar(width=0.25, position=2, color='y')
    (df3.No_U_F * 100 / df3.ix[2, 'Tot_U_F']).plot.bar(width=0.25, position=3, color='r')

    plt.tight_layout()

    plt.subplots_adjust(wspace=0.25, hspace=0.40)

    plt.tick_params(labelsize=8)

    ##### Legend Patches #####

    cpatch = mpatches.Patch(color='c', label='Si')
    bluepatch = mpatches.Patch(color='b', label='Si')
    yellowpatch = mpatches.Patch(color='y', label='A Volte')
    redpatch = mpatches.Patch(color='r', label='No')

    ##########################

    plt.legend(prop={'size': 8}, loc=9, bbox_to_anchor=(0.2, -0.11), ncol=3, handles=[bluepatch, yellowpatch, redpatch])
    plt.show()
    print(df3)
    df4 = pd.DataFrame()

    ### Extract: From 1 to 9 / From 14 to 17 ###

    siwm1 = [df3.ix[1:9, 'Si_W_M'], df3.ix[14:20, 'Si_W_M']]
    siwm2 = [df3.ix[1:9, 'Maybe_W_M'], df3.ix[14:20, 'Maybe_W_M']]
    siwm3 = pd.concat(siwm1)
    siwm4 = pd.concat(siwm2)

    simm1 = [df3.ix[1:9, 'Si_M_M'], df3.ix[14:20, 'Si_M_M']]
    simm2 = [df3.ix[1:9, 'Maybe_M_M'], df3.ix[14:20, 'Maybe_M_M']]
    simm3 = pd.concat(simm1)
    simm4 = pd.concat(simm2)

    sium1 = [df3.ix[1:9, 'Si_U_M'], df3.ix[14:20, 'Si_U_M']]
    sium2 = [df3.ix[1:9, 'Maybe_U_M'], df3.ix[14:20, 'Maybe_U_M']]
    sium3 = pd.concat(sium1)
    sium4 = pd.concat(sium2)

    siwf1 = [df3.ix[1:9, 'Si_W_F'], df3.ix[14:20, 'Si_W_F']]
    siwf2 = [df3.ix[1:9, 'Maybe_W_F'], df3.ix[14:20, 'Maybe_W_F']]
    siwf3 = pd.concat(siwf1)
    siwf4 = pd.concat(siwf2)

    simf1 = [df3.ix[1:9, 'Si_M_F'], df3.ix[14:20, 'Si_M_F']]
    simf2 = [df3.ix[1:9, 'Maybe_M_F'], df3.ix[14:20, 'Maybe_M_F']]
    simf3 = pd.concat(simf1)
    simf4 = pd.concat(simf2)

    siuf1 = [df3.ix[1:9, 'Si_U_F'], df3.ix[14:20, 'Si_U_F']]
    siuf2 = [df3.ix[1:9, 'Maybe_U_F'], df3.ix[14:20, 'Maybe_U_F']]
    siuf3 = pd.concat(siuf1)
    siuf4 = pd.concat(siuf2)

    siwm1 = [df3.ix[1:9, 'Si_W_M'], df3.ix[14:20, 'Si_W_M']]
    siwm2 = [df3.ix[1:9, 'Maybe_W_M'], df3.ix[14:20, 'Maybe_W_M']]
    siwm3 = pd.concat(siwm1)
    siwm4 = pd.concat(siwm2)

    ### BUILD NEW DF from extracted rows ###

    df4['SIWM'] = siwm3 + siwm4
    df4['SIWF'] = siwf3 + siwf4
    df4['SIMM'] = simm3 + simm4
    df4['SIMF'] = simf3 + simf4
    df4['SIUM'] = sium3 + sium4
    df4['SIUF'] = siuf3 + siuf4

    df4['NOWM'] = df3['No_W_M']
    df4['NOWF'] = df3['No_W_F']
    df4['NOMM'] = df3['No_M_M']
    df4['NOMF'] = df3['No_M_F']
    df4['NOUM'] = df3['No_U_M']
    df4['NOUF'] = df3['No_U_M']

    print(df4)

    #### Bar plot New DF with only yes or no answers ####

    plt.figure()

    plt.subplot(231)
    plt.title('Working Class Men')
    (df4.SIWM * 100 / df3.ix[2, 'Tot_M_F']).plot.bar(width=0.25, position=1)
    (df4.NOWM * 100 / df3.ix[2, 'Tot_M_F']).plot.bar(width=0.25, position=2, color='r')

    plt.subplot(232)
    plt.title('Middle Class Men')
    (df4.SIMM * 100 / df3.ix[2, 'Tot_M_M']).plot.bar(width=0.25, position=1)
    (df4.NOMM * 100 / df3.ix[2, 'Tot_M_M']).plot.bar(width=0.25, position=2, color='r')

    plt.subplot(233)
    plt.title('Upper Class Men')
    (df4.SIUM * 100 / df3.ix[2, 'Tot_U_M']).plot.bar(width=0.25, position=1)
    (df4.NOUM * 100 / df3.ix[2, 'Tot_U_M']).plot.bar(width=0.25, position=2, color='r')

    plt.subplot(234)
    plt.title('Working Class Women')
    (df4.SIWF * 100 / df3.ix[2, 'Total_W_F']).plot.bar(width=0.25, position=1)
    (df4.NOWF * 100 / df3.ix[2, 'Total_W_F']).plot.bar(width=0.25, position=2, color='r')

    plt.subplot(235)
    plt.title('Middle Class Women')
    (df4.SIMF * 100 / df3.ix[2, 'Tot_M_F']).plot.bar(width=0.25, position=1)
    (df4.NOMF * 100 / df3.ix[2, 'Tot_M_F']).plot.bar(width=0.25, position=2, color='r')

    plt.subplot(236)
    plt.title('Upper Class Women')
    (df4.SIUF * 100 / df3.ix[2, 'Tot_U_F']).plot.bar(width=0.25, position=1)
    (df4.NOUF * 100 / df3.ix[2, 'Tot_U_F']).plot.bar(width=0.25, position=2, color='r')

    plt.show()

    ### Pie Chart Positive/Negative Attitude Towards Dialect ###

    plt.figure()

    plt.subplot(231)
    plt.title('Working Class Men')
    totwm = [df4['SIWM'].sum(), df4['NOWM'].sum()]
    plt.pie(totwm, autopct='%1.1f%%', shadow=True, colors=['c', 'r'])

    plt.subplot(232)
    plt.title('Middle Class Men')
    totmm = [df4['SIMM'].sum(), df4['NOMM'].sum()]
    plt.pie(totmm, autopct='%1.1f%%', shadow=True, colors=['c', 'r'])

    plt.subplot(233)
    plt.title('Upper Class Men')
    totum = [df4['SIUM'].sum(), df4['NOUM'].sum()]
    plt.pie(totum, autopct='%1.1f%%', shadow=True, colors=['c', 'r'])

    plt.subplot(234)
    plt.title('Working Class Women')
    totwf = [df4['SIWF'].sum(), df4['NOWF'].sum()]
    plt.pie(totwf, autopct='%1.1f%%', shadow=True, colors=['c', 'r'])

    plt.subplot(235)
    plt.title('Middle Class Women')
    totmf = [df4['SIMF'].sum(), df4['NOMF'].sum()]
    plt.pie(totmf, autopct='%1.1f%%', shadow=True, colors=['c', 'r'])

    plt.subplot(236)
    plt.title('Upper Class Women')
    totuf = [df4['SIUF'].sum(), df4['NOUF'].sum()]
    plt.pie(totuf, autopct='%1.1f%%', shadow=True, colors=['c', 'r'])

    plt.legend(prop={'size': 12}, loc=9, bbox_to_anchor=(0.2, -0.11), ncol=2, handles=[cpatch, redpatch])
    plt.show()


superplot()
