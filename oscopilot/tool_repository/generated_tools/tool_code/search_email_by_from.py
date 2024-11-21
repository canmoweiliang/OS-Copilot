import os
import subprocess
import time
import pyautogui

def search_email_by_from(from_email):
    """
    Search the emails by the from.
    
    Args:
    from(str): the from used to search the emails.

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
        pyautogui.hotkey('ctrl', 'y')  # Go to Folder pane
        pyautogui.hotkey('home')  # Move to the top of the folder list
    except subprocess.CalledProcessError as e:
        print(f"Error activating Outlook: {e}")
        
    try:
        subprocess.run(["xdotool", "key", "alt+q"])
        subprocess.run(["xdotool", "key", "ctrl+a"])
        time.sleep(1)
        subprocess.run(["xdotool", "type", "--delay", "100", "from:("])
        subprocess.run(["xdotool", "type", "--delay", "100", from_email])
        subprocess.run(["xdotool", "type", "--delay", "100", ")"])
        subprocess.run(["xdotool", "key", "Return"])
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'home')
        return True
    except Exception as e:
        print(f"Error during search action: {e}")
    
    return False

