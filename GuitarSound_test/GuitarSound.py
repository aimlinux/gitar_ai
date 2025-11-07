import random
import time
import tkinter as tk
import ttkbootstrap as tb
import fluidsynth

# ===============================
# 🎸 FluidSynth初期化
# ===============================
sf = fluidsynth.Synth()
sf.start(driver="dsound")

# ▼ ここを自分の SoundFont ファイルのパスに変更してください！
soundfont_path = "C:/Users/kxiyt/Documents/GitHub/gitar_ai/GuitarA.sf2"
sf.load_soundfont(soundfont_path)

# アコースティックギター（MIDI楽器番号25）
sf.program_select(0, 0, 0, 25)

# ===============================
# 🎶 コード定義（ピッチ: MIDIノート番号）
# ===============================
CHORDS = {
    "C":  [60, 64, 67],        # C E G
    "G":  [67, 71, 74],        # G B D
    "Am": [69, 72, 76],        # A C E
    "F":  [65, 69, 72],        # F A C
    "Dm": [62, 65, 69],        # D F A
    "Em": [64, 67, 71],        # E G B
}

# ===============================
# 🎵 コードを鳴らす関数
# ===============================
def play_chord(chord_name, duration=1.0):
    """指定したコードを鳴らす"""
    if chord_name not in CHORDS:
        return

    notes = CHORDS[chord_name]
    for n in notes:
        sf.noteon(0, n, 100)
    time.sleep(duration)
    for n in notes:
        sf.noteoff(0, n)

# ===============================
# 🎼 コード進行を自動生成
# ===============================
def generate_progression():
    """4つのコードからなる進行を生成"""
    chord_list = random.sample(list(CHORDS.keys()), 4)
    progression_label.config(text=" - ".join(chord_list))

    # 順に鳴らす
    root.update()
    for c in chord_list:
        play_chord(c, duration=1.2)

# ===============================
# 🎨 GUI（tkinter + ttkbootstrap）
# ===============================
root = tb.Window(themename="minty")
root.title("🎸 Guitar Progression Generator")
root.geometry("500x300")

title_label = tb.Label(root, text="🎶 Guitar Chord Progression Generator 🎶", font=("Segoe UI", 16, "bold"))
title_label.pack(pady=20)

progression_label = tb.Label(root, text="Press the button to generate chords", font=("Segoe UI", 14))
progression_label.pack(pady=20)

generate_button = tb.Button(
    root,
    text="🎸 Generate Progression 🎸",
    bootstyle="info-outline",
    width=25,
    command=generate_progression,
    padding=(12, 12)
)
generate_button.pack(pady=20)

root.mainloop()

# 終了時にサウンドエンジンを停止
sf.delete()
