import math
import customtkinter as ctk

from tkinter import messagebox


# --- MÉTRICAS ---
def distancia_taxi(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def distancia_euclidea(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def distancia_maximo(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

# --- CONVERSIÓN A METROS ---
def convertir_a_metros(valor, unidad):
    if unidad in ['m', 'M']:
        return valor
    elif unidad in ['k', 'K']:
        return valor * 1000
    elif unidad in ['a', 'A']:  # millas
        return valor * 1609.34
    else:
        raise ValueError("Unidad no válida.")

# --- COMPROBAR SI TRES PUNTOS ESTÁN EN LÍNEA RECTA ---
def estan_en_linea(p1, p2, p3):
    # Usamos el determinante para ver si están alineados:
    # (x2-x1)(y3-y1) - (y2-y1)(x3-x1) == 0
    return (p2[0]-p1[0]) * (p3[1]-p1[1]) == (p2[1]-p1[1]) * (p3[0]-p1[0])

# --- FUNCIÓN PRINCIPAL PARA CALCULAR LONGITUD DEL CAMINO ---
def calcular_longitud_camino(puntos, unidad, metrica):
    if metrica == 't':
        distancia_func = distancia_taxi
    elif metrica == 'e':
        distancia_func = distancia_euclidea
    elif metrica == 'm':
        distancia_func = distancia_maximo
    else:
        raise ValueError("Métrica no válida")

    longitud_total = 0
    for i in range(1, len(puntos)):
        d = distancia_func(puntos[i - 1], puntos[i])
        d_metros = convertir_a_metros(d, unidad)
        longitud_total += d_metros

    return longitud_total


# --- INTERFAZ ---
class CaminoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de longitud de caminos (Grupo2)")
        self.geometry("500x500")
        ctk.set_appearance_mode("light")

        self.unidad = ctk.StringVar(value="m")
        self.metrica = ctk.StringVar(value="t")
        self.camino = []

        self.crear_widgets()

    def crear_widgets(self):
        ctk.CTkLabel(self, text="Unidad (m/k/a):").pack(pady=5)
        ctk.CTkEntry(self, textvariable=self.unidad).pack()

        ctk.CTkLabel(self, text="Métrica (t/e/m):").pack(pady=5)
        ctk.CTkEntry(self, textvariable=self.metrica).pack()

        ctk.CTkLabel(self, text="Coordenada X:").pack(pady=5)
        self.entry_x = ctk.CTkEntry(self)
        self.entry_x.pack()

        ctk.CTkLabel(self, text="Coordenada Y:").pack(pady=5)
        self.entry_y = ctk.CTkEntry(self)
        self.entry_y.pack()

        ctk.CTkButton(self, text="Agregar punto", command=self.agregar_punto).pack(pady=10)
        ctk.CTkButton(self, text="Terminar camino", command=self.terminar).pack(pady=5)

        self.label_resultado = ctk.CTkLabel(self, text="Longitud: -")
        self.label_resultado.pack(pady=20)

    def agregar_punto(self):
        try:
            x = int(self.entry_x.get())
            y = int(self.entry_y.get())
            nuevo_punto = (x, y)

            if nuevo_punto == (0, 0):
                messagebox.showinfo("Fin", "Usá el botón 'Terminar camino' para finalizar.")
                return

            if len(self.camino) >= 2:
                if estan_en_linea(self.camino[-2], self.camino[-1], nuevo_punto):
                    messagebox.showinfo("No se admite nuevo punto", "El punto está en la recta con los dos anteriores.")
                    return

            self.camino.append(nuevo_punto)
            messagebox.showinfo("Punto agregado", f"Se agregó el punto {nuevo_punto}")
            self.entry_x.delete(0, 'end')
            self.entry_y.delete(0, 'end')

        except ValueError:
            messagebox.showerror("Error", "Coordenadas inválidas")

    def terminar(self):
        if not self.camino:
            self.label_resultado.configure(text="Longitud: 0 metros")
            return

        try:
            total = calcular_longitud_camino(self.camino, self.unidad.get(), self.metrica.get())
            self.label_resultado.configure(text=f"Longitud: {total:.2f} metros")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = CaminoApp()
    app.mainloop()
