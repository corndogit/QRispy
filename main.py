import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from qr_codec import make_qr_code, decode_qr_code


def main():
    # Window
    window = tk.Tk()
    window.title("QRispy")
    canvas = tk.Canvas(window, width=700, height=350)
    canvas.grid(columnspan=2, rowspan=2)

    # Title
    title = ttk.Label(window)
    title.config(text="Encode:")
    title.grid(column=0, row=0, sticky='NW', padx=25, pady=10)

    # Text input
    text_input = tk.Entry(window, width=48)
    text_input.grid(column=0, row=0, sticky='NW', padx=25, pady=30)
    convert_input = ttk.Button(window, text="Convert")
    convert_input.grid(column=0, row=0, sticky='NE', pady=50, padx=68)
    browse_input = ttk.Button(window, text="Browse")
    browse_input.grid(column=0, row=0, sticky='NE', pady=75, padx=68)

    # QR code display
    img_qr = Image.open('output.png').resize((270, 270))
    img_qr = ImageTk.PhotoImage(img_qr)
    img_qr_label = ttk.Label(image=img_qr)
    img_qr_label.image = img_qr
    img_qr_label.grid(column=1, row=0)

    # radio buttons
    mode = tk.StringVar()
    subtitle = ttk.Label(window, text="Mode:")
    subtitle.grid(column=0, row=1, sticky='NW', padx=25)
    encode = ttk.Radiobutton(window, text="Encode", value='encode')
    decode = ttk.Radiobutton(window, text="Decode", value='decode')
    encode.grid(column=0, row=1, sticky='NW', padx=25, pady=25)
    decode.grid(column=0, row=1, sticky='NW', padx=125, pady=25)

    window.mainloop()


if __name__ == '__main__':
    main()
