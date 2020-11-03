void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo11","canvas_plotflow_tempo11",0,0,700,500);
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
  S6_PT_0->SetBinContent(1,56875.05692);
  S6_PT_0->SetBinContent(2,155113.7916);
  S6_PT_0->SetBinContent(3,252835.486308);
  S6_PT_0->SetBinContent(4,347971.981156);
  S6_PT_0->SetBinContent(5,394506.078636);
  S6_PT_0->SetBinContent(6,399676.578356);
  S6_PT_0->SetBinContent(7,435352.676424);
  S6_PT_0->SetBinContent(8,411568.577712);
  S6_PT_0->SetBinContent(9,387267.479028);
  S6_PT_0->SetBinContent(10,343318.581408);
  S6_PT_0->SetBinContent(11,328841.282192);
  S6_PT_0->SetBinContent(12,265244.585636);
  S6_PT_0->SetBinContent(13,236807.087176);
  S6_PT_0->SetBinContent(14,193375.189528);
  S6_PT_0->SetBinContent(15,168556.990872);
  S6_PT_0->SetBinContent(16,132363.792832);
  S6_PT_0->SetBinContent(17,116852.393672);
  S6_PT_0->SetBinContent(18,99789.874596);
  S6_PT_0->SetBinContent(19,78073.945772);
  S6_PT_0->SetBinContent(20,62562.566612);
  S6_PT_0->SetBinContent(21,51187.557228);
  S6_PT_0->SetBinContent(22,44465.957592);
  S6_PT_0->SetBinContent(23,29988.668376);
  S6_PT_0->SetBinContent(24,34125.038152);
  S6_PT_0->SetBinContent(25,20164.788908);
  S6_PT_0->SetBinContent(26,23267.06874);
  S6_PT_0->SetBinContent(27,15511.37916);
  S6_PT_0->SetBinContent(28,11892.059356);
  S6_PT_0->SetBinContent(29,9306.827496);
  S6_PT_0->SetBinContent(30,6721.597636);
  S6_PT_0->SetBinContent(31,7238.643608);
  S6_PT_0->SetBinContent(32,5687.505692);
  S6_PT_0->SetBinContent(33,3619.321804);
  S6_PT_0->SetBinContent(34,5687.505692);
  S6_PT_0->SetBinContent(35,3619.321804);
  S6_PT_0->SetBinContent(36,6204.551664);
  S6_PT_0->SetBinContent(37,3102.275832);
  S6_PT_0->SetBinContent(38,3102.275832);
  S6_PT_0->SetBinContent(39,1551.137916);
  S6_PT_0->SetBinContent(40,1034.091944);
  S6_PT_0->SetBinContent(41,16028.429132); // overflow
  S6_PT_0->SetEntries(10000);
  // Style
  S6_PT_0->SetLineColor(9);
  S6_PT_0->SetLineStyle(1);
  S6_PT_0->SetLineWidth(1);
  S6_PT_0->SetFillColor(9);
  S6_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_12","mystack");
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
