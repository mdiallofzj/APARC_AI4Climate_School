# Practical on Causal Inference for the SPARC training school "Climate Data Analysis and Artificial Intelligence in the Global South" 29-31 October 2023, University of Rwanda - College of Science and Technology, Kigali, Rwanda.


*Modified* worked examples to the scenarios described in the paper Kretschmer et al., Quantifying Teleconnection pathways using Causal Networks (2021). 
Originally developed for the MPE CDT summer school 2022 (University of Reading) 


Example notebooks:
- Example 1 - [Common Drivers](notebooks-summerschool/example1_common_drivers_csv.ipynb)
- Example 2 - [Mediators](notebooks-summerschool/example2_mediators_csv.ipynb)
- Example 3 - [Direct and Indirect Pathways](notebooks-summerschool/example3_indirect_path_csv.ipynb)
- Example 4 - [Blocking the right paths](notebooks-summerschool/example4_blocking_paths_csv.ipynb)
- Example 5 - [Non-linear example](notebooks-summerschool/example5_nonlinear_csv.ipynb)

Data sources:
The [sample data](sample_data_csv) used in these notebooks has been derived from:
[NOAA Climate Indices](https://psl.noaa.gov/data/climateindices/list/)
[NOAA NCEP Reanalyses](https://psl.noaa.gov/cgi-bin/db_search/SearchMenus.pl)


How to run the code: 

######### If using Google Colab (need a google account)

1. Copy the folder causality-master-SPARCtrainingschool/ to YOUR Google Drive

2. Save the data folder sample_data_csv/ to your local machine (e.g. in your Desktop): this is needed to be able to upload the data for the exercise. 

3. In your Google Drive, browse to the folder causality-master-SPARCtrainingschool/notebooks-summerschool/ and select the file you want to start from (e.g. example1_common_drivers_csv.ipynb). By clicking on the file, you should be able to open it via Google Collaboratory directly. If this does not happen, please follow the steps at https://www.freecodecamp.org/news/google-colaboratory-python-code-in-your-google-drive/. 

4. Among the first lines fo code you find : 
from google.colab import files
uploaded = files.upload()

Running these lines opens an interactive session where you are asked to upload the files you want to use. You will select the appropriate files in your local folder sample_data_csv/ you have just downloaded to your drive.

5. You are all set! just keep going through the code and do the exercises :) 


####### If using Jupiter notebook (if you do not have a Google account)

1. Download the folder causality-master-summerschool/ to your local machine (e.g. in Desktop)

2. Open Jupyter Notebook on your machine

3. Open the file you want to start from in causality-master-summerschool/notebooks-summerschool/.

4. Comment out (or do not run) the lines of code needed for Google Colab 
from google.colab import files
uploaded = files.upload()
Instead, load the files needed for the exercise from you local folder causality-master-summerschool/sample_data_csv/

5. You are all set! just keep going through the code and do the exercises :) 


