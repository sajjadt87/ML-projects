import pandas as pd
import numpy as np

#setting random seed and num of samples
np.random.seed(42)
n_samples = 35000

#creation of dataset
data = {
    'blade_length': np.random.randint(10, 101, n_samples), #explanation of each att is explained at explanation.txt
    'wind_speed': np.random.randint(5, 26, n_samples),     
    'turbine_stats': np.random.choice(['optimal', 'needs to be repaired', 'off'], n_samples),  
    'energy_output': (np.random.randint(100, 5001, n_samples) + np.random.normal(0, 200, n_samples).astype(int)).clip(100, 5000),
    'motor_tempreture': np.random.randint(20, 81, n_samples), 
    'blade_angle': np.random.randint(0, 46, n_samples),       
    'vibration_level': np.random.randint(0, 11, n_samples),   
    'humidity': np.random.randint(20, 91, n_samples),         
    'air_pressure': np.random.randint(900, 1101, n_samples), 
    'category': np.random.choice(['small', 'medium', 'large', np.nan], n_samples, p=[0.3, 0.3, 0.3, 0.1]),  
    'anti_rust': np.random.choice([0, 1, np.nan], n_samples, p=[0.4, 0.4, 0.2]), 
    'efficiency': np.random.randint(0, 101, n_samples)  
}

#turning the dict into a DataFrame
df = pd.DataFrame(data)

#adding NaNs
for col in ['blade_length', 'wind_speed', 'efficiency']:
    missing_mask = np.random.rand(n_samples) < 0.05  # 5% گمشده
    df.loc[missing_mask, col] = np.nan

#saving the file as a csv file
df.to_csv('wind_turbines/dataset/wind_turbines_.csv', index=False)