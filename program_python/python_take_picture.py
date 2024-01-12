import os
import cv2
import keyboard
from datetime import datetime
from imutils.video import VideoStream

rtsp_url = "rtsp://admin:pt_otics1*@192.168.1.108"
camera_laptop = 0
vidio_streaming = VideoStream(camera_laptop).start()

def ambil_gambar():
    frame = vidio_streaming.read()
    waktu_sekarang = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "D:\\on\\Project_Artificial_Intelegent\\Deteksi_Kamera_Part_HLA\\src\\dataset\\new"
    filename = f"snapshot_{waktu_sekarang}.png"
    full_path = os.path.join(path, filename)
    cv2.imwrite(full_path, frame)
    print(f"Gambar disimpan di: {full_path}")

def main():
    print("Program Pengambil Gambar Klik Enter")
    while True:
        frame = vidio_streaming.read()
        cv2.imshow('Deteksi HLA', frame)        
        key = cv2.waitKey(1) & 0xFF
        key = keyboard.read_event(suppress=True).name
        if key == "enter":
            ambil_gambar()
        elif key == "q":
            break
    cv2.destroyAllWindows()
    vidio_streaming.stop()

if __name__ == "__main__":
    main()
