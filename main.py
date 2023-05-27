import cv2

def split_video_to_frames(video_in_path, frame_out_path):
    vidcap = cv2.VideoCapture(video_in_path)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1