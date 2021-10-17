from detectors import *
from utils.images import *

img = load_image('../data/1.bmp')


alg = MPCM()
alg.process(img)

show_image(img)
show_image(alg.result)
plt.show()
