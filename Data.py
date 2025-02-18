import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données
file_path = "heart_disease_data.csv"
df = pd.read_csv(file_path)

# Définition du style des graphiques
sns.set_style("whitegrid")

# Graphique 1: Répartition des maladies cardiaques en fonction de l'âge
plt.figure(figsize=(8, 6))
sns.histplot(df, x="Age", hue="HeartDisease", multiple="stack", bins=20, palette={0: "green", 1: "red"})
plt.title("Répartition des maladies cardiaques selon l'âge")
plt.tight_layout()
plt.savefig("graph_1_age.png")
plt.close()

# Graphique 2: Répartition des maladies cardiaques selon le sexe
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Sex", hue="HeartDisease", palette={0: "green", 1: "red"})
plt.title("Répartition des maladies cardiaques selon le sexe")
plt.tight_layout()
plt.savefig("graph_2_sex.png")
plt.close()

# Graphique 3: Répartition des maladies cardiaques selon le type de douleur thoracique
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="ChestPainType", hue="HeartDisease", palette={0: "green", 1: "red"})
plt.title("Répartition des maladies cardiaques selon le type de douleur thoracique")
plt.tight_layout()
plt.savefig("graph_3_chest_pain.png")
plt.close()