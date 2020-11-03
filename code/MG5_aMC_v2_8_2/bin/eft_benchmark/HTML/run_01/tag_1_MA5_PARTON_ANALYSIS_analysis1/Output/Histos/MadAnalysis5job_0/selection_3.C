void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo43","canvas_plotflow_tempo43",0,0,700,500);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  canvas->SetHighLightColor(2);
  canvas->SetFillColor(0);
  canvas->SetBorderMode(0);
  canvas->SetBorderSize(3);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(0);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
  canvas->SetLeftMargin(0.14);
  canvas->SetRightMargin(0.05);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S4_PT_0 = new TH1F("S4_PT_0","S4_PT_0",40,0.0,500.0);
  // Content
  S4_PT_0->SetBinContent(0,0.0); // underflow
  S4_PT_0->SetBinContent(1,17023.0035637);
  S4_PT_0->SetBinContent(2,46086.6660338);
  S4_PT_0->SetBinContent(3,71967.1748098);
  S4_PT_0->SetBinContent(4,98401.269638);
  S4_PT_0->SetBinContent(5,112241.110909);
  S4_PT_0->SetBinContent(6,114870.728542);
  S4_PT_0->SetBinContent(7,116254.674676);
  S4_PT_0->SetBinContent(8,107535.574075);
  S4_PT_0->SetBinContent(9,105182.805658);
  S4_PT_0->SetBinContent(10,88990.175974);
  S4_PT_0->SetBinContent(11,79717.4869215);
  S4_PT_0->SetBinContent(12,62140.8911067);
  S4_PT_0->SetBinContent(13,58542.5311764);
  S4_PT_0->SetBinContent(14,48993.0329007);
  S4_PT_0->SetBinContent(15,39581.9454355);
  S4_PT_0->SetBinContent(16,36121.983918);
  S4_PT_0->SetBinContent(17,30586.0494092);
  S4_PT_0->SetBinContent(18,20206.1634567);
  S4_PT_0->SetBinContent(19,20621.3672933);
  S4_PT_0->SetBinContent(20,17576.5958148);
  S4_PT_0->SetBinContent(21,13563.048245);
  S4_PT_0->SetBinContent(22,11625.4674676);
  S4_PT_0->SetBinContent(23,10518.2805658);
  S4_PT_0->SetBinContent(24,7335.11547377);
  S4_PT_0->SetBinContent(25,7888.70892465);
  S4_PT_0->SetBinContent(26,5259.1392831);
  S4_PT_0->SetBinContent(27,5535.93650845);
  S4_PT_0->SetBinContent(28,4151.95238134);
  S4_PT_0->SetBinContent(29,3459.96031778);
  S4_PT_0->SetBinContent(30,2906.3668669);
  S4_PT_0->SetBinContent(31,2075.97619067);
  S4_PT_0->SetBinContent(32,2214.37480334);
  S4_PT_0->SetBinContent(33,968.788888979);
  S4_PT_0->SetBinContent(34,1107.18690176);
  S4_PT_0->SetBinContent(35,1383.98412711);
  S4_PT_0->SetBinContent(36,1383.98412711);
  S4_PT_0->SetBinContent(37,691.992063556);
  S4_PT_0->SetBinContent(38,1107.18690176);
  S4_PT_0->SetBinContent(39,968.788888979);
  S4_PT_0->SetBinContent(40,830.390476268);
  S4_PT_0->SetBinContent(41,5259.1392831); // overflow
  S4_PT_0->SetEntries(10000);
  // Style
  S4_PT_0->SetLineColor(9);
  S4_PT_0->SetLineStyle(1);
  S4_PT_0->SetLineWidth(1);
  S4_PT_0->SetFillColor(9);
  S4_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_44","mystack");
  stack->Add(S4_PT_0);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("Events  ( L_{int} = 10 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("p_{T} [ t~_{1} ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_3.eps");

}
