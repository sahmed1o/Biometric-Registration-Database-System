import cv2
import numpy as np
import dlib

#This code combines FaceTracking.py with IrisTrackingRectDLIB.py

def show_polyface (frame, poslandmarkpoints):
    
        #Precision Tracking Of face with full poly fill
        drawlinethickness = 1

        #chin
        for p in range(0, 16):
            cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), (0,255,0), drawlinethickness)
        
        #Manual Connections for Chin
        cv2.line(frame, (poslandmarkpoints.part(0).x, poslandmarkpoints.part(0).y), (poslandmarkpoints.part(17).x, poslandmarkpoints.part(17).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(0).x, poslandmarkpoints.part(0).y), (poslandmarkpoints.part(36).x, poslandmarkpoints.part(36).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(0).x, poslandmarkpoints.part(0).y), (poslandmarkpoints.part(31).x, poslandmarkpoints.part(31).y), (0,255,0), drawlinethickness)
        

        #left eye
        for p in range(36, 41):
            cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(41).x, poslandmarkpoints.part(41).y), (poslandmarkpoints.part(36).x, poslandmarkpoints.part(36).y), (0,255,0), drawlinethickness) #close off line for left eye
        cv2.line(frame, (poslandmarkpoints.part(39).x, poslandmarkpoints.part(39).y), (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(39).x, poslandmarkpoints.part(39).y), (poslandmarkpoints.part(31).x, poslandmarkpoints.part(31).y), (0,255,0), drawlinethickness) 
        
        
        #right eye
        for p in range(42, 47):
            cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(47).x, poslandmarkpoints.part(47).y), (poslandmarkpoints.part(42).x, poslandmarkpoints.part(42).y), (0,255,0), drawlinethickness) #close off line for right eye
        cv2.line(frame, (poslandmarkpoints.part(42).x, poslandmarkpoints.part(42).y), (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), (0,255,0), drawlinethickness) #close off line for left eye
        cv2.line(frame, (poslandmarkpoints.part(42).x, poslandmarkpoints.part(42).y), (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), (0,255,0), drawlinethickness) 
        
        
        #nose 
        for p in range(27, 35):
            cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), (poslandmarkpoints.part(30).x, poslandmarkpoints.part(30).y), (0,255,0), drawlinethickness) #close off line for nose
        cv2.line(frame, (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), (poslandmarkpoints.part(31).x, poslandmarkpoints.part(31).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(30).x, poslandmarkpoints.part(30).y), (poslandmarkpoints.part(32).x, poslandmarkpoints.part(32).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(30).x, poslandmarkpoints.part(30).y), (poslandmarkpoints.part(33).x, poslandmarkpoints.part(33).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(30).x, poslandmarkpoints.part(30).y), (poslandmarkpoints.part(34).x, poslandmarkpoints.part(34).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(33).x, poslandmarkpoints.part(33).y), (poslandmarkpoints.part(51).x, poslandmarkpoints.part(51).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), (poslandmarkpoints.part(54).x, poslandmarkpoints.part(54).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(31).x, poslandmarkpoints.part(31).y), (poslandmarkpoints.part(48).x, poslandmarkpoints.part(48).y), (0,255,0), drawlinethickness) 
        
       
        #mouth
        for p in range(48, 59):
            cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(59).x, poslandmarkpoints.part(59).y), (poslandmarkpoints.part(48).x, poslandmarkpoints.part(48).y), (0,255,0), drawlinethickness) #close off line for right eye
        for p in range(60, 67):
            cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(60).x, poslandmarkpoints.part(60).y), (poslandmarkpoints.part(67).x, poslandmarkpoints.part(67).y), (0,255,0), drawlinethickness) #close off line for right eye

        cv2.line(frame, (poslandmarkpoints.part(58).x, poslandmarkpoints.part(58).y), (poslandmarkpoints.part(7).x, poslandmarkpoints.part(7).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(56).x, poslandmarkpoints.part(56).y), (poslandmarkpoints.part(9).x, poslandmarkpoints.part(9).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(48).x, poslandmarkpoints.part(48).y), (poslandmarkpoints.part(3).x, poslandmarkpoints.part(3).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(48).x, poslandmarkpoints.part(48).y), (poslandmarkpoints.part(6).x, poslandmarkpoints.part(6).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(2).x, poslandmarkpoints.part(2).y), (poslandmarkpoints.part(31).x, poslandmarkpoints.part(31).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(54).x, poslandmarkpoints.part(54).y), (poslandmarkpoints.part(13).x, poslandmarkpoints.part(13).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(54).x, poslandmarkpoints.part(54).y), (poslandmarkpoints.part(10).x, poslandmarkpoints.part(10).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), (poslandmarkpoints.part(14).x, poslandmarkpoints.part(14).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), (poslandmarkpoints.part(16).x, poslandmarkpoints.part(16).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(16).x, poslandmarkpoints.part(16).y), (poslandmarkpoints.part(45).x, poslandmarkpoints.part(45).y), (0,255,0), drawlinethickness) 
        cv2.line(frame, (poslandmarkpoints.part(16).x, poslandmarkpoints.part(16).y), (poslandmarkpoints.part(26).x, poslandmarkpoints.part(26).y), (0,255,0), drawlinethickness)

        
        #brows
        for p in range(17, 21):
            cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), (0,255,0), drawlinethickness)
        for p in range(22, 26):
            cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(21).x, poslandmarkpoints.part(21).y), (poslandmarkpoints.part(22).x, poslandmarkpoints.part(22).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(19).x, poslandmarkpoints.part(19).y), (poslandmarkpoints.part(24).x, poslandmarkpoints.part(24).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(18).x, poslandmarkpoints.part(18).y), (poslandmarkpoints.part(37).x, poslandmarkpoints.part(37).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(21).x, poslandmarkpoints.part(21).y), (poslandmarkpoints.part(38).x, poslandmarkpoints.part(38).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(21).x, poslandmarkpoints.part(21).y), (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(22).x, poslandmarkpoints.part(22).y), (poslandmarkpoints.part(43).x, poslandmarkpoints.part(43).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(25).x, poslandmarkpoints.part(25).y), (poslandmarkpoints.part(44).x, poslandmarkpoints.part(44).y), (0,255,0), drawlinethickness)
        cv2.line(frame, (poslandmarkpoints.part(22).x, poslandmarkpoints.part(22).y), (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), (0,255,0), drawlinethickness)
        

def begin_eyetracking (frame, poslandmarkpoints):
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
        cv2.rectangle(frame, (right_eye1x-40,right_eye1y-20), (right_eye2x+40,right_eye2y+20), (0,0,255), 1)
        cv2.rectangle(frame, (left_eye1x-40,left_eye1y-20), (left_eye2x+40,left_eye2y+20), (0,0,255), 1)


cap = cv2.VideoCapture(0)
show_poly = 1 #show poly face (yes|no) (1|0)
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
        cv2.rectangle(frame, (x-20,y-20), (x1+20,y1+20), (0,255,0), 1) # form a rectangle based on previous two coordinates
        cv2.line(frame, (x+10, y-20), (x+65, y-55), (0,255,0), 1)
        cv2.putText(frame, 'REGISTER USER', (x+70, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2) #show text
        
        poslandmarkpoints = predictor(gray, face)

        
        #display eye tracking
        begin_eyetracking(frame, poslandmarkpoints)
        
        #if show_poly = 1, then show polyface
        if show_poly == 1:
            show_polyface(frame, poslandmarkpoints)



    
    #if is_facetracking flag = 1, then draw a rectangle as default
    width  = cap.get(3) # video capture width
    height = cap.get(4) # video capture height
    offset = 100 #offset value to create rectangle in center of screen
    cv2.rectangle(frame, (offset+40,offset), (int(width)-offset-40,int(height)-offset), (0,255,0), 1) # form a rectangle based on previous two coordinates
    if not faces:
        cv2.putText(frame, 'Align Face in Center. Tracking...', (offset+40, offset-30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2) #show text
                    
    cv2.imshow("PrecisionFaceWithEyeTracking", frame)
    key = cv2.waitKey(1)
    if key == 27: #esc key is pressed
        break


cap.release()
cv2.destroyAllWindows()

