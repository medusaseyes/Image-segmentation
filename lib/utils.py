from PIL import Image
import glob, os

def image_conversion(img_dir):
    for filename in glob.iglob(img_dir + '**/*.bmp', recursive=True):
        image = Image.open(filename)
        filename = filename.replace(chr(92), "/").replace(img_dir+"/", "")

        if image.mode != "RGB":
            image = image.convert(mode="RGB")
            image.save(f"{img_dir}/{filename}")
            print(f"{filename} = {image.mode}")

    for filename in glob.iglob(img_dir + '**/*.tif', recursive=True):
        image = Image.open(filename)
        filename = filename.replace(chr(92), "/").replace(img_dir+"/", "")
        
        if image.format == "TIFF":
            trash = f"{img_dir}/{filename}"
            filename = filename.replace(".tif", ".bmp")
            image.save(f"{img_dir}/{filename}")
            os.remove(trash)
