import os
import subprocess
import time
import pyautogui

def delete_email():
    """
    Delete the email(s).
    
    Args:
    None

    Returns:
    status(bool): There are two status: True and False. If the status is True, then the task complete. Otherwise, the task not complete.
    """
        
    try:
        pyautogui.hotkey('down')
        pyautogui.hotkey('up')
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Delete"])
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Error during search action: {e}")
        
    return False

