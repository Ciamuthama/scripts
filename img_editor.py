from PIL import Image,ImageEnhance,ImageFilter
import os

path = './imgs'
outputPath ='./editedImgs'

for filename in os.listdir(path):
    img = Image.open( f"{path}/{filename}")
    edit = img.filter(ImageFilter.GaussianBlur(radius=10)).convert("L")
    
    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{outputPath}/{clean_name}_edited.jpg")
    

