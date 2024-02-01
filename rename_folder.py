import os

base_dir = '/repos/indian_painting_dataset'

# for i in os.walk(base_dir):
#     if 'Google Search' in i[0]:
#         os.rename(i[0], i[0].replace(' - Google Search', ''))

valid_images = [".jpg", ".gif", ".png", ".tga", '.jpeg', '.webp']
for i in os.walk(base_dir):
    for k, j in enumerate(os.listdir(i[0])):
        ext = os.path.splitext(j)[1]
        if ext.lower() in valid_images:
            try:
                os.rename(os.path.join(i[0], j), os.path.join(i[0], i[0].split('\\')[1].split()[0] + str(k) + ext))
            except FileExistsError:
                print('file already exists')