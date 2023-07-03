import os
import subprocess

directory = os.getcwd()
images = os.path.join(directory, "Doge")

for filename in os.listdir(images):
    if filename.endswith(".png"):
        original_path = os.path.join(images, filename)
        new_path = os.path.join(directory, "sized/" + filename)

        print('Running: "magick convert "' + original_path + '" -resize 50% "' + new_path + '""')
        subprocess.run(['cmd', '/c', 'magick', "convert", original_path, "-resize", "50%", new_path], shell=True)