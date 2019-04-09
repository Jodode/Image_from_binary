from PIL import Image, ImageDraw, ImageFont

print("""
  _                  _           _           _      
 | |                | |         | |         | |     
 | |__  _   _       | | ___   __| | ___   __| | ___ 
 | '_ \| | | |  _   | |/ _ \ / _` |/ _ \ / _` |/ _ \\
 | |_) | |_| | | |__| | (_) | (_| | (_) | (_| |  __/
 |_.__/ \__, |  \____/ \___/ \__,_|\___/ \__,_|\___|
         __/ |                                      
        |___/                                       
""")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GREEN = (0, 255, 0)
RED = (255, 0, 0)

GREY = (128, 128, 128)

filename = input("Enter filename for future image\n > ")
data = list(input("Enter binary data\n > "))

size = (150 + 55 * len(data), 75)

img = Image.new("RGB", size, WHITE)

draw = ImageDraw.Draw(img)

fnt = ImageFont.truetype("/usr/share/fonts/ttf/Hack-Bold.ttf", 40)

draw.text((15, 15), "NRZ", font=fnt, fill=BLACK)

x = 120
y = 25

def do_zero_segment(cur_x, cur_y):

    draw.line([cur_x, 35, cur_x + 10, 35], fill=GREY, width=2)
    draw.line([cur_x + 20, 35, cur_x + 30, 35], fill=GREY, width=2)
    draw.line([cur_x + 40, 35, cur_x + 50, 35], fill=GREY, width=2)
    # make green and red line

    draw.line([cur_x, 45, cur_x + 50, 45], fill=BLACK, width=2)
    
    draw.line([cur_x, 20, cur_x + 25, 20], fill=RED, width=3)
    draw.line([cur_x, 50, cur_x + 25, 50], fill=RED, width=3)
    cur_x += 25
    draw.line([cur_x, 20, cur_x + 25, 20], fill=GREEN, width=3)
    draw.line([cur_x, 50, cur_x + 25, 50], fill=GREEN, width=3)
    cur_x += 25

def do_one_segment(cur_x, cur_y):

    draw.line([cur_x, 35, cur_x + 10, 35], fill=GREY, width=2)
    draw.line([cur_x + 20, 35, cur_x + 30, 35], fill=GREY, width=2)
    draw.line([cur_x + 40, 35, cur_x + 50, 35], fill=GREY, width=2)
    # make green and red line

    draw.line([cur_x, 25, cur_x + 50, 25], fill=BLACK, width=2)
    
    draw.line([cur_x, 20, cur_x + 25, 20], fill=RED, width=3)
    draw.line([cur_x, 50, cur_x + 25, 50], fill=RED, width=3)
    cur_x += 25
    draw.line([cur_x, 20, cur_x + 25, 20], fill=GREEN, width=3)
    draw.line([cur_x, 50, cur_x + 25, 50], fill=GREEN, width=3)
    cur_x += 25

def connect_line(cur_x):
    draw.line([cur_x, 25, cur_x, 45], fill=BLACK, width=2)

stack = []

if data[0] == "1":
    do_one_segment(x, y)
    stack.append("1")
elif data[0] == "0":
    do_zero_segment(x, y)
    stack.append("0")
x += 50

for i in data[1:]:
    if i == "1":
        do_one_segment(x, y)
        stack.append(i)
    elif i == "0":
        do_zero_segment(x, y)
        stack.append(i)
    if stack[-1] != stack[-2]:
        connect_line(x)
    x += 50

# img.show()
img.save(filename + ".png", "PNG")