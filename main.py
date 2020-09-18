import sys
import qrcode
from PIL import Image, ImageDraw, ImageFont


# Rewrite figure name to save
FIGURE_NAME = ''


def get_concat_v(im1):
    im = Image.new("RGB", (410, 100), 'white')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('YuGothL.ttc', size=20)
    draw.text((50, 0), f'SSID  : {SSID_NAME}', fill='black', font=font)
    draw.text((50, 20), f'PASS : {PASSWORD}', fill='black', font=font)

    dst = Image.new('RGB', (410, 510))
    dst.paste(im1, (0, 0))
    dst.paste(im, (0, 410))
    return dst


def Input():
    if len(sys.argv) == 4:
        SSID_NAME, PASSWORD, ENCRYPTION_METHOD = sys.argv[1], sys.argv[2], sys.argv[3]
    elif len(sys.argv) == 3:
        SSID_NAME, PASSWORD, ENCRYPTION_METHOD = sys.argv[1], sys.argv[2], 'WPA/WPA2'
    else:
        print('SSID : ', end='')
        SSID_NAME = input()
        print('PASSWORD : ', end='')
        PASSWORD = input()
        print('ENCRYPTION_METHOD : ', end='')
        ENCRYPTION_METHOD = input()
    return SSID_NAME, PASSWORD, ENCRYPTION_METHOD


SSID_NAME, PASSWORD, ENCRYPTION_METHOD = Input()
QR_CODE = qrcode.make(f'WIFI:T:{ENCRYPTION_METHOD};S:{SSID_NAME};P:{PASSWORD};;')
get_concat_v(QR_CODE).save(FIGURE_NAME)