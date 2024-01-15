import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import mplhep as hep

def txt_to_np(input_file):

	data = []

	with open(input_file,'r') as file:

		for i in file:

			data.append(i.split())

	return np.array(data,dtype='float')

LO_p  	= txt_to_np('outputs/0_3.txt')
LO_m 	= txt_to_np('outputs/0_1.txt')
NLO_p 	= txt_to_np('outputs/1_3.txt')
NLO_m 	= txt_to_np('outputs/1_1.txt')
NNLO_p 	= txt_to_np('outputs/2_3.txt')
NNLO_m 	= txt_to_np('outputs/2_1.txt')

mass 	= LO_p[:,0]
LO 	= LO_p[:,1] + LO_m[:,1]
NLO 	= NLO_p[:,1] + NLO_m[:,1]
NNLO 	= NNLO_p[:,1] + NNLO_m[:,1]

title 	= "W_diff_QCD_xsec.png" 

mass 	= mass.reshape(80,5)
LO 	= LO.reshape(80,5)
NLO 	= NLO.reshape(80,5)
NNLO 	= NNLO.reshape(80,5)

mass 	= np.average(mass,axis=1)
LO 	= np.sum(LO,axis=1)/100
NLO 	= np.sum(NLO,axis=1)/100
NNLO 	= np.sum(NNLO,axis=1)/100

plt.style.use(hep.style.CMS)

fig = plt.figure(figsize=(10,10))
gs 	= GridSpec(nrows=2,ncols=1,height_ratios=[3,1])

#--------------------------------------------------------------------------------------------------------------------------

ax0 	= plt.subplot(gs[0])
ax0.plot(mass, LO,'bv-',linewidth=2,markersize=5,label='QCD LO')
ax0.plot(mass,NLO,'r^-',linewidth=2,markersize=5,label='QCD NLO')
ax0.set_xlim((0,8000))
leg = ax0.legend(loc="lower left",fontsize=20,ncol=1)
for i in leg.get_lines():
        i.set_linewidth(2)
for line, text in zip(leg.get_lines(), leg.get_texts()):
        text.set_color(line.get_color())
ax0.set_ylabel('$d\sigma/dM$ [pb/GeV]',fontsize=20)
ax0.grid(linestyle="dotted")
ax0.set_yscale('log')
hep.cms.label(fontsize=20, data=False, loc=1, year='Run3', com=13.6)

#--------------------------------------------------------------------------------------------------------------------------

ax1 	= plt.subplot(gs[1],sharex = ax0)

plt.setp(ax0.get_xticklabels(), visible = False)
ax1.plot(mass,NLO/LO,'ko-',markersize=5)
ax1.set_xlabel(r'$M_{l\nu}$ [GeV]',fontsize=20)
ax1.set_ylabel('NLO/LO',fontsize=20,labelpad=39)
ax1.hlines(1,0,8000,color='gray')
ax1.set_xlim((0,8000))
ax1.set_ylim(0,2)
ax1.grid(linestyle = "dotted",linewidth = 1)

#--------------------------------------------------------------------------------------------------------------------------

#plt.savefig('Figure/'+title)
plt.show()
