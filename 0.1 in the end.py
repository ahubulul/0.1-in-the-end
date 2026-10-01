import sys
import threading
import tkinter as tk
from time import sleep
import pygame

pygame.mixer.init()
try:
    pygame.mixer.music.load("0.1 in the end .mp3")
except Exception as e:
    print(
        f"Lỗi tải nhạc: {e}. Vui lòng kiểm tra lại tên file '0.1 in the end .mp3'"
    )

root = tk.Tk()
root.title("Lyrics Player")
root.geometry("600x400")
root.configure(bg="#1e1e1e")  

label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 16, "bold"),
    fg="#ffffff",
    bg="#1e1e1e",
    wraplength=550,
    justify="center",
)
label.pack(expand=True)

def animate_lyrics():
    if pygame.mixer.music.get_busy() or True:
        pygame.mixer.music.play()

    lines = [
        ("Nơi anh về trời đổ cơn mưa", 0.05, 0.3),
        ("Không biết bây giờ em đã ổn chưa", 0.06, 0.3),
        ("Anh không thể yêu thêm một người", 0.06, 0.1),
        ("Cảm xúc của anh chẳng còn như xưa", 0.05, 0.1),
        ("Lối anh đi nơi đó không em đêm tối bao vây, anh thì xin thua", 0.06, 0.1),
        ("Chắc em không muốn nhớ anh rồi", 0.06, 0.1),
        ("Cảm xúc bây giờ đọng lại lưa thưa", 0.05, 0.5),
    ]

    sleep(1.0)

    for line, char_delay, line_delay in lines:
        current_text = ""
        for char in line:
            current_text += char
            label.config(text=current_text)
            sleep(char_delay)
        sleep(line_delay)

def start_app():
    threading.Thread(target=animate_lyrics, daemon=True).start()

def on_closing():
    pygame.mixer.music.stop()
    root.destroy()
    sys.exit()


root.protocol("WM_DELETE_WINDOW", on_closing)

root.after(500, start_app)
root.mainloop()