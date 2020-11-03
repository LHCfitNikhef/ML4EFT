void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo31","canvas_plotflow_tempo31",0,0,700,500);
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
  TH1F* S7_ETA_0 = new TH1F("S7_ETA_0","S7_ETA_0",40,-10.0,10.0);
  // Content
  S7_ETA_0->SetBinContent(0,0.0); // underflow
  S7_ETA_0->SetBinContent(1,0.0);
  S7_ETA_0->SetBinContent(2,0.0);
  S7_ETA_0->SetBinContent(3,0.0);
  S7_ETA_0->SetBinContent(4,0.0);
  S7_ETA_0->SetBinContent(5,0.0);
  S7_ETA_0->SetBinContent(6,0.0);
  S7_ETA_0->SetBinContent(7,517.863013);
  S7_ETA_0->SetBinContent(8,517.863013);
  S7_ETA_0->SetBinContent(9,1035.726026);
  S7_ETA_0->SetBinContent(10,4660.767117);
  S7_ETA_0->SetBinContent(11,14500.160364);
  S7_ETA_0->SetBinContent(12,35214.680884);
  S7_ETA_0->SetBinContent(13,77161.581937);
  S7_ETA_0->SetBinContent(14,144483.803627);
  S7_ETA_0->SetBinContent(15,260485.106539);
  S7_ETA_0->SetBinContent(16,367164.909217);
  S7_ETA_0->SetBinContent(17,427754.810738);
  S7_ETA_0->SetBinContent(18,441219.311076);
  S7_ETA_0->SetBinContent(19,410147.510296);
  S7_ETA_0->SetBinContent(20,401343.810075);
  S7_ETA_0->SetBinContent(21,397718.809984);
  S7_ETA_0->SetBinContent(22,422058.310595);
  S7_ETA_0->SetBinContent(23,484719.712168);
  S7_ETA_0->SetBinContent(24,417915.410491);
  S7_ETA_0->SetBinContent(25,355771.908931);
  S7_ETA_0->SetBinContent(26,229931.205772);
  S7_ETA_0->SetBinContent(27,161573.204056);
  S7_ETA_0->SetBinContent(28,72500.82182);
  S7_ETA_0->SetBinContent(29,32625.370819);
  S7_ETA_0->SetBinContent(30,13982.300351);
  S7_ETA_0->SetBinContent(31,2071.452052);
  S7_ETA_0->SetBinContent(32,1035.726026);
  S7_ETA_0->SetBinContent(33,517.863013);
  S7_ETA_0->SetBinContent(34,0.0);
  S7_ETA_0->SetBinContent(35,0.0);
  S7_ETA_0->SetBinContent(36,0.0);
  S7_ETA_0->SetBinContent(37,0.0);
  S7_ETA_0->SetBinContent(38,0.0);
  S7_ETA_0->SetBinContent(39,0.0);
  S7_ETA_0->SetBinContent(40,0.0);
  S7_ETA_0->SetBinContent(41,0.0); // overflow
  S7_ETA_0->SetEntries(10000);
  // Style
  S7_ETA_0->SetLineColor(9);
  S7_ETA_0->SetLineStyle(1);
  S7_ETA_0->SetLineWidth(1);
  S7_ETA_0->SetFillColor(9);
  S7_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_32","mystack");
  stack->Add(S7_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ t_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_6.eps");

}
