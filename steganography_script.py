import cv2
import os
import urllib.request
from urllib.parse import urlparse

def download_image(url, save_path):
    urllib.request.urlretrieve(url, save_path)

def extract_image_url(url):
    # Extracts the direct image URL from iStock-style URLs
    parsed_url = urlparse(url)
    if parsed_url.netloc == 'www.istockphoto.com' and '/photo/' in parsed_url.path:
        return f"https://{parsed_url.netloc}/photos/{parsed_url.path.split('/')[-1]}/download?size=large"

    return url

def encrypt_image(image_path, secret_message, password):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Unable to read the image. Please check the image path.")
        return

    d = {chr(i): i for i in range(256)}

    m = 0
    n = 0
    z = 0

    for char in secret_message:
        img[n, m, z] = d[char]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("Encryptedmsg.jpg", img)
    os.system("start Encryptedmsg.jpg")

def decrypt_image(image_path, password, passcode):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Unable to read the image. Please check the image path.")
        return

    c = {i: chr(i) for i in range(256)}

    message = ""
    n = 0
    m = 0
    z = 0

    if password == passcode:
        for _ in range(len(secret_message)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decryption message:", message)
    else:
        print("Not a valid key")

# Input
image_url = input("Enter the URL of the image: ")
secret_message = input("Enter secret message: ")
password = input("Enter password: ")

# Extract direct image URL from iStock-style URLs
image_url = extract_image_url(image_url)

# Download image
download_image(image_url, "downloaded_image.jpg")
print("Image Path:", os.path.abspath("downloaded_image.jpg"))

# Encryption
encrypt_image("downloaded_image.jpg", secret_message, password)

# Decryption
passcode = input("Enter passcode for Decryption: ")
decrypt_image("Encryptedmsg.jpg", password, passcode)
