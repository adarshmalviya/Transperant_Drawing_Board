# Drawing Board By Adarsh Malviya
import cv2
import numpy

def getmask(imgblur):
    #for red
    lower_red = numpy.array([162, 91, 84])
    higher_red = numpy.array([179, 255, 255])

    mask = cv2.inRange(imgblur, lower_red, higher_red)

    return mask

if __name__ == "__main__":
    frame = cv2.VideoCapture(0)
   
    pen = []
    while True:
        _, rframe = frame.read()
        cv2.imshow("Original ", rframe)
        imgHSV = cv2.cvtColor(rframe, cv2.COLOR_BGR2HSV)

        mask = getmask(imgHSV)

        contors, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
        max_area = 0
        for contour in contors:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                largest = contour
        #drawing contours
        if max_area != 0:
            pen.append(largest)
            for cordi in pen:
                cv2.drawContours(rframe, cordi, 1, (0,0,255), 20)

        cv2.imshow("Drawing", rframe)

        # Quit with 'Esc' key
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
