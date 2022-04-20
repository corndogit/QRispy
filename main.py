import tkinter as tk
from PIL import Image
from qr_codec import make_qr_code, decode_qr_code


def main():
    # Window
    window = tk.Tk()
    window.title("QRispy")
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.grid(columnspan=4)

    window.mainloop()


if __name__ == '__main__':
    main()
