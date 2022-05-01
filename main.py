import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox
from PIL import Image, ImageTk
from qr_codec import make_qr_code, decode_qr_code


class EncodeFrame(ttk.Frame):
    def __init__(self, container, mode):
        super().__init__(container)

        # Title
        self.title = ttk.Label(self, text=mode)
        self.title.grid(column=0, row=0, sticky='NW', padx=25, pady=10)

        # QR code display
        self.img_qr = ImageTk.PhotoImage(Image.open('main_logo.png'))
        self.img_qr_label = ttk.Label(self, image=self.img_qr)
        self.img_qr_label.grid(column=1, row=0)

        # Text input
        def get_text_to_encode(text):
            make_qr_code(text).save('output.png')
            generated_qr = ImageTk.PhotoImage(Image.open('output.png').resize((270, 270)))
            self.img_qr_label.configure(image=generated_qr)

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
                    generated_qr = ImageTk.PhotoImage(Image.open('output.png').resize((270, 270)))
                    self.img_qr_label.configure(image=generated_qr)
                    # tk.messagebox.showinfo(title='Success!', message='Your QR code was saved as output.png')
                except UnicodeDecodeError:
                    tk.messagebox.showerror(title='Error',
                                            message='Unable to read file (please use only plaintext files)')
        text_input = tk.Entry(self, width=48)
        text_input.grid(column=0, row=0, sticky='NW', padx=25, pady=30)
        convert_input = ttk.Button(self, text="Convert", command=lambda: get_text_to_encode(text_input.get()))
        convert_input.grid(column=0, row=0, sticky='NE', pady=55, padx=24)
        browse_input = ttk.Button(self, text="Convert from file...", command=lambda: get_file_to_encode())
        browse_input.grid(column=0, row=0, sticky='NW', pady=55, padx=24)

        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")


class DecodeFrame(ttk.Frame):
    def __init__(self, container, mode):
        super().__init__(container)

        # Title
        title = ttk.Label(self, text=mode)
        title.grid(column=0, row=0, sticky='NW', padx=25, pady=10)


class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self['text'] = 'Options'

        # radio buttons
        self.selected_value = tk.IntVar()

        ttk.Radiobutton(
            self,
            text='Encode',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='Decode',
            value=1,
            variable=self.selected_value,
            command=self.change_frame).grid(column=1, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

        # initialise frames
        self.frames = {
            0: EncodeFrame(container, 'Encode:'),
            1: DecodeFrame(container, 'Decode: ')
        }

        self.change_frame()

    def change_frame(self):
        frame = self.frames[self.selected_value.get()]
        frame.tkraise()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('QRispy')
        self.geometry('700x350')
        self.resizable(False, False)


if __name__ == '__main__':
    app = App()
    ControlFrame(app)
    app.mainloop()
