from PIL import Image
def resize_img(size1,size2):

    image=Image.open('IMG20230625191721.jpg')
    print(f"Current size: {image.size}")
    resized_img=image.resize((size1,size2))
    resized_img.save('resized_pic-'+ str(size1)+'.jpg')


size1=int(input("Enter Width: "))
size2=int(input("Enter Height:"))
resize_img(size1,size2)