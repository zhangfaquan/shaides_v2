import os
import sys
from PIL import Image
import time


num_imgs = 75
batch = 25
path = "data_gestures/test/misc"
# data_gestures/train/arm
# data_gestures/train/misc
# data_objects/train/google
# data_objects/train/lamp
# data_objects/train/misc

img_width = 300
img_height = 300


def main(i):
    os.system("wget -q -O out.jpg http://192.168.1.185/capture?_cb=1593037200070")
    img = Image.open('out.jpg')
    img = img.resize((img_width, img_height))
    img = img.transpose(Image.ROTATE_180)
    img.save('out.jpg')
    os.rename("out.jpg", "{}/img_{}_{}.jpg".format(path, batch, i))


if __name__ == "__main__":
    print("Get ready...")
    time.sleep(5)
    for i in range(num_imgs):
        main(i)
        print(i)
        time.sleep(0.5)
    print("Done.")

