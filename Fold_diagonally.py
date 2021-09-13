from PIL import Image
import random



#img = Image.new("RGB", (width, height), (255, 255, 255))
load_path = r"test.png"
save_path = load_path;
#save_path = r"images\Fold_diagonally.png";

img = Image.open(load_path)
width, height = img.size


if (width != height):
    print("width dose not equals height.");
    exit();




for x in range(0, width):
    for y in range(0, width-x):
        color = img.getpixel((x,y))
        img.putpixel((width-1 - y, width-1 - x), color), 

img.save(save_path, "PNG")

print("Image completed")



