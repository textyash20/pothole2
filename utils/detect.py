import numpy as np
from utils import detector_util, save_image
import cv2
import time
import constants
from database import db


def count_no_of_times_pothole_found(lst):
    my_list = lst
    x = y = cnt = 0
    for i in my_list:
        x = y
        y = i
        if x == 0 and y == 1:
            cnt = cnt + 1
    return cnt


def detect_pothole(path, latitude, longitude, user_email_session, img_name):
    lat = latitude
    lon = longitude
    img = path
    # img_name = img_name
    print('sessisdj')
    print()
    score_trash = 0.95
    lst1 = []
    # detection_graph, sess = detector_util.load_inference_graph()
    detection_graph = constants.detection_graph
    sess = constants.sess
    num_potholes_detect = 100
    print("entering dtetect pothole method")
    im_height, im_width = (None, None)
    while True:
        frame = cv2.imread(img)
        frame = np.array(frame)
        new_lat = lat
        new_lon = lon

        if im_height == None:
            im_height, im_width = frame.shape[:2]

        '''try:
            #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            print('inside colour conversion')
        except:
            print("ERROR CONVERING TO RGB")
        '''
        # Passing image through tensorflow model

        boxes, scores, classes = detector_util.detect_objects(frame, detection_graph, sess)

        # drawing bbox on image
        a = detector_util.draw_box_on_image(num_potholes_detect, score_trash, scores, boxes, classes, im_width,
                                            im_height, frame, lat, lon)
        lst1.append(a)
        print(a)
        print('before writing image')
        # no_of_times_potholes_detetced=count_no_of_times_pothole_found(lst1)
        # print(no_of_times_potholes_detetced)

        # return frame
        if a != 0:
            try:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                imS = cv2.resize(frame, (960, 540))
                print('inside image saving')
                try:
                    img_path_save, image_name_save = save_image.get_save_location_of_detected()
                    cv2.imwrite(img_path_save, frame)
                    print('done saving')
                    time.sleep(5)
                    db.savei(user_email_session, image_name_save, img_path_save, new_lat, new_lon, a)
                except:
                    print('except')
                    pass

                # new code from TG
                print('inside image encoding')
                try:
                    (flag, encodedImage) = cv2.imencode(".jpg", frame)
                except:
                    print('cant encode')
                    pass

                # print(type(encodedImage))

                # yield the output frame in the byte format
                try:
                    print('yielding')
                    return (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
                except:
                    print('cant yield')
                    pass

            except:
                print("cant write")
                return 0
        else:
            try:
                (flag, encodedImage) = cv2.imencode(".jpg", frame)
            except:
                print('cant encode')
                pass

            # print(type(encodedImage))

            # yield the output frame in the byte format
            try:
                print('yielding')
                return (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
            except:
                print('cant yield')
                pass
