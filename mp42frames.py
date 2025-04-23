import cv2
import os

# set the file name and folder name
file_video_name = "MVI_3996.MP4"
folder_name = file_video_name.split(".")[0]

# check if the video file exists
if not os.path.exists(file_video_name):
    print("The video file does not exist.")
    exit()

# create the folder
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# capture the video
cap = cv2.VideoCapture(file_video_name)
# get the frame rate and frame count
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# loop through the video and save the frames
for i in range(int(frame_count/fps)):
    arr_frame=[]
    arr_lap=[]
    for j in range(fps):
        success, frame = cap.read()
        # get Laplacian of the frame
        laplacian = cv2.Laplacian(frame, cv2.CV_64F).var()

        # if the Laplacian is greater than 5, save the frame
        if laplacian > 5:
            arr_lap.append(laplacian)
            arr_frame.append(frame)

    # get the frame with the highest Laplacian
    selected_frame = arr_frame[arr_lap.index(max(arr_lap))]
    # save the frame to the folder
    cv2.imwrite(f"{folder_name}/{i}.jpg", selected_frame)