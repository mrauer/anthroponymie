# Anthroponymie

## Introduction

L’objectif d'anthroponymie est de mesurer l'évolution culturelle d’un pays à travers l’origine des prénoms donnés lors des naissances. Il est relativement difficile de déterminer l’origine d’un prénom avec certitude, mais nous avons créé une méthodologie qui semble porter ses fruits et donne un aperçu de la situation d'évolution récente.

## Méthodologie

L’Insee (Institut national de la statistique et des études économiques) met à disposition de tous un fichier nommé [Fichier des prénoms](https://www.insee.fr/fr/statistiques/2540004). Celui-ci couvre l'intégralité des prénoms donnés aux nouveaux français entre 1900 et 2018 . Nous disposons par année du prénom, du sexe et du nombre de fois celui-ci a été donné.

L'idée initiale est d’ajouter deux dimensions supplémentaires "Pays d’origine" ainsi qu’un groupe que nous appellerons tout au long de l'étude "Cluster culturel". Par exemple, en tant que personne, nous pouvons facilement déterminer que "Jean" est un prénom français, et "Matteo" un prénom italien, les deux étant des prénoms culturellement proches (latin). Néanmoins, est-il possible pour une machine de déterminer l’origine d’un prénom?

Pour obtenir l’origine d’un prénom, nous avons fait appel à Wikipedia. En collectant tous les personnages illustres portant le même prénom, et en utilisant le pays de naissance de ceux-ci comme un marqueur, nous avons obtenu des données semblant refléter la réalité (pour la machine, il y a une majorité de "Jean" illustres né en France, et une majorité de "Matteo" illustres né en Italie).

## Visualisation

Voici les résultats de l'étude en utilisant l'integralité des prénoms. Nous pouvons observer, qu'à partir des années 1960, la diversité des prénoms en France a fortement augmenté. La part des clusters "UNKNOWN" (non classifiés) et de plus de 20% en 2015, ce qui signifie qu’il est nécessaire de catégoriser plus de prénoms pour minimiser cet effet. Nous observons que plus de 10% des prénoms en France dans les années 20xx appartiennent au groupe culturel "ANGLO". Le groupe "LATIN-EUROPE" est passé de 762.455 naissances en 1955 à 313.181 en 2018:

![Proportion des naissances en France par Cluster Culturel](/data/chart.jpg "Proportion des naissances en France par Cluster Culturel")

## Clusters culturels

Comme vous pouvez aisément l’imaginer, il existe certain prénoms dont l’origine est difficile à déterminer. Prenez par exemple un nom anglais tel que “Brandon”. Celui-ci sera répartie dans un nombre important de pays. Néanmoins, ces pays ont en général en commun une proximité culturelle (Canada, Royaume-Uni, Etats-Unis, etc…). On peut imaginer, que la culture mexicaine est plus proche de la culture colombienne que de la culture chinoise. Il se trouve qu’il y a eu quelques études à ce sujet, et nous avons utilisé les données du lien suivant pour créer nos groupes culturels et avoir un meilleur aperçu de l'évolution de la culture du pays. [Clusters Culturels](https://growthorientedsustainableentrepreneurship.files.wordpress.com/2016/07/gl-cultural-clusters-methodology-and-findings.pdf)

## Collection des données

Le fichier initial contient 33.484 prénoms distincts.

Cette version d'anthroponymie couvre 100% de la population (35.606 prénoms avec doublons H/F), soit 83.564.357 de personnes.

Pour démarrer le projet, lancez la commande:

```sh
make run
```

Voici les commandes disponibles:

```sh
make cut cutoff=0.85    (créer un sous-groupe du fichier initial)
make urls cutoff=0.85   (collecte des liens Wikipedia par prénom)
make countries          (ajoute la dimension pays)
make show               (vue des données collectées)
make stats              (ajout des clusters culturels)
make agg                (créer le fichier à la base de la visualisation)
```

## Configuration

Si vous souhaitez collecter des données additionnelles ou recommencer le processus de A à Z (car les sources changent effectivement en permanence) il vous faut au préalable un fichier de configuration à la base du project.

Celui-ci doit se nommer `.env`, et voici son contenu:

```sh
AWS_ACCESS_KEY_ID=AKIAU***************
AWS_SECRET_ACCESS_KEY=fkmHxhFg8ob*****************************
BUCKET_NAME=anthroponymie
PERCENT=1
```

Nous utilisons Amazon S3 pour le stockage des fichiers, mais toute innovation est la bienvenue.

## Contribution

Le projet est sous license MIT, il vous est donc possible de contribuer.

Voici les commandes nécessaires pour lancer une machine virtuelle (Il vous faut au préalable Docker):

```sh
make build (contruction de l'image)
make run (utilisation de l'image)
```

### Ajouts manuels
Etant donné l’existence de pays fort représentés dans les données, mais non classifiés en tant que cluster culturel, nous avons grossièrement ajouté certains pays manuellement. La classification suivante n’engage que l’auteur:

* Algeria DZ -> `ARAB`
* Belgium BE -> `LATIN-EUROPE`
* Cameroon CM -> `SUB-SAHARA AFRICA`
* Côte d'Ivoire CI -> `SUB-SAHARA AFRICA`
* Lebanon LB -> `ARAB`
* Norway NO -> `NORDIC-EUROPE`
* Tunisia TN -> `ARAB`
* Romania RO -> `LATIN-EUROPE`
* Czechia CZ -> `EASTERN-EUROPE`
* Ukraine UA -> `EASTERN-EUROPE`
* Chile CL -> `LATIN-AMERICA`
* Senegal SN -> `SUB-SAHARA AFRICA`
* Bulgaria BG -> `EASTERN-EUROPE`
* Croatia HR -> `EASTERN-EUROPE`
* Serbia RS ->  `EASTERN-EUROPE`
* Cuba CU -> `LATIN-AMERICA`
* Mali ML -> `ARAB`
* Syria SY ->  `ARAB`
* Burkina Faso BF -> `ARAB`
* Irak IQ -> `ARAB`
* Pakistan PK -> `ARAB`
* Congo CD -> `SUB-SAHARA AFRICA`
* Vietnam VN -> `CONFUCIAN-ASIA`
* Guinea GN -> `ARAB`
* Kenya KE -> `SUB-SAHARA AFRICA`
* Belarus BY -> `EASTERN-EUROPE`
* Slovakia SK -> `EASTERN-EUROPE`
* Uruguay UY -> `LATIN-AMERICA`
* Peru PE -> `LATIN-AMERICA`
* South Africa SA -> `ANGLO`
* Estonia EE -> `EASTERN-EUROPE`
