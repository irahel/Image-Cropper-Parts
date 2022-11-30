from PIL import Image
import os

#CONSTANTS
NEW_PATH        = r'cropped'
EXTENSION       = '.jpg'
EXTENSION_NAME  = 'JPEG'
CROP_SIZE       = 200

print("Inited")

#Create folder
if not os.path.exists(NEW_PATH):
    os.makedirs(NEW_PATH)

image_count = 1

print("Getting archives")
images = os.listdir()

for element in images:
    #Open archive
    print("Opening image ", image_count)
    try:
        img = Image.open(element)
        print("Open sucessfull")
    except:
        print("Open error")
        continue

    width, height = img.size

    print("Calculating crops")
    width_crop  = int(width / CROP_SIZE)
    height_crop = int(height / CROP_SIZE)

    last_width  = 0
    last_height = 0
    part = 1

    for _ in range (height_crop):    
        for _ in range (width_crop):
            print("Cropping part ", part)
            new_img = img.crop((last_width, last_height, last_width + CROP_SIZE, last_height + CROP_SIZE))
            new_img.save(
                f'{NEW_PATH}/image_{str(image_count)}_cropped_part_{str(part)}{EXTENSION}',
                EXTENSION_NAME,
            )


            last_width += CROP_SIZE
            part += 1
        last_height += CROP_SIZE
        last_width = 0

    image_count += 1
    img._getexif()

print("Ended")