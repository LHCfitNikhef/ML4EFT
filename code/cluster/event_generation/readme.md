# Generating training data

* To generate training data (MC toys) one runs the following command

```
nohup python <path to mg5_aMC> <path to runcard> &
```
Example runcards for VH production are provided [here](https://github.com/LHCfitNikhef/ML4EFT/tree/classifier_quad/code/cluster/event_generation/mg5_runcards).

* In case of multiple runcards we a script is provided [here](https://github.com/LHCfitNikhef/ML4EFT/tree/classifier_quad/code/cluster/event_generation/generate_events.sh) that submits jobs for each runcard in parallel.