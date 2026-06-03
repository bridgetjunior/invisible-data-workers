import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def moyenne_salaire(s) -> float:
    s = s.replace(" ", "")
    if "-" in s:
        a,b = s.split("-")
        return (float(a) + float(b)) /2
    else:
        return float(s)
    

st.title("Travail invisible derrière l'IA")
st.subheader("Réalisée par ABU Bridget et RAHARIMINO Mialy")

st.divider()

data = pd.read_csv("workers.csv")
data["Salaire_heure (en $)"] = data["Salaire_heure (en $)"].apply(moyenne_salaire)

st.subheader("Données")
st.dataframe(data)

st.divider()
st.subheader("Comparaison des salaires")
tab = px.bar(data, x ="Pays", y = "Salaire_heure (en $)", title = "Salaire par pays")
st.plotly_chart(tab)

st.divider()

# Simulation interactive

data2 = pd.DataFrame({
    "Pays": ["Kenya", "Madagascar", "Inde", "USA"],
    "Région": ["Sud", "Sud", "Sud", "Nord"],
    "Salaire_heure": [1.75, 1.0, 2.0, 20.0],
    "Type_tache": ["annotation", "annotation simple", "modération", "annotation"]
})

st.subheader("Simulation du cout des annotations")

nb_max = st.slider( "Nombre maximum d'annotations à simuler",1, 500000, 1, step= 99)

simul = []
nb_annot = np.linspace(0, nb_max, max(5, nb_max//10000))

minutes = nb_annot
heures = minutes / 60

for i, row in data2.iterrows():
    salaire = row["Salaire_heure"]
    cout = salaire * heures
    simul.append(pd.DataFrame({"Pays" : row["Pays"], "Nb_annotations": nb_annot,"Cout_total": cout}))
    

df_simul = pd.concat(simul)

graph = px.line(df_simul, x="Nb_annotations", y="Cout_total", color="Pays", title="Coût total en fonction du nombre d'annotations")
st.plotly_chart(graph)

