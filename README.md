# **Streamlit Mine Table**

This is a Project is an interactive, multi-page Streamlit dashboard designed to simplify the entire data preprocessing workflow from uploading raw datasets to cleaning, visualizing, and exporting refined data.

# Table of Contents
1. [Go to Uploading](#uploading)
2. [Go to Preprocessing](#preprocessing)
3. [Go to Visualization](#visualization)
4. [Go to Export](#export)


## Uploading 
<img width="1756" height="933" alt="image" src="https://github.com/user-attachments/assets/faf6a35b-4314-4294-b486-e22e1d36130d" />
It's an entry point to start interaction with dashboard, well it contains a dummy data file and you can upload your own file of csv or excel format with size limit of 200MB

## Preprocessing 
<img width="1738" height="868" alt="image" src="https://github.com/user-attachments/assets/bc5b9e2a-5c94-4d41-8a9a-a81e0635c083" />
Here we focuses on cleaning and preparing data before analysis.It includes :

- **Column Renaming**: Select an existing column and provide a new name to that column
- **Droping Column**: Select any column which you find not useful or noisy, remove it completely from the entire dataset.
- **Handling Missing Values**: Missing values inside the numeric columns are handled with these available methods :
    - Fill with mean
    - Fill with median
    - Drop rows containing missing values
    - Fill with a custom value
It prevents errors in analysis and model training.

## Visualization 
<img width="1707" height="893" alt="image" src="https://github.com/user-attachments/assets/193ec81c-1c91-411a-a18b-e6bd900040cb" />
Here we can see the insights of the data after processing, here we can see the Column Statistics, Data Distribution, Missing and Duplicate values.
It improves dataset reliability.

## Export 
<img width="1736" height="670" alt="image" src="https://github.com/user-attachments/assets/8ff23030-b42d-417c-a47c-88721d60f305" />
Now we can download our dataset in CSV or Excel format, with customized name of the output file
