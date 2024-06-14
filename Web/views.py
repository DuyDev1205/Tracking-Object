from flask import Blueprint, render_template, request
import speech_recognition as brain_ear #install speechrecognition
import pyaudio #install pyaudio

import os

def Hear():
    read = brain_ear.Recognizer()
    with brain_ear.Microphone() as source:
        print("Máy: Tôi đang nghe")
        audio = read.listen(source)
    try:
        text = read.recognize_google(audio,language="vi-VI")
    except:
        text = ""
    print("Bạn: " + text)
    return text

def Speak(brain_mouth):
    output = gTTS(brain_mouth, lang = "vi", slow = False)
    output.save("output.mp3")
    playsound.playsound('output.mp3', True)
    os.remove("output.mp3")

def multiplication(i, A):
    b = 0
    while(i < len(A)):
        if (A[i] == "x"):
            if (',' in A[i - 1]):
                A[i - 1] = A[i - 1].replace(',','.')
                a = float(A[i - 1])
                if (',' in A[i + 1]):
                    A[i + 1] = A[i + 1].replace(',','.')
                    b = float(A[i + 1])
                else:
                    b = int(A[i + 1])
                S = a * b
            else:
                a = int(A[i - 1])
                if (',' in A[i + 1]):
                    A[i + 1] = A[i + 1].replace(',','.')
                    b = float(A[i + 1])
                else:
                    b = int(A[i + 1])
                S = a * b
            S = str(S).replace('.',',')
            A[i - 1] = S
            A[i] = "*"
            A[i + 1] = "*"
            A.remove("*")
            A.remove("*")
            b = 1
        else: 
            break
    return b

def division(i, A):
    b = 0
    while(i < len(A)):
        if (A[i] == ":"):
            if (',' in A[i - 1]):
                A[i - 1] = A[i - 1].replace(',','.')
                a = float(A[i - 1])
                if (',' in A[i + 1]):
                    A[i + 1] = A[i + 1].replace(',','.')
                    b = float(A[i + 1])
                else:
                    b = int(A[i + 1])
                S = a / b
                if (a % b == 0):
                    S = round(S)
            else:
                a = int(A[i - 1])
                if (',' in A[i + 1]):
                    A[i + 1] = A[i + 1].replace(',','.')
                    b = float(A[i + 1])
                else:
                    b = int(A[i + 1])
                S = a / b
                if (a % b == 0):
                    S = round(S)
            S = str(S).replace('.',',')
            A[i - 1] = S
            A[i] = "*"
            A[i + 1] = "*"
            A.remove("*")
            A.remove("*")
            b = 1
        else: 
            break
    return b

def Calculator(A):
    if("ngoặc" in A):
        while("ngoặc" in A):
            A.remove("ngoặc")
        A[A.index("mở")] = "("
        A[A.index("đóng")] = ")"
    if("nhân" in A):
        A[A.index("nhân")] = "x"
    if("chia" in A):
        A[A.index("chia")] = ":"
    i = 0
    while(i < len(A)):
        b1 = 1
        b2 = 1
        while(b1 == 1 or b2 == 1):
            b1 = multiplication(i, A)
            b2 = division(i,A)
        i = i + 1

    #Cộng trừ
    if (',' in A[0]):
        A[0] = A[0].replace(',','.')
        S = float(A[0])
    else:
        S = int(A[0])
    i = 0
    while(i + 2 < len(A)):
        if (A[i + 1] == "+"):
            if (',' in A[i + 2]):
                A[i + 2] = A[i + 2].replace(',','.')
                S = S + float(A[i + 2])
            else:
                S = S + int(A[i + 2])
        else:
            if (',' in A[i + 2]):
                A[i + 2] = A[i + 2].replace(',','.')
                S = S - float(A[i + 2])
            else:
                S = S - int(A[i + 2])
        i = i + 2
    return str(S)


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

# @views.route("/result", methods = ['POST', 'GET'])
# def result():
#     text = ""
#     while(text != "tắt máy" and text != "Tắt máy"):
#         text = Hear()
#         if text == "Xin chào":
#             brain_mouth = "Chào bạn"
#         elif text == "tắt máy" or text == "Tắt máy":
#             brain_mouth = "Hẹn gặp lại"
#         elif text == "":
#             brain_mouth = "Xin lỗi, bạn có thể nói lại được không?"
#         else:
#             A = text.split()
#             brain_mouth = "= " + Calculator(A)
#         print("Máy: " + brain_mouth)
#         Speak(brain_mouth)
#     return render_template("index.html")