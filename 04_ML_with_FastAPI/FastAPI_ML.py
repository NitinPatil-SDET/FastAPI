# ============================================================
# INSURANCE PREMIUM PREDICTION MODEL
# ============================================================
# Goal:
# Predict Insurance Premium Category
# (Low / Medium / High)
#
# ML Algorithm Used:
# Random Forest Classifier
#
# Steps:
# 1. Load dataset
# 2. Feature Engineering
# 3. Data Preprocessing
# 4. Model Training
# 5. Model Evaluation
# 6. Save Model
# ============================================================


# ==========================
# Import Required Libraries
# ==========================

import pandas as pd
import numpy as np
import pickle

# Machine Learning Algorithm
from sklearn.ensemble import RandomForestClassifier

# Train/Test Split
from sklearn.model_selection import train_test_split

# Convert categorical values to numerical values
from sklearn.preprocessing import OneHotEncoder

# Apply different preprocessing on different columns
from sklearn.compose import ColumnTransformer

# Create an end-to-end ML workflow
from sklearn.pipeline import Pipeline

# Evaluation Metrics
from sklearn.metrics import accuracy_score, classification_report


# ==========================
# Load Dataset
# ==========================

path = r"C:\Nitin\FastAPI\04_ML_with_FastAPI\insurance.csv"

# Read CSV file into DataFrame
df = pd.read_csv(path)

print("Dataset Shape:", df.shape)
print(df.head())


# ==========================
# Explore Dataset
# ==========================

# Display all unique occupations available
print("\nUnique Occupations:")
print(df["occupation"].unique())


# ============================================================
# FEATURE ENGINEERING
# ============================================================
# Instead of using raw data directly,
# we create meaningful features.
#
# Age + Weight + Height + Smoking habits
# become more useful business features.
# ============================================================

# Create copy of original dataset
df_feat = df.copy()


# ------------------------------------------------------------
# Feature 1 : BMI
# Formula:
# BMI = Weight / Height²
#
# BMI is a better health indicator than
# weight and height separately.
# ------------------------------------------------------------

df_feat["bmi"] = (
    df_feat["weight"] /
    (df_feat["height"] ** 2)
)


# ------------------------------------------------------------
# Feature 2 : Age Group
#
# Convert numerical age into categories.
#
# Example:
# 20 -> young
# 35 -> adult
# 50 -> middle_aged
# 70 -> senior
# ------------------------------------------------------------

def age_group(age):

    if age < 25:
        return "young"

    elif age < 45:
        return "adult"

    elif age < 60:
        return "middle_aged"

    else:
        return "senior"


# Apply function on age column
df_feat["age_group"] = df_feat["age"].apply(age_group)


# ------------------------------------------------------------
# Feature 3 : Lifestyle Risk
#
# Business Rule:
#
# Smoker + BMI > 30 = High Risk
#
# Smoker only OR BMI > 27 = Medium Risk
#
# Otherwise = Low Risk
# ------------------------------------------------------------

def lifestyle_risk(row):

    if row["smoker"] and row["bmi"] > 30:
        return "high"

    elif row["smoker"] or row["bmi"] > 27:
        return "medium"

    else:
        return "low"


# axis=1 means process row-by-row
df_feat["lifestyle_risk"] = df_feat.apply(
    lifestyle_risk,
    axis=1
)


# ------------------------------------------------------------
# Feature 4 : City Tier
#
# Convert city names into Tier:
#
# Tier 1 = Metro Cities
# Tier 2 = Medium Cities
# Tier 3 = Other Cities
# ------------------------------------------------------------

tier_1_cities = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Chennai",
    "Kolkata",
    "Hyderabad",
    "Pune"
]

tier_2_cities = [
    "Jaipur",
    "Chandigarh",
    "Indore",
    "Lucknow",
    "Patna",
    "Ranchi",
    "Visakhapatnam",
    "Coimbatore",
    "Bhopal",
    "Nagpur",
    "Vadodara",
    "Surat",
    "Rajkot",
    "Jodhpur",
    "Raipur",
    "Amritsar",
    "Varanasi",
    "Agra",
    "Dehradun",
    "Mysore",
    "Jabalpur",
    "Guwahati",
    "Thiruvananthapuram",
    "Ludhiana",
    "Nashik",
    "Allahabad",
    "Udaipur",
    "Aurangabad",
    "Hubli",
    "Belgaum",
    "Salem",
    "Vijayawada",
    "Tiruchirappalli",
    "Bhavnagar",
    "Gwalior",
    "Dhanbad",
    "Bareilly",
    "Aligarh",
    "Gaya",
    "Kozhikode",
    "Warangal",
    "Kolhapur",
    "Bilaspur",
    "Jalandhar",
    "Noida",
    "Guntur",
    "Asansol",
    "Siliguri"
]


def city_tier(city):

    if city in tier_1_cities:
        return 1

    elif city in tier_2_cities:
        return 2

    else:
        return 3


# Apply city tier logic
df_feat["city_tier"] = df_feat["city"].apply(city_tier)


# ============================================================
# Check Final Engineered Dataset
# ============================================================

print("\nEngineered Dataset Sample:\n")

print(
    df_feat[
        [
            "income_lpa",
            "occupation",
            "bmi",
            "age_group",
            "lifestyle_risk",
            "city_tier",
            "insurance_premium_category"
        ]
    ].head()
)


# ============================================================
# FEATURES (X) AND TARGET (Y)
# ============================================================

# Input columns for prediction
X = df_feat[
    [
        "bmi",
        "age_group",
        "lifestyle_risk",
        "city_tier",
        "income_lpa",
        "occupation"
    ]
]

# Target column
y = df_feat["insurance_premium_category"]


# ============================================================
# DATA PREPROCESSING
# ============================================================

# Categorical columns
categorical_features = [
    "age_group",
    "lifestyle_risk",
    "occupation",
    "city_tier"
]

# Numerical columns
numeric_features = [
    "bmi",
    "income_lpa"
]


# ------------------------------------------------------------
# One Hot Encoding
#
# Example:
#
# occupation
# ----------
# Engineer
# Doctor
#
# becomes
#
# Engineer Doctor
#    1       0
#    0       1
# ------------------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[

        (
            "cat",
            OneHotEncoder(),
            categorical_features
        ),

        (
            "num",
            "passthrough",
            numeric_features
        )

    ]
)


# ============================================================
# MODEL PIPELINE
# ============================================================
#
# Pipeline ensures:
# Raw Data
#    ↓
# Encoding
#    ↓
# Model Training
#    ↓
# Prediction
#
# Everything happens automatically.
# ============================================================

pipeline = Pipeline(
    steps=[

        (
            "preprocessor",
            preprocessor
        ),

        (
            "classifier",
            RandomForestClassifier(
                random_state=42
            )
        )

    ]
)


# ============================================================
# TRAIN TEST SPLIT
# ============================================================
#
# 80% -> Training Data
# 20% -> Testing Data
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=1
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))


# ============================================================
# MODEL TRAINING
# ============================================================

print("\nTraining Model...")

pipeline.fit(
    X_train,
    y_train
)

print("Training Complete.")


# ============================================================
# MODEL PREDICTION
# ============================================================

y_pred = pipeline.predict(X_test)


# ============================================================
# MODEL EVALUATION
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nModel Accuracy:")
print(round(accuracy * 100, 2), "%")

print("\nClassification Report:\n")
print(
    classification_report(
        y_test,
        y_pred
    )
)


# ============================================================
# VIEW SAMPLE TEST DATA
# ============================================================

print("\nRandom Test Records:\n")
print(X_test.sample(5))


# ============================================================
# SAVE TRAINED MODEL
# ============================================================
#
# Why save?
#
# Train Once
#      ↓
# Save model.pkl
#      ↓
# FastAPI loads model.pkl
#      ↓
# Prediction without retraining
# ============================================================

model_path = "model.pkl"

with open(model_path, "wb") as file:
    pickle.dump(
        pipeline,
        file
    )

print(f"\nModel saved successfully at: {model_path}")


# ============================================================
# END OF PROJECT
# ============================================================