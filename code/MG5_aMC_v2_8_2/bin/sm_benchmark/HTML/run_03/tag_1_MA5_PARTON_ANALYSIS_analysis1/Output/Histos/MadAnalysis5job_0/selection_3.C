void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo97","canvas_plotflow_tempo97",0,0,700,500);
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
  S4_PT_0->SetBinContent(1,58575.1284632);
  S4_PT_0->SetBinContent(2,159137.795825);
  S4_PT_0->SetBinContent(3,243112.693622);
  S4_PT_0->SetBinContent(4,332271.291282);
  S4_PT_0->SetBinContent(5,402250.489446);
  S4_PT_0->SetBinContent(6,431278.888685);
  S4_PT_0->SetBinContent(7,409507.589256);
  S4_PT_0->SetBinContent(8,404323.889392);
  S4_PT_0->SetBinContent(9,395511.689623);
  S4_PT_0->SetBinContent(10,359226.290575);
  S4_PT_0->SetBinContent(11,320867.291582);
  S4_PT_0->SetBinContent(12,268512.592955);
  S4_PT_0->SetBinContent(13,232227.093907);
  S4_PT_0->SetBinContent(14,184019.195172);
  S4_PT_0->SetBinContent(15,157582.695866);
  S4_PT_0->SetBinContent(16,143586.796233);
  S4_PT_0->SetBinContent(17,114558.396994);
  S4_PT_0->SetBinContent(18,92268.7875792);
  S4_PT_0->SetBinContent(19,68942.4081912);
  S4_PT_0->SetBinContent(20,61166.9483952);
  S4_PT_0->SetBinContent(21,51836.39864);
  S4_PT_0->SetBinContent(22,45616.0288032);
  S4_PT_0->SetBinContent(23,45097.6688168);
  S4_PT_0->SetBinContent(24,29028.3792384);
  S4_PT_0->SetBinContent(25,30583.4791976);
  S4_PT_0->SetBinContent(26,22808.0194016);
  S4_PT_0->SetBinContent(27,17106.0095512);
  S4_PT_0->SetBinContent(28,14514.1896192);
  S4_PT_0->SetBinContent(29,10885.6397144);
  S4_PT_0->SetBinContent(30,9848.9157416);
  S4_PT_0->SetBinContent(31,7257.0958096);
  S4_PT_0->SetBinContent(32,7257.0958096);
  S4_PT_0->SetBinContent(33,8293.8237824);
  S4_PT_0->SetBinContent(34,6220.3678368);
  S4_PT_0->SetBinContent(35,7257.0958096);
  S4_PT_0->SetBinContent(36,6220.3678368);
  S4_PT_0->SetBinContent(37,2591.819932);
  S4_PT_0->SetBinContent(38,3628.5479048);
  S4_PT_0->SetBinContent(39,3628.5479048);
  S4_PT_0->SetBinContent(40,2073.4559456);
  S4_PT_0->SetBinContent(41,12959.09966); // overflow
  S4_PT_0->SetEntries(10000);
  // Style
  S4_PT_0->SetLineColor(9);
  S4_PT_0->SetLineStyle(1);
  S4_PT_0->SetLineWidth(1);
  S4_PT_0->SetFillColor(9);
  S4_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_98","mystack");
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
