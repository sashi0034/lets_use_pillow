from PIL import Image

load_path = r"test.png"
save_path = r"test.png";


old_img = Image.open(load_path)
width, height = old_img.size

multiply_x =10
multiply_y = 5


new_img = Image.new("RGB", (multiply_x*width, multiply_y*height), (255, 255, 255))

for x in range(0, multiply_x):
    for y in range(0, multiply_y):
        new_img.paste(old_img, (x*width, y*height))
        


new_img.save(save_path, "PNG")

print("Image completed")


        



















