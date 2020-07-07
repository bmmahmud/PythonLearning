# B.M.ASHIK MAHMUD
# TRAINING PYTHON - IMAGE JOIN

from PIL import Image

img1 = Image.open("F:/PythonLearning/PythonTraining/Training/figure-A.png")
img2 = Image.open("F:/PythonLearning/PythonTraining/Training/figure-B.png")
img3 = Image.open("F:/PythonLearning/PythonTraining/Training/figure-C.png")
img4 = Image.open("F:/PythonLearning/PythonTraining/Training/figure-D.png")

# img4.show()

# JOIN TWO IMAGE
# width,height = img1.size
# imageSize = Image.new('RGB',(1200,480)) # Defininf the main Frame size
# imageSize.paste(img1,(0,0))
# imageSize.paste(img2,(width,0))
# imageSize.save("two_image.png")
#
# imgJointwo = Image.open("F:/PythonLearning/PythonTraining/Training/two_image.png")
# imgJointwo.show()



# JOIN Four IMAGE
width,height = img1.size
imageSize = Image.new('RGB',(1200,960)) # Defininf the main Frame size
imageSize.paste(img1,(0,0))
imageSize.paste(img2,(width,0))
imageSize.paste(img3,(0,height))
imageSize.paste(img4,(width,height))

imageSize.save("four_image.png")

imgJointwo = Image.open("F:/PythonLearning/PythonTraining/Training/four_image.png")
imgJointwo.show()


