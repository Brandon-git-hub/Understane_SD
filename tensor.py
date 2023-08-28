import torch
import numpy as np
from einops import rearrange, repeat

# image[None] -> at front add one dim
image = np.array([1,2,3])
new_img = image[None][None]
print(new_img)
print(new_img.shape)

# einops.repeat
init_img = torch.randn(1,3,512,512)
init_img = repeat(init_img,'1 ... -> b ...', b=4)
print('init_img shape', init_img.shape)

# torch.stack
ex_batch = torch.randn(4,3,256,256)
extend_ex = list()
extend_ex.append(ex_batch)
extend_ex = torch.stack(extend_ex, 0)
print(extend_ex.shape)

# einops.rearrange
grid = rearrange(extend_ex, 'n b c h w -> (n b) c h w')
print(grid.shape)

