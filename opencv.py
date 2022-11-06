import cv2

img = cv2.imread('samsung.png')

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(type(img))
print(img.shape)

img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('image', img_convert)
cv2.waitKey(0)
cv2.destroyAllWindows()
