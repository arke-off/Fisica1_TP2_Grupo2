import customtkinter as ctk
import math

def distancia_taxi(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def distancia_maximo(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

def convertir_a_metros(distancia, unidad):
    if unidad == 'Kilómetros':
        return distancia * 1000
    elif unidad == 'Millas':
        return distancia * 1609.34
    else:
        return distancia

def calcular_distancia():
    try:
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())

        unidad = unidad_combo.get()
        tipo = tipo_combo.get()

        p1 = (x1, y1)
        p2 = (x2, y2)

        if tipo == 'Taxi':
            distancia = distancia_taxi(p1, p2)
        elif tipo == 'Euclídea':
            distancia = distancia_euclidiana(p1, p2)
        else:
            distancia = distancia_maximo(p1, p2)

        distancia_m = convertir_a_metros(distancia, unidad)
        resultado_label.configure(text=f"Distancia: {distancia_m:.2f} metros")
    except ValueError:
        resultado_label.configure(text="⚠️ Error: ingresa solo números en las coordenadas.")

# Interfaz
app = ctk.CTk()
app.title("Calculadora de Distancias (Grupo2)")
app.geometry("400x500")

ctk.CTkLabel(app, text="Coordenadas del Punto 1").pack(pady=5)
entry_x1 = ctk.CTkEntry(app, placeholder_text="x1")
entry_x1.pack()
entry_y1 = ctk.CTkEntry(app, placeholder_text="y1")
entry_y1.pack()

ctk.CTkLabel(app, text="Coordenadas del Punto 2").pack(pady=5)
entry_x2 = ctk.CTkEntry(app, placeholder_text="x2")
entry_x2.pack()
entry_y2 = ctk.CTkEntry(app, placeholder_text="y2")
entry_y2.pack()

ctk.CTkLabel(app, text="Unidad de medida").pack(pady=5)
unidad_combo = ctk.CTkComboBox(app, values=["Metros", "Kilómetros", "Millas"])
unidad_combo.pack()
unidad_combo.set("Metros")

ctk.CTkLabel(app, text="Tipo de distancia").pack(pady=5)
tipo_combo = ctk.CTkComboBox(app, values=["Taxi", "Euclídea", "Máximo"])
tipo_combo.pack()
tipo_combo.set("Euclídea")

calcular_btn = ctk.CTkButton(app, text="Calcular Distancia", command=calcular_distancia)
calcular_btn.pack(pady=15)

resultado_label = ctk.CTkLabel(app, text="")
resultado_label.pack(pady=10)

app.mainloop()
