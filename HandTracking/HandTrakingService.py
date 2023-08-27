import cv2
import mediapipe as mp

class HandTrackingService():
    def __init__(self, static_mode=False, max_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.static_mode = static_mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.hands_ms = mp.solutions.hands
        self.hand_object = mp.solutions.hands.Hands()
        


    def getHandLandmarks(self,frame,draw=True):

        imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        return self.hand_object.process(imgRGB).multi_hand_landmarks




    def handPoints(self, frame, handNo=0, draw=True):
        landmark_list=[]
        if self.processed_image.multi_hand_landmarks:
            hand=self.processed_image.multi_hand_landmarks[handNo]
            for id, landmark in enumerate(hand.landmark):
                    height, width, color= frame.shape
                    Px, Py=int(landmark.x*width),int(landmark.y*height)
                    landmark_list.append([id,Px,Py])
        return landmark_list
