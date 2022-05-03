import textwrap
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText
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

        # Inputs
        def get_file_to_decode():
            file = fd.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=(('QR code to decode', '*.png'),
                           ('All files', '*.*'))
            )
            if file:
                decoded_data = decode_qr_code(file)
                output_file = open('output.txt', 'w')
                output_file.write(decoded_data)
                output_file.close()
                return decoded_data

        def change_text(text):
            decoded_string = get_file_to_decode()
            if decoded_string:
                try:
                    text.delete('1.0', 'end')
                    text.insert('1.0', decoded_string)
                except IndexError:
                    text.insert('1.0', decoded_string)

        browse_input = ttk.Button(self, text="Convert from file...", command=lambda: change_text(text_box))
        browse_input.grid(column=0, row=0, sticky='NW', pady=40, padx=24)

        # decoded text
        text_box = ScrolledText(self, width=55, height=16)
        text_box.grid(column=1, row=0, sticky='E', padx=60)
        text_box_contents = textwrap.dedent("""
        Convert a QR code image to text
        
        Tips:
        * Make sure the QR code is clearly legible and in focus
        * Make sure the QR code is on a light background
        """)
        text_box.insert('1.0', text_box_contents)

        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")


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
        # self.resizable(False, False)


if __name__ == '__main__':
    app = App()
    ControlFrame(app)
    app.mainloop()
