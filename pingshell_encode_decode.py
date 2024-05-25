from pynput.keyboard import Controller
import time

def read_binary_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            binary_str = file.read().replace(" ", "")
            return binary_str
    except FileNotFoundError:
        return None

def binary_to_text(binary_str):
    try:
        decimal_value = int(binary_str, 2)
        text = chr(decimal_value)
        return text
    except ValueError:
        return None

def type_text(text):
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press('r')
    keyboard.release(Key.cmd)
    keyboard.release('r')
    keyboard.type(text)

def main():
    file_path = "incoming.txt"
    binary_str = read_binary_from_file(file_path)

    if binary_str:
        plaintext = binary_to_text(binary_str)
        if plaintext:
            print(f"Plaintext: {plaintext}")
            time.sleep(2)  # Optional delay before typing
            type_text(plaintext)
        else:
            print("Invalid binary input")
    else:
        print(f"File '{file_path}' not found")

if __name__ == "__main__":
    main()