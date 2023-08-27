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

    def drawHandBoundaries(self, img, hand_landmarks):
        image_width, image_height = img.shape[1], img.shape[0]

        if hand_landmarks:
            for hand in hand_landmarks:
                landmark_array = np.empty((0, 2), int)
                for id, landmark in enumerate(hand.landmark):
                    landmark_x = min(int(landmark.x * image_width), image_width - 1)
                    landmark_y = min(int(landmark.y * image_height), image_height - 1)

                    landmark_point = [np.array((landmark_x, landmark_y))]

                    landmark_array = np.append(landmark_array, landmark_point, axis=0)
                x, y, w, h = cv2.boundingRect(landmark_array)
                self.drawBoundaries(img,x-5,x+w+5,y-5,y+h+5)


    def drawBoundaries(self, img, min_x, max_x, min_y, max_y, color = (255, 0, 0),thickness=1):
        cv2.rectangle(img, (min_x, min_y),(max_x, max_y), color, thickness)
         
