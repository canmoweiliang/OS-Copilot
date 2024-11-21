import subprocess
import pyautogui
import time

def open_email(folder, mail_index):
    """
    Open an email, and user can read email from three folders: Inbox, Drafts and Sent.

    Args:
    folder(str): the folder's name - Inbox, Drafts, Sent Items
    mail_index(int): the e-mail's index

    Returns:
    status(bool): There are two status: True and False. If the status is True, then the task complete. Otherwise, the task not complete.
    """
    try:
        output = subprocess.check_output(['xdotool', 'search', '--onlyvisible', '--name', 'Outlook']).decode('utf-8')
        window_ids = output.strip().split('\n')
        window_id = window_ids[0]
    except subprocess.CalledProcessError:
        print("未找到Outlook窗口")
        return False
    time.sleep(2)

    try:
        subprocess.run(['xdotool', 'windowactivate', window_id], check=True)
        pyautogui.press('esc')  # Close any open mail window from the previous run
        pyautogui.hotkey('ctrl', 'shift', '1')  # Go to Mail view
        pyautogui.hotkey('ctrl', 'y')  # Go to Folder pane
        pyautogui.hotkey('home')  # Move to the top of the folder list
    except subprocess.CalledProcessError as e:
        print(f"Error activating Outlook: {e}")

    folder_shortcuts = {
        "Inbox": ['g', 'i'],
        "Drafts": ['g', 'd'],
        "Sent": ['g', 's']
    }
    if folder_index in folder_shortcuts:
        shortcut = folder_shortcuts[folder]
        pyautogui.press(shortcut[0])
        pyautogui.press(shortcut[1])
    else:
        print("无效的文件夹选择")
    time.sleep(2)

    pyautogui.hotkey('home')  # Move to the top of the message list
    for i in range(mail_index - 1):
        pyautogui.hotkey('down')  # Move down to the target message
    
    time.sleep(1)
    return True
 
