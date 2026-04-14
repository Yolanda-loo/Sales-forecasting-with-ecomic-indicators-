import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Step 1: Load datasets
sales_df = pd.read_csv("data/sales_data.csv")  # Example columns: Date, Revenue
econ_df = pd.read_csv("data/economic_indicators.csv")  # Example columns: Date, InflationRate, UnemploymentRate, ConsumerConfidenceIndex

# Step 2: Preprocess
sales_df["Date"] = pd.to_datetime(sales_df["Date"])
econ_df["Date"] = pd.to_datetime(econ_df["Date"])

# Merge sales with economic indicators
merged_df = pd.merge(sales_df, econ_df, on="Date", how="left")

# Prophet requires columns: ds (date), y (target)
df = merged_df.rename(columns={"Date": "ds", "Revenue": "y"})

# Step 3: Initialize Prophet model with regressors
model = Prophet()
model.add_regressor("InflationRate")
model.add_regressor("UnemploymentRate")
model.add_regressor("ConsumerConfidenceIndex")

# Step 4: Fit model
model.fit(df)

# Step 5: Create future dataframe
future = model.make_future_dataframe(periods=90)  # Forecast next 90 days
future = pd.merge(future, econ_df, left_on="ds", right_on="Date", how="left").drop(columns=["Date"])

# Step 6: Forecast
forecast = model.predict(future)

# Step 7: Visualization
fig1 = model.plot(forecast)
plt.title("Sales Forecast with Economic Indicators")
plt.show()

fig2 = model.plot_components(forecast)
plt.show()

# Step 8: Save forecast results
forecast.to_csv("data/sales_forecast.csv", index=False)
print("Forecast saved to data/sales_forecast.csv")
