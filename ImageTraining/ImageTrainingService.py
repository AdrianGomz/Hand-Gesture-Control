import cv2
import numpy as np
import math
import time

class ImageTrainingService():
    def __init__(self):
        self.imageSize = 300
        self.counter = 0

    def getTrainingImage(self, img, boundaries):
        if boundaries:
            offset = 10
            hand_proced_images = []
            for boundary in boundaries:
                x, y, w, h = boundary

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
                hand_proced_images.append(imgBackground)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                self.counter+=1
                cv2.imwrite(f'trainingImages/b/image_{time.time()}.jpg', imgBackground)
                print(self.counter)

            return hand_proced_images


