import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)
blue1 = '#4c95cb'
blue2 = '#0068b6'
blue3 = '#00487f'
green1 = '#4ca85c'
green2 = '#008317'
green3 = '#005b10'
yellow1 = '#f4bd54'
yellow2 = '#f0a10b'
yellow3= '#a87007'
red1 = '#df4c4c'
red2 = '#d20000'
red3 = '#930000'

##### runs to have spectra generated #######
run1 = { 'Name':'T0.3_v1000_chi300_cond',
        'Name_plot':'M3.6-v1000-T0.3-c',
        'Dir':'../../Blob_paper2/Files/',
        'Mach':3.8,
        'tcc':1.7,
        'f_list':['0013', '0038', '0080', '0132'],
        'marker':'^',
        'color':green2}
run2 = { 'Name':'T0.3_v1700_chi300_cond',
        'Name_plot':'M6.5-v1700-T0.3-c',
        'Dir':'../../Blob_paper2/Files/',
        'Mach':6.5,
        'tcc':1.0,
        'f_list':['0003', '0020', '0046', '0078'],
        'marker':'^',
        'color':yellow1}
run3 = { 'Name':'T0.3_v3000_chi300_cond',
        'Name_plot':'M11.4-v3000-T0.3-c',
        'Dir':'../../Blob_paper2/Files/',
        'Mach':11.4,
        'tcc':0.56,
        'f_list':['0001', '0004', '0014', '0035'],
        'marker':'^',
        'color':red1}
run4 = { 'Name':'T3_v3000_chi3000_cond',
        'Name_plot':'M3.6-v3000-T3-c',
        'Dir':'../../Blob_paper2/Files/',
        'Mach':3.6,
        'tcc':1.8,
        'f_list':['0001', '0004', '0007', '0010'],
        'marker':'^',
        'color':red2}
run5 = { 'Name':'T3_v860_chi3000_cond',
        'Name_plot':'M1.0-v860-T3-c',
        'Dir':'../../Blob_paper2/Files/',
        'Mach':1.0,
        'tcc':6.2,
        'f_list':['0001', '0003', '0006', '0010'],
        'marker':'^',
        'color':blue2}
run6 = { 'Name':'T1_v1700_chi1000_cond',
        'Name_plot':'M3.5-v1700-T1-c',
        'Dir':'../../Blob_paper2/Files/',
        'Mach':3.5,
        'tcc':1.8,
        'f_list':['0002', '0010', '0017', '0028'],
        'marker':'^',
        'color':yellow2}
run7 = { 'Name':'T1_v480_chi1000_cond',
        'Name_plot':'M1.0-v480-T1-c',
        'Dir':'../../Blob_paper2/Files/',
        'Mach':1.0,
        'tcc':6.4,
        'f_list':['0002', '0009', '0017', '0031'],
        'marker':'^',
        'color':blue1}
run8 = { 'Name':'T10_v1500_chi10000_cond',
        'Name_plot':'M1.0-v1500-T10-c',
        'Dir':'../../Blob_paper2/Files/',
        'Mach':1.0,
        'tcc':6.5,
        'f_list':['0001', '0002', '0004', '0008'],
        'marker':'^',
        'color':yellow3}
run9 = { 'Name':'T0.3_v1000_chi300',
        'Name_plot':'M3.8-v1000-T0.3',
        'Dir':'../../Blob_paper1/Files/',
        'Mach':3.8,
        'f_list':['0025', '0033', '0042', '0058'],
        'marker':'o',
        'color':green2}
run10 = { 'Name':'T0.3_v1700_chi300',
        'Name_plot':'M6.5-v1700-T0.3',
        'Dir':'../../Blob_paper1/Files/',
        'Mach':6.5,
        'f_list':['0022', '0032', '0053', '0085'],
        'marker':'o',
        'color':yellow1}
run11 = { 'Name':'T0.3_v3000_chi300',
        'Name_plot':'M11.4-v3000-T0.3',
        'Dir':'../../Blob_paper1/Files/',
        'Mach':11.4,
        'f_list':['0028', '0044', '0065', '0110'],
        'marker':'o',
        'color':red1}
run12 = { 'Name':'T3_v3000_chi3000',
        'Name_plot':'M3.6-v3000-T3',
        'Dir':'../../Blob_paper1/Files/',
        'Mach':3.6,
        'f_list':['0021', '0030', '0040', '0062'],
        'marker':'o',
        'color':red3}
run13 = { 'Name':'T3_v430_chi3000',
        'Name_plot':'M0.5-v430-T3',
        'Dir':'../../Blob_paper1/Files/',
        'Mach':0.5,
        'f_list':['0010', '0011', '0016', '0024'],
        'marker':'o',
        'color':blue2}
run14 = { 'Name':'T3_v860_chi3000',
        'Name_plot':'M1.0-v860-T3',
        'Dir':'../../Blob_paper1/Files/',
        'Mach':1.0,
        'f_list':['0010', '0018', '0030', '0038'],
        'marker':'o',
        'color':blue3}
run15 = { 'Name':'T1_v1700_chi1000',
        'Name_plot':'M3.5-v1700-T1',
        'Dir':'../../Blob_paper1/Files/',
        'Mach':3.5,
        'f_list':['0021', '0029', '0038', '0052'],
        'marker':'o',
        'color':yellow2}
run16 = { 'Name':'T1_v3000_chi1000',
        'Name_plot':'M6.2-v3000-T1',
        'Dir':'../../Blob_paper1/Files/',
        'Mach':6.2,
        'f_list':['0022', '0032', '0048', '0095'],
        'marker':'o',
        'color':red2}
run17 = { 'Name':'T1_v480_chi1000',
        'Name_plot':'M1.0-v480-T1',
        'Dir':'../../Blob_paper1/Files/',
        'Mach':1.0,
        'f_list':['0009', '0013', '0024', '0035'],
        'marker':'o',
        'color':blue1}
run18 = { 'Name':'T10_v1500_chi10000',
        'Name_plot':'M1.0-v1500-T10',
        'Dir':'../../Blob_paper1/Files/',
        'Mach':1.0,
        'f_list':['0014', '0021', '0029', '0044'],
        'marker':'o',
        'color':yellow3}
run19 = { 'Name':'HC_v1000_chi300_cond',
        'Name_plot':'M3.8-v1000-T0.3-hc',
        'Dir':'../../Blob_paper3/Files/',
        'Mach':3.8,
        'f_list':['0054', '0060', '0080', '0107'],
        'marker':'s',
        'color':green2}
run20 = { 'Name':'HC_v1700_chi1000_cond',
        'Name_plot':'M3.5-v1700-T1-hc',
        'Dir':'../../Blob_paper3/Files/',
        'Mach':3.5,
        'f_list':['0024', '0050', '0082', '0083'],
        'marker':'s',
        'color':yellow2}
run21 = { 'Name':'HC_v3000_chi3000_cond',
        'Name_plot':'M3.6-v3000-T3-hc',
        'Dir':'../../Blob_paper3/Files/',
        'Mach':3.6,
        'f_list':['0007', '0015', '0026', '0049'],
        'marker':'s',
        'color':red2}
run22 = { 'Name':'LowCond_v1700_chi300_cond',
        'Name_plot':'M6.5-v1700-T0.3-lc',
        'Dir':'../../Blob_paper3/Files/',
        'Mach':6.5,
        'f_list':['0016', '0075', '0115', '0184'],
        'marker':'.',
        'color':yellow2}





runListTemp = []
runListTemp.append(run1)
runListTemp.append(run2)
runListTemp.append(run3)
runListTemp.append(run7)
runListTemp.append(run6)
runListTemp.append(run5)
runListTemp.append(run4)
runListTemp.append(run8)
runListTemp.append(run9)
runListTemp.append(run10)
runListTemp.append(run11)
runListTemp.append(run17)
runListTemp.append(run15)
runListTemp.append(run16)
runListTemp.append(run13)
runListTemp.append(run14)
runListTemp.append(run12)
runListTemp.append(run18)
runListTemp.append(run19)
runListTemp.append(run20)
runListTemp.append(run21)
runListTemp.append(run22)

runListMach = []
runListMach.append(run7)
runListMach.append(run5)
runListMach.append(run8)
runListMach.append(run1)
runListMach.append(run6)
runListMach.append(run4)
runListMach.append(run2)
runListMach.append(run3)
runListMach.append(run13)
runListMach.append(run17)
runListMach.append(run14)
runListMach.append(run18)
runListMach.append(run9)
runListMach.append(run15)
runListMach.append(run12)
runListMach.append(run10)
runListMach.append(run16)
runListMach.append(run11)
runListMach.append(run19)
runListMach.append(run20)
runListMach.append(run21)
runListMach.append(run22)

runListVel = []
runListVel.append(run7)
runListVel.append(run5)
runListVel.append(run1)
runListVel.append(run2)
runListVel.append(run6)
runListVel.append(run8)
runListVel.append(run3)
runListVel.append(run4)
runListVel.append(run17)
runListVel.append(run13)
runListVel.append(run14)
runListVel.append(run9)
runListVel.append(run10)
runListVel.append(run15)
runListVel.append(run18)
runListVel.append(run11)
runListVel.append(run16)
runListVel.append(run12)
runListVel.append(run19)
runListVel.append(run20)
runListVel.append(run21)
runListVel.append(run22)




### dictionaries of ion info
ion1 = {'ion':'O VI',
            'fieldname':'O_p5_number_density',
            'ionfolder': '/OVI/',
            'color': 'brown',
            'axis': [2, 1],
            'loc':[-3.0, 18],
            'split':[0.0, -2.4, 0.0, 3.4],
            'x_cool':-2.027,
            'y_cool':13.88,
            'dx_cool':0.935,
            'dy_cool':0.744,
            'x_cond':0.365,
            'y_cond':14.28,
            'dx_cond':0.619,
            'dy_cond':2.74}
ion2 = {'ion':'Mg II',
            'fieldname':'Mg_p1_number_density',
            'ionfolder': '/MgII/',
            'color': 'green',
            'axis': [3, 1],
            'loc':[-3.0, 16.5],
            'split':[-2.25, -1.5, 2, -1.5],
            'x_cool':-1.413,
            'y_cool':14.15,
            'dx_cool':1.54,
            'dy_cool':1.231,
            'x_cond':0.231,
            'y_cond':15.58,
            'dx_cond':0.266,
            'dy_cond':-0.071}
ion3 = {'ion':'N V',
            'fieldname':'N_p4_number_density',
            'ionfolder': '/NV/',
            'color': 'red',
            'axis': [2, 0],
            'loc':[-3.0, 18],
            'split':[-0.2, -2.4, -0.2, 3.4],
            'x_cool':-1.993,
            'y_cool':13.26,
            'dx_cool':0.952,
            'dy_cool':0.723,
            'x_cond':0.361,
            'y_cond':13.56,
            'dx_cond':0.163,
            'dy_cond':3.098}
ion4 = {'ion':'C IV',
            'fieldname':'C_p3_number_density',
            'ionfolder': '/CIV/',
            'color': 'orange',
            'axis': [1, 1],
            'loc':[-3.0, 18.4],
            'split':[-2.25, 3, 2, 3],
            'x_cool':-1.59,
            'y_cool':15.911,
            'dx_cool':1.463,
            'dy_cool':1.022,
            'x_cond':0.1736,
            'y_cond':17.17,
            'dx_cond':0.4335,
            'dy_cond':0.3603}
ion5 = {'ion':'Si III',
            'fieldname':'Si_p2_number_density',
            'ionfolder': '/SiIII/',
            'color': 'cyan',
            'axis': [4, 1],
            'loc':[-3.0, 18],
            'split':[-4, 4.25, 2, 4.25]}
ion6 = {'ion':'Si IV',
            'fieldname':'Si_p3_number_density',
            'ionfolder': '/SiIV/',
            'color': 'blue',
            'axis': [1, 0],
            'loc':[-3.0, 18.5],
            'split':[-2.25, 2.5, 2, 2.5],
            'x_cool':-1.512,
            'y_cool':15.486,
            'dx_cool':1.482,
            'dy_cool':1.081,
            'x_cond':0.1925,
            'y_cond':16.76,
            'dx_cond':0.406,
            'dy_cond':0.177}
ion7 = {'ion':'Ne VIII',
            'fieldname':'Ne_p7_number_density',
            'ionfolder': '/NeVIII/',
            'color':'pink',
            'axis': [3, 0],
            'loc':[-3.0, 16.5],
            'split':[-2.25, 0.8, 1.7, -2.8],
            'x_cool':-2.104,
            'y_cool':13.037,
            'dx_cool':0.875,
            'dy_cool':0.824,
            'x_cond':-.1011,
            'y_cond':13.709,
            'dx_cond':0.459,
            'dy_cond':0.8305}
ion8 = {'ion':'H I',
            'fieldname':'H_p0_number_density',
            'ionfolder': '/HI/',
            'color':'gray',
            'axis': [0, 0],
            'loc':[-3.0, 19.5],
            'split':[-4, 4.25, 2, 4.25],
            'x_cool':-1.423,
            'y_cool':17.152,
            'dx_cool':1.529,
            'dy_cool':1.2078,
            'x_cond':0.225,
            'y_cond':18.56,
            'dx_cond':0.2709,
            'dy_cond':-0.0257}
ion9 = {'ion':'C II',
            'fieldname':'C_p1_number_density',
            'ionfolder': '/CII/',
            'color':'purple',
            'axis': [4, 0],
            'loc':[-3.0, 18],
            'split':[-4, 4.25, 2, 4.25]}
ion10 = {'ion':'C III',
            'fieldname':'C_p2_number_density',
            'ionfolder': '/CIII/',
            'color': 'magenta',
            'axis': [0, 1],
            'loc':[-3.0, 19.5],
            'split':[-2.25, 4.1, 2, 4.1],
            'x_cool':-1.52,
            'y_cool':16.66,
            'dx_cool':1.512,
            'dy_cool':1.107,
            'x_cond':0.2026,
            'y_cond':17.99,
            'dx_cond':0.418,
            'dy_cond':0.214}


ionList = []
ionList.append(ion1)
ionList.append(ion2)
ionList.append(ion3)
ionList.append(ion4)
#ionList.append(ion5)
ionList.append(ion6)
ionList.append(ion7)
ionList.append(ion8)
#ionList.append(ion9)
ionList.append(ion10)

def readbestTauB(ion, runName):
    openfile = open('../rankNum'+ion['ionfolder']+ion['ionfolder'][1:-1]+'_bestFitParameters_withTemp.txt', 'r')
    Taus = []
    bs = []
    for line in openfile:
        splitLine = line.split(', ')
        if splitLine[0] == runName:
            Taus.append(float(splitLine[4]))
            bs.append(float(splitLine[7]))

    return Taus, bs

#define functions for the emcee best fit
def model(t, b, x):
    return t*(0.01)/(1.01-x**b)

#fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
fig, ax = plt.subplots(4, 2) #, sharey='row')
for ion in ionList:
    ind = 0.
    cond_low = [0, 0]
    cond_high = [0, 0]
    cool_low = [0, 0]
    cool_high = [0, 0]
    print(ion['ion'])
    for run in runListVel:
        ind = ind+1.
        taus, bs = readbestTauB(ion, run['Name'])
        x = np.linspace(0, 1, 7880)

'''
        if ind in [1, 2, 3]:
            b_avg = np.average(bs)
            tau_avg = np.average(taus)
            cond_low[0] = cond_low[0]+b_avg
            cond_low[1] = cond_low[1]+tau_avg

        if ind in [6, 7, 8]:
            b_avg = np.average(bs)
            tau_avg = np.average(taus)
            cond_high[0] = cond_high[0]+b_avg
            cond_high[1] = cond_high[1]+tau_avg

        if ind in [9, 10, 11]:
            b_avg = np.average(bs)
            tau_avg = np.average(taus)
            cool_low[0] = cool_low[0]+b_avg
            cool_low[1] = cool_low[1]+tau_avg

        if ind in [16, 17, 18]:
            b_avg = np.average(bs)
            tau_avg = np.average(taus)
            cool_high[0] = cool_high[0]+b_avg
            cool_high[1] = cool_high[1]+tau_avg
'''

        ax[ion['axis'][0], ion['axis'][1]].scatter(np.log10(bs), np.log10(taus), label=run['Name_plot'], marker = run['marker'], color = run['color'])

    ax[ion['axis'][0], ion['axis'][1]].arrow(ion['x_cool'], ion['y_cool'], ion['dx_cool'], ion['dy_cool'],
        width = 0.05, head_width=0.2, length_includes_head = True, overhang = 0.3, color = 'black', alpha = 0.5)

    ax[ion['axis'][0], ion['axis'][1]].arrow(ion['x_cond'], ion['y_cond'], ion['dx_cond'], ion['dy_cond'],
        width = 0.05, head_width=0.2, length_includes_head = True, overhang = 0.3, color = 'red', alpha = 0.5)
    ax[ion['axis'][0], ion['axis'][1]].set_xlim(-3.25, 2.0)
    ax[ion['axis'][0], ion['axis'][1]].annotate(ion['ion'], xy = ion['loc'], fontsize = 15 )
    if ion['axis'][0] == 0:
        ax[ion['axis'][0], ion['axis'][1]].set_ylim(16, 20)
    if ion['axis'][0] == 1:
        ax[ion['axis'][0], ion['axis'][1]].set_ylim(14.5, 19)
    if ion['axis'][0] == 2:
        ax[ion['axis'][0], ion['axis'][1]].set_ylim(12, 19)
    if ion['axis'][0] == 3:
        ax[ion['axis'][0], ion['axis'][1]].set_ylim(12, 17)

'''
    print('Cond:')
    print(str(np.log10(cond_low[0]/3.))+', '+str(np.log10(cond_low[1]/3.)))
    print(str(np.log10(cond_high[0]/3.) - np.log10(cond_low[0]/3.))+', '+str(np.log10(cond_high[1]/3.) - np.log10(cond_low[1]/3.)))
    print('Cool:')
    print(str(np.log10(cool_low[0]/3.))+', '+str(np.log10(cool_low[1]/3.)))
    print(str(np.log10(cool_high[0]/3.) - np.log10(cool_low[0]/3.))+', '+str(np.log10(cool_high[1]/3.) - np.log10(cool_low[1]/3.)))
'''


    #if ion['ion'] in ['C III', 'Si IV', 'O VI', 'Mg II']:
    #    ax[ion['axis'][0], ion['axis'][1]].plot([ion['split'][0], ion['split'][2]], [ion['split'][1], ion['split'][3]], linestyle = 'dashed', color = 'gray', alpha = 0.9)

ax[3,0].set_xlabel(r'$log(q)$', fontsize=14)
ax[3,1].set_xlabel(r'$log(q)$', fontsize=14)
ax[0,0].set_ylabel(r'$log(N_0\ (cm^{-2}))$', fontsize=14)
ax[1,0].set_ylabel(r'$log(N_0\ (cm^{-2}))$', fontsize=14)
ax[2,0].set_ylabel(r'$log(N_0\ (cm^{-2}))$', fontsize=14)
ax[3,0].set_ylabel(r'$log(N_0\ (cm^{-2}))$', fontsize=14)
ldg = ax[3, 0].legend(loc='upper left', bbox_to_anchor=(0.05, -0.2), fontsize=10, ncol=4)
#box = ax[ion['axis'][0], ion['axis'][1]].get_position()
#ax[ion['axis'][0], ion['axis'][1]].set_position([box.x0, box.y0, box.width * 0.8, box.height])
#fig.subplots_adjust(wspace=0.05)
#fig.subplots_adjust(hspace=0.1)
fig.set_size_inches(10, 12)
plt.tight_layout()


#fig.savefig('../rankTau'+ion['ionfolder']+ion['ionfolder'][1:-1]+'.png')
fig.savefig('Num_jumboVel_withTemp.pdf', bbox_extra_artists=(ldg,), bbox_inches='tight')
