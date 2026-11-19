import keyboard
import os
import lines
import pyautogui
import time
from pathlib import Path

from PIL.Image import new

# 저장할 파일 이름 지정 (따옴표 필수)
file_name = "mouse_move"
file_path = os.path.abspath(file_name)


def record_coordinate(): #좌표 기록
  x, y = pyautogui.position()
  log_text = f"{x}, {y}\n"

  try:
    with open(file_path, "a", encoding="UTF-8") as f:
      f.write(log_text)
      f.flush()
    print(f"[기록됨] X: {x}, Y: {y} -> {file_path}")
  except Exception as e:
    print(f"파일 쓰기 오류: {e}")

def record_key(event):
  key = keyboard.read_key()
  if event.event_type == keyboard.KEY_DOWN:
    if key == "space":
      key = " "
    elif key == "enter":
      key = "\n"
    elif key == "backspace":
      key = "-back"

    print(f"{key}")

    with open(file_path, 'a', encoding='utf-8') as f:
      f.write(key)


def save_notepad(filename, content): #메모장 기록 및 저장
  with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

def mouse_control():
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()

    for line in data:
        line = line.strip()

        if not line:
            continue

        if line == "left":
            pyautogui.click(button="left")
            print("왼쪽 클릭")

        elif line == "right":
            pyautogui.click(button="right")
            print("오른쪽 클릭")

        else:
            mx, my = line.split(',')
            mx = int(mx.strip())
            my = int(my.strip())

            pyautogui.moveTo(mx, my)
            print(f"마우스 이동: {mx}, {my}")

def move_cursor_left():
  with open(file_path, 'a', encoding='utf-8') as f:
    f.write("left\n")
    print("input left")

def move_cursor_right():
  with open(file_path, 'a', encoding='utf-8') as f:
    f.write("right\n")
    print("input right")

def find_file(filename):
  target_file = Path()
  for filename in target_file.glob("*.txt"):
    with open(filename, 'r', encoding='utf-8') as file:
      content = file.read()


def aaa(event):
  if event.event_type == keyboard.KEY_DOWN:
    key = event.name

    if key == "space":
      key = " "
    elif key == "enter":
      key = "\n"
    elif key == "backspace":
      key = "-back"

    # 각각의 키가 눌릴 때마다 콘솔에 한 줄씩 표시
    print(f"입력된 키: {key}")

    with open(file_path, 'a', encoding='utf-8') as f:
      f.write(key)
      f.write("+")


if input() == "record":
    keyboard.add_hotkey("alt+s", move_cursor_left)
    keyboard.add_hotkey("alt+d", move_cursor_right)
    keyboard.add_hotkey("alt+f", record_coordinate)

    print("단축키 감지 중... ESC를 누르면 종료")

    keyboard.wait("esc")
elif input() == "move":
    print("동작을 시작합니다.")
    keyboard.add_hotkey("alt+s", mouse_control)
    keyboard.wait("esc")
else:
    print("에러")

