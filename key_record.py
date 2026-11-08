import keyboard
import os
import pyautogui
import time

# 저장할 파일 이름 지정 (따옴표 필수)
file_name = "coordinate"
file_path = os.path.abspath(file_name)


def record_coordinate():
  x, y = pyautogui.position()
  log_text = f"X: {x}, Y: {y}\n"

  try:
    with open(file_path, "a", encoding="UTF-8") as f:
      f.write(log_text)
      f.flush()
    print(f"[기록됨] X: {x}, Y: {y} -> {file_path}")
  except Exception as e:
    print(f"파일 쓰기 오류: {e}")


print("기록을 시작합니다. 'c'를 누르면 좌표가 저장되고, 'esc'를 누르면 종료됩니다.")

# 'c' 키를 누르면 record_coordinate 함수 실행
keyboard.add_hotkey("c", record_coordinate)

# 'esc' 키를 누를 때까지 프로그램 유지
keyboard.wait("esc")

print("기록을 마칩니다.")
