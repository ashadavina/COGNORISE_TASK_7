#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import qrcode
import cv2

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def decode_qr_code(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return "Error: Unable to load or read the image file."
    
    detector = cv2.QRCodeDetector()
    retval, decoded_info, points = detector.detectAndDecode(img)
    if retval:
        return decoded_info
    else:
        return "QR Code not detected or could not be decoded."

def main():
    while True:
        print("\n1. Generate QR Code")
        print("2. Decode QR Code")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter the data to encode: ")
            filename = input("Enter the filename to save QR code (with extension): ")
            generate_qr_code(data, filename)
            print(f"QR code generated and saved as {filename}")
        elif choice == '2':
            image_path = input("Enter the path to the image containing QR code: ")
            decoded_data = decode_qr_code(image_path)
            print("Decoded data:", decoded_data)
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()


# In[ ]:




