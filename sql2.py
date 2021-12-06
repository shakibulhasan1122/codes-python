import mysql.connector
from mysql.connector import Error
import sql3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(name,pwd,add,cnt, photo):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='login',
                                             user='sakib',
                                             password='sakib123hasan')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO logintable
                          (username,password,Address,Contact, photo) VALUES (%s,%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)
        

        # Convert data into tuple format
        insert_blob_tuple = (name,pwd,add,cnt, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#insertBLOB("ahsan","komla" ,"Barishal","88097445433","pic.jpg")
sql3.readBLOB("ahsan", "D:\ahsan_pic.jpg")