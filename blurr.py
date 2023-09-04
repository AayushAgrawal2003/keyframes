import numpy as np
import cv2 as cv


img = cv.imread("./main.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

image  = np.asarray(gray_img)


laplacian = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])


new_image = np.zeros((len(image) -2, len(image[0] - 2)), np.float32)


def convolve(arr1, arr2):
    final = 0
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            final += arr1[i][j] * arr2[i][j]

    return(final)

for i in range(len(image)-2):
    for j in range(len(image[0])-2):
        # print(image[i:i+3 , j:j+3] , laplacian)
        new_image[i][j] = convolve(gray_img[i:i+3 ,j:j+3] , laplacian)


print(new_image)
new_image = cv.cvtColor(new_image, cv.COLOR_GRAY2BGR) 
cv.imshow("sample", new_image)

cv.waitKey(0)

