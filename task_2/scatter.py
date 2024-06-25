import pandas as pd
import matplotlib.pyplot as plt

# Charger le jeu de données
data = pd.read_csv('Housing.csv')

# Afficher les premières lignes du jeu de données pour vérifier le chargement
print(data.head())

# Graphique nuage de points (scatter plot) pour 'area' et 'price'
plt.figure(figsize=(8, 6))
plt.scatter(data["area"], data["price"], c="blue", alpha=0.7)
plt.xlabel("Superficie")
plt.ylabel("Prix")
plt.title("Superficie vs Prix")
plt.grid(True)
plt.show()