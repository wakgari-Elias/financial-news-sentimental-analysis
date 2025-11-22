
# Financial News Sentiment Analysis

**Predicting Stock Price Moves Using Financial News Headlines**



## 📌 Project Overview

This project focuses on analyzing a large corpus of financial news to understand how headlines impact stock price movements. The main objective is to perform **sentiment analysis** on news headlines, explore statistical patterns, and prepare the dataset for correlation analysis with stock prices.  

This repository covers **Task 1** of the Nova Financial Insights challenge, including **Git setup, Python environment, exploratory data analysis (EDA), and CI/CD configuration**.



## 🗂 Folder Structure


├── .vscode/
│   └── settings.json                 # VS Code workspace settings
├── .github/
│   └── workflows/
│       └── unittests.yml             # CI workflow using GitHub Actions
├── data/
│   ├── raw/                          # Raw dataset(s)
│   │   └── raw_analyst_ratings.csv
│   └── processed/                    # Cleaned/aggregated datasets
├── notebooks/
│   ├── __init__.py
│   ├── README.md
│   └── EDA_task1.ipynb               # Jupyter Notebook for Task 1 EDA
├── scripts/
│   ├── __init__.py
│   └── README.md
├── src/
│   └── __init__.py
├── tests/
│   └── __init__.py
├── .gitignore
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone Repository


git clone https://github.com/wakgari-Elias/financial-news-sentiment-analysis.git
cd financial-news-sentiment-analysis


### 2. Create & Activate Virtual Environment

* **Windows (PowerShell):**


python -m venv venv
venv\Scripts\Activate.ps1


After activation, your terminal prompt should start with `(venv)`.


### 3. Install Dependencies


pip install --upgrade pip
pip install -r requirements.txt


* Optional for future steps:


pip install pandas_ta yfinance


### 4. Launch Jupyter Notebook in VS Code

* Open VS Code → Select Python Interpreter (`venv`) → Open `notebooks/EDA_task1.ipynb`
* Run the notebook cells step by step (Markdown for instructions, Code for execution)



## 📝 Task 1 Deliverables

### 1. Git & GitHub

* Repository created and cloned locally
* Branch `task-1` created for EDA and analysis
* Frequent commits with descriptive messages

### 2. Python Environment

* Virtual environment (`venv`) setup
* Dependencies installed and frozen to `requirements.txt`
* Jupyter notebook configured to use the environment

### 3. Exploratory Data Analysis (EDA)

* **Descriptive Statistics**

  * Headline lengths, word counts
  * Number of articles per publisher
  * Publication date trends over time
* **Text Analysis**

  * Keyword frequency
  * Topic extraction preparation
* **Time Series Analysis**

  * Articles by hour and weekday
  * Visualizing spikes during market events
* **Publisher Analysis**

  * Top publishers
  * Email domain extraction (if applicable)

### 4. CI/CD Integration

* GitHub Actions workflow `.github/workflows/unittests.yml`
* Runs tests on push and pull requests for branches `main` & `task-1`
* Example test in `tests/test_sample.py` for validating environment setup

---

## 📊 How to Run the Notebook

1. Activate the virtual environment
2. Open `.ipynb` in VS Code
3. Run Markdown cells for instructions
4. Run Code cells to:

   * Load `raw_analyst_ratings.csv`
   * Generate descriptive statistics
   * Visualize publication trends
   * Extract keywords and top publishers

---

## 🧪 Testing

* Run all tests using pytest:


pytest tests/

* CI/CD automatically runs the same workflow on GitHub Actions for every push or pull request.



## 📌 Notes

* This repository is designed for **Task 1** (EDA & Git/CI setup) only.
* Subsequent tasks (sentiment scoring, stock price merging, correlation analysis) will be added to future branches.
* All code is structured for **scalability** and **memory-efficient processing** (important for ~1M rows dataset).

---

## 📚 References & Tools

* [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Matplotlib & Seaborn]([https://matplotlib.org/](https://matplotlib.org/), [https://seaborn.pydata.org/](https://seaborn.pydata.org/))
* [GitHub Actions CI/CD](https://docs.github.com/en/actions)

---

## ✨ Contribution Guidelines

1. Always create a branch for new tasks/features
2. Commit frequently with descriptive messages
3. Use notebooks for exploratory analysis
4. Push changes and create pull requests to merge into main


