# 📈 Sales Forecasting with Economic Indicators

![Status](https://img.shields.io/badge/Project-Active-brightgreen)
![Tool](https://img.shields.io/badge/Python-Prophet%20%7C%20Pandas%20%7C%20Matplotlib-blue)
![Focus](https://img.shields.io/badge/Domain-Time--Series%20Forecasting%20%7C%20Business%20Planning-orange)

## 🚀 Objective
Forecast future sales by integrating historical sales data with external economic indicators (inflation, unemployment, consumer confidence).  
This project demonstrates how **time-series modeling enriched with regressors** can provide actionable insights for strategic planning.

---

## 🛠️ Workflow
1. **Data Preparation**  
   - Dataset: `sales_data.csv` (Date, Revenue).  
   - Dataset: `economic_indicators.csv` (Date, InflationRate, UnemploymentRate, ConsumerConfidenceIndex).  
   - Merge datasets into a unified time-series.

2. **Model Training**  
   - Algorithm: Prophet (time-series forecasting).  
   - External regressors: Inflation, Unemployment, Consumer Confidence.  
   - Train model and save as `sales_forecast_model.pkl`.

3. **Forecasting**  
   - Predict sales for the next 90 days.  
   - Generate forecast plots with confidence intervals.  
   - Save results to `sales_forecast.csv`.

4. **Visualization**  
   - Line chart: Actual vs Predicted sales.  
   - Trend components (seasonality, economic drivers).  
   - Feature importance analysis.

5. **Insights**  
   - Identify economic factors influencing sales.  
   - Provide recommendations for pricing, marketing, and inventory strategies.

---

## 📂 Deliverables
- `/data` → Sales and economic datasets, forecast results.  
- `/scripts` → Forecasting script (`train_forecast_model.py`).  
- `/models` → Saved forecasting model (`sales_forecast_model.pkl`).  
- `/visuals` → Forecast plots and trend components.  
- `/insights` → Markdown file summarizing findings and recommendations.  
- `README.md` → Documentation (this file).  

---

## 🔍 Business Value
- **Strategic Planning** → Anticipate sales trends with economic context.  
- **Revenue Optimization** → Adjust pricing and promotions based on inflation/unemployment.  
- **Operational Efficiency** → Align inventory and staffing with forecasted demand.  

---

## 📸 Example Visualizations
*(Insert forecast plot and trend component screenshots here)*

---

## 🧭 Next Steps
- Extend forecast horizon to 12 months.  
- Add additional regressors (exchange rates, fuel prices).  
- Deploy pipeline to cloud (Azure Data Factory + Power BI integration).
