#%%
from quad_clas.analyse.animate_2d import animate_learning_2d
from quad_clas.analyse.animate import Animate
#%%
# 1D

path_to_models = {'lin': {
    'cuu_quad': '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_llbb/ltd/model_cuu_quad_v3',
    'cuu_quad': '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_llbb/ltd/model_cuu_quad_v3'}}

#%%
animation1D = Animate(architecture=[2,100, 100, 100, 1],
                      c=[0, 9],
                      c_train={
                          "cuu_quad": 100.0,
                          "cuu_quad": 100.0
                      },
                      path_to_models=path_to_models,
                      save_path='/data/theorie/jthoeve/ML4EFT_higgs/output/animations/26_04/cuu_quad.gif',
                      frames=50,
                      lin=True,
                      quad=False)
animation1D.make_animation()

#%%
# 2D
# animate_learning_2d(mc_reps=30,
#                     path_to_model='/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_robust_scaler/model_chw_lin/mc_run_{mc_run}',
#                     network_size=[2, 30, 30, 30, 30, 30, 1],
#                     c1=10,
#                     c2=0,
#                     lin=True,
#                     quad=False,
#                     cross=False,
#                     path_sm_data=None)
