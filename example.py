from utils.images import *
from detectors.fast_saliency import FastSaliency


if __name__ == '__main__':
    img_file = r'E:\NutFiles\ProgramCache\DATASETS\sirst\masks/Misc_2_pixels0.png'
    img = load_image(img_file)

    img[10:20, 20:30] = 1.
    label = img > 0
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(label.astype(np.uint8))

    plt.figure()
    # plt.imshow(cv2.flip(label.astype(np.uint8), 0), origin='lower')
    plt.imshow(label)
    plt.plot(centroids[2,0], centroids[2,1] , 'r.')

    plt.figure()
    plt.imshow(labels)
    plt.show()

    print(label[np.int(centroids[2,1]), np.int(centroids[2,0])])

    # detector = lcm(0, 0)
    # detector.process(img)
    # show_image(detector.result)
    #
    # plt.show()

