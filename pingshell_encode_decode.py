from pynput.keyboard import Controller
import time

def press_windows_r():
    # Simulate pressing the Windows key and "R" key
    kdefeyboard = Controller()
    keyboard.press(keyboard._Key.cmd)  # Press Windows key
    keyboard.press('r')  # Press "R" key
    keyboard.release('r')  # Release "R" key
    keyboard.release(keyboard._Key.cmd)  # Release Windows key

def read_binary_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            binary_str = file.read().replace(" ", "")
            return binary_str
    except FileNotFoundError:
        return None

def binary_to_text(binary_str):
    try:
        # Split the binary string into 8-bit chunks
        chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        # Convert each chunk to its decimal value and then to an ASCII character
        text = "".join(chr(int(chunk, 2)) for chunk in chunks)
        return text
    except ValueError:
        return None

def type_text(text):
    keyboard = Controller()
    keyboard.type(text)

def main():
    file_path = "incoming.txt"
    binary_str = read_binary_from_file(file_path)

    if binary_str:
        plaintext = binary_to_text(binary_str)
        if plaintext:
            print(f"Plaintext: {plaintext}")
            #time.sleep(1)  # Optional delay before typing
            press_windows_r()  # Simulate Windows + R keypress
            time.sleep(1)  # Optional delay before typing
            type_text(plaintext)  # Type the plaintext
        else:
            print("Invalid binary input")
    else:
        print(f"File '{file_path}' not found")

if __name__ == "__main__":
    main()
