# QRispy
Uses qrcode and pyzbar libraries to encode/decode QR codes in Python.

## Usage
### Terminal
`main.py <encode/decode> <input_data>`

* For `encode`, `input_data` would be a string and outputs QR code to output.png.  
* For `decode`, `input_data` would be an image file containing QR code to read.

## Examples
###Encoding a string to QR code
![QR code](https://i.imgur.com/MrNDhWh.png)  
This QR code contains the word 'Test'. QR codes are automatically scaled relative to the length of bytes.

### Decoding a QR code
Calling `decode_qr_code()` on the image path returns a list object containing the QR code data (in bytes) and metadata. By calling the `data.decode()` method we can encode it with UTF-8 or ASCII.

#### Todo
* Encode bytes returned from decoded QR code into a string, return to user.
* Implement style options for QR code supported by the qrcode library
