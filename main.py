import qrcode
import sys


def make_qr_code(data: str):
    """| Turns string of data into a QR code in PNG format"""
    image = qrcode.make(data)
    return image


def main():
    """| Usage in terminal: main.py <string> <output_img>"""
    try:
        script, data_input, filename = sys.argv
        make_qr_code(data_input).save(filename)
        print(f"Generated QR code, saved to {filename}")
    except ValueError:
        data_input = input("Enter text to encode:\n> ")
        filename = input("Enter name for output file:\n> ")
        make_qr_code(data_input).save(filename)
        print(f"Generated QR code, saved to {filename}")


if __name__ == '__main__':
    main()
