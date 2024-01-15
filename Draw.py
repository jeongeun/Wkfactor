import numpy as np
import sys

lepton = sys.argv[1]

def txt_to_np(input_file):

        data = []

        with open(input_file,'r') as file:

                for i in file:

                        data.append(i.split())

        return np.array(data,dtype='float')

QCD_LO_p        = txt_to_np('outputs/0_3.txt')
QCD_LO_m        = txt_to_np('outputs/0_1.txt')
QCD_NLO_p       = txt_to_np('outputs/1_3.txt')
QCD_NLO_m       = txt_to_np('outputs/1_1.txt')
QCD_NNLO_p      = txt_to_np('outputs/2_3.txt')
QCD_NNLO_m      = txt_to_np('outputs/2_1.txt')

EWK_LO_p        = txt_to_np('outputs/LO_{}_p.txt'.format(lepton))
EWK_LO_m        = txt_to_np('outputs/LO_{}_m.txt'.format(lepton))
EWK_NLO_p       = txt_to_np('outputs/NLO_{}_p.txt'.format(lepton))
EWK_NLO_m       = txt_to_np('outputs/NLO_{}_m.txt'.format(lepton))

mass		= QCD_LO_p[:,0]
QCD		= {}
QCD['LO']	= (QCD_LO_p + QCD_LO_m)[:,1]
QCD['NLO']	= (QCD_NLO_p + QCD_NLO_m)[:,1]
QCD['NNLO']	= (QCD_NNLO_p + QCD_NNLO_m)[:,1]

EWK = {}
EWK['LO']	= (EWK_LO_p + EWK_LO_m)[:,2]
EWK['NLO']	= (EWK_NLO_p + EWK_NLO_m)[:,2]

title   = "W_diff_QCD_xsec_{}.png".format(lepton)

mass    = np.average(mass.reshape(80,5),axis=1)

for key,val in QCD.items():
	QCD[key] = np.sum(val.reshape(80,5),axis=1)*1000

for key,val in EWK.items():
	EWK[key] = np.sum(val.reshape(80,5),axis=1)*1000

if len(sys.argv) == 3:
	tev = int(sys.argv[2])
else:
	tev = 15



for key in QCD.keys():
	
	print('QCD ' + key + ' : ' + str(np.sum(QCD[key][tev:])))

for key in EWK.keys():
	print('EWK ' + key + ' : ' + str(np.sum(EWK[key][tev:])))




#import matplotlib.pyplot as plt
#from matplotlib.gridspec import GridSpec
#import mplhep as hep
#
#plt.style.use(hep.style.CMS)
#
#fig	= plt.figure(figsize=(10,10))
#gs	= GridSpec(nrows=2,ncols=1,height_ratios=[3,1])
#
#ax0	= plt.subplot(gs[0])
#for key,val in QCD.items():
#	ax0.plot(mass, QCD[key], '-', linewidth=2, color='#30A9DE', label=r"{}")
#ax0.set_xlim((0.2,8))
#leg = ax0.legend(loc="lower left",fontsize=20,ncol=1)
#for i in leg.get_lines():
#        i.set_linewidth(2)
#for line, text in zip(leg.get_lines(), leg.get_texts()):
#        text.set_color(line.get_color())
#ax0.set_ylabel(r"Uncertainty (%)",fontsize=20)
#ax0.grid(linestyle="dotted")
#hep.cms.label(fontsize=20, data=False, loc=1, year=year, com=com)
#
#ax1 = plt.subplot(gs[1],sharex = ax0)
#plt.setp(ax0.get_xticklabels(), visible = False)
#ax1.plot(refer[:,0]/1000,target[:,2]/refer[:,2],'ko--')
#ax1.hlines(1,0,8,color='gray')
#ax1.set_xlim((0.2,8))
#ax1.set_ylim((0,2))
#ax1.set_xlabel(r"$M_{W\prime} (TeV)$",fontsize=20)
#ax1.set_ylabel('Ratio',fontsize=20)
#ax1.grid(linestyle = "dotted",linewidth = 1)
#
#plt.show()
