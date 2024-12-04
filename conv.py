import tkinter as tk


def converter_para_fahrenheit():
    try:
        celsius = float(entrada_temperatura.get())
        fahrenheit = (celsius * 9 / 5) + 32
        rotulo_resultado.config(text=f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
    except ValueError:
        rotulo_resultado.config(text="Por favor, insira um número válido.")

def converter_para_celsius():
    try:
        fahrenheit = float(entrada_temperatura.get())
        celsius = (fahrenheit - 32) * 5 / 9
        rotulo_resultado.config(text=f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
    except ValueError:
        rotulo_resultado.config(text="Por favor, insira um número válido.")


janela = tk.Tk()
janela.title("Conversor de Temperatura")
janela.geometry("300x150")

rotulo_temperatura = tk.Label(janela, text="Temperatura:")
rotulo_temperatura.grid(row=0, column=0, padx=10, pady=10)

entrada_temperatura = tk.Entry(janela)
entrada_temperatura.grid(row=0, column=1, padx=10, pady=10)

botao_para_fahrenheit = tk.Button(
    janela, text="Para Fahrenheit", command=converter_para_fahrenheit
)
botao_para_fahrenheit.grid(row=1, column=0, padx=10, pady=10)

botao_para_celsius = tk.Button(
    janela, text="Para Celsius", command=converter_para_celsius
)
botao_para_celsius.grid(row=1, column=1, padx=10, pady=10)

rotulo_resultado = tk.Label(janela, text="Resultado:")
rotulo_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()