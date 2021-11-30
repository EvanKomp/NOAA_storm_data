# NOAA_storm_data
Pull and extract NOAA storm data fro the purposes of the C-HACK tutorial

# Steps
1. Install and activate the environment `conda env create --file environment.yml`
2. Execute the script to get raw data for 2008 and 2015 `bash get_raw.sh` 
3. Execute the cleaning script to get the data down to only the important info `python clean.py`
