# 🏦 FRED Economic Data ETL Pipeline

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Airflow](https://img.shields.io/badge/Airflow-2.8.0-orange.svg)](https://airflow.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Latest-blue.svg)](https://www.docker.com/)
[![GCP](https://img.shields.io/badge/GCP-BigQuery-4285F4.svg)](https://cloud.google.com/)

## 📊 Project Overview

Automated ETL pipeline that extracts economic indicators from the Federal Reserve Economic Data (FRED) API, processes and stores data in Google Cloud Platform, and visualizes insights through interactive Power BI dashboards.

## 🏗️ Architecture
```
FRED API → Airflow (Docker) → Google Cloud Storage → BigQuery → Power BI
```

## 🛠️ Tech Stack

- **Orchestration**: Apache Airflow (Dockerized)
- **Language**: Python 3.10
- **Cloud Platform**: Google Cloud Platform
  - Cloud Storage (GCS) - Data Lake
  - BigQuery - Data Warehouse
- **Visualization**: Microsoft Power BI
- **Version Control**: Git, GitHub

## 📈 Data Sources & Metrics

### **API**: Federal Reserve Economic Data (FRED)

### **Economic Indicators**:
- **GDP**: USA, China, Thailand, Germany, Japan
- **Inflation**: Consumer Price Index (CPI)
- **Employment**: Unemployment Rate
- **Exchange Rates**: USD/THB, EUR/USD, USD/CNY
- **Interest Rates**: Federal Funds Rate
- **Market Data**: S&P 500, Stock Indices

### **Coverage**: 50+ indicators across 10+ countries

## 🚀 Features

✅ **Daily Automated Extraction** - Scheduled data pulls from FRED API  
✅ **Multi-Country Analysis** - Economic comparison across regions  
✅ **Data Quality Validation** - Automated checks and alerts  
✅ **Cloud-Native Storage** - Scalable GCS and BigQuery  
✅ **Interactive Dashboards** - Real-time Power BI visualizations  
✅ **Containerized Deployment** - Docker for easy setup  

## 📁 Project Structure
```
fred-economic-etl/
├── dags/
│   └── fred_etl_dag.py         # Airflow DAG orchestration
├── scripts/
│   ├── extract_fred.py         # Data extraction from FRED
│   ├── upload_to_gcs.py        # Upload to Cloud Storage
│   └── load_to_bigquery.py     # Load to BigQuery
├── sql/
│   └── create_tables.sql       # BigQuery table schemas
├── dashboards/
│   └── economic_dashboard.pbix # Power BI dashboard
├── docs/
│   └── architecture.png        # System architecture diagram
├── docker-compose.yml          # Airflow Docker setup
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## 🎯 Quick Start

### **Prerequisites**
- Docker Desktop
- Python 3.10+
- Google Cloud Account (Free tier)
- FRED API Key ([Get here](https://fred.stlouisfed.org/docs/api/api_key.html))

### **Setup**
```bash
# Clone repository
git clone https://github.com/kiatdara/fred-economic-etl.git
cd fred-economic-etl

# Start Airflow with Docker
docker-compose up -d

# Access Airflow UI
# Open browser: http://localhost:8080
# Username: airflow
# Password: airflow
```

## 📊 Dashboard Preview

*Coming soon - Power BI dashboards showing:*
- Global GDP trends
- Inflation comparison
- Exchange rate analysis
- Economic health indicators

## 🎓 Skills Demonstrated

- **Data Engineering**: ETL pipeline design and implementation
- **Cloud Computing**: GCP services (GCS, BigQuery)
- **Orchestration**: Apache Airflow DAG development
- **Containerization**: Docker and docker-compose
- **Data Visualization**: Power BI dashboard creation
- **Python Programming**: API integration, data processing
- **SQL**: BigQuery queries and table management
- **Version Control**: Git workflow and GitHub collaboration

## 📝 Future Enhancements

- [ ] Add data quality monitoring with Great Expectations
- [ ] Implement CI/CD pipeline with GitHub Actions
- [ ] Add Terraform for infrastructure as code
- [ ] Create dbt models for data transformation
- [ ] Add email/Slack notifications for pipeline failures

## 👤 Author

**Kiatdara**
- GitHub: [@kiatdara](https://github.com/kiatdara)
- Email: kiatdara@gmail.com

## 📄 License

This project is open source and available under the MIT License.

---

⭐ If you find this project useful, please consider giving it a star!
