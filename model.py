from ultralytics import YOLO
if __name__=='__main__':
    # Tải mô hình YOLOv8x
    model = YOLO('yolov8m-obb.pt')

    # Huấn luyện mô hình
    model.train(data='data.yaml', epochs=10, imgsz=320, batch=256)

    # Lưu mô hình đã huấn luyện
    model.save('complete_model.pt')
