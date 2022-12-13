# Generating training data

Generating training is done in two steps:

1. Create the event directory with `sh MG_init.sh <example_run>`. In case conditional cuts are required, it is possible
   to specify these in `custom_cuts/dummy_fct.f` and `custom_cuts/kin_functions.f` .
2. Generate events in parallel with `sh MGbatch_<process>.sh <example_run>`. 

One can modify the number of MC datasets by opening `MGbatch_<process>.sh` and changing the value of `NDATASETS`.

