# NBA home player prediction

This repo contains the code for the NBA home player prediction project.

# how to run

1. clone the repo
2. install the dependencies using the requirements.txt file
3. open the jupyter notebook file and run the code

# This repo does not contain models
We ran into issues to while saving the models on GitHub, due to their size. 
```
remote: error: File models/lgbm_model_with_outcome.pkl is 132.13 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: File models/rf_model_modified_dataset.pkl is 1303.75 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: File models/rf_model_with_outcome.pkl is 1452.32 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: File models/lgbm_model_modified_dataset.pkl is 106.72 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
To https://github.com/Hannestly/NBA_prediction.git
```


# each notebook is labeled in the following format:

knn_03-19_dataset_with_outcome.ipynb     -KNN model with the dataset that has the outcome variable
knn_03-19_modified_dataset.ipynb         -KNN model with the modified dataset
lgbm_03-20_modified_dataset.ipynb        -LGBM model with the modified dataset
lgbm_03-20-dataset_with_outcome.ipynb    -LGBM model with the dataset that has the outcome variable
rf_03-19_dataset_with_outcome.ipynb      -Random Forest model with the dataset that has the outcome variable
rf_03-19_modified_dataset.ipynb          -Random Forest model with the modified dataset

# Evaluation outcomes
| **Model**     | **Acc.** | **F1-micro** | **F1-macro** | **F1-weighted** |
| ------------- | -------- | ------------ | ------------ | --------------- |
| Random Forest | 0.370    | 0.370        | 0.253        | 0.337           |
| KNN           | 0.273    | 0.273        | 0.162        | 0.238           |
| Light GBM     | 0.426    | 0.426        | 0.289        | 0.412           |

detailed individual model evaluations are recorded in the 'evaluations' folder
Additionally the aggregated evaluation data, as well as model parameters can be found in 'overall_evaluation.xlsx'
