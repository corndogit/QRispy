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
    decode_qr = decode(Image.open(data))
    return decode_qr


def main():
    """| Usage in terminal: main.py <encode/decode> <input> <output>"""
    try:
        script, task, data_input = sys.argv
        if task.lower() == 'encode':
            make_qr_code(data_input).save('output.png')
            print(f"Generated QR code, saved to output.png")
        elif task.lower() == 'decode':
            print(decode_qr_code(data_input))
        else:
            print("Invalid task  - please use 'encode' or 'decode'")
    except ValueError:
        print("Incorrect arguments (Usage: main.py <encode/decode> <input> <output>)")


if __name__ == '__main__':
    main()
