# Zoom Meeting Automator

Zoom Automator is a Python script that automatically opens the Zoom app, logs in to your account, joins a scheduled meeting, admits participants, and closes the meeting and the app after 30 minutes.

## Prerequisites

- Python 3.x installed
- `pyautogui`, `psutil`, `schedule` and `requests` libraries installed
- Zoom app installed

## Setup

1. Install the required Python libraries if you haven't already:

   ```bash
   pip install pyautogui psutil schedule requests
   ```

2. Replace the meeting_time_1, meeting_time_2, and meeting_url variables in the zoom_automator.py script with your desired meeting times and URL:

   ```python
    meeting_time_1 = '10:00'  # Set the first desired meeting time (24-hour format)
    meeting_time_2 = '15:00'  # Set the second desired meeting time (24-hour format)
    meeting_url = 'https://your-zoom-meeting-url'  # Replace with your meeting URL
   ```

3. Replace 'your_email@example.com' and 'your_password' in the login_to_zoom() function call with your Zoom email and password:

   ```python
    login_to_zoom('your_email@example.com', 'your_password')  # Replace with your email and password
   ```
4. Take a screenshot of the "Sign In" button on the Zoom app's main screen, crop the image to just the button, and save it as "sign_in_button.png" in the same directory as the script.

5. Take a screenshot of the "Admit" button that appears when someone is waiting to join a Zoom meeting, crop the image to just the button, and save it as "admit_button.png" in the same directory as the script.

## Running the script
1. Open a terminal or command prompt.

2. Navigate to the directory where the zoom_automator.py script is located.

3. Run the script:

   ```bash
    python zoom_automator.py
   ```

The script will now run every day at the specified meeting times, join the meeting with the given URL, admit participants, and close the meeting and the Zoom app after 30 minutes.

---

## To run the script as a service

### Windows:

To create a background service for the zoom_automator.py script on Windows, you can use NSSM (Non-Sucking Service Manager).

Download NSSM from https://nssm.cc/download and extract the contents to a directory.

Open a command prompt as Administrator, navigate to the NSSM directory, and run:

   ```bash
    nssm install ZoomAutomator
   ```

In the NSSM GUI, set the following fields:

Path: The path to your Python executable (usually `C:\Python3x\python.exe`)

Startup directory: The directory containing the zoom_automator.py script

Arguments: The name of your script, i.e., zoom_automator.py

Click the "Install service" button. NSSM will install the service and start it automatically.

The script will now run as a background service on Windows, and it will start automatically when the system boots up.

### Linux:

To create a background service for the zoom_automator.py script on Linux, you can use systemd.

Create a new file called zoom-automator.service in the `/etc/systemd/system` directory:

   ```bash
sudo nano /etc/systemd/system/zoom-automator.service
   ```

Add the following content to the file, replacing /path/to/python with the path to your Python executable and /path/to/zoom_automator.py with the path to the zoom_automator.py script:

   ```makefile
[Unit]
Description=Zoom Automator

[Service]
ExecStart=/path/to/python /path/to/zoom_automator.py
Restart=always
User=your_username
Group=your_groupname

[Install]
WantedBy=multi-user.target
   ```
Save and close the file.

Reload the systemd configuration:

   ```
sudo systemctl daemon-reload
   ```

Enable and start the service:

   ```bash
sudo systemctl enable zoom-automator
sudo systemctl start zoom-automator
   ```
The script will now run as a background service on Linux, and it will start automatically when the system boots up.

Keep in mind that running a script as a background service will make it less interactive. Debugging or observing the script's behavior might be more difficult when it's running as a service.