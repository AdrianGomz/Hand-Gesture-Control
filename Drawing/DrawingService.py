import cv2
import mediapipe as mp
import numpy as np

class DrawingService(): 
    def __init__(self):
        self.hands_ms = mp.solutions.hands
        self.mpDraw = mp.solutions.drawing_utils

    def drawHands(self,frame,hand_landmarks):
        if hand_landmarks:
            for hand_in_image in hand_landmarks:
                    self.mpDraw.draw_landmarks(frame, hand_in_image, self.hands_ms.HAND_CONNECTIONS)

    def drawHandBoundaries(self, img, boundaries):
        for boundary in boundaries:
            x, y, w, h = boundary
            self.drawBoundaries(img,x-5,x+w+5,y-5,y+h+5)



    def drawBoundaries(self, img, min_x, max_x, min_y, max_y, color = (255, 0, 0),thickness=1):
        cv2.rectangle(img, (min_x, min_y),(max_x, max_y), color, thickness)
         
