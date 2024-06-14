import cv2
from ultralytics import YOLO
import yaml
import mysql.connector

# Load data from the YAML file
with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Print class names from the YAML data
print(data['names'])

# Uncomment these lines if you want to use YOLO
# class_indices = list(range(len(data['names'])))
# # Load YOLOv8-OBB model
# model = YOLO(r'D:\VSCode\Tracking Objective\train8\weights\best.pt')
# result = model(source=0, show=True, conf=0.8, classes=class_indices, project='.')

# Database connection configuration
config = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "123456",
    "database": "dss"
}
# câu truy vấn sql
connection = mysql.connector.connect(**config)
cursor = connection.cursor()
cursor.execute("SELECT date FROM golddss ORDER BY date ASC LIMIT 1")
result = cursor.fetchone()
cursor.close()
connection.close()
print(result)
