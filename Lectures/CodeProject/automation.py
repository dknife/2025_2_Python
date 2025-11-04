from PIL import Image
import os

input_folder = "images"
output_folder = "resized"
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith( (".jpg", ".png") ) :
        img = Image.open(os.path.join(input_folder, file))
        img = img.resize( (200, 200) )
        img.save(os.path.join(output_folder, file))
        print(f'{file} resized')


