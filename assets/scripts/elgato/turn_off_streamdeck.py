from StreamDeck.DeviceManager import DeviceManager
import subprocess
import time

def close_app(app_name):
    script = f'''
    ignoring application responses
        tell application "{app_name}" to quit
    end ignoring
    '''
    subprocess.run(["osascript", "-e", script])

def is_app_running(app_name):
    # Check if the specified application is running using AppleScript.
    script = f'tell application "System Events" to exists process "{app_name}"'
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return result.stdout.strip() == "true"


if __name__ == "__main__":
    app_name = "Stream Deck"

    # Close Elgato Stream Deck application if it's running on macOS
    print("Is stream deck running?", is_app_running(app_name))

    if is_app_running(app_name):
        print("Closing Elgato Stream Deck application...")
        close_app(app_name)

    # Wait for a moment to ensure the app is closed
    time.sleep(2)

    streamdecks = DeviceManager().enumerate()

    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))

    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()

        print("Opened '{}' device (serial number: '{}', fw: '{}')".format(
            deck.deck_type(), deck.get_serial_number(), deck.get_firmware_version()
        ))
        
        deck.set_brightness(0)
        
        deck.close()