# coding:utf-8
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random, time, os
import glob
from PIL import Image
from skimage import io

PATH = '/Users/xuanyuanjing/code/spider/ganji/GJIMG/model/*.png'

# 验证码中的字符, 就不用汉字了
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

traindata = glob.glob(PATH)

def gen_captcha_text_and_image():
    path = random.sample(traindata, 1)[0]
    name = path.split("/")[-1].split(".")[0]
    img = 1.0 - io.imread(path, as_grey=True)
    return name, img

if __name__ == '__main__':
    # 测试
    while (1):
        print(len(traindata))
        text, image = gen_captcha_text_and_image()
        print 'begin ', time.ctime(), type(image)
        f = plt.figure()
        ax = f.add_subplot(111)
        ax.text(0.1, 0.9, text, ha='center', va='center', transform=ax.transAxes)
        plt.imshow(image)

        plt.show()
        print 'end ', time.ctime()
        exit(0)
