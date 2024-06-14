import cv2 as cv
import os
import time
import signal
import sys
# Tạo thư mục để lưu các khung hình nếu chưa có
folder_path = 'images'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Kiểm tra số lượng khung hình đã có trong thư mục
def get_last_frame_number(folder):
    frames = [f for f in os.listdir(folder) if f.endswith('.jpg')]
    if not frames:
        return 0
    frame_numbers = [int(f.split('_')[1].split('.')[0]) for f in frames]
    return max(frame_numbers)

# Hàm xóa tất cả các ảnh trong thư mục
def delete_all_images(folder_path):
    # Kiểm tra thư mục có tồn tại hay không
    if not os.path.exists(folder_path):
        print(f"Thư mục {folder_path} không tồn tại.")
        return

    # Liệt kê tất cả các tệp trong thư mục
    files = os.listdir(folder_path)
    
    # Xóa từng tệp ảnh
    for file in files:
        if file.endswith('.jpg'):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            print(f"Đã xóa {file_path}")

    print(f"Tất cả các tệp ảnh trong thư mục {folder_path} đã được xóa.")    

# Đặt tín hiệu ngắt (Ctrl+C) để giải phóng camera
def release_camera(signum, frame):
    global cam
    print("Giải phóng camera và đóng tất cả các cửa sổ.")
    cam.release()
    cv.destroyAllWindows()
    sys.exit(0)

signal.signal(signal.SIGINT, release_camera)
signal.signal(signal.SIGTERM, release_camera)

# Hàm chụp ảnh từ camera
def get_images():
    global cam
    # Mở camera
    cam = cv.VideoCapture(0)
    # time.sleep(2)  # Đợi một chút để camera ổn định

    last_frame_number = get_last_frame_number(folder_path)
    next_frame_number = last_frame_number + 1
    frame_count = 0
    total_frames = 300
    start_time = time.time()

    while frame_count < total_frames:
        ret, frame = cam.read()
        if not ret:
            print("Không thể truy cập camera")
            break
        
        # Lưu khung hình vào thư mục images
        frame_count += 1
        frame_filename = f'{folder_path}/frame_{next_frame_number:04d}.jpg'
        cv.imwrite(frame_filename, frame)
        next_frame_number += 1
        
        # Hiển thị khung hình
        cv.imshow('webcam', frame)

        # Kiểm tra phím 'q' để thoát
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        # Đảm bảo tốc độ lấy mẫu là 60 khung hình mỗi giây
        elapsed_time = time.time() - start_time
        expected_time_per_frame = frame_count / 60
        if elapsed_time < expected_time_per_frame:
            time.sleep(expected_time_per_frame - elapsed_time)

    # Giải phóng camera và đóng tất cả các cửa sổ khi hoàn thành
    print("Giải phóng camera và đóng tất cả các cửa sổ.")
    cam.release()
    cv.destroyAllWindows()

get_images()

# Xóa tất cả các ảnh trong thư mục images
# delete_all_images('images')
