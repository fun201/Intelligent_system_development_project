"""
Example to introduce how to read a video file
"""

# Import the required packages
import cv2
import argparse

# We first create the ArgumentParser object
# The created object 'parser' will have the necessary information
# to parse the command-line arguments into data types.
#parser = argparse.ArgumentParser()

# We add 'video_path' argument using add_argument() including a help.
#parser.add_argument("video_path", help="path to the video file")
#args = parser.parse_args()

# Create a VideoCapture object. In this case, the argument is the video file name:
#capture = cv2.VideoCapture(args.video_path)

capture = cv2.VideoCapture("Mac_compatible_collision_seq.mp4")

# Check if the video is opened successfully
if capture.isOpened()is False:
    print("Error opening the video file!")
 
# Read until video is completed, or 'q' is pressed
while capture.isOpened():
    # Capture frame-by-frame from the video file
    ret, frame = capture.read()

    if ret is True:
        # Display the resulting frame
        cv2.imshow('Original frame from the video file', frame)

        # Convert the frame from the video file to grayscale:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the grayscale frame
        cv2.imshow('Grayscale frame', gray_frame)
        
 
 
        key=cv2.waitKey(20)
        
        if key & 0xFF == ord('P'):
            #P to pause and play video
            pass
        elif key & 0xFF == ord('C'):
            #C for canny edge detection to change the input video frames with canny edges as
# output.
            pass
        elif key & 0xFF == ord('b'):
            #  B to only show blue channel from BGR colour input. OutputB = inputBGR
            b = frame.copy()
            b[:,:,1] = 0  #green
            b[:,:,2] = 0  #red
        
            cv2.imshow("Blue frame",b)  
# =============================================================================
#             image = cv2.imread('wellington.jpg')
#             cv2.imshow('Original',image)
#             b = image.copy()
#             b[:,:,1] = 0  #green
#             b[:,:,2] = 0  #red
#             cv2.imshow('blue channel',b)
#             cv2.waitKey(0)
# =============================================================================
        elif key & 0xFF == ord('g'):
            #  G to only show green channel from BGR colour input. OutputG = inputBGR
            g = frame.copy()
            g[:,:,0] = 0  #blue
            g[:,:,2] = 0  #red
            cv2.imshow("Green frame",g)  
        elif key & 0xFF == ord('r'):
            #  R to only show red channel from BGR colour input. OutputR = inputBGR
            r = frame.copy()
            r[:,:,0] = 0  #blue
            r[:,:,1] = 0  #Green
            cv2.imshow("Red frame",r)  
        elif key & 0xFF == ord('D'):
            #  D to switch video to default BGR mode. OutputBGR = inputBGR
            pass
        elif key & 0xFF == ord('S'):
            #  S to start recording output video until S key is pressed again. The video is recorded
            pass
        elif key & 0xFF == ord('q'):
            break
                # Press q on keyboard to exit the program
  
    # Break the loop
    else:
        break
 
# Release everything
capture.release()
cv2.destroyAllWindows()


# =============================================================================
# import cv2
# # 1. create an object. zero for external camera 
# video = cv2.VideoCapture(0)
# #9.save video
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
# 
# #8. a is variable 
# a=0
# 
# while  True:
#         a=a + 1
# 
#        #3. create a frame object
#         check, frame = video.read()
# 
#         print(check)
#         print(frame)
#        #6. Converting to grayscale
#         gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 
#         #10.
#         out.write(frame)
# 
#       #4. Show the frame 
#         cv2.imshow('frame', frame)
#         #11
#         cv2.imshow("Capturing", gray)
# 
#       #5. For press any key to out(miliseconds)
#       #cv2.waitKey(0)
# 
#       #7. for playing 
# # =============================================================================
# #         frame_index =0
# #         gray_frame = "some frame"
# # =============================================================================
#         key=cv2.waitKey(20)
#         
#         if key & 0xFF == ord('P'):
#             #P to pause and play video
#             pass
#         elif key & 0xFF == ord('C'):
#             #C for canny edge detection to change the input video frames with canny edges as
# # output.
#             pass
#         elif key & 0xFF == ord('B'):
#             #  B to only show blue channel from BGR colour input. OutputB = inputBGR
#             pass
#         elif key & 0xFF == ord('G'):
#             #  G to only show green channel from BGR colour input. OutputG = inputBGR
#             pass
#         elif key & 0xFF == ord('R'):
#             #  R to only show red channel from BGR colour input. OutputR = inputBGR
#             pass
#         elif key & 0xFF == ord('D'):
#             #  D to switch video to default BGR mode. OutputBGR = inputBGR
#             pass
#         elif key & 0xFF == ord('S'):
#             #  S to start recording output video until S key is pressed again. The video is recorded
#             pass
#         elif key & 0xFF == ord('q'):
#             break
# # =============================================================================
# #         if key & 0xFF == ord('c'):
# #             frame_name = "camera_frame_{}.png".format(frame_index)
# #             gray_frame_name = "grayscale_camera_frame_{}.png".format()
# #             cv2.imwrite(frame_name,frame)
# #             cv2.imwrite(gray_frame_name,gray_frame)
# #             frame_index+=1 
# #         elif key & 0xFF == ord('q'):
# #             break
# # =============================================================================
# 
# 
# 
# 
# 
# print(a)
# 
# # 2. shutdown the camera 
# video.release()
# out.release()
# cv2.destroyAllWindows()
# =============================================================================

# =============================================================================
# 1), Using Python and OpenCV library write python scripts (.py) to read video input from a
# webcam (or a pre-recorded video in a loop back). You are given this option because not
# everyone has a webcam handy. You don’t have to attempt both input types. Only one.
# 2), As soon as the script starts, it starts reading the video. If reading a video file, use an avi
# video format and you are allowed to hardcode the file name into your script.

# The script should perform the following actions based on user’s key inputs:
#     P to pause and play video. OutputBGR = inputBGR. Note the resuming from pause
# mode, would show the current webcam frame. Or with an input video the


# subsequent video frame after being paused.
#  C for canny edge detection to change the input video frames with canny edges as
# output. OutputBW = Canny (inputBGR), where OutputBW is a black and white video,
# with white indicating the edges and black pixels for the rest.
#  B to only show blue channel from BGR colour input. OutputB = inputBGR
#  G to only show green channel from BGR colour input. OutputG = inputBGR
#  R to only show red channel from BGR colour input. OutputR = inputBGR
#  D to switch video to default BGR mode. OutputBGR = inputBGR
#  S to start recording output video until S key is pressed again. The video is recorded
# numerically (#) as #.avi. The recorded video could be for canny edges, blue channel,
# green channel, red channel, or BGR channels depending on which choice was chosen
# by user previously
# =============================================================================
