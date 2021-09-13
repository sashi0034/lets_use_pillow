from PIL import Image

load_path = r"test.png"
#save_path = load_path
save_path = r"test.png";

def hex_to_rgb(value):
    return ((value & 0xff0000) >>16, (value & 0x00ff00) >>8, (value & 0x0000ff) >>0, 255)

replace_rgba = hex_to_rgb(0x4c9cdc)
print(hex_to_rgb(0x4c9cdc));
new_rgba = [0,0];
new_rgba[0] = hex_to_rgb(0x3a89d5)
new_rgba[1] = hex_to_rgb(0x5fcde4)



img = Image.open(load_path)
width, height = img.size



for x in range(0, width):
    for y in range(0, height):
        c = img.getpixel((x,y))
        if (c==replace_rgba):
            r = (x+y)%2
            img.putpixel((x,y),new_rgba[r])
            



img.save(save_path, "PNG")


print("Image completed")


        



















