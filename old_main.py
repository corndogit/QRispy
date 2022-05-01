import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox
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

    # QR code display
    img_qr = ImageTk.PhotoImage(Image.open('main_logo.png'))
    img_qr_label = ttk.Label(window, image=img_qr)
    img_qr_label.grid(column=1, row=0)

    # Text input
    text_input = tk.Entry(window, width=48)
    text_input.grid(column=0, row=0, sticky='NW', padx=25, pady=30)
    convert_input = ttk.Button(window, text="Convert", command=lambda: get_text_to_encode(text_input.get()))
    convert_input.grid(column=0, row=0, sticky='NE', pady=50, padx=68)
    browse_input = ttk.Button(window, text="Convert from file...", command=lambda: get_file_to_encode())

    def get_text_to_encode(text):
        make_qr_code(text).save('output.png')
        generated_qr = ImageTk.PhotoImage(Image.open('output.png'))
        img_qr_label.configure(image=generated_qr)
        # tk.messagebox.showinfo(title='Success!', message='Your QR code was saved as output.png')

    def get_file_to_encode():
        file = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=(('Text to encode', '*.txt'),
                       ('All files', '*.*'))
        )
        if file:
            try:
                read_file = "".join(open(file, 'r').readlines())
                make_qr_code(read_file).save('output.png')
                generated_qr = ImageTk.PhotoImage(Image.open('output.png'))
                img_qr_label.configure(image=generated_qr)
                # tk.messagebox.showinfo(title='Success!', message='Your QR code was saved as output.png')
            except UnicodeDecodeError:
                tk.messagebox.showerror(title='Error', message='Unable to read file (please use only plaintext files)')

    browse_input.grid(column=0, row=0, sticky='NE', pady=75, padx=68)

    # radio buttons - for switching between encode and decode layout
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
