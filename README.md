# E-commerce Sales Analysis

**Project:** Data Analytics — E-commerce Sales Analysis & Dashboard  
**Author:** [Your Name]  
**Purpose:** Analyze e-commerce data to extract insights about revenue, product performance and customer behavior. Prepare visuals and a dashboard for an internship application.

## Contents
- `data/` - raw and processed data files
- `notebooks/Ecommerce_Sales_Analysis.ipynb` - full notebook with EDA & visualizations
- `src/` - modular scripts for preprocessing, EDA, and a lightweight dashboard
- `Ecommerce_Sales_Analysis_Project.pdf` - project report
- `requirements.txt` - python dependencies

## How to run
1. Clone repo
2. Put dataset `sales_data_sample.csv` in the `data/` folder (download from Kaggle or your source)
3. Create virtual env & install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate      # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
4. Clean data:
   ```bash
   python src/data_preprocessing.py --input data/sales_data_sample.csv --output data/processed/cleaned_sales_data.csv
   ```
5. Produce plots:
   ```bash
   python src/eda_visuals.py --input data/processed/cleaned_sales_data.csv
   ```
6. (Optional) Generate simple HTML dashboard:
   ```bash
   python src/dashboard_plotly.py --input data/processed/cleaned_sales_data.csv --out dashboard.html
   ```

## Power BI
- Use `data/processed/cleaned_sales_data.csv` to import into Power BI.
- DAX snippets for KPIs are provided in `DAX_snippets.md`

## License
MIT — feel free to reuse & adapt for your internship submission.
