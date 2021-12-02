# Generating training data

* To generate training data (MC toys) one runs the following command

```
nohup python <path to mg5_aMC> <path to runcard> &
```
Example runcards for VH production are provided [here](https://github.com/LHCfitNikhef/ML4EFT/tree/classifier_quad/code/cluster/event_generation/mg5_runcards).

* In case of multiple runcards we a script is provided [here](https://github.com/LHCfitNikhef/ML4EFT/tree/classifier_quad/code/cluster/event_generation/generate_events.sh) that submits jobs for each runcard in parallel.

* The lhe to npy converter lets one read in the events directly as a numpy array as opposed to lhe events. This is done for speed up purposes - reading in a lhe file and computing the kinematics for each event is too costly to on the fly.
The converter can be found [here](https://github.com/LHCfitNikhef/ML4EFT/blob/classifier_quad/code/cluster/event_generation/lhe_to_npy.sh)