import pygetwindow as gw
import pyautogui
import pyperclip
import time

def get_firefox_window():
    firefox_windows = [window for window in gw.getWindowsWithTitle('Mozilla Firefox')]
    if firefox_windows:
        return firefox_windows[0]  # Assuming there's only one Firefox window
    else:
        return None

def save_open_tab_links():
    firefox_window = get_firefox_window()
    if firefox_window:
        firefox_window.activate()
        time.sleep(1)  # Give some time for the window to activate
        firefox_window.maximize()  # Ensure the window is maximized to show all tabs

        # Press Ctrl+L to focus the address bar
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.5)  # Give some time for the address bar to focus

        # Press Ctrl+C to copy the URL
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)  # Give some time for the URL to be copied
        first_tab_url = pyperclip.paste()

        # Close the "Copy" dialog if it appears
        if "Save to Pocket" in first_tab_url:
            pyautogui.press('enter')

        # Repeat the process to switch to the next tab and get its URL
        tab_links = [first_tab_url]
        while True:
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(0.5)  # Give some time for the tab to switch

            # Press Ctrl+L again to focus the address bar
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(0.5)  # Give some time for the address bar to focus

            # Press Ctrl+C to copy the URL
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.5)  # Give some time for the URL to be copied
            tab_url = pyperclip.paste()

            if tab_url == first_tab_url:  # Stop when we reach the first tab again
                break
            tab_links.append(tab_url)

        # Write the URLs to a plain text file
        with open('open_tab_links.txt', 'w') as f:
            for link in tab_links:
                f.write(link + '\n')

        print("Tab links saved successfully!")
    else:
        print("No Firefox window found.")

save_open_tab_links()
