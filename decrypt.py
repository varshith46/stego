import cv2

img = cv2.imread("encryptedImage.png")

try:
    with open("key.txt", "r") as f:
        correct_pass = f.read().strip()
except FileNotFoundError:
    print("Key missing!")
    exit()

password = input("Enter password: ")
if password != correct_pass:
    print("Access denied!")
    exit()

msg_bytes = bytearray()
for n in range(img.shape[0]):
    for m in range(img.shape[1]):
        for z in range(3):
            byte = img[n, m, z]
            if byte == 0:  # Stop at NULL byte
                break
            msg_bytes.append(byte)
        else:
            continue
        break
    else:
        continue
    break

msg = msg_bytes.decode("utf-8")
print("Secret message:", msg)

