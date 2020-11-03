void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo27","canvas_plotflow_tempo27",0,0,700,500);
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
  S5_ETA_0->SetBinContent(8,1035.7260688);
  S5_ETA_0->SetBinContent(9,517.8630344);
  S5_ETA_0->SetBinContent(10,2589.315172);
  S5_ETA_0->SetBinContent(11,12946.57086);
  S5_ETA_0->SetBinContent(12,35214.6823392);
  S5_ETA_0->SetBinContent(13,77161.5851256);
  S5_ETA_0->SetBinContent(14,142930.209494);
  S5_ETA_0->SetBinContent(15,254788.616925);
  S5_ETA_0->SetBinContent(16,335575.222291);
  S5_ETA_0->SetBinContent(17,410665.327279);
  S5_ETA_0->SetBinContent(18,459862.330547);
  S5_ETA_0->SetBinContent(19,442255.029378);
  S5_ETA_0->SetBinContent(20,419469.027864);
  S5_ETA_0->SetBinContent(21,380111.42525);
  S5_ETA_0->SetBinContent(22,401861.726694);
  S5_ETA_0->SetBinContent(23,462451.630719);
  S5_ETA_0->SetBinContent(24,441737.129343);
  S5_ETA_0->SetBinContent(25,362504.12408);
  S5_ETA_0->SetBinContent(26,254788.616925);
  S5_ETA_0->SetBinContent(27,157430.310458);
  S5_ETA_0->SetBinContent(28,75090.134988);
  S5_ETA_0->SetBinContent(29,35214.6823392);
  S5_ETA_0->SetBinContent(30,8285.8085504);
  S5_ETA_0->SetBinContent(31,2589.315172);
  S5_ETA_0->SetBinContent(32,517.8630344);
  S5_ETA_0->SetBinContent(33,1035.7260688);
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
  THStack* stack = new THStack("mystack_28","mystack");
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
