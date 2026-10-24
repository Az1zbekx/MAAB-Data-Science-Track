# 🎓 MAAB Academy: Data Science & AI Engineering Track

[![CI](https://github.com/Az1zbekx/MAAB-Data-Science-Track/actions/workflows/ci.yml/badge.svg)](https://github.com/Az1zbekx/MAAB-Data-Science-Track/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![SQL](https://img.shields.io/badge/SQL-PostgreSQL%20%7C%20MySQL-orange.svg?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-scikit--learn%20%7C%20NumPy-yellow.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![FastAPI](https://img.shields.io/badge/Deployment-FastAPI-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A rigorous, end-to-end curriculum portfolio covering mathematical fundamentals, relational data engineering, core machine learning from mathematical first principles, and production API serving.

---

## 🗺️ Curriculum Architecture & Modules

```
MAAB-Data-Science-Track/
├── 01-Python-Foundations/      # Core programming, OOP, data structures & algorithms
├── 02-SQL-Databases/           # Relational schema design, complex joins, aggregation & indexing
├── 03-Machine-Learning/        # Mathematical ML from scratch, metrics & FastAPI deployment
├── 04-Deep-Learning/           # (Upcoming) Neural networks, PyTorch & architectures
├── 05-Computer-Vision/         # (Upcoming) YOLOv8/11, detection, tracking & edge deployment
└── 06-Agentic-AI/              # (Upcoming) LangGraph, hybrid RAG & tool calling workflows
```

---

## 📚 Module Breakdown

### 🔹 Module 1: Python Foundations (`01-Python-Foundations/`)
A 17-lesson intensive sequence establishing core algorithmic fluency in Python:
- **Core Syntax & Logic:** Data types, control flow, functions, recursion, lambda expressions.
- **Data Structures:** Lists, tuples, dictionaries, sets, comprehensions, and memory references.
- **Object-Oriented Programming (OOP):** Classes, inheritance, polymorphism, encapsulation, dunder methods.
- **File I/O & Error Handling:** Context managers (`with`), structured exception handling, custom exceptions.

### 🔹 Module 2: Relational Databases & SQL (`02-SQL-Databases/`)
14 comprehensive units spanning relational modeling and query optimization:
- **Data Definition & Manipulation (DDL/DML):** `CREATE`, `ALTER`, `INSERT`, `UPDATE`, `DELETE`, constraints.
- **Complex Joins & Subqueries:** `INNER`, `LEFT`, `RIGHT`, `FULL OUTER`, correlated subqueries, CTEs (`WITH`).
- **Aggregation & Analytics:** `GROUP BY`, `HAVING`, window functions (`ROW_NUMBER`, `RANK`, `PARTITION BY`).
- **Performance & Design:** Indexing strategies, normalization (1NF - 3NF), and query profiling.

### 🔹 Module 3: Machine Learning & Production Serving (`03-Machine-Learning/`)
25+ in-depth practical modules combining mathematical mechanics with engineering deployment:
- **Mathematical Foundations:** Gradient Descent from scratch, loss function derivation, convexity.
- **Regression:** Simple & Multiple Linear Regression, Polynomial Features, Regularization (Ridge / Lasso L1/L2).
- **Classification:** Logistic Regression, Multiclass Classification, Naive Bayes (Gaussian / Multinomial), Support Vector Machines (SVM kernels).
- **Tree-Based Models (From Scratch):** Decision Tree implementation from first principles (Gini Impurity, Information Gain, Entropy), Random Forests, Ensemble Learning (Bagging, Boosting, Stacking).
- **Unsupervised Learning & Dimensionality Reduction:** K-Means clustering, DBSCAN density clustering, Principal Component Analysis (PCA).
- **Production Pipeline & Serving:** Scikit-Learn `Pipeline`, data preprocessing & scaling, containerized serving with **FastAPI** (`Deploying the model with FastAPI 1 & 2`).

---

## 🚀 Quickstart: Running Machine Learning Labs

### 1. Clone the Unified Track
```bash
git clone https://github.com/Az1zbekx/MAAB-Data-Science-Track.git
cd MAAB-Data-Science-Track
```

### 2. Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r 03-Machine-Learning/requirements.txt
```

### 3. Launch FastAPI Model Serving
```bash
cd "03-Machine-Learning/Deploying the model with FastAPI 1"
uvicorn app:app --reload --port 8000
```
Open interactive Swagger API docs at `http://localhost:8000/docs`.

---

## 👤 Author & Academic Track

- **Developer:** [Azizbek (Az1zbekx)](https://github.com/Az1zbekx)
- **Institution:** PDP University & MAAB Academy
- **Engineering Philosophy:** *"Understand the mathematical mechanics of every algorithm before scaling it with production code."*
