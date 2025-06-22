# 🔐 Password Strength Classifier

This project uses machine learning to predict the **strength of passwords** (Weak, Medium, Strong) based on their characters using TF-IDF vectorization and a Random Forest classifier.

## 📈 Model Info

- **Accuracy**: 95.5%
- **Features**: Character-level TF-IDF
- **Model**: RandomForestClassifier

## 🧠 What It Does

- Takes user input as a password
- Transforms it into a TF-IDF vector
- Predicts the strength level: `Weak`, `Medium`, or `Strong`

## ▶️ How to Run

```bash
pip install -r requirements.txt
jupyter notebook
.
