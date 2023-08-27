import cv2
import mediapipe as mp
import numpy as np
from keras.models import load_model
from cvzone.ClassificationModule import Classifier

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




    def getHandBoundaries(self, image_height, image_width, hand_landmarks):
        if hand_landmarks:
            boundaries = []
            for hand in hand_landmarks:
                landmark_array = np.empty((0, 2), int)
                for id, landmark in enumerate(hand.landmark):
                    landmark_x = min(int(landmark.x * image_width), image_width - 1)
                    landmark_y = min(int(landmark.y * image_height), image_height - 1)

                    landmark_point = [np.array((landmark_x, landmark_y))]

                    landmark_array = np.append(landmark_array, landmark_point, axis=0)

                x, y, w, h = cv2.boundingRect(landmark_array)
                boundaries.append([x,y,w,h])
            return boundaries
        
    def classifyGestureKeras(self, img):

        model = load_model("resources/keras_Model.h5", compile=False)

        class_names = open("resources/labels.txt", "r").readlines()
        image = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)


        image = (image / 127.5) - 1

        # Predicts the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
    def classifyGesture(self, img):
        return
        classifier = Classifier("resources/keras_Model.h5", "resources/labels.txt")
        print(classifier.getPrediction(img))

