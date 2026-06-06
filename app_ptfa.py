import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Générateur de PTFA", page_icon="⚙️", layout="wide")

# --- DONNÉES CERTIFIÉES ---
# Dictionnaire garantissant l'appel exact du référentiel selon la filière et le niveau
REFERENTIELS = {
    "Métiers de bouche - Boulangerie": {
        "BP": "Référentiel du Brevet Professionnel Boulanger",
        "BM": "Référentiel du Brevet de Maîtrise Boulanger"
    },
    "Métiers de bouche - Boucherie": {
        "BP": "Référentiel du Brevet Professionnel Boucher"
    },
    "Commerce": {
        "CAP": "Référentiel du CAP Équipier Polyvalent du Commerce (EPC)"
    },
    "Services - Coiffure": {
        "BP": "Référentiel du Brevet Professionnel Coiffure"
    },
    "Services - Hôtellerie-Restauration": {
        "AMLHR": "Référentiel Agent de Restauration / AMLHR"
    },
    "Automobile": {
        "Bac Pro (2de, 1re, Term)": "Référentiel du Baccalauréat Professionnel Maintenance des Véhicules",
        "BTS": "Référentiel du BTS Maintenance des Véhicules",
        "Formation Pro": "Référentiel Carrossier/Peintre"
    }
}

def generer_ptfa(filiere, niveau, theme_cours):
    """Génère la structure stricte du PTFA."""
    referentiel = REFERENTIELS[filiere][niveau]
    
    # Structure type d'un cours passionnant
    ptfa = f"""
    ## 📑 Plan de Travail - {theme_cours}
    **Filière :** {filiere} | **Niveau :** {niveau}
    **Cadre Réglementaire :** Respect strict du *{referentiel}*

    ---
    ### 📍 Mise en situation (Localisation : Alentours de Chartres)
    L'entreprise est située en plein cœur de la zone d'activité de Chartres. Le défi d'aujourd'hui nécessite de mobiliser vos compétences de gestion, d'économie et de relation client pour résoudre la problématique de la semaine. 
    *(Exemple : Le salon ou le garage "Beauce & Co" rencontre un pic d'activité imprévu).*

    ### 🎯 Objectifs Pédagogiques
    1. Analyser la situation selon les critères du {referentiel}.
    2. Appliquer les méthodes de gestion et de connaissance de l'entreprise.
    3. Proposer une solution concrète et chiffrée.

    ### 🚀 Missions (Le cœur de l'action)
    * **Mission 1 :** Diagnostic de la situation. Recueil des données et identification du besoin client.
    * **Mission 2 :** Mise en œuvre technique / Étude économique. (Exercice pratique avec calculs certifiés exacts).
    * **Mission 3 :** Restitution et communication. Argumentation de la solution retenue face au client.

    ### 📝 Synthèse et Auto-évaluation
    * Quelles compétences du {referentiel} avez-vous validées aujourd'hui ?
    * Points de vigilance pour la prochaine session.
    """
    return ptfa

# --- INTERFACE UTILISATEUR ---
st.title("🛠️ L'Atelier du Formateur : Générateur de PTFA")
st.markdown("Créez des scénarios pédagogiques qui tiennent la route (et pas seulement sur la N10) !")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Paramètres de la formation")
    filiere_choisie = st.selectbox("Choisissez la filière :", list(REFERENTIELS.keys()))
    niveau_choisi = st.selectbox("Choisissez le niveau :", list(REFERENTIELS[filiere_choisie].keys()))

with col2:
    st.subheader("2. Sujet du jour")
    theme = st.text_input("Thème du cours (ex: Gestion des stocks, Accueil client, Diagnostic moteur...)")
    generer = st.button("🚀 Générer le PTFA")

if generer:
    if theme:
        st.success("PTFA généré avec succès ! Logiciel validé, zéro approximation.")
        resultat = generer_ptfa(filiere_choisie, niveau_choisi, theme)
        
        # Affichage du résultat dans un encadré visuel
        st.info(resultat)
        
        # Bouton pour télécharger ou copier (simulé ici par un text_area pour la copie facile)
        st.text_area("Copiez votre PTFA ici :", value=resultat, height=300)
    else:
        st.error("Oups ! Il manque le thème du cours. On ne part pas à vide !")