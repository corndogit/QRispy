# QRispy
A GUI interface that uses qrcode and pyzbar libraries to encode/decode QR codes in Python.

## Usage
QRispy can be used as either with a GUI or in CLI

### GUI
Currently, only generating QR codes is supported in the GUI version. You can either enter some text directly into the entry box or select a plaintext file to read text from. The generated QR code is saved automatically as 'output.png'
![GUI preview](https://corndog.s-ul.eu/d6Y0V6bk.png)
### Terminal
The qr_codec library can be run directly with the following parameters:  
`qr_codec.py <encode/decode> <input_data>`

* For `encode`, `input_data` would be a string and outputs QR code to output.png.  
* For `decode`, `input_data` would be path to an image file containing QR code to read.

## Examples

###Encoding a string to QR code
![QR code](https://i.imgur.com/MrNDhWh.png)  
This QR code contains the word 'Test'. QR codes are automatically scaled relative to the length of bytes.

### Decoding a QR code  
Calling `decode_qr_code()` on the image path returns a list object containing the QR code data (in bytes) and metadata. By calling the `data.decode()` method we can encode it with UTF-8 or ASCII.

#### Todo
* Add GUI to decode QR codes
* Implement style options for QR code supported by the qrcode library
* Add format options for saving (.PNG or .SVG)

#### Known bugs
* `qrcode.exceptions.DataOverflowError` thrown when a text file with too many characters is selected. 