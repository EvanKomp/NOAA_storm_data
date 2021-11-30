#!/bin/bash

# Download the 1980 and 2018 data
mkdir data
cd data
curl -O https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d2018_c20211120.csv.gz
curl -O https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d2005_c20210803.csv.gz

gzip -d StormEvents_details-ftp_v1.0_d2018_c20211120.csv.gz
gzip -d StormEvents_details-ftp_v1.0_d2005_c20210803.csv.gz