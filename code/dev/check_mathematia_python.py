#%%
from quad_clas.core.truth import vh_prod

hats = 0.3 ** 2
ptv = 0.1
cHW = 0
cHq3 = 0
lin = True
quad = False
vh_prod.dsigma_part_dpt_vh_down(hats, ptv, cHW, cHq3, lin, quad)