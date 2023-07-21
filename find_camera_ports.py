#our projects channel -> t.me/EngineeringLab
#aparat channel       -> www.aparat.com/EngineeringLab
#youtube channel      -> https://www.youtube.com/@sm_faraji
#GitHub               -> https://github.com/SmFaraji

import cv2

def find_camera_ports():
    connected_cameras = []

    # Iterate through possible port numbers (0-9)
    for i in range(10):

        cap = cv2.VideoCapture(i)

        # check if the camera is opened successfully
        if cap.isOpened():
            connected_cameras.append(i)
            cap.release()

    return connected_cameras

camera_ports = find_camera_ports()
if camera_ports:
    print("---->there is " + str(len(camera_ports)) + " active video port:" + str(camera_ports))
else:
    print("---->no camera port available! be sure about connecting camera device to system")
