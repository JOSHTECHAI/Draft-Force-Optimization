<p align="center"><h2>DEVELOPMENT AND IMPLEMENTATION OF A MACHINE LEARNING MODEL FOR OPTIMIZATION OF DRAFT FORCE DEMANDS OF DISC PLOUGH FOR TILLAGE OPERATIONS IN FUNAAB</h2></p>

## Project Overview
The goal is to accurately predict draft force requirements based on various soil, operational, and environmental parameters and optimize tillage conditions for improved efficiency. The research follows a data-driven approach, machine learning modeling, and optimization techniques. 
## Objectives
* To characterize the operational parameters of disc ploughs in local conditions.
* To develop a dataset for machine learning applications.
* To develop and compare different machine learning model for draft force predictions.
* To identify the best performing model and integrate it with an optimization algorithm.
* To develop a user-friendly interface for practical implementation in agricultural settings.
## Data Collection
A synthetic dataset was generated using computational models and simulation techniques. This approach involves creating data that mimics real-world conditions based on established physical, mathematical, and empirical relationships governing the draft force dynamics in tillage operations. It encompasses a range of variables that are critical for modeling the draft force demands of a disc plough during tillage operations. Synthetic data can be generated for a wide range of operating conditions, including extreme or rare scenarios that might be difficult or unsafe to replicate in field experiments. Synthetic data allow researchers can precisely control the input parameters, allowing for systematic investigations of individual variable effects on draft force. Generating synthetic data reduces the need for extensive field trials, saving both time and resources during the initial stages of model development.
## Description of Dataset
* Soil Moisture Content (%)
  * Effect: Inverse Relationship (up to an optimum level).
  * Explanation: Higher soil moisture reduces soil cohesion and shear strength, making plowing easier, thus lowering draft force. However, excess moisture (>30-40%) can increase draft force due to soil sticking to the plough.
  * Trend: Moderate moisture decrease draft force, excessive moisture increase draft force.
* Bulk Density (g/cm³)
  * Effect: Direct Relationship
  * Explanation: Higher bulk density means more compact soil, which requires more force to break. Dense soils have higher resistance to penetration, increasing draft force demands.
  * Trend: Increase in Bulk Density increases Draft Force.
* Soil Texture and Composition
  * Effect: Varied Relationship (Depends on Soil Type)
  * Explanation: 
    * Sandy soils → Low draft force (low cohesion and shear strength).
    * Loamy soils → Moderate draft force (balanced composition).
    * Clayey soils → High draft force (high cohesion and resistance).
  * Trend: Clayey Soil → Increase Draft Force, Sandy Soil → Decrease Draft Force
* Ploughing Depth (cm)
  * Effect: Direct Relationship
  * Explanation: As depth increases, the volume of soil being cut and lifted increases, leading to higher draft force demands.
  * Trend: Increase in Depth →  Increases Draft Force
* Disc Angle and Configuration
  * Effect: Nonlinear Relationship
  * Explanation: 
    * Increasing the disc angle (up to ~45°) increases soil penetration but also increases draft force.
    * If the angle is too high (>45°), soil inversion is inefficient, increasing resistance.
  * Trend: Moderate disc angle (~30-45°) optimizes draft force. Too high or too low increases resistance.
* Operating Speed (km/h)
  * Effect: Direct Relationship
  * Explanation: Higher speeds increase soil resistance due to inertia and impact forces, leading to higher draft force demands.
  * Trend: Increase in Speed → Increases the Draft Force.
* Width of Cut (cm)
  * Effect: Direct Relationship
  * Explanation: A wider cut means more soil is engaged with the plough, increasing resistance and draft force requirements.
  * Trend: Increase in  Width → Increases the Draft Force
* Ambient Temperature (°C)
  * Effect: Indirect Relationship
  * Explanation: 
    * High temperatures decreases soil moisture → increase soil hardness → increase draft force.
    * Low temperatures may increase soil stiffness in some cases, increasing resistance.
  * Trend: Increase in Temperature (if it dries soil) → Increases Draft Force
* Humidity (%)
  * Effect: Indirect Relationship
  * Explanation: 
    * High humidity can help retain soil moisture, reducing draft force.
    * Low humidity in dry conditions can harden the soil, increasing draft force.
  * Trend: Increase in Humidity → Increases Draft Force (if moisture is retained)

Based on the information specific to FUNAAB (Federal University of Agriculture, Abeokuta, Nigeria), relationships and specific range of parameters obtained from literature the dataset was generated using Python and provided in CSV format.

## Data Cleaning
* Missing values: Checked for missing values to ensure data quality and the result shows that there were no missing values.
* Duplicate values: Checked for duplicate values to ensure data quality and the result shows that there were no duplicate values.

## Exploratory Data Analysis
### Univariate Analysis
The Histograms for the numerical features show that:
* Most features follow normal or skewed distributions. 
* Draft Force (kN/m) is bounded between 1.95 and 4.25, as expected. 
* Soil Moisture Content (%) and Bulk Density (g/cm³) show some variation but remain within reasonable ranges.

The boxplots for numerical features show that:
* Potential outliers detected in Soil Moisture Content (%) and Width of Cut (cm).
* Draft Force (kN/m) appears well-bounded within the expected range.
* Bulk Density (g/cm³) shows a tight distribution, suggesting minimal variability.

### Bivariate Analysis
**The Correlation Heatmap give the following insight:**
Draft Force (kN/m) is strongly correlated with:
* Ploughing Depth (cm) (0.70) → Deeper plowing increases draft force.
* Width of Cut (cm) (0.65) → Wider cuts require more force.
* Disc Angle (°) (0.52) → Larger angles lead to more soil resistance.

Negative correlation observed with:
* Soil Moisture Content (%) (-0.42) → Wetter soils reduce draft force.
* Humidity (%) (-0.33) → More humidity retains moisture, lowering resistance.

**The Scatter Plots give the following insight:**
* Ploughing Depth (cm), Width of Cut (cm), and Disc Angle (°) show strong positive relationships with Draft Force.
* Soil Moisture Content (%) and Humidity (%) exhibit negative correlations, as expected.
* The scatter plots confirm that Draft Force increases with more aggressive tillage settings.

## Data Preprocessing
### Winsorization for Outlier Handling
Instead of replacing outliers with the median, we can cap extreme values at the lower and upper bounds using Winsorization.
* Winsorization prevents extreme values from distorting the dataset while keeping them.
* Better than removing or replacing outliers entirely, especially when the dataset is small.
* Best used when dealing with skewed data distributions.

### Data Scaling using RobustScaler
RobustScaler is a feature scaling method that’s particularly useful when your data contains outliers. Unlike StandardScaler (which uses the mean and standard deviation) or MinMaxScaler (which uses the minimum and maximum values), RobustScaler relies on robust statistics:
* Median: It subtracts the median of each feature to center the data.
* Interquartile Range (IQR): It divides by the IQR (the difference between the 75th and 25th percentiles) to scale the data.

### Label Encoding applied for "Soil Texture" (0 = Sandy Loam, 1 = Sandy Clay Loam)
This tool from sklearn.preprocessing converts categorical labels into unique integers (e.g., 0, 1, 2 ...). Each distinct category in 'Soil Texture' is assigned a unique integer. This method first "fits" the encoder to the unique values in 'Soil Texture' (learning the mapping from categories to integers) and then "transforms" the column by replacing the original categorical values with their corresponding integers. 

## Feature Engineering
Creating interaction terms
* Depth × Width (captures impact of larger plowing areas).
* Moisture × Bulk Density (soil composition effect on draft force).
* Humidity × Bulk Density (soil composition effect on draft force).
* Angle × Depth (effect of disc angle at different depths).

## Model Selection
The machine learning models applied are: **Decision Tree** and **Random Forest**.
### **Decision Trees** 
A supervised machine learning algorithm used for classification and regression tasks. It mimics human decision-making by splitting data into subsets based on feature values, forming a tree-like structure. Decision tree is a tree-based algorithm capable of identifying nonlinear relationships between variables and making predictions through a series of if-then rules. It can also be utilized to segment customers based on their behavior and optimize pricing strategies effectively.
### **Random Forest**
An ensemble learning method used for both classification and regression tasks. It builds multiple decision trees during training and combines their outputs (via averaging for regression or majority voting for classification) to improve accuracy and reduce overfitting. It is a robust and versatile algorithm that works well with both categorical and numerical data.

### Model Evaluation
| Model                       | R² Score      |MAE           |RMSE          |
| --------------------------- | ------------- |------------- |------------- |
| DecisionTreeRegressor       | 0.975456      |0.064467      |0.126154      |
| RandomForestRegressor       | 0.992435      |0.039199      |0.070038      |

RandomForestRegressor outperforms DecisionTreeRegressor with higher R², lower MAE, and lower RMSE.

## Feature Importance Analysis
* 6 Width of Cut (cm): 0.572562
* 3 Ploughing Depth (cm):  0.261180
* 9 Depth × Width : 0.115733
* 2 Soil Texture : 0.024489
* 0 Soil Moisture Content (%): 0.020444
* 7 Ambient Temperature (°C): 0.000788
* 5 Operating Speed (km/h): 0.000774
* 10 Moisture × Bulk Density: 0.000760
* 11 Humidity × Bulk Density: 0.000753
* 8  Humidity (%): 0.000729

The feature importance analysis using RandomForestRegressor has identified the key variables influencing draft force.
The most significant features include width of cut, ploughing depth, Depth x Width, Soil Texture and Soil Moisture Conten (%) which have the highest impact on draft force variation.
These insights can guide tillage optimization strategies, ensuring efficient energy use while maintaining effective soil penetration.
