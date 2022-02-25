from quad_clas.analyse.animate_2d import animate_learning_2d

animate_learning_2d(mc_reps=30,
                    path_to_model='/Users/jaco/Documents/ML4EFT/models/lin/cHq3/mc_run_{mc_run}',
                    network_size=[2, 30, 30, 30, 30, 30, 1],
                    c1=0,
                    c2=10,
                    lin=True,
                    quad=False,
                    cross=False,
                    path_sm_data=None)
