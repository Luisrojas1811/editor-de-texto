import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    ruta = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if ruta:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        area_texto.delete("1.0", tk.END)
        area_texto.insert("1.0", contenido)
        ventana.title(f"Editor de Texto — {ruta}")

def guardar_archivo():
    ruta = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if ruta:
        with open(ruta, "w", encoding="utf-8") as archivo:
            contenido = area_texto.get("1.0", tk.END)
            archivo.write(contenido)
        ventana.title(f"Editor de Texto — {ruta}")

ventana = tk.Tk()
ventana.title("Editor de Texto")
ventana.geometry("600x400")

barra = tk.Frame(ventana)
barra.pack(fill="x")

tk.Button(barra, text="Abrir", command=abrir_archivo).pack(side="left", padx=5, pady=5)
tk.Button(barra, text="Guardar", command=guardar_archivo).pack(side="left", padx=5, pady=5)

area_texto = tk.Text(ventana, font=("Arial", 12))
area_texto.pack(fill="both", expand=True)

ventana.mainloop()