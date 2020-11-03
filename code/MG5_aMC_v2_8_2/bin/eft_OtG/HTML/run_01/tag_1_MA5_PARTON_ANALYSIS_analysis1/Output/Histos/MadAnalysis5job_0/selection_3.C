void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo115","canvas_plotflow_tempo115",0,0,700,500);
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
  S4_PT_0->SetBinContent(1,75742.952709);
  S4_PT_0->SetBinContent(2,212080.279585);
  S4_PT_0->SetBinContent(3,339196.667349);
  S4_PT_0->SetBinContent(4,435357.358093);
  S4_PT_0->SetBinContent(5,478827.253908);
  S4_PT_0->SetBinContent(6,534811.148519);
  S4_PT_0->SetBinContent(7,564449.645666);
  S4_PT_0->SetBinContent(8,536128.448392);
  S4_PT_0->SetBinContent(9,513076.150611);
  S4_PT_0->SetBinContent(10,432064.15841);
  S4_PT_0->SetBinContent(11,367517.964623);
  S4_PT_0->SetBinContent(12,334586.267793);
  S4_PT_0->SetBinContent(13,296385.47147);
  S4_PT_0->SetBinContent(14,244353.376479);
  S4_PT_0->SetBinContent(15,206152.580156);
  S4_PT_0->SetBinContent(16,165975.884023);
  S4_PT_0->SetBinContent(17,162682.68434);
  S4_PT_0->SetBinContent(18,106698.789729);
  S4_PT_0->SetBinContent(19,114602.388968);
  S4_PT_0->SetBinContent(20,88915.641441);
  S4_PT_0->SetBinContent(21,65204.8037234);
  S4_PT_0->SetBinContent(22,40835.3360692);
  S4_PT_0->SetBinContent(23,39518.066196);
  S4_PT_0->SetBinContent(24,34907.6266398);
  S4_PT_0->SetBinContent(25,23710.8377176);
  S4_PT_0->SetBinContent(26,24369.4776542);
  S4_PT_0->SetBinContent(27,21734.9379078);
  S4_PT_0->SetBinContent(28,25686.7375274);
  S4_PT_0->SetBinContent(29,13172.688732);
  S4_PT_0->SetBinContent(30,17783.1282882);
  S4_PT_0->SetBinContent(31,8562.2471758);
  S4_PT_0->SetBinContent(32,8562.2471758);
  S4_PT_0->SetBinContent(33,5269.0754928);
  S4_PT_0->SetBinContent(34,5927.7094294);
  S4_PT_0->SetBinContent(35,4610.4405562);
  S4_PT_0->SetBinContent(36,1975.9028098);
  S4_PT_0->SetBinContent(37,4610.4405562);
  S4_PT_0->SetBinContent(38,2634.5377464);
  S4_PT_0->SetBinContent(39,1975.9028098);
  S4_PT_0->SetBinContent(40,5269.0754928);
  S4_PT_0->SetBinContent(41,20417.6680346); // overflow
  S4_PT_0->SetEntries(10000);
  // Style
  S4_PT_0->SetLineColor(9);
  S4_PT_0->SetLineStyle(1);
  S4_PT_0->SetLineWidth(1);
  S4_PT_0->SetFillColor(9);
  S4_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_116","mystack");
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
