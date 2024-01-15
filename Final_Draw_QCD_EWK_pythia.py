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

PYTHIA100      = txt_to_np('out_pythia/out_{}100_pythia.txt'.format(lepton))
PYTHIA200      = txt_to_np('out_pythia/out_{}200_pythia.txt'.format(lepton))
PYTHIA500      = txt_to_np('out_pythia/out_{}500_pythia.txt'.format(lepton))
PYTHIA1000     = txt_to_np('out_pythia/out_{}1000_pythia.txt'.format(lepton))
PYTHIA2000     = txt_to_np('out_pythia/out_{}2000_pythia.txt'.format(lepton))
PYTHIA3000     = txt_to_np('out_pythia/out_{}3000_pythia.txt'.format(lepton))
PYTHIA4000     = txt_to_np('out_pythia/out_{}4000_pythia.txt'.format(lepton))
PYTHIA5000     = txt_to_np('out_pythia/out_{}5000_pythia.txt'.format(lepton))
PYTHIA6000     = txt_to_np('out_pythia/out_{}6000_pythia.txt'.format(lepton))

mass            = QCD_LO_p[:,0]
#mass 	= (EWK_LO_p[:,0]+EWK_LO_p[:,1])/2
pythiamass          = PYTHIA100[:,0]

PYTHIAall           = {}
PYTHIAall           = (PYTHIA100 + PYTHIA200 + PYTHIA500 + PYTHIA1000 + PYTHIA2000 + PYTHIA3000 + PYTHIA4000 + PYTHIA5000 + PYTHIA6000)[:,1]

#print(PYTHIAall)

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
mask_pythia  = PYTHIAall != 0.0

#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

Additive        = QCD['NNLO'] + ( EWK['NLO'] - EWK['LO'] )
Factorize       = QCD['NNLO'] * np.where(mask_ewk, EWK['NLO'] / EWK['LO'], 0.0)
Mixed           = QCD['LO'] * np.where(mask_qcd, ((QCD['NLO'] - QCD['LO']) / QCD['LO']) , 0.0) * np.where(mask_ewk, ((EWK['NLO'] - EWK['LO']) / EWK['LO']), 0.0 )

RatioAdditivePYTHIA      = np.where(mask_pythia, ((Additive) / PYTHIAall), 0.0 )
RatioMixedPYTHIA         = np.where(mask_pythia, ((Additive + Mixed) / PYTHIAall), 0.0 )

print("mass[0-5]", pythiamass[0:5])
print("kfac_mixed",  RatioMixedPYTHIA[0:5])
print("@@ {}: 0-100 avg".format(lepton), np.average(RatioMixedPYTHIA[0:5]))

print("mass[5-10]", pythiamass[5:10])
print("kfac_mixed", RatioMixedPYTHIA[5:10])
print("@@ {}: 100-200 avg".format(lepton), np.average(RatioMixedPYTHIA[5:10]))

print(pythiamass[10:25])
print(RatioMixedPYTHIA[10:25])
print("@@ {}: 200-500 avg".format(lepton), np.average(RatioMixedPYTHIA[10:25]))

print(pythiamass[25:50])
print(RatioMixedPYTHIA[25:50])
print("@@ {}: 500-1000 avg".format(lepton), np.average(RatioMixedPYTHIA[25:50]))

print(pythiamass[50:100])
print(RatioMixedPYTHIA[50:100])
print("@@ {}: 1000-2000 avg".format(lepton), np.average(RatioMixedPYTHIA[50:100]))

print(pythiamass[100:150])
print(RatioMixedPYTHIA[100:150])
print("@@ {}: 2000-3000 avg".format(lepton), np.average(RatioMixedPYTHIA[100:150]))

print(pythiamass[150:200])
print(RatioMixedPYTHIA[150:200])
print("@@ {}: 3000-4000 avg".format(lepton), np.average(RatioMixedPYTHIA[150:200]))

print(pythiamass[200:250])
print(RatioMixedPYTHIA[200:250])
print("@@ {}: 4000-5000 avg".format(lepton), np.average(RatioMixedPYTHIA[200:250]))

print(pythiamass[250:300])
print(RatioMixedPYTHIA[250:300])
print("@@ {}: 5000-6000 avg".format(lepton), np.average(RatioMixedPYTHIA[250:300]))

print(pythiamass[300:400])
print(RatioMixedPYTHIA[300:400])
print("@@ {}: 6000-8000 avg".format(lepton), np.average(RatioMixedPYTHIA[300:400]))

title_qcd 	= "W_diff_QCD_xsec_{}_pythia.png".format(lepton) 
title_ewk 	= "W_diff_EWK_xsec_{}_pythia.png".format(lepton) 
title_add 	= "W_diff_Additive_xsec_{}_pythia.png".format(lepton) 
title_mix 	= "W_diff_Mixed_xsec_{}_pythia.png".format(lepton) 
title_final 	= "W_diff_Final_xsec_{}_pythia.png".format(lepton) 


#if lepton == "m":
#    lepton = "\mu"
#elif lepton == "t":
#    lepton = "\tau"

plt.style.use(hep.style.CMS)

fig = plt.figure(figsize=(10,10))
gs 	= GridSpec(nrows=2,ncols=1,height_ratios=[3,1])
#--------------------------------------------------------------------------------------------------------------------------
ax0 	= plt.subplot(gs[0])
#ax0.plot(mass, QCD['LO'] ,  'b<-', linewidth=0.3, markersize=1, label='QCD LO (FEWZ)')
ax0.plot(mass, Additive + Mixed  ,  'rv-', linewidth=0.3, markersize=1, label=r'Additive + Mixed, QCD $\times$ EW')
ax0.plot(mass, Additive  ,  'kv-', linewidth=0.3, markersize=1, label=r'Additive, QCD $\bigoplus$ EW')
#ax0.plot(mass, Factorize , 'g^-', linewidth=0.3, markersize=1, label=r'Factorize, QCD $\bigotimes$ EW')
ax0.plot(pythiamass, PYTHIAall,  'c<-', linewidth=0.3, markersize=1, label='PYTHIA LO (Default)')
ax0.set_xlim((100,8000))
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
ax1.plot(pythiamass, RatioMixedPYTHIA ,'rv-',linewidth=0.3, markersize=1, label='K factor = Additive + Mixed / PYTHIA LO')
ax1.plot(pythiamass, RatioAdditivePYTHIA ,'kv-',linewidth=0.3, markersize=1, label='K factor = Additive / PYTHIA LO')
#ax1.plot(mass,  Additive/PYTHIAall,'k^-',linewidth=0.3, markersize=1)
#ax1.plot(mass, Factorize/PYTHIAall,'g^-',linewidth=0.3, markersize=1)
#ax1.plot(mass, QCD['LO']/PYTHIAall,'r^-',linewidth=0.3, markersize=1)
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
ax1.hlines(1,100,8000,color='gray')
ax1.set_xlim((100,8000))
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
