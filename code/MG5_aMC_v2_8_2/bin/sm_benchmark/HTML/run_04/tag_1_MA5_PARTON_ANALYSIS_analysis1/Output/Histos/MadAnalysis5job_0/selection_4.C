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
  S5_ETA_0->SetBinContent(6,518.9789946);
  S5_ETA_0->SetBinContent(7,0.0);
  S5_ETA_0->SetBinContent(8,518.9789946);
  S5_ETA_0->SetBinContent(9,1037.9579892);
  S5_ETA_0->SetBinContent(10,3632.8529622);
  S5_ETA_0->SetBinContent(11,15569.369838);
  S5_ETA_0->SetBinContent(12,39961.3795842);
  S5_ETA_0->SetBinContent(13,72138.0792494);
  S5_ETA_0->SetBinContent(14,154136.798396);
  S5_ETA_0->SetBinContent(15,270388.097187);
  S5_ETA_0->SetBinContent(16,359652.396258);
  S5_ETA_0->SetBinContent(17,412069.295712);
  S5_ETA_0->SetBinContent(18,473308.895075);
  S5_ETA_0->SetBinContent(19,427638.69555);
  S5_ETA_0->SetBinContent(20,388715.295955);
  S5_ETA_0->SetBinContent(21,398056.895858);
  S5_ETA_0->SetBinContent(22,436461.295459);
  S5_ETA_0->SetBinContent(23,424524.795583);
  S5_ETA_0->SetBinContent(24,433866.395486);
  S5_ETA_0->SetBinContent(25,336817.396495);
  S5_ETA_0->SetBinContent(26,244439.097457);
  S5_ETA_0->SetBinContent(27,159326.598342);
  S5_ETA_0->SetBinContent(28,77846.84919);
  S5_ETA_0->SetBinContent(29,36328.529622);
  S5_ETA_0->SetBinContent(30,15050.3898434);
  S5_ETA_0->SetBinContent(31,4670.8109514);
  S5_ETA_0->SetBinContent(32,2594.894973);
  S5_ETA_0->SetBinContent(33,518.9789946);
  S5_ETA_0->SetBinContent(34,0.0);
  S5_ETA_0->SetBinContent(35,0.0);
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
