---

# Marketing Analytics Dashboard | Power BI, SQL, Python

This project delivers end-to-end analysis of customer and product engagement data using Power BI for data visualization, SQL for data transformation, and Python for sentiment analysis. It simulates a real-world marketing scenario by integrating multiple tools and environments including **Docker** and **Azure Data Studio**.

---

## Project Overview

This repository includes all files used to develop a Power BI dashboard that helps marketing teams:
- Track and analyze customer behavior
- Understand product performance
- Visualize engagement metrics by time, product, and region
- Enrich customer reviews with sentiment analysis using Python

---

##  Technologies Used

| Tool / Technology | Purpose |
|-------------------|---------|
| **SQL Server (Docker)** | Host the marketing analytics database |
| **Azure Data Studio** | Manage and query SQL data |
| **Power BI** | Create the final interactive dashboard |
| **Python (NLTK)** | Perform sentiment analysis on customer reviews |
| **DAX** | Create calculated columns and KPIs in Power BI |

---

## Files Included

- `*.sql` – Scripts to create and populate all dimension and fact tables
- `customer_reviews_enrichment.py` – Python script to enrich review text with sentiment score
- `fact_customer_reviews_with_sentiment.csv` – Enriched dataset with sentiment results
- `Ecommerce_Sales_Report.pbix` – Power BI dashboard file
- `requirements.txt` – Python dependencies for sentiment analysis
- `.bak` – SQL Server database backup (used to restore database inside Docker container)
- `.pptx` – Project presentation slides (optional if uploaded)

---

##  How to Run the Project

### 1. Set Up SQL Server with Docker
```bash
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=YOUR_PASSWORD" ^
-p 1433:1433 ^
-v "C:\Users\<your-user>\docker_volumes\sql_backups:/var/opt/mssql/backup" ^
--name sqlserver -d mcr.microsoft.com/mssql/server:2022-latest
```

### 2. Restore the Database
Use Azure Data Studio to connect to `localhost:1433` with:
- **Username**: `USERNAME`
- **Password**: `YOUR_PASSWORD`

Then run:
```sql
RESTORE DATABASE PortfolioProject_MarketingAnalytics
FROM DISK = '/var/opt/mssql/backup/Episode 2 - PortfolioProject_MarketingAnalytics.bak'
WITH MOVE 'PortfolioProject_MarketingAnalytics' TO '/var/opt/mssql/data/PortfolioProject_MarketingAnalytics.mdf',
     MOVE 'PortfolioProject_MarketingAnalytics_log' TO '/var/opt/mssql/data/PortfolioProject_MarketingAnalytics_log.ldf',
     REPLACE;
```

### 3. Run Python Script
Install dependencies:
```bash
pip install -r requirements.txt
```

Run sentiment analysis script:
```bash
python customer_reviews_enrichment.py
```

### 4. Open Power BI Dashboard
Open `Ecommerce_Sales_Report.pbix` and configure the data source to point to your local SQL Server.

---

##  View the Live Dashboard

🔗 [Power BI Report Link](https://app.powerbi.com/groups/me/reports/9f9d9e7e-66a6-4ea4-b33c-ca7fd733f7e2/7adefa3ef97290b0941f?experience=power-bi)

---

##  Learning Outcomes

- Set up and manage SQL Server inside Docker
- Perform data cleaning and joins in SQL
- Build interactive visual dashboards in Power BI
- Use Python (NLTK) for text analytics and sentiment classification
- Combine multiple technologies in a realistic marketing analytics use case

---

##  Contact

If you’d like to collaborate or have questions about the project, feel free to reach out via [LinkedIn](https://linkedin.com/in/your-profile) or email.
```

---

