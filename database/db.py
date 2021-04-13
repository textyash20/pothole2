import sqlite3
from flask import sessions

session = {}
import constants


def login_validatlilon(eml, pwd):
    email = eml
    password = pwd
    try:
        conn = sqlite3.connect(constants.DB_USER_PATH)
        print("succes")
        cursor = conn.cursor()
    except:
        print("An exception occurred")
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor.execute("""SELECT * FROM user WHERE email = '{}' AND password = '{}'""".format(email, password))
        users = cursor.fetchall()
        print(users)
    except:
        print("error")
    conn.commit()
    conn.close()

    session['user_email'] = users[0][1]
    print(session)

    if len(users) == 1:
        return users
    else:
        return 0


def uniq_email(eml):
    email_unq = eml
    try:
        # conn=constants.DB_USER_PATH
        conn = sqlite3.connect(constants.DB_USER_PATH)
        print("succes")
        cursor1 = conn.cursor()
    except:
        print("An exception occurred")
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor1.execute("""SELECT * FROM user WHERE email = '{}'""".format(email_unq))
        users = cursor1.fetchall()
        conn.commit()
        conn.close()
        if len(users) == 1:
            print('match found')
            return 1
        else:
            print('no match found')
            return 0
    except:
        print("error")


def register_user(users_name, eml, pwd):
    email = eml
    password = pwd
    name = users_name
    try:
        # conn = constants.DB_USER_PATH
        conn = sqlite3.connect(constants.DB_USER_PATH)

        print("succes")
        cursor2 = conn.cursor()
    except:
        print("An exception occurred")
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor2.execute(
            """INSERT INTO user (name,email,password)VALUES( '{}','{}','{}')""".format(name, email, password))
        print("user added succesful")
        conn.commit()
        conn.close()

    except:
        print("error")


def savei(email, filename, filepath, lat, lon, num_pot):
    my_email = email
    my_filename = filename
    my_filepath = filepath
    my_lat = lat
    my_lon = lon
    num_pothole = num_pot

    try:
        conn4 = sqlite3.connect(constants.DB_USER_PATH)
        # cursor = conn.cursor()
        print("succes")
        # cursor = conn.cursor()
    except:
        print("An exception occurred")
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor4 = conn4.cursor()
        print('cursor')

    except:
        print("c except")

    try:
        cursor4.execute(
            """INSERT INTO image(email,filename,filepath,lat,lon,count)VALUES('{}','{}','{}',{},{},{})""".format(
                my_email, my_filename, my_filepath, my_lat, my_lon, num_pothole))
        print("pohole data stored succesfull")
        conn4.commit()
        conn4.close()

    except:
        print("error")


def admshow():
    try:
        conn5 = sqlite3.connect(constants.DB_USER_PATH)
        print("succes")
        cursor5 = conn5.cursor()
    except:
        print("An exception occurred")
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor5.execute("""SELECT email,lat,lon,count FROM image""")
        users_image = cursor5.fetchall()
    except:
        print("error")
    conn5.commit()
    conn5.close()
    return users_image


def view_previous(email):
    email_id = email
    try:
        conn6 = sqlite3.connect(constants.DB_USER_PATH)
        print("succes")
        cursor6 = conn6.cursor()
    except:
        print("An exception occurred")
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor6.execute("""SELECT email,lat,lon,count FROM image WHERE email='{}'""".format(email_id))
        users_image = cursor6.fetchall()
    except:
        print("error")
    conn6.commit()
    conn6.close()
    return users_image



def view_recent(email):
    email_id = email
    try:
        conn9 = sqlite3.connect(constants.DB_USER_PATH)
        print("succes")
        cursor9 = conn9.cursor()
    except:
        print("An exception occurred")
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor9.execute("""SELECT email,lat,lon,count FROM image WHERE email='{}'""".format(email_id))
        users_image = cursor9.fetchall()
        users_recent=users_image[(len(users_image)-1)]
    except:
        print("error")
    conn9.commit()
    conn9.close()
    return users_recent


def user_info_basic(u_email):
    try:
        conn7 = sqlite3.connect(constants.DB_USER_PATH)
        print("succes")
        cursor7 = conn7.cursor()
    except:
        print("An exception occurred")
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor7.execute("""SELECT name FROM user WHERE email='{}'""".format(u_email))
        users_name = cursor7.fetchall()
    # print('sadsad')
    # print(users_name[0][0])
    except:
        print("error")
    conn7.commit()
    conn7.close()
    return users_name[0][0]


def user_complaint_basic(u_email):
    try:
        conn8 = sqlite3.connect(constants.DB_USER_PATH)
        print("succes")
        cursor8 = conn8.cursor()
    except:
        print("An exception occurred")
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor8.execute("""SELECT filename FROM image WHERE email='{}'""".format(u_email))
        temp_ar = cursor8.fetchall()
        count = len(temp_ar)


    except:
        print("error")
    conn8.commit()
    conn8.close()
    return count


"""
def save_img(email_user,file_name,file_path,lattitude,longitude):
    filepath=file_path
    filename=file_name
    emailuser=email_user
    my_lat=lattitude
    my_lon=longitude


    print("inside db save")
    try:
        conn3 = sqlite3.connect('database/image_db.db')
        print("succes")
        cursor3 = conn3.cursor()
    except:
        print('exception')

    try:
        mylat=my_lat
        mylon=my_lon
        cursor3.execute(INSERT INTO user_image(email,filename,filepath,latitude,longitude)VALUES( '{}','{}','{}',{},{}).format(emailuser,filename,filepath,mylat,mylon))
        print("pohole data stored succesfull")
        conn3.commit()
        conn3.close()

    except:
        print("error")
        """
