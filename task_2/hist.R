# Charger les données
df <- read.csv("Housing.csv")

# Afficher les premières lignes du dataset
head(df)
# Histogramme pour les chambres à coucher
hist(df$bedrooms, breaks=10, main="Histogramme des chambres à coucher", xlab="Nombre de chambres", ylab="Fréquence", col="blue")
