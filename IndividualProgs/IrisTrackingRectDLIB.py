import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

#refer to the 68-face-landmarks-labeled-by-dlib-software-automatically.png to understand why certain coordinates are used to find certain parts of the face

detector = dlib.get_frontal_face_detector()  #front face classifier
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #assigned coordinates of the face by DLIB

while True:
    ret, frame = cap.read() #return status variable and the captured image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #grayscale image for detection filtering of eyes

    faces = detector(gray) #array of all faces
    for face in faces:
        x, y  = face.left(), face.top() # Top Left coordinates of face in window
        x1, y1 = face.right(), face.bottom() # Bottom right coordinates of face in windows
        cv2.rectangle(frame, (x,y), (x1,y1), (0,255,0), 2) # form a rectangle based on previous two coordinates

        poslandmarkpoints = predictor(gray, face)

        # LEFT EYE TRACKING WITH DLIB
        # Using the DLIB landmarks diagram, coordinates 38 will be used for length of box
        # Width
        #(poslandmarkpoints.part(38).x, poslandmarkpoints.part(38).y)   coordinate for left most eye to determine width of eye rectangle
        
        # Using the DLIB landmarks diagram, coordinates 41 will be used for height of box
        # Height
        #(poslandmarkpoints.part(41).x, poslandmarkpoints.part(41).y)   first coordinate for left most eye to determine width of eye rectangle

        #x1,y1 ------
        #|          |
        #|          |
        #|          |
        #--------x2,y2
        
        left_eye1x = poslandmarkpoints.part(38).x
        left_eye1y = poslandmarkpoints.part(38).y
        left_eye2x = poslandmarkpoints.part(41).x
        left_eye2y = poslandmarkpoints.part(41).y
        

      
        
        # RIGHT EYE TRACKING WITH DLIB
        # Using the DLIB landmarks diagram, coordinates 44 will be used for length of box
        # Width
        #(poslandmarkpoints.part(44).x, poslandmarkpoints.part(44).y)   coordinate for left most eye to determine width of eye rectangle
        
        # Using the DLIB landmarks diagram, coordinates 47 will be used for height of box
        # Height
        #(poslandmarkpoints.part(47).x, poslandmarkpoints.part(47).y)   first coordinate for left most eye to determine width of eye rectangle

        
        #x1,y1 ------
        #|          |
        #|          |
        #|          |
        #--------x2,y2
        
                
        right_eye1x = poslandmarkpoints.part(44).x
        right_eye1y = poslandmarkpoints.part(44).y
        right_eye2x = poslandmarkpoints.part(47).x
        right_eye2y = poslandmarkpoints.part(47).y

       

        # ================================ tracking left eye on new window ================================
        
        #Right Eye Tracking
        rightEyeTrack = np.array([(right_eye1x-40,right_eye1y-20),
                                 (right_eye1x-40,right_eye2y+20),
                                 (right_eye2x+40,right_eye2y-20),
                                 (right_eye2x+40,right_eye2y+20)
                                 ],
                                np.int32)
        

        
        #Left Eye Tracking
        leftEyeTrack = np.array([(left_eye1x-40,left_eye1y-20),
                                 (left_eye1x-40,left_eye2y+20),
                                 (left_eye2x+40,left_eye2y-20),
                                 (left_eye2x+40,left_eye2y+20)
                                 ],
                                np.int32)

        lemin_x = np.min(leftEyeTrack[:, 0])
        lemax_x = np.max(leftEyeTrack[:, 0])
        lemin_y = np.min(leftEyeTrack[:, 1])
        lemax_y = np.max(leftEyeTrack[:, 1])

        left_eye = frame[lemin_y : lemax_y, lemin_x : lemax_x]
        left_eye = cv2.resize(left_eye, None, fx = 5, fy = 5) #fx and fy is the scale factor for frame
        cv2.imshow("Left Eye", left_eye)

        # ================================ tracking left eye on new window ================================

        
        # ================================ tracking right eye on new window ================================

        remin_x = np.min(rightEyeTrack[:, 0])
        remax_x = np.max(rightEyeTrack[:, 0])
        remin_y = np.min(rightEyeTrack[:, 1])
        remax_y = np.max(rightEyeTrack[:, 1])

        right_eye = frame[remin_y : remax_y, remin_x : remax_x]
        right_eye = cv2.resize(right_eye, None, fx = 5, fy = 5) #fx and fy is the scale factor for frame
        cv2.imshow("Right Eye", right_eye)

        # ================================ tracking right eye on new window ================================

        #draw rectangle after eye frame is on window to prevent drawn polys from showing in eye window        
        cv2.rectangle(frame, (right_eye1x-40,right_eye1y-20), (right_eye2x+40,right_eye2y+20), (0,255,0), 2)
        cv2.rectangle(frame, (left_eye1x-40,left_eye1y-20), (left_eye2x+40,left_eye2y+20), (0,255,0), 2)
                
    cv2.imshow("IrisTrackingRectDLIB", frame)
    key = cv2.waitKey(1)
    if key == 27: #esc key is pressed
        break


cap.release()
cv2.destroyAllWindows()
