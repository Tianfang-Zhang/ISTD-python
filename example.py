from utils.load_images import *
from detectors.example_class import *

if __name__ == '__main__':
    img = load_image('E:/NutFiles/ProgramCache/GoogleDriveFiles/AerialDetection (1)/data/dota/test/images/P0006.png')

    detector = example_class(1, 2)
    detector.process(img)
    detector.show_result()

    plt.show()

