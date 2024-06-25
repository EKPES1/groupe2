# Charger les données
df <- read.csv("Housing.csv")

# Afficher les premières lignes du dataset
head(df)
# Graphique de dispersion
plot(df$area, df$price, main="Graphique de dispersion de la superficie vs le prix", xlab="Superficie (en pieds carrés)", ylab="Prix (en dollars)", pch=19, col=rgb(0.2,0.4,0.6,0.5))
