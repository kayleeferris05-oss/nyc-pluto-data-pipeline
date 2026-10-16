# NYC PLUTO Municipal Data Engineering & EDA Pipeline

## 📌 Project Overview
This project features an end-to-end data cleaning, validation, and exploratory data analysis (EDA) pipeline built in Python (`pandas`, `matplotlib`). The pipeline ingests, cleans, and profiles New York City's massive primary land use tax lot dataset (`pluto_26v2.csv`), scaling across **858,284 rows and 99 initial columns**.

---

## 🛠️ Data Cleaning Log
| Step # | Operation / Task | Columns Affected | Description / Notes |
| :--- | :--- | :--- | :--- |
| **1** | **Ingestion & Encoding** | All (858,284 rows, 99 cols) | Loaded raw dataset using pandas with `latin-1` encoding to resolve special municipal character errors. |
| **2** | **Missing Value Audit** | All 99 Columns | Scanned for null values across all 99 fields. Identified highly sparse optional fields (e.g., `notes`, `spdist3`, `zonedist4`); flagged for selective retention rather than dropping. |
| **3** | **Duplicate Check** | Full Dataset (858,284 rows) | Verified 0 duplicate rows (`df.duplicated().sum() == 0`), confirming row-level uniqueness across tax lots. |
| **4** | **Sparse Feature Pruning** | 22 Columns Dropped | Removed columns exhibiting >90% missing data (shrinking dataset from 99 to 77 columns) to optimize feature space. |
| **5** | **String Normalization** | 16 Text Fields | Standardized string columns by stripping trailing/leading whitespace for uniform data formatting. |
| **6** | **Cleaned Data Export** | 858,284 rows, 77 cols | Exported production-ready dataset to `pluto_cleaned.csv` (`index=False`) for downstream analytical modeling. |

---

## 📊 Exploratory Data Analysis
### NYC Tax Lot Distribution by Borough
* **Objective:** Validate dataset completeness across municipal geographic boundaries and establish baseline sample volumes for downstream modeling ($N = 858,284$ records).
* **Key Insights:** 
  * **Queens (`QN`)** and **Brooklyn (`BK`)** lead the city in raw tax lot volume due to extensive low-rise residential density.
  * **Manhattan (`MN`)** exhibits the lowest lot count (~50k) despite high structural density, highlighting its reliance on high-rise, multi-unit parcels.

![Borough Distribution](borough_distribution.png)

---

## 🚀 Tech Stack & Libraries
* **Language:** Python (IDLE / Terminal environment)
* **Data Manipulation:** `pandas`
* **Visualization:** `matplotlib`