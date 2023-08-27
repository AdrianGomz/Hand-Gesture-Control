import cv2
import numpy as np
import math

class ImageTrainingService():
    def __init__(self):
        self.imageSize = 300

    def getTrainingImage(self, img, boundaries):
        if boundaries:
            offset = 10
            x, y, w, h = boundaries[0]

            imgBackground = np.ones((self.imageSize, self.imageSize,3),np.uint8)


            imgCrop = img[y - offset : y + h + offset,
                           x - offset : x + w + offset]

            aspectRatio = h / w
            if aspectRatio > 1:
                k = self.imageSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop,(wCal, self.imageSize))
                wGap = math.ceil((self.imageSize - wCal) / 2)
                imgBackground[:, wGap:wCal+wGap] = imgResize
            else:
                k = self.imageSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop,(self.imageSize, hCal))
                hGap = math.ceil((self.imageSize - hCal) / 2)
                imgBackground[hGap:hCal + hGap, :] = imgResize


            cv2.imshow("TrainerImage",imgBackground)
            cv2.waitKey(1)


