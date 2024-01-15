import numpy as np
import sys
#import ROOT
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


QCD_LO_p        = txt_to_np('outputs/0_3.txt')
QCD_LO_m        = txt_to_np('outputs/0_1.txt')
QCD_NLO_p       = txt_to_np('outputs/1_3.txt')
QCD_NLO_m       = txt_to_np('outputs/1_1.txt')
QCD_NNLO_p      = txt_to_np('outputs/2_3.txt')
QCD_NNLO_m      = txt_to_np('outputs/2_1.txt')

EWK_LO_p  	= txt_to_np('outputs/LO_{}_p.txt'.format(lepton))
EWK_LO_m 	= txt_to_np('outputs/LO_{}_m.txt'.format(lepton))
EWK_NLO_p 	= txt_to_np('outputs/NLO_{}_p.txt'.format(lepton))
EWK_NLO_m 	= txt_to_np('outputs/NLO_{}_m.txt'.format(lepton))

MG_LO120     = txt_to_np('out_{}120.txt'.format(lepton))
MG_LO200     = txt_to_np('out_{}200.txt'.format(lepton))
#MG_LO400     = txt_to_np('out_{}400.txt'.format(lepton))
MG_LO800     = txt_to_np('out_{}800.txt'.format(lepton))
MG_LO1500     = txt_to_np('out_{}1500.txt'.format(lepton))
MG_LO2500     = txt_to_np('out_{}2500.txt'.format(lepton))
MG_LO4000     = txt_to_np('out_{}4000.txt'.format(lepton))
MG_LO6000     = txt_to_np('out_{}6000.txt'.format(lepton))

mass            = QCD_LO_p[:,0]
#mass 	= (EWK_LO_p[:,0]+EWK_LO_p[:,1])/2
mgmass          = MG_LO120[:,0]

MGAll           = {}
#MGAll           = (MG_LO120 + MG_LO200 + MG_LO800 + MG_LO1500 + MG_LO2500 + MG_LO4000)[:,1]
MGAll           = (MG_LO120 + MG_LO200 + MG_LO800 + MG_LO1500 + MG_LO2500 + MG_LO4000 + MG_LO6000)[:,1]

#print(MGAll)

QCD             = {}
QCD['LO']       = (QCD_LO_p + QCD_LO_m)[:,1]
QCD['NLO']      = (QCD_NLO_p + QCD_NLO_m)[:,1]
QCD['NNLO']     = (QCD_NNLO_p + QCD_NNLO_m)[:,1]

EWK = {}
EWK['LO']       = (EWK_LO_p + EWK_LO_m)[:,2]
EWK['NLO']      = (EWK_NLO_p + EWK_NLO_m)[:,2]

#EWK_LO 	= EWK_LO_p[:,2] + EWK_LO_m[:,2]
#EWK_NLO = NLO_p[:,2] + NLO_m[:,2]
mask_qcd = QCD['LO'] != 0.0
mask_ewk = EWK['LO'] != 0.0
mask_mg  = MGAll != 0.0

#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

Additive        = QCD['NNLO'] + ( EWK['NLO'] - EWK['LO'] )
Factorize       = QCD['NNLO'] * np.where(mask_ewk, EWK['NLO'] / EWK['LO'], 0.0)
Mixed           = QCD['LO'] * np.where(mask_qcd, (QCD['NLO'] - QCD['LO']) / QCD['LO'], 0.0) * np.where(mask_ewk, (EWK['NLO'] - EWK['LO']) / EWK['LO'], 0.0 )

RatioAdditiveMG      = np.where(mask_mg, ((Additive) / MGAll), 0.0 )
RatioMixedMG         = np.where(mask_mg, ((Additive + Mixed) / MGAll), 0.0 )

print(mgmass[0:5])
print(RatioMixedMG[0:5])
print("@@ {}: 0-120 avg".format(lepton), np.average(RatioMixedMG[0:5]))

print(mgmass[6:10])
print(RatioMixedMG[6:10])
print("@@ {}: 120-200 avg".format(lepton), np.average(RatioMixedMG[6:10]))

print(mgmass[10:20])
print(RatioMixedMG[10:20])
print("@@ {}: 200-400 avg".format(lepton), np.average(RatioMixedMG[10:20]))

print(mgmass[20:40])
print(RatioMixedMG[20:40])
print("@@ {}: 400-800 avg".format(lepton), np.average(RatioMixedMG[20:40]))

print(mgmass[40:75])
print(RatioMixedMG[40:75])
print("@@ {}: 800-1500 avg".format(lepton), np.average(RatioMixedMG[40:75]))

print(mgmass[75:125])
print(RatioMixedMG[75:125])
print("@@ {}: 1500-2500 avg".format(lepton), np.average(RatioMixedMG[75:125]))

print(mgmass[125:200])
print(RatioMixedMG[125:200])
print("@@ {}: 2500-4000 avg".format(lepton), np.average(RatioMixedMG[125:200]))

print(mgmass[200:300])
print(RatioMixedMG[200:300])
print("@@ {}: 4000-6000 avg".format(lepton), np.average(RatioMixedMG[200:300]))

print(mgmass[301:400])
print(RatioMixedMG[301:400])
print("@@ {}: 6000-8000 avg".format(lepton), np.average(RatioMixedMG[301:400]))

title_qcd 	= "W_diff_QCD_xsec_{}.png".format(lepton) 
title_ewk 	= "W_diff_EWK_xsec_{}.png".format(lepton) 
title_add 	= "W_diff_Additive_xsec_{}.png".format(lepton) 
title_mix 	= "W_diff_Mixed_xsec_{}.png".format(lepton) 
title_final 	= "W_diff_Final_xsec_{}.png".format(lepton) 

plt.style.use(hep.style.CMS)

fig = plt.figure(figsize=(10,10))
gs 	= GridSpec(nrows=2,ncols=1,height_ratios=[3,1])
#--------------------------------------------------------------------------------------------------------------------------
ax0 	= plt.subplot(gs[0])
#ax0.plot(mass, QCD['LO'] ,  'b<-', linewidth=0.3, markersize=1, label='QCD LO (FEWZ)')
ax0.plot(mass, Additive + Mixed  ,  'rv-', linewidth=0.3, markersize=1, label=r'Additive+Mixed, QCD $\times$ EW')
ax0.plot(mass, Additive  ,  'kv-', linewidth=0.3, markersize=1, label=r'Additive, QCD $\bigoplus$ EW')
#ax0.plot(mass, Factorize , 'g^-', linewidth=0.3, markersize=1, label=r'Factorize, QCD $\bigotimes$ EW')
ax0.plot(mgmass, MGAll,  'c<-', linewidth=0.3, markersize=1, label='MGMLM LO (Default)')
ax0.set_xlim((50,8000))
leg = ax0.legend(loc="upper right", title='High Order QCD and EW Combination', title_fontsize=16, fontsize=20,ncol=1)
for i in leg.get_lines():
        i.set_linewidth(2)
for line, text in zip(leg.get_lines(), leg.get_texts()):
        text.set_color(line.get_color())
ax0.set_ylabel(r'$d\sigma(W \rightarrow \%s\nu)/dM_{\%s\nu}$ (pb/20GeV)' %(lepton, lepton), fontsize=20)
ax0.grid(linestyle="dotted")
ax0.set_yscale('log')
#ax0.set_xscale('log')
hep.cms.label(fontsize=20, data=True, loc=0, year='Run3', com=13.6)
#--------------------------------------------------------------------------------------------------------------------------

ax1 	= plt.subplot(gs[1],sharex = ax0)

plt.setp(ax0.get_xticklabels(), visible = False)
ax1.plot(mgmass, RatioMixedMG ,'c^-',linewidth=0.3, markersize=1, label='Additive + Mixed / MGMLM LO')
ax1.plot(mgmass, RatioAdditiveMG ,'k^-',linewidth=0.3, markersize=1, label='Additive / MGMLM LO')
#ax1.plot(mass,  Additive/MGAll,'k^-',linewidth=0.3, markersize=1)
#ax1.plot(mass, Factorize/MGAll,'g^-',linewidth=0.3, markersize=1)
#ax1.plot(mass, QCD['LO']/MGAll,'r^-',linewidth=0.3, markersize=1)
#ax1.plot(mass,  (Additive + Mixed)/QCD['LO'],'r^-',linewidth=0.3, markersize=1)
#ax1.plot(mass,  Additive/QCD['LO'],'k^-',linewidth=0.3, markersize=1)
#ax1.plot(mass, Factorize/QCD['LO'],'g^-',linewidth=0.3, markersize=1)
#ax1.set_xlabel(r'$M_{%s\nu}$ [GeV]' % lepton,fontsize=20)
leg = ax1.legend(loc="upper left", fontsize=15,ncol=1)
for i in leg.get_lines():
        i.set_linewidth(2)
for line, text in zip(leg.get_lines(), leg.get_texts()):
        text.set_color(line.get_color())

ax1.set_xlabel(r'Invariant $M_{\%s\nu}$ (GeV)' %(lepton), fontsize=20)
ax1.set_ylabel('HO Comb./LO',fontsize=20,labelpad=39)
ax1.hlines(1,50,8000,color='gray')
ax1.set_xlim((50,8000))
ax1.set_ylim(0,4.0)
#ax1.set_xscale('log')
ax1.grid(linestyle = "dotted",linewidth = 1)
plt.savefig('Figure/'+title_final)

###----QCD plot----------------------------------------------------------------------------------------------------------------------

#ax0 	= plt.subplot(gs[0])
###ax0.plot(mass, LO,'bv-',linewidth=2,markersize=5,label='EWK LO')
###ax0.plot(mass,NLO,'r^-',linewidth=2,markersize=5,label='EWK NLO')
#ax0.plot(mass, QCD['LO'],  'kv-', linewidth=0.3, markersize=1, label='QCD LO ')
#ax0.plot(mass, QCD['NLO'], 'r^-', linewidth=0.3, markersize=1, label='QCD NLO')
#ax0.plot(mass, QCD['NNLO'],'g<-', linewidth=0.3, markersize=1, label='QCD NNLO')
#ax0.set_xlim((0,8000))
#leg = ax0.legend(loc="upper right", title='FEWZ_3.2 Calculation',fontsize=20,ncol=1)
#for i in leg.get_lines():
#        i.set_linewidth(2)
#for line, text in zip(leg.get_lines(), leg.get_texts()):
#        text.set_color(line.get_color())
#ax0.set_ylabel(r'$d\sigma(W \rightarrow l\nu)/dM_{l\nu}$ (pb/20GeV)',fontsize=20)
#ax0.grid(linestyle="dotted")
#ax0.set_yscale('log')
#ax0.set_xscale('log')
#hep.cms.label(fontsize=20, data=True, loc=0, year='Run3', com=13.6)
#
##--------------------------------------------------------------------------------------------------------------------------
#
#ax1 	= plt.subplot(gs[1],sharex = ax0)
#
#plt.setp(ax0.get_xticklabels(), visible = False)
#ax1.plot(mass,QCD['NLO']/QCD['LO'],'r^-',linewidth=0.3, markersize=1)
#ax1.plot(mass,QCD['NNLO']/QCD['LO'],'g<-',linewidth=0.3, markersize=1)
##ax1.set_xlabel(r'$M_{%s\nu}$ [GeV]' % lepton,fontsize=20)
#ax1.set_xlabel(r'Invariant $M_{l\nu}$ (GeV)' ,fontsize=20)
#ax1.set_ylabel('N(N)LO/LO',fontsize=20,labelpad=39)
#ax1.hlines(1,0,8000,color='gray')
#ax1.set_xlim((0,8000))
#ax1.set_ylim(0,2.0)
#ax1.set_xscale('log')
#ax1.grid(linestyle = "dotted",linewidth = 1)

#plt.savefig('Figure/'+title_qcd)

####----Electroweak Plot----------------------------------------------------------------------------------------------------------------------
##ax0.plot(mass, EWK['LO'],  'kv-', linewidth=0.3, markersize=1, label='EWK LO ')
##ax0.plot(mass, EWK['NLO'], 'r^-', linewidth=0.3, markersize=1, label='EWK NLO')
##ax0.set_xlim((0,8000))
##leg = ax0.legend(loc="upper right", title='MCSANCv2 Calculation',fontsize=20,ncol=1)
##for i in leg.get_lines():
##        i.set_linewidth(2)
##for line, text in zip(leg.get_lines(), leg.get_texts()):
##        text.set_color(line.get_color())
##ax0.set_ylabel(r'$d\sigma(W \rightarrow %s\nu)/dM_{%s\nu}$ (pb/20GeV)' %(lepton, lepton), fontsize=20)
##ax0.grid(linestyle="dotted")
##ax0.set_yscale('log')
##ax0.set_xscale('log')
##hep.cms.label(fontsize=20, data=True, loc=0, year='Run3', com=13.6)
##
###--------------------------------------------------------------------------------------------------------------------------
##
##ax1 	= plt.subplot(gs[1],sharex = ax0)
##
##plt.setp(ax0.get_xticklabels(), visible = False)
##ax1.plot(mass,EWK['NLO']/EWK['LO'],'r^-',linewidth=0.3, markersize=1)
###ax1.set_xlabel(r'$M_{%s\nu}$ [GeV]' % lepton,fontsize=20)
##ax1.set_xlabel(r'Invariant $M_{%s\nu}$ (GeV)' %(lepton), fontsize=20)
##ax1.set_ylabel('NLO/LO',fontsize=20,labelpad=39)
##ax1.hlines(1,0,8000,color='gray')
##ax1.set_xlim((0,8000))
##ax1.set_ylim(0,2.0)
##ax1.set_xscale('log')
##ax1.grid(linestyle = "dotted",linewidth = 1)
##
###--------------------------------------------------------------------------------------------------------------------------
#plt.savefig('Figure/'+title_ewk)
#plt.show()
