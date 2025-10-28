
import qrcode
import matplotlib.pyplot as plt

url = input("QR로 만들 URL을 입력하세요: ")

print(url)

# 제대로 된 URL인지 체크하자.

if not url.startswith( ("http://", "https://") ):
    print("URL 이상")
    url = "https://" + url

print(url)

# URL을 이용하여 QR을 만들자

qr = qrcode.QRCode(
                    version = 2,
                    error_correction = qrcode.constants.ERROR_CORRECT_L,
                    box_size = 10,
                    border = 1)

qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='gray')
img.save('qr.png')

# 만든 이미지를 그리자

plt.figure(figsize=(6, 6))
plt.imshow(img)
plt.axis('off')
plt.show()


    



            
