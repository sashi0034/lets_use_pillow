from PIL import Image

path = r"test.bmp"

im1 = Image.open(path)
im1 = im1.convert(mode='P', dither=None)
print(im1);
im1.save(path, "BMP")


