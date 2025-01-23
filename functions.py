import random
import tkinter as tk

LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
codex = {}
mixPhrase = []
decodePhrase = []

def tkinter_app():
    root = tk.Tk()
    root.title('Cryptoquip')
    window_width = 600
    window_height = 600

    # Create a Text widget to display results
    T = tk.Text(root, height=10, width=52)
    T.pack(pady=20)

    # Create Entry widgets for user input
    phrase_entry = tk.Entry(root, width=52)
    phrase_entry.pack(pady=10)

    # Create a StringVar for storing the selected radio button value
    selected = tk.StringVar(value="encode")

    # Create a "Change Letter" box, initially hidden
    change_letter_frame = tk.Frame(root)
    change_label = tk.Label(change_letter_frame, text="Change Letter")
    change_label.pack(pady=5)

    old_label = tk.Label(change_letter_frame, text="Letter to change:")
    old_label.pack(pady=5)
    old_entry = tk.Entry(change_letter_frame)
    old_entry.pack(pady=5)

    new_label = tk.Label(change_letter_frame, text="Change to:")
    new_label.pack(pady=5)
    new_entry = tk.Entry(change_letter_frame)
    new_entry.pack(pady=5)

    def apply_change():
        old = old_entry.get().lower()
        new = new_entry.get().lower()

        if old in mixPhrase:
            codex[old] = new
            for j in range(len(mixPhrase)):
                if mixPhrase[j] == old:
                    decodePhrase[j] = new

            # Update the Text widget with the new decoded phrase
            T.delete(1.0, tk.END)
            T.insert(tk.END, "Original: " + ' '.join(mixPhrase) + "\n")
            T.insert(tk.END, "New: " + ' '.join(decodePhrase) + "\n")
        else:
            T.insert(tk.END, f"Letter '{old}' not found in codex.\n")

    # Button to apply letter change
    apply_button = tk.Button(change_letter_frame, text="Apply Change", command=apply_change)
    apply_button.pack(pady=10)

    # Hide change letter section initially
    change_letter_frame.pack_forget()

    def handle_action():
        action = selected.get()
        phrase = phrase_entry.get().lower()

        # Clear the previous output
        T.delete(1.0, tk.END)

        if action == 'encode':
            encode(phrase, T)
        elif action == 'decode':
            decode(phrase, T)
        else:
            T.insert(tk.END, "Invalid action. Please select 'Encode' or 'Decode'.\n")

        # Show the Change Letter section after pressing Start
        change_letter_frame.pack(pady=20)

    def restart():
        # Reset everything (input fields, output, codex, mixPhrase, decodePhrase)
        phrase_entry.delete(0, tk.END)  # Clear the phrase entry
        selected.set("encode")  # Reset the radio button to "encode"
        T.delete(1.0, tk.END)  # Clear the result Text widget
        change_letter_frame.pack_forget()  # Hide the Change Letter section
        # Clear the previous encoding/decoding data
        global codex, mixPhrase, decodePhrase
        codex = {}
        mixPhrase = []
        decodePhrase = []

    # Radio buttons for selecting Encode or Decode
    encode_radio = tk.Radiobutton(root, text="Encode", value="encode", variable=selected)
    encode_radio.pack()

    decode_radio = tk.Radiobutton(root, text="Decode", value="decode", variable=selected)
    decode_radio.pack()

    # Button to start encoding or decoding based on user input
    action_button = tk.Button(root, text="Start", command=handle_action)
    action_button.pack()

    # Button to restart the app and clear everything
    restart_button = tk.Button(root, text="Restart", command=restart)
    restart_button.pack(pady=10)

    # Center window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.mainloop()


# This function encrypts the phrase
def encode(phrase, T):
    global LETTER, codex, mixPhrase
    mixPhrase = []  # Clear previous mixPhrase
    for i in phrase:
        if i.isalpha():
            if i not in codex:
                ranLet = random.choice(LETTER)
                if i == ranLet:
                    encode(phrase, T)  # Recursion to avoid the same letter being encoded
                codex[i] = ranLet
                mixPhrase.append(ranLet)
                if ranLet in LETTER:
                    LETTER.remove(ranLet)
            else:
                mixPhrase.append(codex.get(i))
        else:
            mixPhrase.append(i)

    # Display the result
    key = random.choice(list(codex.items()))
    write(key, phrase)
    T.insert(tk.END, "Your hint is: " + str(key) + "\n")
    T.insert(tk.END, ' '.join(mixPhrase) + "\n")


# Decode functionality
def decode(phrase, T):
    global mixPhrase, decodePhrase
    decodePhrase = []  # Clear previous decodePhrase
    for i in phrase:
        mixPhrase.append(i)
        decodePhrase.append(i)

    # Display the mix phrase
    T.insert(tk.END, "Encoded phrase: " + ' '.join(mixPhrase) + "\n")
    T.insert(tk.END, "To decode, enter the substitution for a letter.\n")
    change(T)


# The "key" parameter right now is the hint a user gets and may be used later for a decode function.
# WRITE
def write(key, phrase):
    with open("crypto.txt", 'a+') as f:
        f.write('Phrase: ')
        for j in phrase:
            f.write(j)
        f.write('\n')
        f.write('Jumble: ')
        for i in mixPhrase:
            f.write(i)
        f.write('\n')
        f.write('Key: ')
        f.write(str(key))
        f.write('\n')


if __name__ == "__main__":
    tkinter_app()
