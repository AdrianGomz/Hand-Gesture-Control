import cv2
import HandTracking.HandTrakingService as HandTrackingService
import Drawing.DrawingService as DrawingService


withdCam,heigtCam=1080,760

camera=cv2.VideoCapture(0)
camera.set(3,withdCam)
camera.set(4,heigtCam)
handTrackerService=HandTrackingService.HandTrackingService(detection_confidence=0.9)
drawingService = DrawingService.DrawingService()


while True:
    confirm, img=camera.read()
    lmList = handTrackerService.getHandLandmarks(img)
    drawingService.drawHands(img,lmList)
    drawingService.drawHandBoundaries(img,lmList)



    cv2.imshow("Camara", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
