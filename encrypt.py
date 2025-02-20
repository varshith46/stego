import cv2

img = cv2.imread("mypic.jpg")
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

with open("key.txt", "w") as f:
    f.write(password)

msg += "\0"  # NULL byte as end marker
msg_bytes = msg.encode("utf-8")

if len(msg_bytes) > img.size:
    print("Message too long!")
    exit()

index = 0
for n in range(img.shape[0]):
    for m in range(img.shape[1]):
        for z in range(3):
            if index < len(msg_bytes):
                img[n, m, z] = msg_bytes[index]
                index += 1
            else:
                break
        else:
            continue
        break

cv2.imwrite("encryptedImage.png", img)
print("Encryption done. Saved as 'encryptedImage.png'.")
