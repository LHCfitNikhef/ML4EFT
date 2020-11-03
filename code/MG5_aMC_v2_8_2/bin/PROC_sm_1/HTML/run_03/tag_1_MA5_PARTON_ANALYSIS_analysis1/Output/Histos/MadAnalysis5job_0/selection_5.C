void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo101","canvas_plotflow_tempo101",0,0,700,500);
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
  S6_PT_0->SetBinContent(1,49447.6627244);
  S6_PT_0->SetBinContent(2,155406.908562);
  S6_PT_0->SetBinContent(3,231596.71276);
  S6_PT_0->SetBinContent(4,302236.216652);
  S6_PT_0->SetBinContent(5,366820.920211);
  S6_PT_0->SetBinContent(6,421818.823241);
  S6_PT_0->SetBinContent(7,417782.323018);
  S6_PT_0->SetBinContent(8,417782.323018);
  S6_PT_0->SetBinContent(9,363793.520044);
  S6_PT_0->SetBinContent(10,360261.519849);
  S6_PT_0->SetBinContent(11,333014.918348);
  S6_PT_0->SetBinContent(12,270953.014929);
  S6_PT_0->SetBinContent(13,239165.213177);
  S6_PT_0->SetBinContent(14,188203.910369);
  S6_PT_0->SetBinContent(15,165498.309118);
  S6_PT_0->SetBinContent(16,121600.9067);
  S6_PT_0->SetBinContent(17,104950.105782);
  S6_PT_0->SetBinContent(18,87290.2648094);
  S6_PT_0->SetBinContent(19,76189.7741978);
  S6_PT_0->SetBinContent(20,62566.4334472);
  S6_PT_0->SetBinContent(21,60548.163336);
  S6_PT_0->SetBinContent(22,46420.2625576);
  S6_PT_0->SetBinContent(23,32796.921807);
  S6_PT_0->SetBinContent(24,26237.5414456);
  S6_PT_0->SetBinContent(25,22705.561251);
  S6_PT_0->SetBinContent(26,20687.2911398);
  S6_PT_0->SetBinContent(27,16146.1808896);
  S6_PT_0->SetBinContent(28,11100.5006116);
  S6_PT_0->SetBinContent(29,11605.0606394);
  S6_PT_0->SetBinContent(30,6559.3843614);
  S6_PT_0->SetBinContent(31,6559.3843614);
  S6_PT_0->SetBinContent(32,7568.520417);
  S6_PT_0->SetBinContent(33,6559.3843614);
  S6_PT_0->SetBinContent(34,3531.9761946);
  S6_PT_0->SetBinContent(35,4541.1122502);
  S6_PT_0->SetBinContent(36,5045.680278);
  S6_PT_0->SetBinContent(37,3027.4081668);
  S6_PT_0->SetBinContent(38,2018.2721112);
  S6_PT_0->SetBinContent(39,2018.2721112);
  S6_PT_0->SetBinContent(40,2522.840139);
  S6_PT_0->SetBinContent(41,11100.5006116); // overflow
  S6_PT_0->SetEntries(10000);
  // Style
  S6_PT_0->SetLineColor(9);
  S6_PT_0->SetLineStyle(1);
  S6_PT_0->SetLineWidth(1);
  S6_PT_0->SetFillColor(9);
  S6_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_102","mystack");
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
