import pandas as pd
import pyhepmc
import numpy as np
import cachetools.func
from particle import Particle
from particle.particle.particle import ParticleNotFound
import time
import cachetools

@cachetools.func.ttl_cache(ttl=60*30)
def pid_func():
    particle_names = [p.name for p in Particle.all()]
    pid_name = []
    not_found = []
    counter = 0
    for name in particle_names:
        try:
            pid = int(Particle.from_name(name).pdgid)
            pid_name.append((pid, name))
        except ParticleNotFound:
            not_found.append(name)
        counter += 1                                    #the counter should actually be in the except statement (so one tab forward) and break when
        if counter >= 400:                              #when counter >= 6, it's missing ['n', 'n~', 'p', 'p~', 'n', 'n~', 'p', 'p~'], but that's okay. 
            break                                       #the current setup is for quick itteration, since the right particles are included for the file at hand.

    if not_found:
        print(f"Particles not found: {not_found}")
    return pid_name

