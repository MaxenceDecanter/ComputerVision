import cv2
import skimage
from skimage.measure import compare_ssim
import datetime
import time

def save_webcam(outPath, fps, mirror=False):
    cap = cv2.VideoCapture(0)

    currentFrame = 0

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(outPath, fourcc, fps, (int(width), int(height)))

    frame = None
    old_frame = frame

    while (cap.isOpened()):

        if frame is not None:
            old_frame = frame
        ret, frame = cap.read()

        if ret == True:

            cv2.imshow('frame', frame)
            if old_frame is not None:
                score = compare_ssim(old_frame, frame, multichannel=True)
                if score < 0.85:
                    print("Mouvement détecté le %s" % datetime.datetime.now())
        else:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        currentFrame += 1
        time.sleep(0.05)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def main():
    save_webcam('output.avi', 30.0, mirror=True)

if __name__ == '__main__':
    main()