#include <iostream>
#include <fstream>
#include <TH1F.h>
#include <TFile.h>

void Readhist(){

    TFile *fe = new TFile("/d0/scratch/jelee/workspace/git_update/histograms_t_mgmlm.root");
    cout << "start" << endl;
    //TH1F* he120 = (TH1F*) fe->Get("tnu_120to200_lhe_m_inv");
    TH1F* he400 = (TH1F*) fe->Get("tnu_400to800_lhe_m_inv");
    TH1F* he800 = (TH1F*) fe->Get("tnu_800to1500_lhe_m_inv");
    TH1F* he1500 = (TH1F*) fe->Get("tnu_1500to2500_lhe_m_inv");
    TH1F* he2500 = (TH1F*) fe->Get("tnu_2500to4000_lhe_m_inv");
    TH1F* he4000 = (TH1F*) fe->Get("tnu_4000to6000_lhe_m_inv");
    TH1F* he6000 = (TH1F*) fe->Get("tnu_6000_lhe_m_inv");

    int binCount = he400->GetNbinsX();
    //cout << "pass binCount = " << binCount << endl;

   // std::ofstream fe120_out("out_tau120_mg.txt");
   // if (fe120_out.is_open()) {
   //     for (int i = 1; i <= binCount; ++i) {
   //          fe120_out << he120->GetBinCenter(i) << " " << he120->GetBinContent(i) << endl;
   //          //cout << "pass 3step = " << i << " " << xbin << " " << bincontent << endl;
   //     }
   // }
   // fe120_out.close();

    std::ofstream fe400_out("out_tau400_mg.txt");
    if (fe400_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe400_out << he400->GetBinCenter(i) << " " << he400->GetBinContent(i) << endl;
        }
    }
    fe400_out.close();

    std::ofstream fe800_out("out_tau800_mg.txt");
    if (fe800_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe800_out << he800->GetBinCenter(i) << " " << he800->GetBinContent(i) << endl;
        }
    }
    fe800_out.close();

    std::ofstream fe1500_out("out_tau1500_mg.txt");
    if (fe1500_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe1500_out << he1500->GetBinCenter(i) << " " << he1500->GetBinContent(i) << endl;
        }
    }
    fe1500_out.close();

    std::ofstream fe2500_out("out_tau2500_mg.txt");
    if (fe2500_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe2500_out << he2500->GetBinCenter(i) << " " << he2500->GetBinContent(i) << endl;
        }
    }
    fe2500_out.close();

    std::ofstream fe4000_out("out_tau4000_mg.txt");
    if (fe4000_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe4000_out << he4000->GetBinCenter(i) << " " << he4000->GetBinContent(i) << endl;
        }
    }
    fe4000_out.close();

    std::ofstream fe6000_out("out_tau6000_mg.txt");
    if (fe6000_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe6000_out << he6000->GetBinCenter(i) << " " << he6000->GetBinContent(i) << endl;
        }
    }
    fe6000_out.close();

    delete fe;
}

//GetBinCenter
//GetBinContent
//GetBinError
//GetBinErrorLow
//GetBinErrorOption
//GetBinErrorUp
//GetBinLowEdge
//
