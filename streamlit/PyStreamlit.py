
import streamlit as st

# --------------------définition des fonctions --------------------------#

# ---------  Fonction d'affichage ------------- #
def insert_img(img):
	col1,col2,col3 = st.columns(3)
	with col1:
		st.write(' ')
	with col2: 
		st.image(img)
	with col3:
		st.write(' ')

def insert_head(img1, img2):
	col1,col2,col3,col4,col5 = st.columns(5)
	with col1:
		st.image(img1)
	with col2: 
		st.write(' ')
	with col3:
		st.write(' ')
	with col4:
		st.write(' ')
	with col5:
		st.image(img2)
  
  
# ---------------------- créer 4 pages différentes sur notre streamlit --------------------------------------  #
# créer une liste de 4 noms des pages

pages = ["Le Projet en détails", "Dataviz du Projet", "Filtrages, Tokenisations, Lemmatisations et Vectorisations", "Modélisations à la demande","Conclusion et Remerciements"]
# pas besoin d'autant de pages ... => modélisation est le + important car demandé pour le projet
page = st.sidebar.radio("Aller vers", pages)

#------------------------------------------------------------------------------------------
# sépration des pages  
#------------------------------------------------------------------------------------------

if page ==pages[0]:  # sur la page 0 Introduction
	# affichage
    st.write("### Frontend Streamlit")
    insert_head('https://datascientest.fr/train/assets/logo_datascientest.png', "logo_SatisPy_Project.png")
	# il faudrait charger le logo de datascientest en png dans le dossier /data/ pour éviter une connexion @
	# il faudrait aussi que insert_head() puisse chercher les images sur /data/ 
	# => probleme de chemin car on est sur /streamlit/ grace au dockerfile
	
	# title du page
    st.markdown("<h1 style='text-align: center; color: white;'>SatisPy Projet</h1>", unsafe_allow_html=True)
    st.write("### Préambule :") # écrire du texte ( # = taille, ##, ###) ici le titre de la page
    st.write("Tout comme le rapport de projet, cette présentation Streamlit est destinée à tout public et ne comporte aucune ligne de code.😉​")
    st.write("### Rapide aperçu du Projet :")
    st.write("On nous a remis un dataset 'reviews_trust.csv' comportant 19.863 lignes et 11 colonnes qui correspond aux commentaires clients \
        et notation de 1 à 5 étoiles sur leurs achats de produit sur 2 sites marchands 'ShowRoom' et 'VeePee'. Ces commentaires proviennent de \
            2 sources récoltant les avis, 'TrustedShop' et 'TrustPilot' et voici un extrait du dataset :")	
    st.write("ZZZZZZZZZZZZZZZ")
 
 
