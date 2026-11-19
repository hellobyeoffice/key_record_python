import keyboard
import os
import pyautogui
import pyperclip
from pathlib import Path
import time


# 저장할 파일 이름 지정 (따옴표 필수)
file_name = ". (9).txt"
file_path = os.path.abspath(file_name)


def record_coordinate(): #좌표 기록
  x, y = pyautogui.position()
  log_text = f"{x}, {y}\n"

  try:
    with open(file_name, "a", encoding="UTF-8") as f:
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

def find_notepad(name,extension):
    file = Path(name).rglob(f"*{extension}")
    pyperclip.copy(str(name.resolve()))
    print("경로 확인")

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




def mouse_move1():
    file_name = ". (1).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move2():
    file_name = ". (2).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move3():
    file_name = ". (3).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move4():
    file_name = ". (4).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move5():
    file_name = ". (5).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move6():
    file_name = ". (6).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move7():
    file_name = ". (7).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move8():
    file_name = ". (8).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move9():
    file_name = ". (9).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move10():
    file_name = ". (10).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move11():
    file_name = ". (11).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move12():
    file_name = ". (12).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move13():
    file_name = ". (13).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_move14():
    file_name = ". (14).txt"
    file_path = os.path.abspath(file_name)

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
def mouse_moveg():
    file_name = ". (g).txt"
    file_path = os.path.abspath(file_name)

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



keyboard.add_hotkey("alt+f", record_coordinate)
keyboard.add_hotkey("alt+s", move_cursor_left)
keyboard.add_hotkey("alt+d", move_cursor_right)
keyboard.wait("esc")


keyboard.add_hotkey("alt+q", mouse_move1)
keyboard.add_hotkey("alt+w", mouse_move2)
keyboard.add_hotkey("alt+e", mouse_move3)
keyboard.add_hotkey("alt+r", mouse_move4)


keyboard.add_hotkey("alt+s", mouse_move1)
keyboard.add_hotkey("alt+a", mouse_move2)
keyboard.add_hotkey("alt+d", mouse_move3)
keyboard.add_hotkey("alt+f", mouse_move4)
keyboard.add_hotkey("alt+g", mouse_moveg)


keyboard.add_hotkey("alt+z", mouse_move5)
keyboard.add_hotkey("alt+x", mouse_move6)
keyboard.add_hotkey("alt+c", mouse_move7)
keyboard.add_hotkey("alt+v", mouse_move8)

keyboard.add_hotkey("alt+1", mouse_move10)
keyboard.add_hotkey("alt+2", mouse_move11)
keyboard.add_hotkey("alt+`", mouse_move12)
keyboard.add_hotkey("alt+4", mouse_move13)

keyboard.add_hotkey("shift+g", mouse_move9)


print("단축키 감지 중...")

keyboard.wait("esc")

keyboard.unhook_all()
