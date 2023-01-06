# streamlit-fastapi-model-serving-mlops-projet2



### Deployment



### Debugging

# ------------ aide installation fred ----------------------- #

# sur un navigateur
1 - aller sur le github de la demoiselle = https://github.com/RihabFekii/streamlit-app
2 - m'indentifier sur github
3 - cliquer sur "fork" ( en haut-droite ) du github demoiselle étant sur son REPO global
    => cela clone la totalité de son REPO sur mon github perso

# sur mon IDE VSC en local
1 - création d'un dossier de travail "streamlit_github_perso"
2 - se placer sur ce dossier => streamlit_github_perso$
3 - $ git init  # pour initialiser git sur ce dossier  ( pas sur que c'est utile car git déjà présent)
4 - $ git clone https://github.com/Fred-Zang/streamlit-app.git  # cloner mon new REPO en local VSC
    => cela va créer les dossier : backend (+dockerfile...) + frontend ( +dockerfile...) + data-models + storage ( csv ) + docker-compose
    => et tous ces dossier dans un dossier de travail principal "streamlit-app"
    => donc il n'y avait pas besoin de créer un dossier de travail au départ

# création des images par dockerfile
1 - se placer sur fred07@PCwikHap:~/DataScientest_fred07/streamlit_github_perso/streamlit-app$
2 - créer tout d'abord le reseau AIservice avant de lancer le docker-compose    
    => $ docker network create AIservice (voir avec $ docker network ls   si pas déjà fait)
3 - lancer le docker-compose pour créer toutes les images ( frontend et backend etc ...)
    => docker-compose up -d --build
    => parfait en 4-5 minutes
    => sauf petit conseil en court de route :
    """ WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. 
    It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
    WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available.
    You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command. """

4 - si docker-compose -d --build déjà lancé alors plus besoin de build car images déjç faites
=> docker-compose -d           # suffisant ensuite

# voir l'API
1 - aller sur localhost:8000/docs
# voir le streamlit
1 - aller sur localhost:8501




