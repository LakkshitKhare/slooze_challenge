Absolutely, Elegant. Here's a complete `README.md` tailored to your challenge submission. It includes setup instructions, project overview, and highlights your modular pipeline and EDA work:

---


# 🛠️ Slooze Data Engineering Challenge

## 📦 Overview

This project is an end-to-end data engineering pipeline that:

1. Scrapes product listings from Amazon India using Selenium and Edge WebDriver.
2. Cleans and filters the data to retain only relevant sellers and attributes.
3. Performs Exploratory Data Analysis (EDA) to uncover pricing trends, seller patterns, and keyword insights.

---

## 📁 Project Structure


slooze_challenge/
├── scraper.py            # Selenium-based scraper for Amazon
├── amazon_data.csv       # Cleaned product data
├── EDA.ipynb             # Jupyter notebook with visualizations and insights
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/LakkshitKhare/slooze_challenge.git
cd slooze_challenge
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Scraper

Make sure `msedgedriver.exe` is in your PATH or in the project folder.

```bash
python scraper.py
```

This will generate `amazon_data.csv`.

### 5. Launch EDA Notebook

```bash
jupyter notebook EDA.ipynb
```

---

## 🧪 EDA Highlights

- 📊 Price distribution and segmentation
- 🏷️ Keyword frequency analysis
- 🧹 Seller filtering using prefix heuristics (`by`)
- 🔍 Outlier detection and data quality checks

---

## 🧠 Notes

- The scraper uses anti-bot headers and JavaScript injection to bypass basic protections.
- Only sellers prefixed with `by` are retained to reduce promotional noise.
- The pipeline is modular and can be extended to other B2B platforms like Alibaba or IndiaMART.

---

## 📤 Submission

This repository is part of the Slooze Data Engineering Challenge.  
For queries or feedback, reach out to: **careers@slooze.xyz**
