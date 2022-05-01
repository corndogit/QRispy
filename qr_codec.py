import sys
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


def make_qr_code(data: str):
    """| Turns string object into a QR code in PNG format"""
    image = qrcode.make(data)
    return image


def decode_qr_code(data):
    """| Finds QR code in image and decodes it using pyzbar library"""
    decode_qr = decode(Image.open(data))  # PIL.PngImagePlugin.PngImageFile
    return decode_qr[0].data.decode('utf-8')


def main():
    """| Usage in terminal: main.py <encode/decode> <input> <output>"""
    try:
        script, task, data_input = sys.argv
        if task.lower() == 'encode':
            make_qr_code(data_input).save('output.png')
            print("Generated QR code, saved to output.png")
        elif task.lower() == 'decode':
            print(decode_qr_code(data_input))
        else:
            print("Invalid task  - please use 'encode' or 'decode'")
    except ValueError:
        print("Incorrect arguments (Usage: main.py <encode/decode> <input> <output>)")


if __name__ == '__main__':
    main()
