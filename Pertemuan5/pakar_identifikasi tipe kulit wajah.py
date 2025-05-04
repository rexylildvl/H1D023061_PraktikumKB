from pyswip import Prolog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

prolog = Prolog()
prolog.consult("pakar_identifikasi tipe kulit wajah_gui.pl")

jenis_kulit = list()
gejala = dict()
index_jenis = 0
index_gejala = 0
current_jenis = ""
current_gejala = ""

def mulai_identifikasi():
    global jenis_kulit, gejala, index_jenis, index_gejala
    prolog.retractall("gejala_pos(_)") 
    prolog.retractall("gejala_neg(_)") 
    
    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)
    
    jenis_kulit = [j["X"].decode() for j in list(prolog.query("jenis_kulit(X)"))]
    for j in jenis_kulit:
        gejala[j] = [g["X"] for g in list(prolog.query(f'gejala(X, "{j}")'))]
    
    index_jenis = 0
    index_gejala = -1
    pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_jenis=False):
    global current_jenis, current_gejala, index_jenis, index_gejala
    
    if ganti_jenis:
        index_jenis += 1
        index_gejala = -1
    
    if index_jenis >= len(jenis_kulit):
        hasil_identifikasi()
        return
    
    current_jenis = jenis_kulit[index_jenis]
    index_gejala += 1
    
    if index_gejala >= len(gejala[current_jenis]):
        hasil_identifikasi(current_jenis)
        return
    
    current_gejala = gejala[current_jenis][index_gejala]
    
    if list(prolog.query(f"gejala_pos({current_gejala})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"gejala_neg({current_gejala})")):
        pertanyaan_selanjutnya(ganti_jenis=True)
        return
    
    pertanyaan = list(prolog.query(f"pertanyaan({current_gejala}, Y)"))[0]["Y"].decode()
    tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"gejala_pos({current_gejala})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"gejala_neg({current_gejala})")
        pertanyaan_selanjutnya(ganti_jenis=True)

def hasil_identifikasi(jenis=""):
    if jenis:
        messagebox.showinfo("Hasil Identifikasi", f"Jenis kulit Anda: {jenis}.")
    else:
        messagebox.showinfo("Hasil Identifikasi", "Jenis kulit Anda tidak teridentifikasi.")
    
    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

# GUI
root = tk.Tk()
root.title("Sistem Pakar Identifikasi Tipe Kulit Wajah")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(
    mainframe,
    text="Aplikasi Identifikasi Tipe Kulit Wajah",
    font=("Arial", 16)
).grid(column=0, row=0, columnspan=3)

ttk.Label(mainframe, text="Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(
    mainframe,
    height=4,
    width=50,
    state=tk.DISABLED
)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = ttk.Button(
    mainframe,
    text="Tidak",
    state=tk.DISABLED,
    command=lambda: jawaban(False)
)
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = ttk.Button(
    mainframe,
    text="Ya",
    state=tk.DISABLED,
    command=lambda: jawaban(True)
)
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(
    mainframe,
    text="Mulai Identifikasi",
    command=mulai_identifikasi
)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()
