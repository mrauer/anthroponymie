#!/bin/bash
source="data/nat2018_csv.zip"
if ! [ -f data/nat2018.csv ]; then
  echo "Downloading source file"
  curl --output $source https://www.insee.fr/fr/statistiques/fichier/2540004/nat2018_csv.zip
  unzip $source -d data/ && rm $source
  echo "Source file downloaded"
fi
