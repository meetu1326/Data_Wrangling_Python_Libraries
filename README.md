# Week 3: Python & Data Wrangling

## Project Overview
This project focuses on practical exploratory data analysis and data preprocessing using Python, Pandas, Matplotlib, and Seaborn. Built for the **Week 3: Python & Data Wrangling** curriculum, the objective is to clean an uncurated dataset, handle messy real-world artifacts (missing values, duplicated records, inconsistent naming), perform row-level filtering, engineer new features, and generate visual summaries of categorical and numerical patterns.

---

## Key Features & Workflow

### 1. Data Ingestion & Schema Normalization
* **Format Flexibility:** Programmatically ingests `.csv` or `.xlsx` files using dynamic path resolution (`os.path`).
* **Header Standardization:** Cleans whitespace, replaces spaces with underscores, and forces lowercase naming to prevent lookup errors.
* **Deduplication:** Identifies and drops identical records across all dimensions.

### 2. Missing Value Imputation
* **Numerical Imputation:** Selects numeric features dynamically and imputes `NaN` values using column-level **medians** to resist outlier distortion.
* **Categorical Imputation:** Detects text-based object columns and replaces null records with a placeholder value (`"Unknown"`) or mode values.

### 3. Row Filtering & Feature Engineering
* **Row-Level Filtering:** Segregates valid records by applying condition masks to eliminate invalid transactions (e.g., negative/zero quantities).
* **Feature Creation:** Builds derived metrics such as calculated spend totals, user tiers, and temporal segments (e.g., extracting transaction month names from timestamps).

### 4. Exploratory Data Visualization
* **Numerical Distributions:** Generates Seaborn `histplot` charts paired with Kernel Density Estimation (KDE) curves to evaluate skewness and distributions.
* **Categorical Frequency:** Visualizes frequency distributions of top categories using Seaborn `countplot` charts with adjusted rotation and color palettes.

### 5. Automated Export
* Serializes the fully preprocessed dataset to `Cleaned_Dataset.csv` with zero index clutter.

---

## Tech Stack
* **Language:** Python 3.10+
* **Data Manipulation:** `pandas`, `numpy`
* **Data Visualization:** `matplotlib`, `seaborn`
* **File Parsing Backend:** `openpyxl`

---

## Project Structure
```text
├── week3_data_wrangling.py    # Main data wrangling & visualization script
├── dataset.csv                # Raw, uncurated input dataset
├── Cleaned_Dataset.csv        # Output dataset post-cleaning
└── README.md                  # Project documentation
