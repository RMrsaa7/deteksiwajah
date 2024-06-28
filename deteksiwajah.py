import cv2

#mencari indeks kamera eksternal
def find_camera_index(max_index=20):
    print("Mencari indeks kamera...")
    for index in range(max_index): 
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print(f"Kamera ditemukan pada indeks {index}")
            cap.release()
            return index
        cap.release()
    print("Tidak ada kamera yang terdeteksi.")
    return None

camera_index = find_camera_index()
if camera_index is not None:
    #menggunakan kamera bawaan
    cap = cv2.VideoCapture(camera_index)
    cap.set(3, 640)  # Lebar
    cap.set(4, 480)  # Tinggi

    while True:
        success, img = cap.read()
        if not success:
            print("Gagal membaca frame dari kamera.")
            break

        facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = facecascade.detectMultiScale(img_gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Kamera", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
else:
    print("Tidak ada kamera eksternal yang ditemukan.")
