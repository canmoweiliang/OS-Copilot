import os
import subprocess
import time
import pyautogui

def compose_and_send_email(recipient, subject, body):
    """
    Compose a new email and send it to other people.

    Args:
    recipient(str): the recipient's email
    subject(str): the e-mail's subject
    body(str): the e-mail's body

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
        pyautogui.hotkey('ctrl', 'shift', '1')  # Go to Mail view
        pyautogui.hotkey('home')  # Move to the top of the message list
    except subprocess.CalledProcessError as e:
        print(f"Error activating Outlook: {e}")
    time.sleep(2)
    try:
        subprocess.run(["xdotool", "key", "n"])
        subprocess.run(["xdotool", "type", "--delay", "100", recipient])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "type", "--delay", "100", subject])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Tab"])
        time.sleep(1)
        subprocess.run(["xdotool", "type", "--delay", "100", body])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "ctrl+Return"])
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Error during search action: {e}")
        
    return False

