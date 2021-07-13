# Food Insecurity in the US

## Predicting Food Insecurity for Participants of the Current Population Survey

### Summary
One of the hardest things to do in life is to ask for help. Too many families in the United States are struggling with food insecurity. This Current Population Survey asked US households numerous questions that may or may not be related to food insecurity, as well as directly if they were facing insecurity. I will use a model to predict insecurity based on responses to the other questions. If I can make a model that is accurate, I may be able to expand the model to predict which households are in-fact struggling with insecurity but are not able to or are unwilling to admit that they do need some help. With these results, we could try to reach out to these struggling families in a different way to ensure they still receive the help that they need.

### Contents
1. Reading in and Cleaning Data
2. Exploratory Data Analysis 
3. Model and Error Metric Selection
4. Model Training
5. Results and Conclusion
6. Sources

### 1. Reading in and Cleaning Data

CSV Format, 138964 Entries x 510 Features

Target
HRFS12M1  
Summary Food Security Status, 12-Month Recall (Recode of HRFS12M4)  
EDITED UNIVERSE:  
HRSUPINT=1  

VALID ENTRIES:  
1 Food Secure High or Marginal Food Security  
2 Low Food Security  
3 Very Low Food Security 
-1 Not in Universe (Didn't participate in survey)
-9 No Response 

HRFS12M1  
1    73120  
-1    57142  
2     5648  
3     2859  
-9      195  
Name: HRFS12M1, dtype: int64  

### 2. Exploratory Data Analysis 

### 3. Model and Error Metric Selection

### 4. Model Training

### 5. Results and Conclusion

### 6. Sources

Data Source(s):
US Census Bureau
https://www.census.gov/data/datasets/2019/demo/cps/cps-food-security.html
