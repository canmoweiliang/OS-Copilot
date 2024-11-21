import os
import subprocess
import time
import pyautogui

def create_calendar_event(title, year, month, day, begin_time, end_time, place, event):
    """
    Create a new event on the Calendar.

    Args:
    title(str): the event's title.
    year, month, day(int): the date of the event.
    begin_time, end_time(str): the event's time, including hour and minute. Such as "17:00", and "07:32".
    place(str): where will the event be hold.
    event(str): the information about event.

    Returns:
    status(bool): There are two status: True and False. If the status is True, then the task complete. Otherwise, the task not complete.
    """
    
    try:
        output = subprocess.check_output(['xdotool', 'search', '--onlyvisible', '--name', 'Outlook']).decode('utf-8')
        window_ids = output.strip().split('\n')
        window_id = window_ids[0]
    except subprocess.CalledProcessError:
        print("未找到Outlook窗口")
    time.sleep(2)
    
    try:
        subprocess.run(['xdotool', 'windowactivate', window_id], check=True)
        pyautogui.press('esc')  # Close any open mail window from the previous run
        pyautogui.hotkey('ctrl', 'shift', '2')  # Go to Calendar
    except subprocess.CalledProcessError as e:
        print(f"Error activating Outlook: {e}")
    time.sleep(2)
    try:
        subprocess.run(["xdotool", "key", "n"])
        subprocess.run(["xdotool", "type", "--delay", "100", title])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        date = year + '/' + month + '/' + day
        subprocess.run(["xdotool", "type", "--delay", "100", date])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "type", "--delay", "100", begin_time])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "type", "--delay", "100", end_time])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "type", "--delay", "100", place])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "type", "--delay", "100", event])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "ctrl+s"])
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Error during search action: {e}")
        
    return False

