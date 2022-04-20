import qrcode
import sys


def make_qr_code(data):
    """Turns data into a QR code in PNG format"""
    image = qrcode.make(data)
    return image


if __name__ == '__main__':
    try:
        script, data_input, filename = sys.argv
        make_qr_code(data_input).save(filename)
        print(f"Generated QR code, saved to {filename}")
    except ValueError:
        print("Not enough arguments supplied (usage: main.py <string> <output_img>)")
