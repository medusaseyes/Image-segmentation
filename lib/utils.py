from PIL import Image
import glob

def image_conversion(img_dir):
    for filename in glob.iglob(img_dir + '**/*.bmp', recursive=True):
        image = Image.open(filename)
        filename = filename.replace(chr(92), "/").replace(img_dir+"/", "")

        if image.mode != "RGB":
            image = image.convert(mode="RGB")
            image.save(f"{img_dir}/{filename}")
            print(f"{filename} = {image.mode}")

    for filename in glob.iglob(img_dir + '**/*.tif', recursive=True):
        print(filename)
        image = Image.open(filename)
        filename = filename.replace(chr(92), "/").replace(img_dir+"/", "")
        print(image.format)
        
        if image.format == "TIFF":
            filename = filename.replace(".tif", ".bmp")
            image.save(f"{img_dir}/{filename}")
"""
    for i in range(1,10):    
        if i<10:
            filename =  "C:/Users/rosid/medusas/Image-segmentation/data/0" +  str(i) +  ".tif"
            img = Image.open(filename)
            filename_bmp =  "C:/Users/rosid/medusas/Image-segmentation/data/0" +  str(i) +  ".bmp"
            img.save(filename_bmp)
        if i>9:
            filename =  "C:/Users/rosid/medusas/Image-segmentation/data/" +  str(i) +  ".tif"
            img = Image.open(filename)
            filename_bmp =  "C:/Users/rosid/medusas/Image-segmentation/data/" +  str(i) +  ".bmp"
            img.save(filename_bmp)
 """       
image_conversion("../data/01/train")
