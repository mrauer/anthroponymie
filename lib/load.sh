#!/bin/bash

# Source: https://www.insee.fr/fr/statistiques/fichier/2540004/nat2018_csv.zip
# Copy data from S3
aws s3 cp s3://"$BUCKET_NAME"/NAMES_"$PERCENT".p data/
aws s3 cp s3://"$BUCKET_NAME"/URLS.p data/
aws s3 cp s3://"$BUCKET_NAME"/nat2018.csv data/
