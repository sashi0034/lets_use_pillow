from PIL import Image

load_path = r"test.png"
save_path = r"test.png"

old_img = Image.open(load_path)
width, height = old_img.size


new_img = Image.new("RGB", (width, height), (255, 255, 255))

centx: int = int(width/2)
img1 = old_img.crop((0,0,centx,height));
img2 = old_img.crop((centx,0,width,height));

new_img.paste(img1, (centx,0))
new_img.paste(img2,(0,0))        


new_img.save(save_path, "PNG")

print("Image completed")


        



















