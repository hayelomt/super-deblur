from PIL import Image
import os

def crop(path, input, height, width, k, page, area):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            try:
                o = a.crop(area)
                o.save(os.path.join(path,"PNG","%s" % page,"IMG-%s.png" % k))
            except:
                pass
            k +=1

def crop_img(input, height, width):
  im = Image.open(input)
  img_width, img_height = im.size
  box = (0, 0, )
  a = im.crop()
  for i in range(0, img_height, height):
    for j in range(0, img_width, width):
      box = (j, i, j+width, i+height)
      print(box)

crop_img('imgs/6.png', 256, 256)
