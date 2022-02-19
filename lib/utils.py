from PIL import Image
import glob

def image_conversion(img_dir):
    for filename in glob.iglob(img_dir + '**/*.png', recursive=True):
        image = Image.open(filename)
        filename = filename.replace(chr(92), "/").replace(img_dir+"/", "")

        if image.mode != "RGB":
            image = image.convert(mode="RGB")
            image.save(filename)
            print(filename)
