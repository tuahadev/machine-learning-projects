# 📊 Outlier Removal from Advertisement Sales Data

This project demonstrates how to detect and remove outliers from a dataset using the **Interquartile Range (IQR)** method in Python.

---

## 📁 Files

- `sales.ipynb`: Main Jupyter Notebook where outliers are detected and removed from the dataset.
- `sales.csv`: Dataset used (if applicable).
- `README.md`: Project overview and instructions.

---

## 🧠 Objective

To clean the dataset by removing extreme outliers from the `TV` advertisement spending column, which could negatively affect model performance in regression tasks.

---

## 🧪 Method Used: Interquartile Range (IQR)

Outliers are detected using the IQR method:
- **Q1** = 25th percentile  
- **Q3** = 75th percentile  
- **IQR** = Q3 - Q1  
- **Outliers** are any values outside the range:
  \[
  [Q1 - 1.5 \times IQR,\ Q3 + 1.5 \times IQR]
  \]

---


## how to run:
pip install pandas matplotlib seaborn

