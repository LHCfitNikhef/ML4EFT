import pandas as pd
import pyhepmc
import numpy as np
import cachetools.func
from particle import Particle
from particle.particle.particle import ParticleNotFound
import time
import pid_func

event_file = "/data/theorie/pherbsch/MG5_aMC_v3_4_1/small_shower_test/Events/run_01/tag_1_pythia8_events.hepmc"

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

#This code block is quite slow, let's cache it and keep it in mind ~3 min.
start_time1 = time.time()

# @cachetools.func.ttl_cache(ttl=60*30)
# def pid_func():
#     particle_names = [p.name for p in Particle.all()]
#     pid_name = []
#     not_found = []
#     counter = 0
#     for name in particle_names:
#         try:
#             pid = int(Particle.from_name(name).pdgid)
#             pid_name.append((pid, name))
#         except ParticleNotFound:
#             not_found.append(name)
#         counter += 1                                    #the counter should actually be in the except statement (so one tab forward) and break when
#         if counter >= 100:                              #when counter >= 6, it's missing ['n', 'n~', 'p', 'p~', 'n', 'n~', 'p', 'p~'], but that's okay. 
#             break                                       #the current setup is for quick itteration, since the right particles are included for the file at hand.

#     if not_found:
#         print(f"Particles not found: {not_found}")
#     return pid_name

pid_name = pid_func.pid_func()

end_time1 = time.time()
total_time1 = end_time1 - start_time1

print("pid_time: {:.2f} seconds".format(total_time1))

particles_list = {}
# Create numpy arrays for particle properties
pids = np.array([p.pid for p in final_state_particles])
momenta = np.array([[p.momentum.px, p.momentum.py, p.momentum.pz, p.momentum.e] for p in final_state_particles])

print(momenta)

for pid, name in pid_name:
    mask = pids == pid
    if mask.any():
        if name not in particles_list:
            particles_list[name] = mask.sum()
        else:
            particles_list[name] += mask.sum()

print("Final state particles found:")
for name, count in particles_list.items():
    print(f"{name}: {count}")

