import os

import cv2
import numpy as np

from generate_trimap import gen_trimap
if __name__ == '__main__':
    images_path="/Volumes/Netease/Selected_data/0005"
    mask_path=os.path.join(images_path,"mask_resize")
    trimap_path=os.path.join(images_path,"trimaps")
    if not os.path.exists(trimap_path):
        os.makedirs(trimap_path)
    for image in os.listdir(mask_path):
        print("读取",image)
        im_path = os.path.join(mask_path,image)
        im = cv2.imread(im_path)
        # im_gray = cv2.imread(im_path, 0)
        # print(im.shape, im[1000, 1400])
        # print(im_gray.shape, im_gray[1000, 1400])
        im = im/128
        im = im*255
        print(im.shape, im[1000, 1400])
        trim = gen_trimap(im)
        print("写入trimap",image,im.shape)
        cv2.imwrite(os.path.join(trimap_path, image),trim)

