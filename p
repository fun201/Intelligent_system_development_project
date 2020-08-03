import cv2
# 1. create an object. zero for external camera 
video = cv2.VideoCapture(0)
#9.save video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

#8. a is variable 
a=0

while  True:
        a=a + 1
    
       #3. create a frame object
        check, frame = video.read()
    
        print(check)
        print(frame)
       #6. Converting to grayscale
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #10.
        out.write(frame)
    
      #4. Show the frame 
        cv2.imshow('frame', frame)
        #11
        cv2.imshow("Capturing", gray)
    
      #5. For press any key to out(miliseconds)
      #cv2.waitKey(0)
    
      #7. for playing 
        frame_index =0
        gray_frame = "some frame"
        key=cv2.waitKey(20)
        if key & 0xFF == ord('c'):
            frame_name = "camera_frame_{}.png".format(frame_index)
            gray_frame_name = "grayscale_camera_frame_{}.png".format()
            cv2.imwrite(frame_name,frame)
            cv2.imwrite(gray_frame_name,gray_frame)
            frame_index+=1 
        elif key & 0xFF == ord('q'):
            break
        
            
    
     
          
print(a)

# 2. shutdown the camera 
video.release()
out.release()
cv2.destroyAllWindows()
