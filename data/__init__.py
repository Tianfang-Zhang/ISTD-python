from utils.datasets import *
import cv2

# dataset = MDFA(base_dir='MDFA/')
dataset = SIRST(base_dir='sirst/')

for i in range(dataset.__len__()):
    img, mask = dataset.__getitem__(i)


    if img.shape == mask.shape:
        continue
    else:
        print(i)
        print(img.shape)
        print(mask.shape)
        break


# mask = cv2.imread(r'sirst\masks/Misc_111_pixels0.png', 0)
# print(mask.shape)
#
# mask_new = cv2.resize(mask, (325 ,220))
# print(mask_new.shape)
# cv2.imwrite('Misc_111_pixels0.png', mask_new)