import csv, os
from PIL import Image 

base_dir = '/repos/indian_painting_dataset'
valid_images = [".jpg", ".gif", ".png", ".tga", '.jpeg', '.webp']

with open('classes.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    field = ['image', 'width', 'height', 'class']

    writer.writerow(field)

    for i in os.walk(base_dir):
        for k, j in enumerate(os.listdir(i[0])):
            ext = os.path.splitext(j)[1]
            if ext.lower() in valid_images:
                try:
                    img = Image.open(os.path.join(i[0], j))
                    writer.writerow([j, img.size[0], img.size[1], i[0].split('\\')[1].split()[0]])
                except Exception as e:
                    print('error', e)