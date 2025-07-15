#HI I am Abhijeet I Hope You WIll Like This code.

from flask import Flask,render_template,jsonify
import math
import cv2
import mediapipe as mp
import threading
import time
from flask_cors import CORS


mppose=mp.solutions.pose

pose=mppose.Pose()

mpdraw=mp.solutions.drawing_utils


app=Flask(__name__)
CORS(app)
cap=cv2.VideoCapture(0)
right_arm_angle=0
right_shoulder_angle=0
left_shoulder_angle=0
left_arm_angle=0
def findangle(p1,p2,p3):
    x1,y1=p1
    x2,y2=p2
    x3,y3=p3
    return math.degrees(math.atan2((y2-y3),(x2-x3))-math.atan2((y2-y1),(x2-x1)))


def drawline(img,point1,point2,color=(0,0,255),thick=3):
    x1,y1=point1
    x2,y2=point2
    ih,iw,ic=img.shape

    cx1=int(iw*x1)
    cy1=int(ih*y1)
    
    cx2=int(iw*x2)
    cy2=int(ih*y2)
    
    cv2.line(img,(cx1,cy1),(cx2,cy2),color,thick)
def drawcircle(img,point,color=(255,0,0),thick=-1,rad=10):
    
    x,y=point
    
    ih,iw,ic=img.shape
    cx=int(iw*x)
    cy=int(ih*y)
    
    cv2.circle(img,(cx,cy),rad,color,thick)

def computer():
    global right_arm_angle
    global right_shoulder_angle
    global left_arm_angle,left_shoulder_angle
    while True:
        ok,frame=cap.read()


        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        result=pose.process(rgb)
        
        if (result.pose_landmarks):
            left_shoulder=result.pose_landmarks.landmark[11].x,result.pose_landmarks.landmark[11].y
            drawcircle(frame,left_shoulder)
            right_shoulder=result.pose_landmarks.landmark[12].x,result.pose_landmarks.landmark[12].y
            drawcircle(frame,right_shoulder)
            left_elbow=result.pose_landmarks.landmark[13].x,result.pose_landmarks.landmark[13].y
            drawcircle(frame,left_elbow)
            right_elbow=result.pose_landmarks.landmark[14].x,result.pose_landmarks.landmark[14].y
            drawcircle(frame,right_elbow)
            right_wrist=result.pose_landmarks.landmark[16].x,result.pose_landmarks.landmark[16].y
            left_wrist=result.pose_landmarks.landmark[15].x,result.pose_landmarks.landmark[15].y
            
            right_hip=result.pose_landmarks.landmark[24].x,result.pose_landmarks.landmark[24].y
            left_hip=result.pose_landmarks.landmark[23].x,result.pose_landmarks.landmark[23].y


            right_arm_angle=(findangle(right_shoulder,right_elbow,right_wrist))
            right_shoulder_angle=(findangle(right_hip,right_shoulder,right_elbow))
            
            left_arm_angle=(findangle(left_shoulder,left_elbow,left_wrist))
            left_shoulder_angle=(findangle(left_hip,left_shoulder,left_elbow))
            # mpdraw.draw_landmarks(frame,(result.pose_landmarks),mppose.POSE_CONNECTIONS)

            drawline(frame,left_shoulder,left_elbow)
            drawline(frame,left_elbow,left_wrist)
            drawline(frame,right_elbow,right_wrist)
            drawline(frame,right_shoulder,right_elbow)            
            cv2.rectangle(frame,(440,20),(612,50),(0,0,0),3)
            cv2.putText(frame,"FACE THIS SIDE",(447,42),cv2.FONT_HERSHEY_PLAIN,1.3,(0,0,255),2)


        cv2.imshow("frame",frame)
        if cv2.waitKey(1)==ord('q'):
            break

    cv2.destroyAllWindows()

@app.route("/")
def main():
    


        
    
   
    return jsonify({
        'right_arm':right_arm_angle-90,
        'right_shoulder':right_shoulder_angle,
        'left_arm':left_arm_angle-90,
        'left_shoulder':left_shoulder_angle
        })
if __name__=="__main__":
    
    t=threading.Thread(target=computer)
    
    t.start()
    
    
    app.run(debug=True)
    



