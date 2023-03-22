import numpy as np
import cv2

img = cv2.imread('/Users/jordan/Documents/GitHub/DTUImageAnalysis/exercises/ex1-IntroductionToImageAnalysis/data/Denmark.jpg', 0)
print(img)

cv2.imshow('Butterfly', img)
if img is None:
    print("Check file path")
cv2.waitKey(0)
cv2.destroyAllWindows()
