
import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt

from scipy import stats
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# STEP 2: Data Collection and Preparation
# Data Source
csv_url = r"/home/abaca/projects/ai_rnd_2023/venv-ai-rnd/StressLevelDataset.csv"
df = pd.read_csv(csv_url)

# Data Cleaning
"""
print("\nAre there any missing points in the dataset?:", df.isnull().values.any())
print("Number of Duplicated Rows:", df.duplicated().sum())
# There werent any duplicated rows nor missing datapoints in the dataset.
"""

# STEP 3: Exploratory Data Analysis
numerical_features = ['anxiety_level','self_esteem','mental_health_history','depression','headache','blood_pressure','sleep_quality','breathing_problem','noise_level','living_conditions','safety','basic_needs','academic_performance','study_load','teacher_student_relationship','future_career_concerns','social_support','peer_pressure','extracurricular_activities','bullying','stress_level']
df[numerical_features].hist(bins=30, figsize=(12, 8))
plt.suptitle('Histograms of Numerical Features')
plt.show()
