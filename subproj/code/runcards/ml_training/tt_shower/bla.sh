{
  "process_id": "tt",
  "epochs": 2000,
  "lr": 0.001,
  "n_batches": 1,
  "output_size": 1,
  "hidden_sizes": [
    25,
    25,
    25
  ],
  "n_dat": 100000,
  "event_data": "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt_llvlvlbb",
  "features": [
    "pt_ll",
    "eta_l1"
  ],
  "loss_type": "CE",
  "scaler_type": "robust",
  "patience": 100,
  "val_ratio": 0.2,
  "c_train": {
    "cQd8": 10,
    "cQj18": 10,
    "cQj38": 10,
    "cQu8": 10,
    "ctd8": 10,
    "ctGRe": -10,
    "ctj8": 10,
    "ctu8": 10
  }
}