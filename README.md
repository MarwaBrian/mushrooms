# Mycological Risk Assessment - Machine Learning Approach
![Mushroom Species ](https://github.com/MarwaBrian/mushrooms/blob/main/mushroooms.png)


## Problem statement
Mycologists face the daunting challenge of quickly and accurately distinguishing edible mushrooms from poisonous mushrooms based on their physical attributes. To address this, the project aims to develop a robust machine learning model using the Mushroom dataset. This model seeks to provide mycologists with a reliable tool for on-the-spot mushroom classification during fieldwork, significantly reducing the risks associated with misidentification and enhancing safety measures for both researchers and the general populace.

## PROJECT OVERVIEW 
The project's focus is to train a machine learning model capable of accurately classifying mushrooms as edible or poisonous by analysing their physical characteristics. The model is designed to assist teams of mycologists in conducting risk assessments associated with fungal species.


## BUSINESS UNDERSTANDING
This project aims to employ machine learning algorithms on the Mushroom dataset, which comprises diverse physical attributes of mushrooms. By leveraging these attributes such as cap shape, odor, and gill size, the goal is to develop a robust model for accurate classification between edible and poisonous mushrooms. This model could significantly improve the efficiency and safety of mushroom identification processes for mycologists and enthusiasts.

## Components

* **Jupyter Notebook**
The [Jupyter Notebook](https://github.com/MarwaBrian/mushrooms/blob/main/index.ipynb) is my key deliverable and contains details of the approach, methodology, data cleaning, exploratory data analysis, pipelines, model building and validation used.

I recommend using [nbviewer](https://nbviewer.jupyter.org/) to view the Jupyter Notebook.

* **Presentation**
The [presentation](https://) gives a high-level overview of our approach, findings and recommendations for non-technical stakeholders. It is aimed to be between 5 and 10 minutes long.

* **Data**

The dataset can be found in the file *"secondary_data.csv"* in the Data folder, in this repository. It was originally provided in the following [repository](https://github.com/MarwaBrian/mushrooms/blob/main/dataset/secondary_data.csv). 

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

## 1. Data Understanding
Here I loaded the data and got a brief introduction to the columns I was working with.

## 2. Exploratory Data Analysis (EDA)
Here we will explore the different features of the dataset to gain a better understanding of the data. We will use data vizualization to uncover trends and patterns. We will use Feature Engineering to create new features from existing ones and perform One-Hot Encoding on categorical variables that we will require for analysis.

Most houses are priced around a half million to a million dollars,
while the most expensive houses imply the order of two million dollars and more

**Overview of mushroom features**
- Categorical features include `class`, `cap-shape`, `cap-surface`, `cap-color`, `does-bruise-or-bleed`, `gill-attachment`, `gill-spacing`, `gill-color`, `stem-root`, `stem-surface`, `stem-color`, `veil-type`, `veil-color`, `has-ring`, `ring-type`, `spore-print-color`, `habitat`, `season` 
- Numerical variables include `cap-diameter`, `stem-height`, `stem-width`.


## 3. Data Preprocessing & Pipeline Setup
Here I worked on data cleaning, handled missing values, data transformation, handled duplicates, data reshaping and other processes to ensure that I have a clean, structured, and suitable format for analysis and modeling.

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








