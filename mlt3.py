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

fnt = ImageFont.truetype("/usr/share/fonts/ttf/Hack-Bold.ttf", 40) # Choose your font

draw.text((15, 15), "MLT-3", font=fnt, fill=BLACK)

x = 160
y = 35
# horizon_y = cur_y

def do_zero_segment(cur_x, cur_y):
    # global cur_x, cur_y

    # make grey line
    draw.line([cur_x, 35, cur_x + 10, 35], fill=GREY, width=2)
    draw.line([cur_x + 20, 35, cur_x + 30, 35], fill=GREY, width=2)
    draw.line([cur_x + 40, 35, cur_x + 50, 35], fill=GREY, width=2)
    # make green and red line
    draw.line([cur_x, cur_y, cur_x + 50, cur_y], fill=BLACK, width=2)
    draw.line([cur_x, 10, cur_x + 25, 10], fill=RED, width=3)
    draw.line([cur_x, 60, cur_x + 25, 60], fill=RED, width=3)
    cur_x += 25
    draw.line([cur_x, 10, cur_x + 25, 10], fill=GREEN, width=3)
    draw.line([cur_x, 60, cur_x + 25, 60], fill=GREEN, width=3)
    cur_x += 25

direction = "up"

flag = False

def do_one_segment(direction, cur_x, cur_y):
    # global cur_x, cur_y

    # make grey line
    draw.line([cur_x, 35, cur_x + 10, 35], fill=GREY, width=2)
    draw.line([cur_x + 20, 35, cur_x + 30, 35], fill=GREY, width=2)
    draw.line([cur_x + 40, 35, cur_x + 50, 35], fill=GREY, width=2)
    # make green and red line
    
    if (direction == "down"):
        draw.line([cur_x, cur_y, cur_x, cur_y + 20], fill=BLACK, width=2)
        draw.line([cur_x, cur_y + 20, cur_x + 50, cur_y + 20], fill=BLACK, width=2)
    elif (direction == "up"):
        draw.line([cur_x, cur_y, cur_x, cur_y - 20], fill=BLACK, width=2)
        draw.line([cur_x, cur_y - 20, cur_x + 50, cur_y - 20], fill=BLACK, width=2)

    draw.line([cur_x, 10, cur_x + 25, 10], fill=RED, width=3)
    draw.line([cur_x, 60, cur_x + 25, 60], fill=RED, width=3)
    cur_x += 25

    draw.line([cur_x, 10, cur_x + 25, 10], fill=GREEN, width=3)
    draw.line([cur_x, 60, cur_x + 25, 60], fill=GREEN, width=3)
    cur_x += 25


stack = ["up"]

for i in data:
    if (i == "1" and not flag):
        flag = True
        do_one_segment("up", x, y)
        x += 50
        y -= 20
        stack.append("up")
    elif (i == "1"):
        if (stack[-1] == "up" and stack[-2] == "up") or (stack[-2] == "up" and stack[-1] == "down"):
            do_one_segment("down", x, y)
            x += 50
            y += 20
            # sec_flag = True
            stack.append("down")
        elif (stack[-1] == "down" and stack[-2] == "down") or (stack[-2] == "down" and stack[-1] == "up"):
            do_one_segment("up", x, y)
            x += 50
            y -= 20
            # sec_flag = True
            stack.append("up")
    elif (i == "0"):
        do_zero_segment(x, y)
        x += 50
    # print(x, y)

# img.show()
img.save(filename + ".png", "PNG")
