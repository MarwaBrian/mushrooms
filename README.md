# House Price Forecasting with Regression Modeling

![King County, Washington](https://github.com/Wairimukimm/dsc-phase-2-project-v2-3/blob/tweaks/king_county.webp)


## Problem statement
Real estate developers encounter difficulties when assessing the precise influence of individual metrics and attributes on house pricing within the KC housing dataset. Their primary concern is the degree to which these factors interact to affect pricing outcomes. The current lack of clarity in pricing decisions can result in instances of both overpricing and underpricing of properties. And to address this issue, we aim to develop a more comprehensive understanding of the dataset's variables, enabling them to make more accurate pricing decisions based on a combination of factors.

## PROJECT OVERVIEW 
The project focuses on the creation of a machine-learning project for house-price forecasting for investors to owners to buyers.

## BUSINESS UNDERSTANDING
House price forecasting is a crucial task in the real estate industry. Accurate predictions assist homebuyers, sellers, and investors in making informed decisions regarding property transactions.

## Components

* **Jupyter Notebook**
The [Jupyter Notebook](https://github.com/Wairimukimm/dsc-phase-2-project-v2-3/blob/main/student.ipynb) is our key deliverable and contains details of the approach and methodology, data cleaning, exploratory data analysis, pipelines, model building and validation.

I recommend using [nbviewer](https://nbviewer.jupyter.org/) to view the Jupyter Notebook.

* **Presentation**
The [presentation](https://) gives a high-level overview of our approach, findings and recommendations for non-technical stakeholders. It is aimed to be between 5 and 10 minutes long.

* **Data**

The dataset can be found in the file *"kc_house_data.csv"* in the Data folder, in this repository. It was originally provided in the following [repository](https://github.com/Wairimukimm/dsc-phase-2-project-v2-3/blob/main/data/kc_house_data.csv). 

## Technologies/ Packages

* Python version: 3.6.9
* Matplotlib version: 3.1.3
* Seaborn version: 0.9.0
* Pandas version: 0.25.1
* Numpy version: 1.16.5
* Statsmodels version: 0.10.1
* Scikit-learn version: 0.21.2  

## To get started

1. Clone this repository - [guidance](https://help.github.com/articles/cloning-a-repository/).
2. Dataset can be found in the file "secondary_data.csv".
3. Check requirements in Technologies section above and download libraries if necessary.

## 1. Data Wrangling
Here I will work on data cleaning, handling missing values, data transformation, handling duplicates, data reshaping and other processes to ensure that I have a clean, structured, and suitable format for analysis and modeling.

## 2. Exploratory Data Analysis (EDA)
Here we will explore the different features of the dataset to gain a better understanding of the data. We will use data vizualization to uncover trends and patterns. We will use Feature Engineering to create new features from existing ones and perform One-Hot Encoding on categorical variables that we will require for analysis.

Most houses are priced around a half million to a million dollars,
while the most expensive houses imply the order of two million dollars and more

**Overview of house features**
- Categorical features of the house include `id`, `date`, `bedrooms`, `floors`, `waterfront`, `view`, `grade`, `year_built`, `yr_renovetd`, `zipcode`, `lat`, `long`.
- Numerical variables include `price`, `sqft_living`, ``.
- it is can be noticed that as `bedrooms` increase, so does the house's selling price
- more `floors`, preferably up to 2.5 have a higher price  

## 3. Base Model
### Logistic Regression Model

After completing the data preprocessing steps involving feature scaling, one-hot encoding of categorical variables, and handling class imbalance using SMOTE, the dataset is now ready for model implementation.

- Accuracy: 0.8636
- Precision: 0.8899627121223651
- Recall: 0.8611929307805597
- F1-score: 0.8753414917106396


## 4. Advance Models
### Naive Bayes
- Accuracy: 0.6225
-             precision    recall  f1-score   support

           0       0.76      0.22      0.34     10848
           1       0.60      0.95      0.74     13580

    accuracy                           0.62     24428
   macro avg       0.68      0.58      0.54     24428
weighted avg       0.67      0.62      0.56     24428


### Random Forest
- Accuracy: 1.0000
-               precision    recall  f1-score   support

           0       1.00      1.00      1.00     10848
           1       1.00      1.00      1.00     13580

    accuracy                           1.00     24428
   macro avg       1.00      1.00      1.00     24428
weighted avg       1.00      1.00      1.00     24428



## Conclusions
In conclusion, while logistic regression and naive bayes showcased reasonable performances, the random forest model delivered exceptional results, demonstrating a superior ability to distinguish between edible and poisonous mushrooms in this dataset.


## Contributor:
|Name     |  GitHub   |
|Brian Chacha |https://github.com/MarwaBrian|








