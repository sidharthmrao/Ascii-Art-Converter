import cv2

image = "07CAT-STRIPES-mediumSquareAt3X-v2.jpg"

img = cv2.imread(f"./{image}")

scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
print("HI")
cv2.imwrite("./img_BW.jpg", blackAndWhiteImage)
print(blackAndWhiteImage.shape)

ascii_shape = []

for i in range(len(blackAndWhiteImage)):
    ascii_shape.append("")
    for j, val in enumerate(blackAndWhiteImage[i]):
        if val == 255:
            ascii_shape[i] += "-" # "- "
        else:
            ascii_shape[i] += "+" # "+ "
    ascii_shape[i] += "\n"

print(ascii_shape)

x = open("./ascii.txt", "w")
x.writelines(ascii_shape)

