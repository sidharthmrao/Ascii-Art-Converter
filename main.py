import cv2

image = "RickAstley2021.jpg"

img = cv2.imread(f"./{image}")

scale_percent = 5  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
 
print('Resized Dimensions : ', resized.shape)

ascii_shape = []

for i in range(len(resized)):
    ascii_shape.append("")
    for j, val in enumerate(resized[i]):
        ascii_shape[i] += chr(val[0]//30 + 33)
        print(chr(val[0] + 33), end="")
    ascii_shape[i] += "\n"

x = open("./ascii.txt", "w")
x.writelines(ascii_shape)

