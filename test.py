import keyboard
import threading
import subprocess
from pathlib import Path

# 현재 눌려 있는 키
pressed_keys = {}

# 현재 동시에 누르고 있는 키 조합
current_combo = []

# 완성된 키 조합들을 저장
recorded_combos = []

# 프로그램 종료 신호
stop_event = threading.Event()


# 하나의 키 조합 기록을 완료하는 함수
def finish_combo():

    # 서로 다른 키가 2개 이상 눌렸을 때만 기록
    if len(current_combo) >= 1:

        combo = " + ".join(current_combo)

        recorded_combos.append(combo)

        print("\n조합 기록:", combo)

    # 다음 키 조합을 기록할 수 있도록 초기화
    current_combo.clear()


# 키보드 이벤트 감지 함수
def key_record(event):

    key = event.name
    code = event.scan_code

    # --------------------------------
    # 1. 키를 눌렀을 때
    # --------------------------------

    if event.event_type == "down":

        # Enter를 누르면 기록 종료
        if key == "enter":

            # 아직 완성되지 않은 조합이 있다면 저장
            finish_combo()

            stop_event.set()
            return

        # 이미 눌러져 있는 키라면 중복 처리하지 않음
        if code not in pressed_keys:

            # 현재 눌린 키 등록
            pressed_keys[code] = key

            # 조합에 동일한 키 이름이 없다면 추가
            if key not in current_combo:
                current_combo.append(key)

        # 현재 눌려 있는 키 출력
        print(
            "\r현재 눌린 키:",
            " + ".join(pressed_keys.values()),
            end="",
            flush=True
        )

    # --------------------------------
    # 2. 키를 뗐을 때
    # --------------------------------

    elif event.event_type == "up":

        # 눌린 키 목록에서 제거
        pressed_keys.pop(code, None)

        # 현재 눌린 키 출력
        print(
            "\r현재 눌린 키:",
            " + ".join(pressed_keys.values()) or "없음",
            end="",
            flush=True
        )

        # 모든 키를 놓으면 조합 기록 완료
        if not pressed_keys:

            finish_combo()


# --------------------------------
# 3. 키보드 감지 시작
# --------------------------------

print("키 조합 기록 시작")
print("여러 키를 동시에 누르세요.")
print("Enter를 누르면 기록이 종료됩니다.")

hook = keyboard.hook(key_record)

try:
    stop_event.wait()

finally:
    keyboard.unhook(hook)


# --------------------------------
# 4. 메모장에 기록
# --------------------------------

file_path = Path.cwd() / "keyboard_record.txt"

content = "\n".join(
    f"{i}. {combo}"
    for i, combo in enumerate(recorded_combos, 1)
)

file_path.write_text(
    "===== 키보드 조합 기록 =====\n" + content,
    encoding="utf-8"
)

print("\n기록 완료:", file_path)

# Windows 메모장 실행
subprocess.Popen(["notepad.exe", str(file_path)])