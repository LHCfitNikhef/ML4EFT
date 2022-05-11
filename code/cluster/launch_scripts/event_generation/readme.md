# Generating training data

Generating training is done in two steps:

1. Create the event directory with `sh MG_init.sh <example_run>`
2. Generate events in parallel with `sh MGbatch.sh <example_run>`. 

One can modify the number of MC datasets by going into `mg5_runcards/example_run` and changing the value of `NDATASETS`.

