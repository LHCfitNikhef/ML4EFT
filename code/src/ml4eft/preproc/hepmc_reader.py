import pyhepmc
import numpy as np
import cachetools.func
import pandas as pd
import os
from particle import Particle


event_file = "/data/theorie/pherbsch/MG5_aMC_v3_4_1/small_shower_test/Events/run_01/tag_1_pythia8_events.hepmc"
# save_loc = <save_loc >

# I'm using caching since we'll be using the final_state_particles often and we don't want to calculate it again.
# Depending on the hepmc file size, the caching might be too short and I'm not sure if the cache resets when we run the same file again.
# The reading of the particles is by far the bottleneck of this code.


@cachetools.func.ttl_cache(ttl=60*30)
def read_particles(hepmc_file):
    final_state_particles = []
    with pyhepmc.open(event_file) as f:
        event = f.read()
        xsec = event.weights[0]
        while event is not None:
            final_state_particles += [p for p in event.particles if p.status == 1]
            event = f.read()
    return final_state_particles, xsec


final_state_particles, xsec = read_particles(event_file)


# here we can specify the particle and the properties we'd like to read from the hepmc file.
particle_name = "e+"
pid = int(Particle.from_name(particle_name).pdgid)
# particle_name = input("Enter a particle name: ")         ##you can turn on a prompt to enter the particle name

transverse_momenta = []

pids = np.array([p.pid for p in final_state_particles])


mask = pids == pid
if mask.any():
    for p in final_state_particles:
        if p.pid == pid:
            transverse_momenta.append(
                np.sqrt(p.momentum.px**2 + p.momentum.py**2))

# make an array of energies of the final state particles
# energies = np.array([p.momentum.e for p in final_state_particles])

# Convert the list to a numpy array
transverse_momenta = np.array(transverse_momenta)


# Create an empty DataFrame
df = pd.DataFrame()

# Add a column for transverse momentum of electrons
df['pt_e'] = transverse_momenta

# add the cross section of the process as a first row in the dataframe
df = pd.concat([pd.DataFrame([xsec], columns=df.columns), df],
               ignore_index=True)

# here I'm saving the pandas dataframe as a pkl.gz file
df.to_pickle(os.path.join(save_loc, "events_0.pkl.gz"), compression="infer")
