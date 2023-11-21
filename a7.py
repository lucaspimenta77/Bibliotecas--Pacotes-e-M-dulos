import matplotlib.pyplot as plt


categorias = ["Categoria A", "Categoria B", "Categoria C", "Categoria D"]
valores = [13, 21, 15, 30]

plt.bar(categorias, valores)


plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Gráfico de Barras Simples")


plt.show()
