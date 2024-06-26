from weatherunion_script import *
import joblib
from tensorflow.keras.models import load_model
import datetime
# Function to predict demand for a given zone
def predict_demand_for_zone(zone, hourly_demand):
    # Load the LSTM model
    model = load_model(f'/Users/aayushjain/codes/projects/company assignements/Snape/City Heatmap/Saved Models and Scales 17 June/lstm_{zone}.h5')
    scaler_X = joblib.load(f'/Users/aayushjain/codes/projects/company assignements/Snape/City Heatmap/Saved Models and Scales 17 June/scaler_x_{zone}.pkl')
    scaler_y = joblib.load(f'/Users/aayushjain/codes/projects/company assignements/Snape/City Heatmap/Saved Models and Scales 17 June/scaler_y_{zone}.pkl')

    # Extract hourly demand for the given zone
    hourly_demand_zone = hourly_demand[zone]

    new_sample = hourly_demand_zone.values
    new_sample = new_sample.reshape(1, -1)

    new_sample_scaled = scaler_X.transform(new_sample)

    new_sample_reshaped = new_sample_scaled.reshape((new_sample_scaled.shape[0], 1, new_sample_scaled.shape[1]))

    y_pred_scaled = model.predict(new_sample_reshaped)
    y_pred = scaler_y.inverse_transform(y_pred_scaled)
    rounded_prediction = round(y_pred.flatten()[0])
    
    return rounded_prediction

# Example usage:
zones = ['airport', 'dakshindari', 'sectorV', 'victoria', 'howrah', 'kolkata_city']

hourly_demand = {
    'airport': hourly_demand_airpot,
    'dakshindari': hourly_demand_dakshinDari,
    'sectorV': hourly_demand_sectorV,
    'victoria': hourly_demand_rabindrasadan,
    'howrah': hourly_demand_howrah,
    'kolkata_city': hourly_demand
}

predicted_values = {}

for zone in zones:
    predicted_values[zone] = predict_demand_for_zone(zone, hourly_demand)

print("Predicted values:", predicted_values)







