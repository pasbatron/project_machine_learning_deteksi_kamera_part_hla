import cv2
from ultralytics import YOLO
import sqlite3
from sqlite3 import Error
import serial
import time

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
def send_data_logging(conn, task):
    sql ='''INSERT INTO table_adjuster_valve_hla(name_line, name_part, quantity, delay, status, andon) VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

ser_arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1) 
model = YOLO('D:\\on\\Project_Artificial_Intelegent\\Deteksi_Kamera_Part_HLA\\src\\best.pt')
video_path = 0
cap = cv2.VideoCapture(video_path)
database = r"D:/on/Project_Artificial_Intelegent/Deteksi_Kamera_Part_HLA/src/database/database_tps.db"

while True:
    success, frame = cap.read()
    if success:
        conn = create_connection(database)
        results = model(frame)
        annotated_frame = results[0].plot()
        result = results[0]
        sum_hla = 0
        for box in result.boxes:
            class_id = result.names[box.cls[0].item()]
            if class_id == "hla":
                sum_hla += 1
        if(sum_hla > 1):
            ser_arduino.write(b"1")
            task = ("Packing_HLA", "Adjuster Valve HLA", str(sum_hla), "-", "1", "oke_andon")
            send_data_logging(conn, task)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            frame = cv2.resize(frame, (400, 250))
            file_name = f"D:\\on\Project_Artificial_Intelegent\\Deteksi_Kamera_Part_HLA\\src\\runs\\hasil\HLA_{timestamp}.png"        
            print("Gambar berhasil disimpan:", file_name)
            cv2.imwrite(file_name, frame) 

        cv2.imshow("YOLOv8 Inference", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:

        break

cap.release()
cv2.destroyAllWindows()
