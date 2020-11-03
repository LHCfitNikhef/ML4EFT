void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo29","canvas_plotflow_tempo29",0,0,700,500);
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
  TH1F* S6_PT_0 = new TH1F("S6_PT_0","S6_PT_0",40,0.0,500.0);
  // Content
  S6_PT_0->SetBinContent(0,0.0); // underflow
  S6_PT_0->SetBinContent(1,50232.7139673);
  S6_PT_0->SetBinContent(2,153287.412106);
  S6_PT_0->SetBinContent(3,256860.020286);
  S6_PT_0->SetBinContent(4,312271.424663);
  S6_PT_0->SetBinContent(5,384772.230389);
  S6_PT_0->SetBinContent(6,430344.133988);
  S6_PT_0->SetBinContent(7,409629.632352);
  S6_PT_0->SetBinContent(8,432415.634152);
  S6_PT_0->SetBinContent(9,383218.630266);
  S6_PT_0->SetBinContent(10,381665.030143);
  S6_PT_0->SetBinContent(11,309164.224417);
  S6_PT_0->SetBinContent(12,266699.421063);
  S6_PT_0->SetBinContent(13,239252.718896);
  S6_PT_0->SetBinContent(14,191091.415092);
  S6_PT_0->SetBinContent(15,170376.913456);
  S6_PT_0->SetBinContent(16,135680.110716);
  S6_PT_0->SetBinContent(17,107715.508507);
  S6_PT_0->SetBinContent(18,94768.9274847);
  S6_PT_0->SetBinContent(19,78197.3161759);
  S6_PT_0->SetBinContent(20,66804.3252761);
  S6_PT_0->SetBinContent(21,54893.4843354);
  S6_PT_0->SetBinContent(22,39875.4531493);
  S6_PT_0->SetBinContent(23,36250.412863);
  S6_PT_0->SetBinContent(24,36768.2729039);
  S6_PT_0->SetBinContent(25,25893.152045);
  S6_PT_0->SetBinContent(26,27964.6022086);
  S6_PT_0->SetBinContent(27,17089.4813497);
  S6_PT_0->SetBinContent(28,11910.8509407);
  S6_PT_0->SetBinContent(29,12946.5710225);
  S6_PT_0->SetBinContent(30,7250.0825726);
  S6_PT_0->SetBinContent(31,9839.3977771);
  S6_PT_0->SetBinContent(32,7767.9456135);
  S6_PT_0->SetBinContent(33,4660.7673681);
  S6_PT_0->SetBinContent(34,5178.630409);
  S6_PT_0->SetBinContent(35,4142.9043272);
  S6_PT_0->SetBinContent(36,4660.7673681);
  S6_PT_0->SetBinContent(37,2589.3152045);
  S6_PT_0->SetBinContent(38,3107.1782454);
  S6_PT_0->SetBinContent(39,1035.7260818);
  S6_PT_0->SetBinContent(40,1553.5891227);
  S6_PT_0->SetBinContent(41,8803.6716953); // overflow
  S6_PT_0->SetEntries(10000);
  // Style
  S6_PT_0->SetLineColor(9);
  S6_PT_0->SetLineStyle(1);
  S6_PT_0->SetLineWidth(1);
  S6_PT_0->SetFillColor(9);
  S6_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_30","mystack");
  stack->Add(S6_PT_0);
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
  stack->GetXaxis()->SetTitle("p_{T} [ t_{1} ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_5.eps");

}
