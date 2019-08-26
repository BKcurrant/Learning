# -*- coding=GBK -*-
import cv2
import numpy as np


def fill2_image():
    image = np.zeros([400, 400, 3], np.uint8)  # 造一张图
    image[200:300, 200:300] = 255
    cv2.imshow('src', image)  # 输出原图
    height, width = image.shape[:2]
    mask = np.ones([height + 2, width + 2, 1], np.uint8)  # mask模板初始化为1
    mask[201:301, 201:301] = 0  # 想填充的区域初始化为0
    cv2.floodFill(image, mask, (200, 200), (0, 0, 255), cv2.FLOODFILL_MASK_ONLY)
    cv2.imshow('dst', image)


fill2_image()
cv2.waitKey(0)
cv2.destroyAllWindows()
