# Créé par ackermann, le 11/12/2020 en Python 3.7
import math
import tkinter as tk
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk

win = tk.Tk()
win.title("Modifier une image")
win.geometry("800x600")
mx,my = 800, 600
cx,cy = mx//2, my//2

img_txt = tk.StringVar()
img_txt.set("Aucun fichier.")
label_img = tk.Label(win, textvariable=img_txt)
label_img.pack()
label_img.place(x=70, y=12.5)



modspop = tk.Menu(win, tearoff=0)
modspop.add_command(label="do")


label_img_original = tk.Label(win, text="Image initiale")
label_img_original.pack()
label_img_original.place(x=cx//2-50, y=150)

label_img_modified = tk.Label(win, text="Image modifiée")
label_img_modified.pack()
label_img_modified.place(x=cx+(cx//2)-50, y=150)

canvas_original = tk.Canvas(win, width=420, height=420)
canvas_original.place(x=cx//2-(420//4), y=cy)

canvas_edited = tk.Canvas(win, width=420, height=420)
canvas_edited.place(x=cx+(cx//(2)-420//4), y=cy)

global edited_image

def valid_char(char):
    return 32 <= ord(char) <= 126


def has_alpha(img):
    return img.mode == "RGBA"


def channels(img):
    return 4 if has_alpha(img) else 3


def string2bits(s):
    return bin(ord(s))[2:].zfill(8)


def bits2string(b):
    return chr(int(b, 2))


def int2bits(i):
    return format(i, '02b')


def bits2int(b):
    return int(b, 2)


def max_len(img):
    w, h = img.size
    n = channels(img)
    return math.floor((n * w * h) / 4)


def max_txt_len(img):
    return int(max_len(img) / 4)


def len_needed(txt):
    return len(txt) * 4


def getpos(i, w):
    return i % w, math.floor(i / w)


def pixels2array(img, length=0):
    buffer = []
    w, h = img.size
    i = 0

    if length == 0:
        length = max_len(img)

    while len(buffer) < length:
        x, y = getpos(i, w)
        buffer += img.getpixel((x, y))[:length-len(buffer)]
        i += 1

    return buffer


def array2pixels(img, arr):
    w, h = img.size

    n = channels(img)
    i = 0

    for a in range(0, len(arr), n):
        x, y = getpos(i, w)
        img.putpixel((x, y), tuple(arr[a:a + n]))

        i += 1

    return img


def hide(img, txt, bytes_sacrified=1):
    buffer = []
    buffer_x = []

    bits_sacrified = bytes_sacrified * 2
    bitsperbyte = 4 - bytes_sacrified + 1

    orig = pixels2array(img, len_needed(txt))

    for i in range(len(txt)):
        bin_str = string2bits(txt[i])
        for x in range(4):
            buffer.append(bin_str[x * 2:x * 2 + 2])

    for i in range(len(orig)):
        if i < len(buffer):
            bin_str = int2bits(orig[i])[:-bits_sacrified]
            buffer_x.append(bits2int(bin_str + buffer[i]))
        else:
            buffer_x.append(orig[i])

    return array2pixels(opened_image, buffer_x)


def find(img, bytes_sacrified=1):
    buffer = []
    buffer_x = ""

    bits_sacrified = bytes_sacrified * 2
    bitsperbyte = 4 - bytes_sacrified + 1

    orig = pixels2array(img)

    for i in range(len(orig)):
        buffer.append(int2bits(orig[i])[-bits_sacrified:])

    for i in range(0, len(buffer) - len(buffer) % bitsperbyte, bitsperbyte):
        char = bits2string("".join(buffer[i:i + bitsperbyte]))

        if valid_char(char):
            buffer_x += char
        else:
            break

    return buffer_x


def resize_image(img):
    w, h = img.size

    size = canvas_original.winfo_width() / 2
    ratio = min(size / h, size / w)

    return img.resize((int(w * ratio), int(h * ratio)), Image.ANTIALIAS)


def rotate_image(img):
    w, h = img.size
    buffer = Image.new(mode=img.mode, size=(h, w))
    for x in range(w):
        for y in range(h):
            channels = img.getpixel((x, y))
            buffer.putpixel((h - y - 1, x), channels)
    return buffer


def decolor_image(img):
    w, h = img.size
    for x in range(w):
        for y in range(h):
            channels = img.getpixel((x, y))
            r, g, b = channels[:3]
            shade = int((r + g + b) / 3)
            img.putpixel((x, y), (shade, shade, shade, channels[3] if len(channels) == 4 else 0))
    return img


def invert_image(img):
    w, h = img.size
    for x in range(w):
        for y in range(h):
            channels = img.getpixel((x, y))
            r, g, b = channels[:3]
            img.putpixel((x, y), (255 - r, 255 - g, 255 - b, channels[3] if len(channels) == 4 else 0))
    return img


def brightness_image(img, n):
    w, h = img.size
    for x in range(w):
        for y in range(h):
            channels = img.getpixel((x, y))
            r, g, b = channels[:3]
            img.putpixel((x, y), (r + n, g + n, b + n, channels[3] if len(channels) == 4 else 0))
    return img


def mirror_image(img):
    w, h = img.size
    hw = int(w / 2)
    for x in range(hw):
        for y in range(h):
            channels = img.getpixel((hw - x, y))
            r, g, b = channels[:3]
            img.putpixel((hw + x, y), (r, g, b, channels[3] if len(channels) == 4 else 0))
    return img


def mirror_image_y(img):
    w, h = img.size
    hh = int(h / 2)
    for x in range(w):
        for y in range(hh):
            channels = img.getpixel((x, hh - y))
            r, g, b = channels[:3]
            img.putpixel((x, hh + y), (r, g, b, channels[3] if len(channels) == 4 else 0))
    return img


def set_image(img, canvas):
    global edited_image
    edited_image = img
    canvas.image = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")


def open_image(path):
    global opened_image
    opened_image = Image.open(path)
    opened_image = resize_image(opened_image)

    opened_image =hide(opened_image, "salut", 4)

    print(find(opened_image))

    set_image(opened_image, canvas_original)
    set_image(opened_image, canvas_edited)


def open_file():
    image_path = askopenfilename(title="Choisir une image")
    filename = image_path.split("/")[-1]
    img_txt.set(filename)
    open_image(image_path)
    print("Opening: " + image_path)


open_img = tk.Button(win, text="Ouvrir...", command=open_file)
open_img.place(x=10, y=10)


def reset():
    if opened_image:
        set_image(opened_image, canvas_edited)


rotate_img = tk.Button(win, text="Reset", command=reset)
rotate_img.place(x=300, y=150)


def rotate():
    if opened_image:
        img = rotate_image(edited_image)
        img = resize_image(img)
        set_image(img, canvas_edited)


rotate_img = tk.Button(win, text="Rotate", command=rotate)
rotate_img.place(x=300, y=200)


def invert():
    if opened_image:
        img = invert_image(edited_image)
        set_image(img, canvas_edited)


decolor_img = tk.Button(win, text="Invert", command=invert)
decolor_img.place(x=300, y=250)


def decolor():
    if opened_image:
        img = decolor_image(edited_image)
        set_image(img, canvas_edited)


decolor_img = tk.Button(win, text="Decolor", command=decolor)
decolor_img.place(x=300, y=300)


def brighter():
    if opened_image:
        img = brightness_image(edited_image, 10)
        set_image(img, canvas_edited)


decolor_img = tk.Button(win, text="Brighter", command=brighter)
decolor_img.place(x=300, y=350)


def darker():
    if opened_image:
        img = brightness_image(edited_image, -10)
        set_image(img, canvas_edited)


decolor_img = tk.Button(win, text="Darker", command=darker)
decolor_img.place(x=350, y=350)


def mirror():
    if opened_image:
        img = mirror_image(edited_image)
        set_image(img, canvas_edited)


decolor_img = tk.Button(win, text="Mirror", command=mirror)
decolor_img.place(x=300, y=400)


def mirror_y():
    if opened_image:
        img = mirror_image_y(edited_image)
        set_image(img, canvas_edited)


decolor_img = tk.Button(win, text="Horizontal Mirror", command=mirror_y)
decolor_img.place(x=350, y=400)



def do_popup(win, event):
    try:
        modspop.tk_popup(event.x_root, event.y_root)
    finally:
        modspop.grab_release()



win.bind("<Button-3>", do_popup)
tk.mainloop()
win.mainloop()