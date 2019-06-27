from PIL import Image

def load_img(file_name):
    im = Image.open(file_name)
    return im

def show_img(img_object):
    img_object.show()

def save_img(img_object, save_name):
    img_object.save(save_name)
img = load_img("image5.jpg")
save_img(img, "Obama.jpg")

#should return a new Image object with filter applied
def obamicon(img_object):
    empty_list = []
    empty_list.append(img_object)

    #create new empty list which you will put all new pixel values int (HINT:USE APPEND)
    original_pixels = img_object.getdata()

    for i in original_pixels:
        if image.color < 182 :
            


   
    #use for loop to iterate through every single pixel
    #at every pixel, sum up the RGB values
    #use conditionals and boolean checks to determine which new color to change to

