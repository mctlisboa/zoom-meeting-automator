import time
import schedule
import pyautogui
import psutil

def open_zoom_if_not_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'zoom.exe':
            return
    pyautogui.hotkey('ctrl', 'alt', 'z')
    time.sleep(5)

def login_to_zoom(email, password):
    open_zoom_if_not_running()
    sign_in_button = pyautogui.locateCenterOnScreen('sign_in_button.png', confidence=0.9)
    if sign_in_button:
        pyautogui.click(sign_in_button.x, sign_in_button.y)
        time.sleep(2)
        pyautogui.write(email)
        pyautogui.press('tab')
        pyautogui.write(password)
        pyautogui.press('enter')
        time.sleep(5)

def open_zoom(meeting_url):
    open_zoom_if_not_running()
    login_to_zoom('your_email@example.com', 'your_password')  # Replace with your email and password
    pyautogui.click(833, 424)  # Click 'Join'
    time.sleep(2)
    pyautogui.write(meeting_url)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')  # Click 'Join with Computer Audio'

def admit_all():
    end_time = time.time() + 1800  # 30 minutes in seconds
    while True:
        if time.time() > end_time:
            break

        admit_button = pyautogui.locateCenterOnScreen('admit_button.png', confidence=0.9)
        if admit_button:
            pyautogui.click(admit_button.x, admit_button.y)
            time.sleep(1)
        else:
            time.sleep(5)

def close_zoom():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'zoom.exe':
            process.kill()
            break

def start_meeting(meeting_time_1, meeting_time_2, meeting_url):
    schedule.every().day.at(meeting_time_1).do(run_meeting, meeting_url=meeting_url)
    schedule.every().day.at(meeting_time_2).do(run_meeting, meeting_url=meeting_url)

    while True:
        schedule.run_pending()
        time.sleep(60)

def run_meeting(meeting_url):
    open_zoom(meeting_url)
    admit_all()
    close_zoom()

if __name__ == '__main__':
    meeting_time_1 = '10:00'  # Set the first desired meeting time (24-hour format)
    meeting_time_2 = '15:00'  # Set the second desired meeting time (24-hour format)
    meeting_url = 'https://your-zoom-meeting-url'  # Replace with your meeting URL
    start_meeting(meeting_time_1, meeting_time_2, meeting_url)

