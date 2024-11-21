import os
import subprocess
import time
import pyautogui

def mark_email_as_read():
    """
    Clear the email's mark.
    
    Args:
    None

    Returns:
    status(bool): There are two status: True and False. If the status is True, then the task complete. Otherwise, the task not complete.
    """
        
    try:
        pyautogui.hotkey('down')
        pyautogui.hotkey('up')
        time.sleep(1)
        pyautogui.hotkey('Insert')
        time.sleep(1)
        pyautogui.hotkey('alt')
        time.sleep(1)
        pyautogui.hotkey('h')
        time.sleep(1)
        pyautogui.hotkey('u')
        time.sleep(1)
        pyautogui.hotkey('e')
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Error during search action: {e}")
        
    return False

