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

    action_label = tk.Label(root, text="Enter 'encode' or 'decode' below:")
    action_label.pack()

    action_entry = tk.Entry(root, width=52)
    action_entry.pack(pady=10)

    def handle_action():
        action = action_entry.get().lower()
        phrase = phrase_entry.get().lower()

        # Clear the previous output
        T.delete(1.0, tk.END)

        if action == 'encode':
            encode(phrase, T)
        elif action == 'decode':
            decode(phrase, T)
        else:
            T.insert(tk.END, "Invalid action. Please enter 'encode' or 'decode'.\n")

    # Button to start encoding or decoding based on user input
    action_button = tk.Button(root, text="Start", command=handle_action)
    action_button.pack()

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


def change(T):
    global codex, mixPhrase, decodePhrase

    def apply_change():
        old = old_entry.get().lower()
        new = new_entry.get().lower()

        if old in codex:
            codex[old] = new
            for j in range(len(mixPhrase)):
                if mixPhrase[j] == old:
                    decodePhrase[j] = new

            # Update the Text widget with the new decoded phrase
            T.delete(1.0, tk.END)
            T.insert(tk.END, "Updated Codex: " + str(codex) + "\n")
            T.insert(tk.END, "Original: " + ' '.join(mixPhrase) + "\n")
            T.insert(tk.END, "New: " + ' '.join(decodePhrase) + "\n")
        else:
            T.insert(tk.END, f"Letter '{old}' not found in codex.\n")

    # Create an interface to change letters in the Tkinter window
    change_window = tk.Toplevel()
    change_window.title("Change Letters")

    old_label = tk.Label(change_window, text="Letter to change:")
    old_label.pack(pady=5)
    old_entry = tk.Entry(change_window)
    old_entry.pack(pady=5)

    new_label = tk.Label(change_window, text="Change to:")
    new_label.pack(pady=5)
    new_entry = tk.Entry(change_window)
    new_entry.pack(pady=5)

    apply_button = tk.Button(change_window, text="Apply Change", command=apply_change)
    apply_button.pack(pady=10)

    change_window.mainloop()


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
