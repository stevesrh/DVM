import cv2


def transformer(image_path):
    image_gray=cv2.imread(image_path,0)
    print(image_gray.shape)
    cv2.imwrite('/Users/shenronghao/PycharmProjects/DVM/gray.png',image_gray)


if __name__ == '__main__':
    image_path ="/Users/shenronghao/PycharmProjects/DVM/截屏2021-12-13 下午5.08.37.png"
    transformer(image_path)
