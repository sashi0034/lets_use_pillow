from PIL import Image




path = r"test.png"
save_path = path
save_format = "PNG"
#save_path = r"images\Add_antialiasing_to_2_colors.png";
pallet = 15;

img = Image.open(path)
width, height = img.size


colors = []
colors_count = {}
for x in range(0, width):
    for y in range(0, height):
        c = img.getpixel((x,y))
        if (c in colors): 
            colors_count[c]=colors_count[c]+1
            continue
        else:
            colors.append(c)
            colors_count[c] = 0
            
        
        
if (len(colors)!=2):
    print("this image dosen't have just 2 colors.")

#colors[0]のほうが少なくなるように
if (colors_count[colors[0]]>colors_count[colors[1]]):
    colors[0], colors[1] = colors[1], colors[0]


new_colors = []
r1, g1, b1, a = colors[0]
r2, g2, b2, a = colors[1]
for i in range(0, pallet+1):
    r=int(r1+(r2-r1)*(i/pallet))
    g=int(g1+(g2-g1)*(i/pallet))
    b=int(b1+(b2-b1)*(i/pallet))
    new_colors.append((r,g,b,a));



def round_check(x, y, c:tuple):
    if (0<=x-1 and img.getpixel((x-1,y))==c):
        return True
    if (0<=y-1 and img.getpixel((x,y-1))==c):
        return True
    if (x+1<=width-1 and img.getpixel((x+1,y))==c):
        return True
    if (y+1<=height-1 and img.getpixel((x,y+1))==c):
        return True
    return False;
    
    
def check_and_draw(x,y,i):
    if (x<1 or y<1 or x>=width-1 or y>=height-1):
        return
    
    if (round_check(x, y, new_colors[i-1])):
        if (img.getpixel((x, y))==colors[1]):
            img.putpixel((x,y),new_colors[i])
        """
        if (img.getpixel((x-1, y))==colors[1]):
            img.putpixel((x-1,y),new_colors[i])
        if (img.getpixel((x+1, y))==colors[1]):
            img.putpixel((x+1,y),new_colors[i])
        if (img.getpixel((x, y-1))==colors[1]):
            img.putpixel((x,y-1),new_colors[i])
        if (img.getpixel((x, y+1))==colors[1]):
            img.putpixel((x,y+1),new_colors[i])
        """




#描画処理
for i in range(1,pallet):
    for x in range(0, width):
        for y in range(0, height):
            #print("reach1",x,y);
            #check_and_draw(x-1,y,i)
            #check_and_draw(x+1,y,i)
            #check_and_draw(x,y-1,i)
            #check_and_draw(x,y+1,i)
            check_and_draw(x,y,i)
            #if (img.getpixel((x, y))==colors[1]):
                #if (round_check(x, y, new_colors[i-1])):
                    #img.putpixel((x,y),new_colors[i])
                #print("reach2",x,y);
            
        

#img.save(save_path, "PNG")
img.save(save_path, save_format)

print("Image completed")



