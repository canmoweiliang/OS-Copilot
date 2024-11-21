import os
import subprocess

def open_thunderbird():
    """
    Open Thunderbird application.

    Args:
    None

    Returns:
    None
    """
    # Check if thunderbird has been installed, if not, install it
    try:
        output = subprocess.check_output("thunderbird")
    except subprocess.CalledProcessError:
        subprocess.run("pip install thunderbird -y")

    # Open Thunderbird
    subprocess.Popen("thunderbird")

