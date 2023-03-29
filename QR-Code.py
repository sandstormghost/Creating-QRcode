# import qrcode module
import qrcode
 
# create QR code instance
qr = qrcode.QRCode(
	version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
	box_size=5,
	border=5
)
 
# Enter data that you want to store
qr_data = 'Welcome To Simplified Python'
 
# Add data 
qr.add_data(qr_data)
qr.make(fit=True)
 
# Create an image from the QR code instance
img = qr.make_image(fill_color='blue', back_color='white')
 
# Save the image
img.save('qr.png')
