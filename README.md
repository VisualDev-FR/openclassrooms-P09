
# Openclassrooms P09 - Développez une application Web en utilisant Django

Cette application permet de demander ou publier des critiques de livres ou d’articles.

L’application présente deux cas d’utilisation principaux : 

1. Les personnes qui demandent des critiques sur un livre ou sur un article particulier ;
2. Les personnes qui recherchent des articles et des livres intéressants à lire, en se basant sur les critiques des autres.

Une base de donnée ```db.sqlite3``` est incluse au dépôt et contient des données générées aléatoirement pour 

### Configuration de l'environnement virtuel :

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont repertoriés dans le fichier ```requirements.txt```

Pour configuer l'environnement, commencez par ouvrir un terminal à la racine du projet, et suivez les étapes suivantes :

1. Créez un environnement virtuel à partir de la commande suivante : 
```bash
python -m venv env
```

2. Activez l'environnement virtuel que vous venez de créer avec la commande suivante :

```bash
env/Scripts/activate
```

3. Installez les packages python spécifiés dans le fichier ```requirement.txt``` :

```bash
pip install -r requirement.txt
```
### Démarrage 

Sur windows, lancer le script ```runserver.bat``` et passez directement à l'étape 4, sinon suivez les étapes suivantes :

1. Activez l'environnement virtuel en vous référant à la section précédante. 

2. Ouvrez un terminal à la racine du projet, et entrez la commande suivante :

```bash
python ./LITReview/manage.py runserver
```

3. Cliquez sur [ce lien](http://127.0.0.1:8000/feed/) pour accéder à la page de connexion de l'application

4. Inscrivez-vous en vous rendant sur la page d'inscription (ou connectez-vous avec un compte existant)

5. Connectez-vous en vous rendant sur la page de connexion et entrant vos identifiants. 

Pour vous connecter avec un compte existant en base de donnée, choisissez un identifiant dans le fichier suivant : ``` /LITReview/scripts/dummy_usernames.txt ```, et connectez vous avec le mot de passe par défaut : ```dummypassword```

### Rapport flake8

Le dépôt contient un rapport flake8, qui n'affiche aucune violation des règles PEP8. 

Il est possible d'en générer un nouveau en activant l'environnement virtuel (voir procédure ci-dessus) et en entrant la commande suivante dans le terminal :

```bash
flake8 ./LITReview/ --format=html --htmldir=flake-report
```

Le fichier ```setup.cfg``` à la racine contient les paramètres concernant la génération du rapport.

Le rapport se trouve dans le repertoire ```flake-report```

### Génération de données

Pour générer un nouvel ensemble de données aléatoires, suivez les étapes suivantes :

1. Fermez la base de donnée si elle est ouverte, et eteignez le serveur s'il est en cours. 

2. Activez l'environnement virtuel en vous référant à la section dédiée plus haut.

3. Ouvrez un terminal à la racine du projet, et entrez la commande suivante :

```bash
python -W ignore ./LITReview/manage.py runscript dummy_data
```

Le script ```dummy_data.py``` contient un ensemble d'instructions qui va :

1. Supprimer tous les tickets / les critiques / les abonnements de la base de données
2. Générer un nouvel ensemble de tickets / critiques / abonnements pour chaque utilisateurs

