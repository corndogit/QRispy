import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from qr_codec import make_qr_code, decode_qr_code


def main():
    # Window
    window = tk.Tk()
    window.title("QRispy")
    window.resizable(False, False)
    frame = tk.Frame(window, width=700, height=350)
    frame.grid(columnspan=2, rowspan=2)

    # Title
    title = ttk.Label(window)
    title.config(text="Encode:")
    title.grid(column=0, row=0, sticky='NW', padx=25, pady=10)

    # Text input
    text_input = tk.Entry(window, width=48)
    text_input.grid(column=0, row=0, sticky='NW', padx=25, pady=30)
    convert_input = ttk.Button(window, text="Convert")
    convert_input.grid(column=0, row=0, sticky='NE', pady=50, padx=68)
    browse_input = ttk.Button(window, text="Browse...", command=lambda: fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=(('text files', '*.txt'),
                   ('All files', '*.*'))
    ))
    browse_input.grid(column=0, row=0, sticky='NE', pady=75, padx=68)

    # QR code display
    img_qr = Image.open('main_logo.png').resize((270, 270))
    img_qr = ImageTk.PhotoImage(img_qr)
    img_qr_label = ttk.Label(image=img_qr)
    img_qr_label.image = img_qr
    img_qr_label.grid(column=1, row=0)

    # radio buttons
    # subtitle = ttk.Label(window, text="Mode:")
    # subtitle.grid(column=0, row=1, sticky='NW', padx=25)
    # selected_mode = tk.StringVar()
    # modes = (('Encode', 'encode'), ('Decode', 'decode'))
    # x_padding = 25
    # for m in modes:
    #     r = ttk.Radiobutton(window,
    #                         text=m[0],
    #                         value=m[1],
    #                         variable=selected_mode)
    #     r.grid(column=0, row=1, sticky='NW', padx=x_padding, pady=25)
    #     x_padding += 100

    window.mainloop()


if __name__ == '__main__':
    main()
