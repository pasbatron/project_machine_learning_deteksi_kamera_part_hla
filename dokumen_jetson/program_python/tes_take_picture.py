import os
import cv2
import keyboard
from datetime import datetime
from imutils.video import VideoStream


rtsp_url = "rtsp://admin:pt_otics1*@192.168.1.108"
vidio_streaming = VideoStream(rtsp_url).start()

def ambil_gambar():
    frame = vidio_streaming.read()
    waktu_sekarang = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "/home/otics/on/project_pt_otics_ai_hla/data/cctv"
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
    parent_directory = r"/home/wanda/Documents/on/PT_Otics_Indonesia/Project_Kamera_Part_HLA/Project_PT.Otics_Indonesia_Kamera_HLA/runs/hasil"
    sub_directory = "Hasil_Deteksi"
    main()
