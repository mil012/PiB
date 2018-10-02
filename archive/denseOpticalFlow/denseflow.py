import cv2
import numpy as np

POINT_DIST = 8                                                                                          # determine separation between ticks (smaller => more cpu processing power needed!)
flagMarker = False
DEFAULT_VIDEO = 'vtest.avi'

def is_opencv_2():
    ver = cv2.__version__
    num = int(ver.split('.')[0])
    return num == 2


# Try using webcam
cap = cv2.VideoCapture(0)                                                                              # init camera (if 0 as argument) /video (if filename as argument)

# If webcam fails, use video file.
if(not cap.isOpened()):
    print("Webcam not found. Using video file {}.".format(DEFAULT_VIDEO))
    cap = cv2.VideoCapture(DEFAULT_VIDEO)
else:
    print("Webcam detected. Using webcam.")                                                             
                                                                                                        # start on color representation form
ret, frame1 = cap.read()                                                                                # init frame
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)                                                          # convert into bgr colorspace
hsv = np.zeros_like(frame1)                                                                             # temp for farneback flow response
hsv[...,1] = 255                                                                                        # saturation always 255 (always show full color)

print("Processing video... (Press Ctrl+C to exit.)")

try:
    while(True):
        ret, frame2 = cap.read()                                                                            # capture next frame
        next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)                                                      # convert next frame into bgr colorspace
        # Handle OpenCV 2
        if(is_opencv_2()):
            flow = -1 * cv2.calcOpticalFlowFarneback(prvs,next, 0.5, 3, 15, 3, 5, 1.2, 0)
        # Handle OpenCV 3
        else:
            flow = -1 * cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)                 # calculate flow between all points
        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])                                                # convert flow values into polar values (for color repr) 
        hsv[...,0] = ang*180/np.pi/2                                                                        # hue represented in radians in OpenCV
        hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)                                          # normalize vibrance (our polar magnitude) between 0-255
        bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)                                                           # convert flow into bgr colorspace for showing
        cv2.imshow('HSV Representation',bgr)                                                                # generate next frame of window
        if flagMarker:
            h, w = next.shape[:2]                                                                           # used for tick viewing
            y, x = np.mgrid[POINT_DIST/2:h:POINT_DIST, POINT_DIST/2:w:POINT_DIST].reshape(2,-1).astype(int) # create temporary grid for ticks
            fx, fy = flow[y,x].T                                                                            # acquire desired ticks from grid
            lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)                                       # stack ticks on top of original image
            lines = np.int32(lines + 0.5)                                                                   # min line size (adds stabilization for smaller values)
            vis = cv2.cvtColor(next, cv2.COLOR_GRAY2BGR)                                                    # convert our image + ticks into something plottable
            cv2.polylines(vis, lines, 0, (0, 255, 0))                                                       # create the lines
            cv2.imshow('Tick Representation',vis)                                                           # generate next frame of window
        k = cv2.waitKey(30) & 0xff
        if k == 27:                                                                                         # Exit if escape is pressed
            break
        if k == ord('t'):                                                                                   # Show direction of gradient if desired
            flagMarker = not flagMarker
            cv2.destroyWindow('Tick Representation')                                                        # Destroys tick window if it exists
        prvs = next                                                                                         # Update previous image
except(KeyboardInterrupt):
    print("Exiting...")
finally:
    cap.release()
    cv2.destroyAllWindows()