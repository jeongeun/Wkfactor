#include <iostream>
#include <fstream>
#include <TH1F.h>
#include <TFile.h>

void Readhist_pythia(){

    TFile *fe = new TFile("../NanoAODAna/CMSSW_13_0_13/src/lnuSpectrumNanoAOD/histograms_t_pythia.root");
    cout << "start" << endl;
    TH1F* he100  = (TH1F*) fe->Get("tnu_100to200_scalePDF");
    TH1F* he200  = (TH1F*) fe->Get("tnu_200to500_scalePDF");
    TH1F* he500  = (TH1F*) fe->Get("tnu_500to1000_scalePDF");
    TH1F* he1000 = (TH1F*) fe->Get("tnu_1000to2000_scalePDF");
    TH1F* he2000 = (TH1F*) fe->Get("tnu_2000to3000_scalePDF");
    TH1F* he3000 = (TH1F*) fe->Get("tnu_3000to4000_scalePDF");
    TH1F* he4000 = (TH1F*) fe->Get("tnu_4000to5000_scalePDF");
    TH1F* he5000 = (TH1F*) fe->Get("tnu_5000to6000_scalePDF");
    TH1F* he6000 = (TH1F*) fe->Get("tnu_6000_scalePDF");

    int binCount = he100->GetNbinsX();
    //cout << "pass binCount = " << binCount << endl;

    std::ofstream fe100_out("out_t100_pythia.txt");
    if (fe100_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe100_out << he100->GetBinCenter(i) << " " << he100->GetBinContent(i) << endl;
             //cout << "pass 3step = " << i << " " << xbin << " " << bincontent << endl;
        }
    }
    fe100_out.close();

    std::ofstream fe200_out("out_t200_pythia.txt");
    if (fe200_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe200_out << he200->GetBinCenter(i) << " " << he200->GetBinContent(i) << endl;
        }
    }
    fe200_out.close();

    std::ofstream fe500_out("out_t500_pythia.txt");
    if (fe500_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe500_out << he500->GetBinCenter(i) << " " << he500->GetBinContent(i) << endl;
        }
    }
    fe500_out.close();

    std::ofstream fe1000_out("out_t1000_pythia.txt");
    if (fe1000_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe1000_out << he1000->GetBinCenter(i) << " " << he1000->GetBinContent(i) << endl;
        }
    }
    fe1000_out.close();

    std::ofstream fe2000_out("out_t2000_pythia.txt");
    if (fe2000_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe2000_out << he2000->GetBinCenter(i) << " " << he2000->GetBinContent(i) << endl;
        }
    }
    fe2000_out.close();

    std::ofstream fe3000_out("out_t3000_pythia.txt");
    if (fe3000_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe3000_out << he3000->GetBinCenter(i) << " " << he3000->GetBinContent(i) << endl;
        }
    }
    fe3000_out.close();

    std::ofstream fe4000_out("out_t4000_pythia.txt");
    if (fe4000_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe4000_out << he4000->GetBinCenter(i) << " " << he4000->GetBinContent(i) << endl;
        }
    }
    fe4000_out.close();

    std::ofstream fe5000_out("out_t5000_pythia.txt");
    if (fe5000_out.is_open()) {
        for (int i = 1; i <= binCount; ++i) {
             fe5000_out << he5000->GetBinCenter(i) << " " << he5000->GetBinContent(i) << endl;
        }
    }
    fe5000_out.close();

    std::ofstream fe6000_out("out_t6000_pythia.txt");
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
