import pandas as pd
from prophet import Prophet
import joblib
import matplotlib.pyplot as plt

# --------------------------
# Load data
# --------------------------
sales = pd.read_csv('../data/sales_data.csv')
econ = pd.read_csv('../data/economic_indicators.csv')

sales['Date'] = pd.to_datetime(sales['Date'])
econ['Date'] = pd.to_datetime(econ['Date'])

# --------------------------
# Merge datasets
# --------------------------
df = pd.merge(sales, econ, on='Date')

# Rename for Prophet
df = df.rename(columns={
    'Date': 'ds',
    'Revenue': 'y'
})

# --------------------------
# Create model
# --------------------------
model = Prophet()

model.add_regressor('InflationRate')
model.add_regressor('UnemploymentRate')
model.add_regressor('ConsumerConfidenceIndex')

# --------------------------
# Train model
# --------------------------
model.fit(df)

# Save model
joblib.dump(model, '../models/sales_forecast_model.pkl')

# --------------------------
# Create future data
# --------------------------
future = model.make_future_dataframe(periods=90)

future = future.merge(
    econ.rename(columns={'Date': 'ds'}),
    on='ds',
    how='left'
)

# Fill missing values
future.fillna(method='ffill', inplace=True)

# --------------------------
# Forecast
# --------------------------
forecast = model.predict(future)

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(
    '../data/sales_forecast.csv', index=False
)

# --------------------------
# Plot forecast
# --------------------------
fig1 = model.plot(forecast)
plt.title("Sales Forecast (Next 90 Days)")
plt.savefig('../visuals/forecast_plot.png')

# --------------------------
# Plot components
# --------------------------
fig2 = model.plot_components(forecast)
plt.savefig('../visuals/components_plot.png')

print("✅ Forecast complete!")
