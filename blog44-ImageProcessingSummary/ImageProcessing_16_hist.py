#encoding:utf-8
#By:Eastmount CSDN 2021-08-20
import cv2  
import numpy as np
import matplotlib.pyplot as plt

#读取图像
img = cv2.imread('lena-hd.png')

#图像灰度转换
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#获取图像高度和宽度
height = grayImage.shape[0]
width = grayImage.shape[1]
result = np.zeros((height, width), np.uint8)

#图像灰度对数变换
for i in range(height):
    for j in range(width):
        gray = 42 * np.log(1.0 + grayImage[i,j])
        result[i,j] = np.uint8(gray)

#计算原图的直方图
hist = cv2.calcHist([img], [0], None, [256], [0,255])

#计算灰度变换的直方图
hist_res = cv2.calcHist([result], [0], None, [256], [0,255])

#原始图像
plt.figure(figsize=(8, 6))
plt.subplot(221), plt.imshow(img, 'gray'), plt.title("(a)"), plt.axis('off')

#绘制原始图像直方图
plt.subplot(222), plt.plot(hist), plt.title("(b)"), plt.xlabel("x"), plt.ylabel("y")

#灰度变换后的图像
plt.subplot(223), plt.imshow(result, 'gray'), plt.title("(c)"), plt.axis('off')

#灰度变换图像的直方图
plt.subplot(224), plt.plot(hist_res), plt.title("(d)"), plt.xlabel("x"), plt.ylabel("y")
plt.show()

