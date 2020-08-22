# Anthroponymie

## Introduction

L’objectif d'anthroponymie est de mesurer l'évolution culturelle d’un pays par l’origine des prénoms donnés lors des naissances. Il est relativement difficile de déterminer l’origine d’un prénom avec certitude mais nous avons créé une méthodologie qui semble porter ses fruits et donne un aperçu de la situation d'évolution récente.

## Méthodologie

L’Insee (Institut national de la statistique et des études économiques) met à disposition de tous un fichier nommé [Fichier des prénoms](https://www.insee.fr/fr/statistiques/2540004). Celui-ci couvre l'intégralité des prénoms donnés aux nouveaux français entre 1900 et 2018 . Nous disposons par année du prénom, du sexe, et du nombre de fois celui-ci a été donné.

L'idée initiale est d’ajouter une colonne supplémentaire "Pays d’origine" ainsi qu’un groupe que nous appellerons tout au long de l'étude un "cluster culturel". Par exemple, en tant que personne, nous pouvons facilement déterminer que "Jean" est un prénom français, et "Matteo" un prénom italien, les deux étant des prénoms culturellement proches (latin). Néanmoins, est-il possible pour une machine de déterminer l’origine d’un prénom?

Pour obtenir l’origine d’un prénom, nous avons fait appel à Wikipedia. En collectant tous les personnages illustres portant le même prénom, et en utilisant le pays de naissance de ceux-ci comme un marqueur, nous avons obtenu des données semblant refléter la réalité (Pour la machine, il y a une majorité de "Jean" illustres né en France, et une majorité de "Matteo" illustre né en Italie).

## Collection des données

Lorem Ipsum
* Each first name is a unique set. (33,484 distincts).
* Get a subset of first name based on cutoff. (ex: 85% of population).
* Process one letter at the time. (ex: M).
* Create pickled dict in data/, empty when initiated (M_85.dat).
* Store URLs in Mongo, and proceed one at the time to extract birthplace.
* Ex: {"laurent":{"france":81, "spain":2, "switzerland":23}}
* Store and zip?
* 85% coverage to start (780 names)

## Visualisation

Voici les résultats de l'étude en utilisant 780 prénoms. Nous pouvons observer, qu'à partir des années 1960, la diversité des prénoms en France a fortement augmenté. La part des clusters "UNKNOWN" (non-classifiés) et de plus de 50% en 2015, ce qui signifie qu’il est nécessaire de catégoriser plus de prénoms pour minimiser cet effet. Nous observons que plus de 10% des prenoms en France dans les années 20xx appartiennent au groupe culturel "ANGLO":

![Proportion des naissances en France par Cluster Culturel](/data/chart.png "Proportion des naissances en France par Cluster Culturel")

## Clusters culturels

Comme vous pouvez aisément l’imaginer, il existe certain prénoms dont l’origine est difficile à déterminer. Prenez par exemple un nom anglais tel que “Brandon”. Celui-ci sera répartie dans un nombre important de pays. Il se trouve, qu’en général ces pays ont en commun un proximite culturelle (Canada, Royaume-Uni, Etats-Unis, etc…). On peut imaginer, que la culture Mexicaine est plus proche de la culture Colombienne que de la culture Chinoise. Il se trouve qu’il y a eu quelques études a ce sujet, et nous avons utilisé les données du lien suivant pour créer nos groupes culturels et avoir un meilleur aperçu de l'évolution de la culture du pays. [Clusters Culturels](https://growthorientedsustainableentrepreneurship.files.wordpress.com/2016/07/gl-cultural-clusters-methodology-and-findings.pdf)

### Ajouts manuels
Etant donné l’existence de pays fort représenté dans les données, mais non classifiés en tant que cluster culturel, nous avons grossièrement ajouté certain pays manuellement. La classification n’engage que l’auteur:

* Tunisia TN -> `ARAB`
* Algeria DZ -> `ARAB`
* Cameroon CM -> `SUB-SAHARA AFRICA`
* Belgium BE -> `LATIN-EUROPE`
* Côte d'Ivoire CI -> `SUB-SAHARA AFRICA`
* Lebanon LB -> `ARAB`
* Norway NO -> `NORDIC-EUROPE`
