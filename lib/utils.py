from PIL import Image
import glob, os

def image_conversion(img_dir):
    """Converte as imagens de rgba para rgb e de .tif para .bmp"""
    for filename in glob.iglob(img_dir + '**/*.bmp', recursive=True):
        image = Image.open(filename)
        filename = filename.replace(chr(92), "/").replace(img_dir+"/", "")

        if image.mode != "RGB":
            image = image.convert(mode="RGB")
            image.save(f"{img_dir}/{filename}")
            print(f"{filename} = {image.mode}")
            image.close()

    for filename in glob.iglob(img_dir + '**/*.tif', recursive=True):
        image = Image.open(filename)
        filename = filename.replace(chr(92), "/").replace(img_dir+"/", "")
        
        if image.format == "TIFF":
            trash = f"{img_dir}/{filename}"
            filename = filename.replace(".tif", ".bmp")
            image.save(f"{img_dir}/{filename}")
            image.close()
            os.remove(trash)

def name_generation(save_cut_dir):
    """Faz a contagem de elementos dentro do dir para auxiliar na criação dos nomes"""
    count = 1

    for filename in glob.iglob(save_cut_dir + '**/*.bmp', recursive=True):
        count+=1
    
    for filename in glob.iglob(save_cut_dir + '**/*.tif', recursive=True):
        count+=1

    return f"{count}.tif"
