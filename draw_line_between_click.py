# importing the module
from msilib import PID_TITLE
import cv2

right_clicks = []
# acuan = right_clicks[:2]
# ikan = right_clicks[3:]

# function to display the coordinates of
# of the points clicked on the image
def click_event (event, x, y, flags, params):

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:

        right_clicks.append([x,y])

        acuan = right_clicks[:2]
        ikan = right_clicks[2:]

        #marking the points with circle
        cv2.circle(img,(x,y),4,(36,255,12),-1)

        #check if click more than 2
        if len(acuan)>= 2:
            cv2.line(img,acuan[-1], acuan[-2],(0, 255, 255), 3)

        if len(ikan)>= 2:
            cv2.line(img,ikan[-1], ikan[-2],(0, 0, 255), 3)

        # while ikan > 2:
        #     cv2.line(img,acuan[-1], acuan[-2],(0, 0, 255), 3)


        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        print(right_clicks)
        print('acuan', acuan)
        print('ikan',ikan)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)

    # checking for right mouse clicks	
    if event==cv2.EVENT_RBUTTONDOWN:

        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)

# driver function
if __name__=="__main__":

    # reading the image
    img = cv2.imread('out8.jpg', 1)

    # resize the picture

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
