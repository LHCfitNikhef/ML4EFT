#%%
from quad_clas.analyse.animate_2d import animate_learning_2d
from quad_clas.analyse.animate import Animate
#%%
# 1D

path_to_models = {'lin': ['/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_{mc_run}',
                         '/Users/jaco/Documents/ML4EFT/models/lin/cHq3/mc_run_{mc_run}']}

animation1D = Animate(architecture=[2, 30, 30, 30, 30, 30, 1],
                      c=[2, 0],
                      path_to_models=path_to_models,
                      mc_runs=30,
                      save_path='/Users/jaco/Documents/ML4EFT/animations/vh_prod/example.gif',
                      frames=150,
                      lin=True,
                      quad=False)
animation1D.make_animation()

#%%
# 2D
animate_learning_2d(mc_reps=30,
                    path_to_model='/Users/jaco/Documents/ML4EFT/models/lin/cHq3/mc_run_{mc_run}',
                    network_size=[2, 30, 30, 30, 30, 30, 1],
                    c1=0,
                    c2=10,
                    lin=True,
                    quad=False,
                    cross=False,
                    path_sm_data=None)
