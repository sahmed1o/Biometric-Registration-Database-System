import cv2
import os
import numpy as np
from PIL import Image
import dlib
import tkinter as tk
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QTableWidget,QInputDialog, QPushButton, QHBoxLayout, QTextEdit, QFormLayout, QListWidget, QDialogButtonBox, QListWidgetItem, QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, QCalendarWidget, QDialog, QComboBox, QLineEdit, QMessageBox
import datetime
from functools import partial

#==================================== DIALOG REGISTER ==============================
class InputDialog_Register(QDialog):

    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Register User")

        self.first = QLineEdit(self)
        self.second = QLineEdit(self)
        self.third = QLineEdit(self)
        self.fourth = QLineEdit(self)
        #first qlabel to hold image 1
        self.imageLabel = QLabel(self)
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QtGui.QPixmap("bgLabel.png"))
        self.imageLabel.setObjectName("label")
        #first qlabel to hold image 2
        self.imageLabel2 = QLabel(self)
        self.imageLabel2.setText("")
        self.imageLabel2.setPixmap(QtGui.QPixmap("bgLabel.png"))
        self.imageLabel2.setObjectName("label2")
        #self.imageLabel.setText("Help\n instructions: \n")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("ID:", self.first)
        layout.addRow("Name:", self.second)
        layout.addRow("Age:", self.third)
        layout.addRow("Gender:", self.fourth)
        layout.addRow("", self.imageLabel)
        layout.addWidget(buttonBox)

        #hide second qlabel
        self.imageLabel2.hide()


        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def accept(self):
        #print ("accepted")
        eyeimage = self.imageLabel2.pixmap().toImage()
        #convert pixmap to numpy array
        width = eyeimage.width()
        height = eyeimage.height()
        channel = 4
        s = eyeimage.bits().asstring(width * height * channel)
        eyeArray = np.fromstring(s, dtype=np.uint8).reshape((height, width, channel))
        im = Image.fromarray(eyeArray).convert('RGBA')
        data = np.array(im) 
        red, green, blue, alpha = data.T 
        data = np.array([blue, green, red, alpha])
        data = data.transpose()
        sub = Image.fromarray(data)
        sub.save("database\\" + self.first.text() + "-" + self.second.text() + "-" + self.third.text() + "-" + self.fourth.text() +"-.png")
        #convert pixmap to numpy array
        #open prompt stating user is registered
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Registered")
        msg.setInformativeText("User #" + self.first.text() + " has been registered to the database.")
        msg.setWindowTitle("User Registration")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        #end
        self.done(0)
            
       
        
    def set_image(self, image_frame, image_frame2):
        self.imageLabel2.setPixmap(QtGui.QPixmap(image_frame2))
        self.imageLabel.setPixmap(QtGui.QPixmap(image_frame))
        



#==================================== DIALOG REGISTER ==============================


#==================================== DIALOG VERIFY ==============================
class InputDialog_Verify(QDialog):

    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("User Information")

        self.first = QLineEdit(self)
        self.second = QLineEdit(self)
        self.third = QLineEdit(self)
        self.fourth = QLineEdit(self)
        
        self.first.setDisabled(True)
        self.second.setDisabled(True)
        self.third.setDisabled(True)
        self.fourth.setDisabled(True)
        
        #first qlabel to hold image 1
        self.imageLabel = QLabel(self)
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QtGui.QPixmap("bgLabel.png"))
        self.imageLabel.setObjectName("label")
        #first qlabel to hold image 2
        self.imageLabel2 = QLabel(self)
        self.imageLabel2.setText("")
        self.imageLabel2.setPixmap(QtGui.QPixmap("bgLabel.png"))
        self.imageLabel2.setObjectName("label2")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, self);

        layout = QFormLayout(self)
        layout.addRow("ID:", self.first)
        layout.addRow("Name:", self.second)
        layout.addRow("Age:", self.third)
        layout.addRow("Gender:", self.fourth)
        layout.addRow("", self.imageLabel)
        layout.addWidget(buttonBox)

        #hide second qlabel
        self.imageLabel2.hide()

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def accept(self):
        #end
        self.done(0)
            
       
        
    def set_image(self, image_frame, image_frame2, idnum, namen, agen, gendern):
        self.imageLabel2.setPixmap(QtGui.QPixmap(image_frame2))
        self.imageLabel.setPixmap(QtGui.QPixmap(image_frame))
        self.first.setText(idnum)
        self.second.setText(namen)
        self.third.setText(agen)
        self.fourth.setText(gendern)
        
        



#==================================== DIALOG VERIFY ==============================

#==================================== GUI PopUp ====================================
class Ui_IrisWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 451, 331))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bgLabel.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Register"))

    
    

#==================================== GUI PopUp ====================================


#==================================== GUI FOR PROGRAM ====================================    
    
#class Ui_MainWindow(object):
class Ui_MainWindow(QWidget):
    
    is_register = 0 # A flag to determine if user has pressed the register user button
    is_verify = 0 # A flag to determine if user has pressed the register user button
    
    cap = None  # video capture variable, this has to be prone to changing in value when user presses button to allow the starting and stopping of video capturing
    root = None # TKinter library is used to grab screen size to position the iris popup window
    popup_window = None
    uiiris = None
    popup_register_window = None
    popup_verify_window = None
    uiregis = None
    uiverify = None
    image_frame = None
    image_frame2 = None
    verify_id = ""
    
    # Popup Window
    def popup_setup(self):
        global popup_window
        global uiiris
        self.popup_window = QtWidgets.QMainWindow()
        self.uiiris = Ui_IrisWindow()
        self.uiiris.setupUi(self.popup_window)
        self.popup_window.setWindowFlags(Qt.FramelessWindowHint)
        
    
    # Popup Register Window 
    def register_dialog_setup(self):
        global popup_register_window
        global uiregis
        self.popup_register_window = QtWidgets.QMainWindow()
        self.uiregis = InputDialog_Register()

    
    # Popup Register Window 
    def verify_dialog_setup(self):
        global popup_verify_window
        global uiverify
        self.popup_verify_window = QtWidgets.QMainWindow()
        self.uiverify = InputDialog_Verify()


        
    # PyQT5 GUI Generator
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7)
        self.RegisterUserButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegisterUserButton.sizePolicy().hasHeightForWidth())
        self.RegisterUserButton.setSizePolicy(sizePolicy)
        self.RegisterUserButton.setObjectName("RegisterUserButton")
        self.verticalLayout_4.addWidget(self.RegisterUserButton)
        self.VerifyUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.VerifyUserButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VerifyUserButton.sizePolicy().hasHeightForWidth())
        self.VerifyUserButton.setSizePolicy(sizePolicy)
        self.VerifyUserButton.setObjectName("VerifyUserButton")
        self.verticalLayout_4.addWidget(self.VerifyUserButton)
        self.ShowRegisteredUsers = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShowRegisteredUsers.sizePolicy().hasHeightForWidth())
        self.ShowRegisteredUsers.setSizePolicy(sizePolicy)
        self.ShowRegisteredUsers.setObjectName("ShowRegisteredUsers")
        self.verticalLayout_4.addWidget(self.ShowRegisteredUsers)
        self.CloseProgramButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseProgramButton.sizePolicy().hasHeightForWidth())
        self.CloseProgramButton.setSizePolicy(sizePolicy)
        self.CloseProgramButton.setObjectName("CloseProgramButton")
        self.verticalLayout_4.addWidget(self.CloseProgramButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.statusPrompt = QtWidgets.QPushButton(self.centralwidget)
        self.statusPrompt.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusPrompt.sizePolicy().hasHeightForWidth())
        self.statusPrompt.setSizePolicy(sizePolicy)
        self.statusPrompt.setCheckable(False)
        self.statusPrompt.setAutoDefault(False)
        self.statusPrompt.setDefault(False)
        self.statusPrompt.setFlat(False)
        self.statusPrompt.setObjectName("statusPrompt")
        self.gridLayout_3.addWidget(self.statusPrompt, 4, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("bgLabel.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("bgLabel.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 2, 2, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bgLabel.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 4, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose_2 = QtWidgets.QAction(MainWindow)
        self.actionClose_2.setObjectName("actionClose_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setShortcutVisibleInContextMenu(False)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRegister = QtWidgets.QAction(MainWindow)
        self.actionRegister.setObjectName("actionRegister")
        self.actionVerify = QtWidgets.QAction(MainWindow)
        self.actionVerify.setObjectName("actionVerify")
        self.actionShow_All = QtWidgets.QAction(MainWindow)
        self.actionShow_All.setObjectName("actionShow_All")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Iris Recognition Registration Database"))
        self.pushButton.setText(_translate("MainWindow", "Iris Registered Database"))
        self.pushButton_7.setText(_translate("MainWindow", "Registered ID: XXXXXXX"))
        self.RegisterUserButton.setText(_translate("MainWindow", "Register User"))
        self.VerifyUserButton.setText(_translate("MainWindow", "Verify User"))
        self.ShowRegisteredUsers.setText(_translate("MainWindow", "Show Registered Users"))
        self.CloseProgramButton.setText(_translate("MainWindow", "Close"))
        self.statusPrompt.setText(_translate("MainWindow", "Registered. OK."))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose_2.setText(_translate("MainWindow", "Close"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionRegister.setText(_translate("MainWindow", "Register"))
        self.actionVerify.setText(_translate("MainWindow", "Verify"))
        self.actionShow_All.setText(_translate("MainWindow", "Show All"))        




#==================================== GUI FOR PROGRAM ====================================
        
    def iris_match_res(self, image_1, image_2):
        
        
        # Feature Matching using ORB Detection
        orb = cv2.ORB_create()
        keypoints_img1, des1 = orb.detectAndCompute(image_1, None) # Determine all keypoints in image 1
        keypoints_img2, des2 = orb.detectAndCompute(image_2, None) # Determine all keypoints in image 2
        
        
        # Brute Force Matching
        # create BFMatcher object
        brute_f = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matchesOriginal = brute_f.match(des1, des1)  # Match image 1 with it self to find out how many keypoints there are for image matching
        matchesNew = brute_f.match(des1, des2)   # Match image 1 with image 2 to find out how many related keypoints there are between the two images
        
        # The match rate is determined by getting the total matches between image 1 and itself, and then dividing it by the number of matches for image 1 and 2.
        # The reason for this calculation is because image 1 matching with itself is essentially a 100% match rate, this gives us the number of keypoints for a 
        # a perfect match. We can then get the match rate by dividing the match ratio of image 1 and 2, by the ideal match rate by comparing how many keypoints
        # are found and dividing the total keypoints.
        if len(matchesOriginal) != 0:
            match_rate = (len(matchesNew)/len(matchesOriginal))*100
        else:
            match_rate = 0
            print("Image Quality is low definition, unable to verify. please use a stronger camera.")

        # Print Match Rate of Two Images
        #print("Match Rate: " + str(match_rate) + "%")

        # Draw all matches in new window
        #matching_result = cv2.drawMatches(image_1, keypoints_img1, image_2, keypoints_img2, matchesNew, None)

        
        # The match rate value is dependent on the camera, if camera is weaker, then a lower value such as 35% is used, if stronger then up the value to 50-70%+
        # If the match rate is greater then 35% we have a match on the Iris
        if match_rate > 35:
            print("IRIS MATCH FOUND IN DATABASE.")
            return True
        else:
            print("NO IRIS MATCH FOUND IN DATABASE.")
            return False
        
        
    # This function opens the dialog to verify the user asking the user to input the identification number to cross-reference their iris
    def register_dialog_open_verify(self):
        inp = QtWidgets.QInputDialog(self)
        inp.setInputMode(QtWidgets.QInputDialog.TextInput)
        inp.setFixedSize(600, 100)

        inp.setWindowTitle('Confirmation')
        inp.setLabelText('Enter Identification Number')

        if inp.exec_() == QtWidgets.QDialog.Accepted:
            #print(inp.textValue())
            global verify_id
            verify_id = inp.textValue()
            #begin iris matching, if no matches found then show message to state its not found else show popup window with user information
            ui.show_user_verification_info()
        else:
            print('cancel')

        inp.deleteLater()

    
    def show_user_verification_info(self):
        is_matched = False 

        #verify iris by pattern matching using ORB detection
        
        #grab user registered IRIS by ID
        iris_f_name = ""
        iris_id = ""
        iris_name = ""
        iris_age = ""
        iris_gender = ""
        #loop through folder until Registered IRIS is found
        for f_name in os.listdir('database'):
            image_name = f_name
            get_id_from_database = image_name.split("-")
            if verify_id.strip() == get_id_from_database[0].strip():
                iris_f_name = f_name
                iris_id = get_id_from_database[0].strip()
                iris_name = get_id_from_database[1].strip()
                iris_age = get_id_from_database[2].strip()
                iris_gender = get_id_from_database[3].strip()
                break

        #convert QImage to numpy array so it can be read by cv2
        incomingImage = self.image_frame2.convertToFormat(4)

        width = incomingImage.width()
        height = incomingImage.height()

        ptr = incomingImage.bits()
        ptr.setsize(incomingImage.byteCount())
        arr = np.array(ptr).reshape(height, width, 4)  #  Copies the data
        
        
        cv2.imwrite('database\\tempfile.png', arr)
        image_1 = cv2.imread('database\\tempfile.png')
        image_2 = cv2.imread('database\\' + iris_f_name) 
        os.remove('database\\tempfile.png') #remove temporary created image file

        # Match IRIS with registered User IRIS by ID to check for a match
        is_matched = ui.iris_match_res(image_1, image_2)

        #show popup window with results
        if is_matched == True:
            if self.image_frame2 is not None:
                #open prompt stating match is found
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Results:")
                msg.setInformativeText("IRIS MATCH FOUND IN DATABASE.")
                msg.setWindowTitle("User Confirmation")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
                #open window showing user information 
                self.uiverify.set_image('database\\' + iris_f_name, 'database\\' + iris_f_name, iris_id, iris_name, iris_age, iris_gender) 
                self.uiverify.exec()
        else:
            #open prompt stating no match is found
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Results:")
            msg.setInformativeText("NO IRIS MATCH FOUND IN DATABASE.")
            msg.setWindowTitle("User Confirmation")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        
    # This function opens the dialog to register the user asking the user to input their information 
    def register_dialog_open_register(self):
        if self.image_frame is not None:
            self.uiregis.set_image(self.image_frame, self.image_frame2)
        self.uiregis.exec()
        #exit(0)

        
    # This function closes the program on button press
    def CloseProgram(self):
        if self.root is not None:
            self.root.destroy()
            self.root = None
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()
        self.popup_window.close()
        QCoreApplication.quit()
            

    # This function registers the users iris by capturing the face and eyes from the user in the videocapture feed
    def RegisterEyes(self):
        if self.is_verify == 0:

            #assign popup text
            self.uiiris.pushButton.setText('Register')
            
            if self.is_register == 0:
                self.uiiris.pushButton.clicked.disconnect()
                self.uiiris.pushButton.clicked.connect(ui.register_dialog_open_register)
                self.is_register = 1
            elif self.is_register == 1:
                self.is_register = 0

            
            if self.is_register == 1:
                if self.root is None:
                    self.root = tk.Tk()

                
                self.RegisterUserButton.setStyleSheet('QPushButton {background-color: #A3C1DA}')
                self.RegisterUserButton.setText('STOP')

                #if using webcam
                self.cap = cv2.VideoCapture(0); #video capture id, 0 will be webcam id

                #if using RTSP IP Camera (for testing an android device camera was used)
                #This segment can be commented out or removed if using a webcamera connected to the device running this program, uncomment line before these two
                #os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
                #self.cap = cv2.VideoCapture("rtsp://YourAddress", cv2.CAP_FFMPEG)
                #This segment can be commented out or removed if using a webcamera connected to the device running this program, uncomment line before these two

                
                
                show_poly = 1 #show poly face (yes|no) (1|0)
                show_align_text = 1 #show align text (yes|no) (1|0)
                
                #refer to the 68-face-landmarks-labeled-by-dlib-software-automatically.png to understand why certain coordinates are used to find certain parts of the face
                detector = dlib.get_frontal_face_detector()  #front face classifier
                predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #assigned coordinates of the face by DLIB

                #id=raw_input('enter user id') #store eyes with id so we can identify whose eyes it is
                numid = 0;
                id = 1;

                ret,frame = self.cap.read(); #return status variable and the captured image
                
                

                #open popup
                self.popup_window.show()
                screen_width = self.root.winfo_screenwidth()
                screen_height = self.root.winfo_screenheight()
                self.popup_window.move(int(screen_width/2),int(screen_height/4))

                while(self.is_register == 1):
                                    
                    ret,frame = self.cap.read(); #return status variable and the captured image
        
                    #Show Recorded Image on Label on GUI for Tracking
                    height, width, channel = frame.shape
                    bytesPerLine = 3 * width
                    offset = 100 #offset value to create rectangle and text above the rectangle in the center of screen
                    #draw the bounding box for face tracking
                    cv2.rectangle(frame, (offset+40,offset), (int(width)-offset-40,int(height)-offset), (255,255,255), 1) # form a rectangle based on previous two coordinates

                    if show_align_text == 1:
                        cv2.putText(frame, 'Align Face in Center. Tracking...', (offset+40, offset-30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2) #show text

                    cv2.cvtColor(frame,cv2.COLOR_BGR2RGB, frame) #OpenCV order is BGR, while Qt is RGB, use this to invert colors back

                    #Get regular frame with no overlay, this is saved in database
                    tempframe = frame.copy()
                    overlay = frame.copy()
                    output = frame.copy()
                    height, width, channel = frame.shape
                    alpha = 0
                    cv2.rectangle(overlay, (0, 0), (width, height), (102,178,250), -1)
                    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
                    tempframe = output
                    
                    #Add blue overlay to captured footage with Iris      
                    overlay = frame.copy()
                    output = frame.copy()
                    height, width, channel = frame.shape
                    alpha = 0.5
                    cv2.rectangle(overlay, (0, 0), (width, height), (102,178,250), -1)
                    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
                    frame = output
                    
                    qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                    self.label.setPixmap(QtGui.QPixmap(qImg))
                    

                    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #grayscale image for detection filtering of eyes
                    faces = detector(gray) #detect all the faces in current frame and return cooorinate of each face

                    

                    #Capture the face first using the landmark points from the detector, if a face is found then search for the eyes on the face through filtering
                    for face in faces:
                        
                        x, y  = face.left(), face.top() # Top Left coordinates of face in window
                        x1, y1 = face.right(), face.bottom() # Bottom right coordinates of face in windows
                        cv2.rectangle(frame, (x-20,y-20), (x1+20,y1+20), (255,255,255), 1) # form a rectangle based on previous two coordinates
                        cv2.line(frame, (x+10, y-20), (x+65, y-55), (255,255,255), 1)
                        cv2.putText(frame, 'REGISTER USER', (x+70, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2) #show text
                        
                        poslandmarkpoints = predictor(gray, face)
             
                        #display iris tracking
                        #save iris frame for register window
                        global image_frame
                        global image_frame2
                        self.image_frame2 = begin_iristracking(tempframe, poslandmarkpoints, self.uiiris.label, False) #grab eye tracking without rect display
                        self.image_frame = begin_iristracking(frame, poslandmarkpoints, self.uiiris.label, True) #grab eye tracking with rect display
                        
                        #recapture frame to erase drawn geometrics
                        ret,frame = self.cap.read(); #return status variable and the captured image
                        #Show Recorded Image on Label on GUI for Tracking
                        height, width, channel = frame.shape
                        bytesPerLine = 3 * width
                        offset = 100 #offset value to create rectangle and text above the rectangle in the center of screen
                        #draw the bounding box for face tracking
                        cv2.rectangle(frame, (offset+40,offset), (int(width)-offset-40,int(height)-offset), (255,255,255), 1) # form a rectangle based on previous two coordinates
                        if show_align_text == 1:
                            cv2.putText(frame, 'Align Face in Center. Tracking...', (offset+40, offset-30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2) #show text
                        cv2.cvtColor(frame,cv2.COLOR_BGR2RGB, frame) #OpenCV order is BGR, while Qt is RGB, use this to invert colors back
                        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                        self.label.setPixmap(QtGui.QPixmap(qImg))
                        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #grayscale image for detection filtering of eyes
                        faces = detector(gray) #detect all the faces in current frame and return cooorinate of each face
                        x, y  = face.left(), face.top() # Top Left coordinates of face in window
                        x1, y1 = face.right(), face.bottom() # Bottom right coordinates of face in windows
                        cv2.rectangle(frame, (x-20,y-20), (x1+20,y1+20), (255,255,255), 1) # form a rectangle based on previous two coordinates
                        cv2.line(frame, (x+10, y-20), (x+65, y-55), (255,255,255), 1)
                        cv2.putText(frame, 'REGISTER USER', (x+70, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2) #show text                    
                        poslandmarkpoints = predictor(gray, face)

                        
                        #Add blue overlay to captured footage with eyes      
                        overlay = frame.copy()
                        output = frame.copy()
                        height, width, channel = frame.shape
                        alpha = 0.5
                        cv2.rectangle(overlay, (0, 0), (width, height), (102,178,250), -1)
                        cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
                        frame = output

                                            
                        #display eye tracking
                        begin_eyetracking(frame, poslandmarkpoints, self.label_2, self.label_3, self.root)


                        
                        #recapture frame to erase drawn geometrics
                        ret,frame = self.cap.read(); #return status variable and the captured image
                        #Show Recorded Image on Label on GUI for Tracking
                        height, width, channel = frame.shape
                        bytesPerLine = 3 * width
                        offset = 100 #offset value to create rectangle and text above the rectangle in the center of screen
                        #draw the bounding box for face tracking
                        cv2.rectangle(frame, (offset+40,offset), (int(width)-offset-40,int(height)-offset), (255,255,255), 1) # form a rectangle based on previous two coordinates
                        if show_align_text == 1:
                            cv2.putText(frame, 'Align Face in Center. Tracking...', (offset+40, offset-30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2) #show text
                        cv2.cvtColor(frame,cv2.COLOR_BGR2RGB, frame) #OpenCV order is BGR, while Qt is RGB, use this to invert colors back
                        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                        self.label.setPixmap(QtGui.QPixmap(qImg))
                        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #grayscale image for detection filtering of eyes
                        faces = detector(gray) #detect all the faces in current frame and return cooorinate of each face
                        x, y  = face.left(), face.top() # Top Left coordinates of face in window
                        x1, y1 = face.right(), face.bottom() # Bottom right coordinates of face in windows
                        cv2.rectangle(frame, (x-20,y-20), (x1+20,y1+20), (255,255,255), 1) # form a rectangle based on previous two coordinates
                        cv2.line(frame, (x+10, y-20), (x+65, y-55), (255,255,255), 1)
                        cv2.putText(frame, 'REGISTER USER', (x+70, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2) #show text                    
                        poslandmarkpoints = predictor(gray, face)

                        #Add blue overlay to captured footage with face      
                        overlay = frame.copy()
                        output = frame.copy()
                        height, width, channel = frame.shape
                        alpha = 0.5
                        cv2.rectangle(overlay, (0, 0), (width, height), (102,178,250), -1)
                        cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
                        frame = output
                        
                        #if show_poly = 1, then show polyface
                        if show_poly == 1:
                            show_polyface(frame, poslandmarkpoints)
                        
                        #Show Recorded Image on Label on GUI for Tracking
                        height, width, channel = frame.shape
                        bytesPerLine = 3 * width
                        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                        #grayscales = qImg.convertToFormat(QtGui.QImage.Format_Grayscale8)
                        self.label.setPixmap(QtGui.QPixmap(qImg))
                    #if faces array is empty then show the message, then no faces are being tracked, show message 'Align Face in Center. Tracking...'
                    if not faces:
                        show_align_text = 1
                    if faces:
                        show_align_text = 0
                        
                   
                    cv2.waitKey(1)

            else:
                if self.root is not None:
                    self.root.destroy()
                    self.root = None
                self.cap.release() 
                self.cap = None
                cv2.destroyAllWindows()
                if self.root is not None:
                    self.root.destroy()
                #close popup
                self.popup_window.close()
                self.RegisterUserButton.setStyleSheet('QPushButton {background-color: #E1E1E1}')
                self.RegisterUserButton.setText('Register User')


    
    # Verify user
    # This function verifies the users iris by capturing the face and eyes from the user in the videocapture feed
    def VerifyEyes(self):
        if self.is_register == 0:

            #assign popup text
            self.uiiris.pushButton.setText('Verify')

            
            if self.is_verify == 0:
                self.uiiris.pushButton.clicked.disconnect()
                self.uiiris.pushButton.clicked.connect(ui.register_dialog_open_verify)
                self.is_verify = 1
            elif self.is_verify == 1:
                self.is_verify = 0

            
            if self.is_verify == 1:
                if self.root is None:
                    self.root = tk.Tk()

                
                self.VerifyUserButton.setStyleSheet('QPushButton {background-color: #A3C1DA}')
                self.VerifyUserButton.setText('STOP')

                #if using webcam
                self.cap = cv2.VideoCapture(0); #video capture id, 0 will be webcam id

                #if using RTSP IP Camera (for testing an android device camera was used)
                #This segment can be commented out or removed if using a webcamera connected to the device running this program, uncomment line before these two
                #os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
                #self.cap = cv2.VideoCapture("rtsp://YourAddress", cv2.CAP_FFMPEG)
                #This segment can be commented out or removed if using a webcamera connected to the device running this program, uncomment line before these two

                
                
                show_poly = 1 #show poly face (yes|no) (1|0)
                show_align_text = 1 #show align text (yes|no) (1|0)
                
                #refer to the 68-face-landmarks-labeled-by-dlib-software-automatically.png to understand why certain coordinates are used to find certain parts of the face
                detector = dlib.get_frontal_face_detector()  #front face classifier
                predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #assigned coordinates of the face by DLIB

                numid = 0;
                id = 1;

                ret,frame = self.cap.read(); #return status variable and the captured image
                
                

                #open popup
                self.popup_window.show()
                screen_width = self.root.winfo_screenwidth()
                screen_height = self.root.winfo_screenheight()
                self.popup_window.move(int(screen_width/2),int(screen_height/4))

                while(self.is_verify == 1):
                                    
                    ret,frame = self.cap.read(); #return status variable and the captured image
        
                    #Show Recorded Image on Label on GUI for Tracking
                    height, width, channel = frame.shape
                    bytesPerLine = 3 * width
                    offset = 100 #offset value to create rectangle and text above the rectangle in the center of screen
                    #draw the bounding box for face tracking
                    cv2.rectangle(frame, (offset+40,offset), (int(width)-offset-40,int(height)-offset), (255,255,255), 1) # form a rectangle based on previous two coordinates

                    if show_align_text == 1:
                        cv2.putText(frame, 'Align Face in Center. Tracking...', (offset+40, offset-30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2) #show text

                    cv2.cvtColor(frame,cv2.COLOR_BGR2RGB, frame) #OpenCV order is BGR, while Qt is RGB, use this to invert colors back

                    #Get regular frame with no overlay, this is saved in database
                    tempframe = frame.copy()
                    overlay = frame.copy()
                    output = frame.copy()
                    height, width, channel = frame.shape
                    alpha = 0
                    cv2.rectangle(overlay, (0, 0), (width, height), (102,178,250), -1)
                    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
                    tempframe = output
                    
                    #Add blue overlay to captured footage with Iris      
                    overlay = frame.copy()
                    output = frame.copy()
                    height, width, channel = frame.shape
                    alpha = 0.5
                    cv2.rectangle(overlay, (0, 0), (width, height), (102,178,250), -1)
                    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
                    frame = output
                    
                    qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                    self.label.setPixmap(QtGui.QPixmap(qImg))
                    

                    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #grayscale image for detection filtering of eyes
                    faces = detector(gray) #detect all the faces in current frame and return cooorinate of each face

                    

                    #Capture the face first using the landmark points from the detector, if a face is found then search for the eyes on the face through filtering
                    for face in faces:
                        
                        x, y  = face.left(), face.top() # Top Left coordinates of face in window
                        x1, y1 = face.right(), face.bottom() # Bottom right coordinates of face in windows
                        cv2.rectangle(frame, (x-20,y-20), (x1+20,y1+20), (255,255,255), 1) # form a rectangle based on previous two coordinates
                        cv2.line(frame, (x+10, y-20), (x+65, y-55), (255,255,255), 1)
                        cv2.putText(frame, 'REGISTER USER', (x+70, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2) #show text
                        
                        poslandmarkpoints = predictor(gray, face)
             
                        #display iris tracking
                        #save iris frame for register window
                        global image_frame
                        global image_frame2
                        self.image_frame2 = begin_iristracking(tempframe, poslandmarkpoints, self.uiiris.label, False) #grab eye tracking without rect display
                        self.image_frame = begin_iristracking(frame, poslandmarkpoints, self.uiiris.label, True) #grab eye tracking with rect display
                        
                        #recapture frame to erase drawn geometrics
                        ret,frame = self.cap.read(); #return status variable and the captured image
                        #Show Recorded Image on Label on GUI for Tracking
                        height, width, channel = frame.shape
                        bytesPerLine = 3 * width
                        offset = 100 #offset value to create rectangle and text above the rectangle in the center of screen
                        #draw the bounding box for face tracking
                        cv2.rectangle(frame, (offset+40,offset), (int(width)-offset-40,int(height)-offset), (255,255,255), 1) # form a rectangle based on previous two coordinates
                        if show_align_text == 1:
                            cv2.putText(frame, 'Align Face in Center. Tracking...', (offset+40, offset-30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2) #show text
                        cv2.cvtColor(frame,cv2.COLOR_BGR2RGB, frame) #OpenCV order is BGR, while Qt is RGB, use this to invert colors back
                        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                        self.label.setPixmap(QtGui.QPixmap(qImg))
                        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #grayscale image for detection filtering of eyes
                        faces = detector(gray) #detect all the faces in current frame and return cooorinate of each face
                        x, y  = face.left(), face.top() # Top Left coordinates of face in window
                        x1, y1 = face.right(), face.bottom() # Bottom right coordinates of face in windows
                        cv2.rectangle(frame, (x-20,y-20), (x1+20,y1+20), (255,255,255), 1) # form a rectangle based on previous two coordinates
                        cv2.line(frame, (x+10, y-20), (x+65, y-55), (255,255,255), 1)
                        cv2.putText(frame, 'REGISTER USER', (x+70, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2) #show text                    
                        poslandmarkpoints = predictor(gray, face)

                        
                        #Add blue overlay to captured footage with eyes      
                        overlay = frame.copy()
                        output = frame.copy()
                        height, width, channel = frame.shape
                        alpha = 0.5
                        cv2.rectangle(overlay, (0, 0), (width, height), (102,178,250), -1)
                        cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
                        frame = output

                                            
                        #display eye tracking
                        begin_eyetracking(frame, poslandmarkpoints, self.label_2, self.label_3, self.root)


                        
                        #recapture frame to erase drawn geometrics
                        ret,frame = self.cap.read(); #return status variable and the captured image
                        #Show Recorded Image on Label on GUI for Tracking
                        height, width, channel = frame.shape
                        bytesPerLine = 3 * width
                        offset = 100 #offset value to create rectangle and text above the rectangle in the center of screen
                        #draw the bounding box for face tracking
                        cv2.rectangle(frame, (offset+40,offset), (int(width)-offset-40,int(height)-offset), (255,255,255), 1) # form a rectangle based on previous two coordinates
                        if show_align_text == 1:
                            cv2.putText(frame, 'Align Face in Center. Tracking...', (offset+40, offset-30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2) #show text
                        cv2.cvtColor(frame,cv2.COLOR_BGR2RGB, frame) #OpenCV order is BGR, while Qt is RGB, use this to invert colors back
                        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                        self.label.setPixmap(QtGui.QPixmap(qImg))
                        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #grayscale image for detection filtering of eyes
                        faces = detector(gray) #detect all the faces in current frame and return cooorinate of each face
                        x, y  = face.left(), face.top() # Top Left coordinates of face in window
                        x1, y1 = face.right(), face.bottom() # Bottom right coordinates of face in windows
                        cv2.rectangle(frame, (x-20,y-20), (x1+20,y1+20), (255,255,255), 1) # form a rectangle based on previous two coordinates
                        cv2.line(frame, (x+10, y-20), (x+65, y-55), (255,255,255), 1)
                        cv2.putText(frame, 'REGISTER USER', (x+70, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2) #show text                    
                        poslandmarkpoints = predictor(gray, face)

                        #Add blue overlay to captured footage with face      
                        overlay = frame.copy()
                        output = frame.copy()
                        height, width, channel = frame.shape
                        alpha = 0.5
                        cv2.rectangle(overlay, (0, 0), (width, height), (102,178,250), -1)
                        cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
                        frame = output
                        
                        #if show_poly = 1, then show polyface
                        if show_poly == 1:
                            show_polyface(frame, poslandmarkpoints)
                        
                        #Show Recorded Image on Label on GUI for Tracking
                        height, width, channel = frame.shape
                        bytesPerLine = 3 * width
                        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                        #grayscales = qImg.convertToFormat(QtGui.QImage.Format_Grayscale8)
                        self.label.setPixmap(QtGui.QPixmap(qImg))
                    #if faces array is empty then show the message, then no faces are being tracked, show message 'Align Face in Center. Tracking...'
                    if not faces:
                        show_align_text = 1
                    if faces:
                        show_align_text = 0
                        
                   
                    cv2.waitKey(1)

            else:
                if self.root is not None:
                    self.root.destroy()
                    self.root = None
                self.cap.release() 
                self.cap = None
                #cv2.destroyWindow('Right Eye')
                cv2.destroyAllWindows()
                if self.root is not None:
                    self.root.destroy()
                #close popup
                self.popup_window.close()
                self.VerifyUserButton.setStyleSheet('QPushButton {background-color: #E1E1E1}')
                self.VerifyUserButton.setText('Verify User')
    

        
    # Open Database table that shows all registered users, place a button at the end cells of the table to get more info on the registered user when clicked
    def ShowAllRegisteredUsers(self): 

        iris_f_name = ""
        iris_id = ""
        iris_name = ""
        iris_age = ""
        iris_gender = ""
        iris_date = ""
        
        #get total number of files in directory, and build table from that information
        path, dirs, files = next(os.walk('database'))
        num_users = len(files)  
        
        #create database table
        self.table = QTableWidget()
        self.table.setRowCount(num_users+30)
        self.table.setColumnCount(7)
        self.table.resize(1624, 800)
        self.table.setWindowTitle("REGISTERED USERS DATABASE")
        self.table.horizontalHeader().setStretchLastSection(True)
        col_headers = ['IDENTIF. #', 'NAME.', 'AGE.', 'GENDER.', 'DATE REGIST.', 'CURRENT REGIST.', 'INFO.']
        self.table.setHorizontalHeaderLabels(col_headers)
        self.table.show()


        #loop through folder until Registered IRIS is found
        row = 0
        for f_name in os.listdir('database'):
            image_name = f_name
            get_id_from_database = image_name.split("-")
            iris_f_name = f_name
            iris_id = get_id_from_database[0].strip()
            iris_name = get_id_from_database[1].strip()
            iris_age = get_id_from_database[2].strip()
            iris_gender = get_id_from_database[3].strip()

            #get date of creation for file to find out when user registered
            t = os.path.getmtime("database\\" + image_name)
            d = datetime.datetime.fromtimestamp(t)
            iris_date = d.strftime('%d-%m-%Y %H:%M:%S')

            #if .png text is returned then we are at end of string, set string to empty
            if iris_id == ".png":
                iris_id = ""
            if iris_name == ".png":
                iris_name = ""
            if iris_age == ".png":
                iris_age = ""
            if iris_gender == ".png":
                iris_gender = ""
            if iris_date == ".png":
                iris_date = ""
            
            #print(iris_id + " | " + iris_name +  " | " + iris_age +  " | " + iris_gender +  " | " + iris_date)
            item = QtWidgets.QTableWidgetItem()
            item.setText(iris_id)
            self.table.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(iris_name)
            self.table.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(iris_age)
            self.table.setItem(row, 2, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(iris_gender)
            self.table.setItem(row, 3, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(iris_date)
            self.table.setItem(row, 4, item)
            item = QtWidgets.QTableWidgetItem()
            d = datetime.datetime.today()
            item.setText(d.strftime('%d-%m-%Y %H:%M:%S'))
            self.table.setItem(row, 5, item)
            infobutton = QPushButton("INFO")
            infobutton.clicked.connect(partial(self.open_info_dialog,iris_id))
            self.table.setCellWidget(row, 6, infobutton)
            row = row+1
            
        
    def open_info_dialog(self, selected_ID):
        temp_id = selected_ID
        #grab user registered IRIS by ID
        iris_f_name = ""
        iris_id = ""
        iris_name = ""
        iris_age = ""
        iris_gender = ""
        #loop through folder until Registered IRIS is found
        for f_name in os.listdir('database'):
            image_name = f_name
            get_id_from_database = image_name.split("-")
            if temp_id == get_id_from_database[0].strip():
                iris_f_name = f_name
                iris_id = get_id_from_database[0].strip()
                iris_name = get_id_from_database[1].strip()
                iris_age = get_id_from_database[2].strip()
                iris_gender = get_id_from_database[3].strip()
                break

        #open window showing user information 
        self.uiverify.set_image('database\\' + iris_f_name, 'database\\' + iris_f_name, iris_id, iris_name, iris_age, iris_gender) 
        self.uiverify.exec()
    
    
#======================== TRACKING IRIS SEGMENT ================================================================


        

def show_polyface (frame, poslandmarkpoints):

    #Precision Tracking Of face with full poly fill
    drawlinethickness = 1

    facetracking_color = (255,255,255)

    
    # right eye coordinate tracking
    right_eye1x = poslandmarkpoints.part(38).x
    right_eye1y = poslandmarkpoints.part(38).y
    right_eye2x = poslandmarkpoints.part(41).x
    right_eye2y = poslandmarkpoints.part(41).y
    
    # left eye coordinate tracking
    left_eye1x = poslandmarkpoints.part(44).x
    left_eye1y = poslandmarkpoints.part(44).y
    left_eye2x = poslandmarkpoints.part(47).x
    left_eye2y = poslandmarkpoints.part(47).y

    #chin
    for p in range(0, 16):
        cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), facetracking_color, drawlinethickness)
    
    #Manual Connections for Chin
    cv2.line(frame, (poslandmarkpoints.part(0).x, poslandmarkpoints.part(0).y), (poslandmarkpoints.part(17).x, poslandmarkpoints.part(17).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(0).x, poslandmarkpoints.part(0).y), (poslandmarkpoints.part(36).x, poslandmarkpoints.part(36).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(0).x, poslandmarkpoints.part(0).y), (poslandmarkpoints.part(31).x, poslandmarkpoints.part(31).y), facetracking_color, drawlinethickness)
    

    #left eye
    for p in range(36, 41):
        cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(41).x, poslandmarkpoints.part(41).y), (poslandmarkpoints.part(36).x, poslandmarkpoints.part(36).y), facetracking_color, drawlinethickness) #close off line for left eye
    cv2.line(frame, (poslandmarkpoints.part(39).x, poslandmarkpoints.part(39).y), (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(39).x, poslandmarkpoints.part(39).y), (poslandmarkpoints.part(31).x, poslandmarkpoints.part(31).y), facetracking_color, drawlinethickness) 

    #draw rectangle for left eye
    cv2.rectangle(frame, (left_eye1x-40,left_eye1y-20), (left_eye2x+40,left_eye2y+20), (255,0,0), 2)
    
    #right eye
    for p in range(42, 47):
        cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(47).x, poslandmarkpoints.part(47).y), (poslandmarkpoints.part(42).x, poslandmarkpoints.part(42).y), facetracking_color, drawlinethickness) #close off line for right eye
    cv2.line(frame, (poslandmarkpoints.part(42).x, poslandmarkpoints.part(42).y), (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), facetracking_color, drawlinethickness) #close off line for left eye
    cv2.line(frame, (poslandmarkpoints.part(42).x, poslandmarkpoints.part(42).y), (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), facetracking_color, drawlinethickness) 

    #draw rectangle for right eye
    cv2.rectangle(frame, (right_eye1x-40,right_eye1y-20), (right_eye2x+40,right_eye2y+20), (255,0,0), 2)
    
    #nose 
    for p in range(27, 35):
        cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), (poslandmarkpoints.part(30).x, poslandmarkpoints.part(30).y), facetracking_color, drawlinethickness) #close off line for nose
    cv2.line(frame, (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), (poslandmarkpoints.part(31).x, poslandmarkpoints.part(31).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(30).x, poslandmarkpoints.part(30).y), (poslandmarkpoints.part(32).x, poslandmarkpoints.part(32).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(30).x, poslandmarkpoints.part(30).y), (poslandmarkpoints.part(33).x, poslandmarkpoints.part(33).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(30).x, poslandmarkpoints.part(30).y), (poslandmarkpoints.part(34).x, poslandmarkpoints.part(34).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(33).x, poslandmarkpoints.part(33).y), (poslandmarkpoints.part(51).x, poslandmarkpoints.part(51).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), (poslandmarkpoints.part(54).x, poslandmarkpoints.part(54).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(31).x, poslandmarkpoints.part(31).y), (poslandmarkpoints.part(48).x, poslandmarkpoints.part(48).y), facetracking_color, drawlinethickness) 
    
   
    #mouth
    for p in range(48, 59):
        cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(59).x, poslandmarkpoints.part(59).y), (poslandmarkpoints.part(48).x, poslandmarkpoints.part(48).y), facetracking_color, drawlinethickness) #close off line for right eye
    for p in range(60, 67):
        cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(60).x, poslandmarkpoints.part(60).y), (poslandmarkpoints.part(67).x, poslandmarkpoints.part(67).y), facetracking_color, drawlinethickness) #close off line for right eye

    cv2.line(frame, (poslandmarkpoints.part(58).x, poslandmarkpoints.part(58).y), (poslandmarkpoints.part(7).x, poslandmarkpoints.part(7).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(56).x, poslandmarkpoints.part(56).y), (poslandmarkpoints.part(9).x, poslandmarkpoints.part(9).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(48).x, poslandmarkpoints.part(48).y), (poslandmarkpoints.part(3).x, poslandmarkpoints.part(3).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(48).x, poslandmarkpoints.part(48).y), (poslandmarkpoints.part(6).x, poslandmarkpoints.part(6).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(2).x, poslandmarkpoints.part(2).y), (poslandmarkpoints.part(31).x, poslandmarkpoints.part(31).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(54).x, poslandmarkpoints.part(54).y), (poslandmarkpoints.part(13).x, poslandmarkpoints.part(13).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(54).x, poslandmarkpoints.part(54).y), (poslandmarkpoints.part(10).x, poslandmarkpoints.part(10).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), (poslandmarkpoints.part(14).x, poslandmarkpoints.part(14).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(35).x, poslandmarkpoints.part(35).y), (poslandmarkpoints.part(16).x, poslandmarkpoints.part(16).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(16).x, poslandmarkpoints.part(16).y), (poslandmarkpoints.part(45).x, poslandmarkpoints.part(45).y), facetracking_color, drawlinethickness) 
    cv2.line(frame, (poslandmarkpoints.part(16).x, poslandmarkpoints.part(16).y), (poslandmarkpoints.part(26).x, poslandmarkpoints.part(26).y), facetracking_color, drawlinethickness)

    
    #brows
    for p in range(17, 21):
        cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), facetracking_color, drawlinethickness)
    for p in range(22, 26):
        cv2.line(frame, (poslandmarkpoints.part(p).x, poslandmarkpoints.part(p).y), (poslandmarkpoints.part(p+1).x, poslandmarkpoints.part(p+1).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(21).x, poslandmarkpoints.part(21).y), (poslandmarkpoints.part(22).x, poslandmarkpoints.part(22).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(19).x, poslandmarkpoints.part(19).y), (poslandmarkpoints.part(24).x, poslandmarkpoints.part(24).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(18).x, poslandmarkpoints.part(18).y), (poslandmarkpoints.part(37).x, poslandmarkpoints.part(37).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(21).x, poslandmarkpoints.part(21).y), (poslandmarkpoints.part(38).x, poslandmarkpoints.part(38).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(21).x, poslandmarkpoints.part(21).y), (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(22).x, poslandmarkpoints.part(22).y), (poslandmarkpoints.part(43).x, poslandmarkpoints.part(43).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(25).x, poslandmarkpoints.part(25).y), (poslandmarkpoints.part(44).x, poslandmarkpoints.part(44).y), facetracking_color, drawlinethickness)
    cv2.line(frame, (poslandmarkpoints.part(22).x, poslandmarkpoints.part(22).y), (poslandmarkpoints.part(27).x, poslandmarkpoints.part(27).y), facetracking_color, drawlinethickness)
    



def begin_eyetracking (frame, poslandmarkpoints, label_2, label_3, root):
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
    
    left_eye1x = poslandmarkpoints.part(44).x
    left_eye1y = poslandmarkpoints.part(44).y
    left_eye2x = poslandmarkpoints.part(47).x
    left_eye2y = poslandmarkpoints.part(47).y
    

  
    
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
    
            
    right_eye1x = poslandmarkpoints.part(38).x
    right_eye1y = poslandmarkpoints.part(38).y
    right_eye2x = poslandmarkpoints.part(41).x
    right_eye2y = poslandmarkpoints.part(41).y

   

    # ================================ tracking left eye on new window ================================
        
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
    
    #draw rectangle after eye frame is on window to prevent drawn polys from showing in eye window 
    cv2.rectangle(frame, (left_eye1x-40,left_eye1y-20), (left_eye2x+40,left_eye2y+20), (255,0,0), 1)
    
    #Show Recorded Image on Label on GUI for Tracking
    height, width, channel = left_eye.shape
    bytesPerLine = 3 * width
    qImg = QtGui.QImage(left_eye.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
    label_2.setPixmap(QtGui.QPixmap(qImg))

    # ================================ tracking left eye on new window ================================

    
    # ================================ tracking right eye on new window ================================

    #draw rectangle on iris in popup box
    #cv2.rectangle(frame, (right_eye1x-35,right_eye1y-14), (right_eye2x+35,right_eye2y+8), (255,0,0), 1)
    
    #Right Eye Tracking
    rightEyeTrack = np.array([(right_eye1x-40,right_eye1y-20),
                             (right_eye1x-40,right_eye2y+20),
                             (right_eye2x+40,right_eye2y-20),
                             (right_eye2x+40,right_eye2y+20)
                             ],
                            np.int32)

     
    remin_x = np.min(rightEyeTrack[:, 0])
    remax_x = np.max(rightEyeTrack[:, 0])
    remin_y = np.min(rightEyeTrack[:, 1])
    remax_y = np.max(rightEyeTrack[:, 1])
    

    cv2.putText(frame, 'RIGHT EYE', (right_eye2x-15 , right_eye2y+17), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255,255,255), 1) #show text
    right_eye = frame[remin_y : remax_y, remin_x : remax_x]
    right_eye = cv2.resize(right_eye, None, fx = 5, fy = 5) #fx and fy is the scale factor for frame

    
    #draw rectangle after eye frame is on window to prevent drawn polys from showing in eye window        
    cv2.rectangle(frame, (right_eye1x-40,right_eye1y-20), (right_eye2x+40,right_eye2y+20), (255,0,0), 1)
    
    #Show Recorded Image on Label on GUI for Tracking
    height, width, channel = right_eye.shape
    bytesPerLine = 3 * width
    qImg = QtGui.QImage(right_eye.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
    label_3.setPixmap(QtGui.QPixmap(qImg))
    


    # ================================ tracking right eye on new window ================================
    

def begin_iristracking (frame, poslandmarkpoints, popup, show_trackobj):
  
    
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
    
    
    right_eye1x = poslandmarkpoints.part(38).x
    right_eye1y = poslandmarkpoints.part(38).y
    right_eye2x = poslandmarkpoints.part(41).x
    right_eye2y = poslandmarkpoints.part(41).y

    # ================================ tracking iris on new window ================================

    #draw rectangle on iris in popup box
    if show_trackobj == True:
        cv2.rectangle(frame, (right_eye1x-35,right_eye1y-14), (right_eye2x+35,right_eye2y+8), (255,0,0), 1)
        cv2.putText(frame, 'IRIS', (right_eye2x+25 , right_eye2y+17), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255,255,255), 1) #show text


    #POPUP WINDOW for Right Eye
    rightEyeTrack2 = np.array([(right_eye1x-50,right_eye1y-20),
                             (right_eye1x-50,right_eye2y+20),
                             (right_eye2x+50,right_eye2y-20),
                             (right_eye2x+50,right_eye2y+20)
                             ],
                            np.int32)

     
    remin_x2 = np.min(rightEyeTrack2[:, 0])
    remax_x2 = np.max(rightEyeTrack2[:, 0])
    remin_y2 = np.min(rightEyeTrack2[:, 1])
    remax_y2 = np.max(rightEyeTrack2[:, 1])

    right_eye2 = frame[remin_y2 : remax_y2, remin_x2 : remax_x2]
    right_eye2 = cv2.resize(right_eye2, None, fx = 5, fy = 5) #fx and fy is the scale factor for frame


    
    #Show Recorded Image on popup label
    height2, width2, channel2 = right_eye2.shape
    bytesPerLine2 = 3 * width2
    qImg2 = QtGui.QImage(right_eye2.data, width2, height2, bytesPerLine2, QtGui.QImage.Format_RGB888)
    popup.setPixmap(QtGui.QPixmap(qImg2))

    return qImg2



    # ================================ tracking iris on new window ================================  


#======================== TRACKING IRIS SEGMENT ================================================================
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    #setup UI Popup Windows
    ui.popup_setup() #setup popup window
    ui.register_dialog_setup() #setup user inputer register window
    ui.verify_dialog_setup() #setup user inputer register window

    #setup button functions for ui
    ui.RegisterUserButton.clicked.connect(ui.RegisterEyes)
    ui.VerifyUserButton.clicked.connect(ui.VerifyEyes)
    ui.CloseProgramButton.clicked.connect(ui.CloseProgram)
    ui.ShowRegisteredUsers.clicked.connect(ui.ShowAllRegisteredUsers)
    ui.uiiris.pushButton.clicked.connect(ui.register_dialog_open_register)
    
    #MainWindow.show()
    MainWindow.showMaximized()
    sys.exit(app.exec_())

    

