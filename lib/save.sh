#!/bin/bash
aws s3 cp data/URLS.p s3://"$BUCKET_NAME"
aws s3 cp data/NAMES_"$PERCENT".p  s3://"$BUCKET_NAME"
aws s3 cp data/nat2018.csv s3://"$BUCKET_NAME"
