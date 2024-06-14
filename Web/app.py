from flask import Flask, render_template, Response
from views import views
import cv2
import openpyxl
app = Flask(__name__)

def generate_frames():
    camera = cv2.VideoCapture(0)  # Mở webcam

    while True:
        success, frame = camera.read()  # Đọc khung hình từ webcam
        if not success:
            break
        else:
            
            frame = cv2.flip(frame, 1)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
def read_excel_data(file_name):
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=4):
        row_data = [cell.value for cell in row]
        data.append(row_data)

    return data
@app.route('/')
def index():
    excel_data = read_excel_data('test.xlsx')
    return render_template('index.html', excel_data=excel_data)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug = True)