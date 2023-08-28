import cv2
import HandTracking.HandTrakingService as HandTrackingService
import Drawing.DrawingService as DrawingService
import ImageTraining.ImageTrainingService as ImageTrainingService
import numpy as np
import time


getTrainingImages = True
withdCam,heigtCam=1080,760

camera=cv2.VideoCapture(0)
camera.set(3,withdCam)
camera.set(4,heigtCam)
handTrackerService=HandTrackingService.HandTrackingService(detection_confidence=0.9)
drawingService = DrawingService.DrawingService()
imageTrainigService = ImageTrainingService.ImageTrainingService()


while True:
    confirm, img=camera.read()
    trainingBackground = np.ones((img.shape[0], img.shape[1], 3),np.uint8)
    
    lmList = handTrackerService.getHandLandmarks(img)

    if lmList:
        drawingService.drawHands(img,lmList)
        drawingService.drawHands(trainingBackground, lmList)
        hand_boundaries = handTrackerService.getHandBoundaries(img.shape[0], img.shape[1], lmList)
        drawingService.drawHandBoundaries(img,hand_boundaries)

        if getTrainingImages:
            trainingImage = imageTrainigService.getTrainingImage(trainingBackground, hand_boundaries)
            class_label = handTrackerService.classifyGesture(trainingImage)
            drawingService.drawLabel(img, class_label, hand_boundaries)
            

    cv2.imshow("Camara", img)

    if getTrainingImages:
        cv2.imshow("handsLandmarks", trainingBackground)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
