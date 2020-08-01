# Anthroponymie

## Introduction

Lorem Ipsum

## Méthodologie

* La première étape consiste au téléchargement et à la décompression du “fichier des prénoms” de l’Insee [Insee](https://www.insee.fr/fr/statistiques/2540004) (nat2018.csv)

## Information

Lorem Ipsum

## Visualisation

Lorem Ipsum

* Each first name is a unique set. (33,484 distincts).
* Get a subset of first name based on cutoff. (ex: 85% of population).
* Process one letter at the time. (ex: M).
* Create pickled dict in data/, empty when initiated (M_85.dat).
* Store URLs in Mongo, and proceed one at the time to extract birthplace.
* Ex: {"laurent":{"france":81, "spain":2, "switzerland":23}}
* Store and zip?
* 85% coverage to start (780 names)

* 70560072
* 85119428
* 82.89%

## Clusters culturels

* [Clusters](https://growthorientedsustainableentrepreneurship.files.wordpress.com/2016/07/gl-cultural-clusters-methodology-and-findings.pdf)

### Ajouts manuels
* Tunisia TN -> `ARAB`
* Algeria DZ -> `ARAB`
* Cameroon CM -> `SUB-SAHARA AFRICA`
* Belgium BE -> `LATIN-EUROPE`
* Côte d'Ivoire CI -> `SUB-SAHARA AFRICA`
* Lebanon LB -> `ARAB`
* Norway NO -> `NORDIC-EUROPE`
