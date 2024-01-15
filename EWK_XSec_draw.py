import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import mplhep as hep

lepton = sys.argv[1]

def txt_to_np(input_file):

	data = []

	with open(input_file,'r') as file:

		for i in file:

			data.append(i.split())

	return np.array(data,dtype='float')


LO_p  	= txt_to_np('outputs/LO_{}_p.txt'.format(lepton))
LO_m 	= txt_to_np('outputs/LO_{}_m.txt'.format(lepton))
NLO_p 	= txt_to_np('outputs/NLO_{}_p.txt'.format(lepton))
NLO_m 	= txt_to_np('outputs/NLO_{}_m.txt'.format(lepton))

mass 	= (LO_p[:,0]+LO_p[:,1])/2
LO 	= LO_p[:,2] + LO_m[:,2]
NLO 	= NLO_p[:,2] + NLO_m[:,2]

title 	= "W_diff_EWK_xsec_{}.png".format(lepton) 

#mass 	= mass.reshape(80,5)
#LO 	= LO.reshape(80,5)
#NLO 	= NLO.reshape(80,5)
mass 	= mass.reshape(400,1)
LO 	= LO.reshape(400,1)
NLO 	= NLO.reshape(400,1)

mass 	= np.average(mass,axis=1)
#LO 	= np.sum(LO,axis=1)/100
#NLO 	= np.sum(NLO,axis=1)/100
LO 	= np.sum(LO,axis=1)
NLO 	= np.sum(NLO,axis=1)

plt.style.use(hep.style.CMS)

fig = plt.figure(figsize=(10,10))
gs 	= GridSpec(nrows=2,ncols=1,height_ratios=[3,1])

#--------------------------------------------------------------------------------------------------------------------------

ax0 	= plt.subplot(gs[0])
ax0.plot(mass, LO,'bv-',linewidth=2,markersize=5,label='EWK LO')
ax0.plot(mass,NLO,'r^-',linewidth=2,markersize=5,label='EWK NLO')
ax0.set_xlim((0,8000))
leg = ax0.legend(loc="lower left",fontsize=20,ncol=1)
for i in leg.get_lines():
        i.set_linewidth(2)
for line, text in zip(leg.get_lines(), leg.get_texts()):
        text.set_color(line.get_color())
ax0.set_ylabel('$d\sigma/dM$ [pb/20 GeV]',fontsize=20)
ax0.grid(linestyle="dotted")
ax0.set_yscale('log')
hep.cms.label(fontsize=20, data=False, loc=1, year='Run3', com=13.6)

#--------------------------------------------------------------------------------------------------------------------------

ax1 	= plt.subplot(gs[1],sharex = ax0)

plt.setp(ax0.get_xticklabels(), visible = False)
ax1.plot(mass,NLO/LO,'ko-',markersize=5)
ax1.set_xlabel(r'$M_{%s\nu}$ [GeV]' % lepton,fontsize=20)
ax1.set_ylabel('NLO/LO',fontsize=20,labelpad=39)
ax1.hlines(1,0,8000,color='gray')
ax1.set_xlim((0,8000))
ax1.set_ylim(0,2)
ax1.grid(linestyle = "dotted",linewidth = 1)

#--------------------------------------------------------------------------------------------------------------------------

plt.savefig('Figure/'+title)
#`plt.show()
