import matplotlib.pyplot as plt
import seaborn as sns

# Dados fictícios de produtos e quantidades vendidas
produtos = ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E"]
quantidades = [150, 200, 300, 250, 180]

# Configuração do estilo do gráfico
sns.set_theme(style="whitegrid")

# Criando o gráfico de barras
plt.figure(figsize=(8, 5))
sns.barplot(x=produtos, y=quantidades, palette="viridis")

# Adicionando rótulos
plt.xlabel("Produtos")
plt.ylabel("Quantidade Vendida")
plt.title("Vendas por Produto")

# Salvando o gráfico como imagem
plt.savefig("grafico.png", dpi=300, bbox_inches="tight")

# Exibindo o gráfico
plt.show()




