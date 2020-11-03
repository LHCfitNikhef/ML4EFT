void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo9","canvas_plotflow_tempo9",0,0,700,500);
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
  TH1F* S5_ETA_0 = new TH1F("S5_ETA_0","S5_ETA_0",40,-10.0,10.0);
  // Content
  S5_ETA_0->SetBinContent(0,0.0); // underflow
  S5_ETA_0->SetBinContent(1,0.0);
  S5_ETA_0->SetBinContent(2,0.0);
  S5_ETA_0->SetBinContent(3,0.0);
  S5_ETA_0->SetBinContent(4,0.0);
  S5_ETA_0->SetBinContent(5,0.0);
  S5_ETA_0->SetBinContent(6,0.0);
  S5_ETA_0->SetBinContent(7,0.0);
  S5_ETA_0->SetBinContent(8,519.824961);
  S5_ETA_0->SetBinContent(9,1039.649922);
  S5_ETA_0->SetBinContent(10,9876.674259);
  S5_ETA_0->SetBinContent(11,10396.49922);
  S5_ETA_0->SetBinContent(12,33788.627465);
  S5_ETA_0->SetBinContent(13,67057.424969);
  S5_ETA_0->SetBinContent(14,161145.78791);
  S5_ETA_0->SetBinContent(15,267709.879915);
  S5_ETA_0->SetBinContent(16,354520.673402);
  S5_ETA_0->SetBinContent(17,435613.367318);
  S5_ETA_0->SetBinContent(18,448608.966343);
  S5_ETA_0->SetBinContent(19,415859.9688);
  S5_ETA_0->SetBinContent(20,419498.768527);
  S5_ETA_0->SetBinContent(21,410661.76919);
  S5_ETA_0->SetBinContent(22,408062.569385);
  S5_ETA_0->SetBinContent(23,433534.067474);
  S5_ETA_0->SetBinContent(24,440811.566928);
  S5_ETA_0->SetBinContent(25,348282.77387);
  S5_ETA_0->SetBinContent(26,234441.082411);
  S5_ETA_0->SetBinContent(27,151788.888612);
  S5_ETA_0->SetBinContent(28,81612.523877);
  S5_ETA_0->SetBinContent(29,36387.74727);
  S5_ETA_0->SetBinContent(30,16634.398752);
  S5_ETA_0->SetBinContent(31,6237.899532);
  S5_ETA_0->SetBinContent(32,2599.124805);
  S5_ETA_0->SetBinContent(33,519.824961);
  S5_ETA_0->SetBinContent(34,519.824961);
  S5_ETA_0->SetBinContent(35,519.824961);
  S5_ETA_0->SetBinContent(36,0.0);
  S5_ETA_0->SetBinContent(37,0.0);
  S5_ETA_0->SetBinContent(38,0.0);
  S5_ETA_0->SetBinContent(39,0.0);
  S5_ETA_0->SetBinContent(40,0.0);
  S5_ETA_0->SetBinContent(41,0.0); // overflow
  S5_ETA_0->SetEntries(10000);
  // Style
  S5_ETA_0->SetLineColor(9);
  S5_ETA_0->SetLineStyle(1);
  S5_ETA_0->SetLineWidth(1);
  S5_ETA_0->SetFillColor(9);
  S5_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_10","mystack");
  stack->Add(S5_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ t~_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_4.eps");

}
