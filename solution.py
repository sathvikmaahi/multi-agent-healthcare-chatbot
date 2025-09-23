import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class AnalysisDataAndFitLinearRegression:
    def __init__(self):
        self.version = 1
    
    def analyse_and_fit_lrm(self, path):
        # Load the dataset
        data = pd.read_csv(path)
        
        # Replace 'NA' strings with proper NaN values
        data = data.replace('NA', np.nan)
        
        # Convert all columns to numeric
        numeric_columns = ['Price', 'Bedroom', 'Space', 'Room', 'Lot', 'Tax', 'Bathroom', 'Garage', 'Condition']
        for col in numeric_columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')
        
        # Remove only completely empty rows (all NaN) for initial analysis
        data_partial = data.dropna(how='all')
        
        # 1. Calculate statistics for houses with 2 bathrooms and 4 bedrooms
        filtered_data = data_partial[(data_partial['Bathroom'] == 2.0) & (data_partial['Bedroom'] == 4.0)]
        
        # Ensure we have data after filtering and handle missing Tax values
        if len(filtered_data) == 0:
            # Handle case where no data matches criteria
            tax_stats = [0.0, 0.0, 0.0, 0.0, 0.0]
        else:
            # Remove rows with missing Tax values for statistics calculation
            tax_data = filtered_data['Tax'].dropna()
            if len(tax_data) == 0:
                tax_stats = [0.0, 0.0, 0.0, 0.0, 0.0]
            else:
                tax_stats = [
                    round(float(tax_data.mean())),
                    round(float(tax_data.std())),
                    round(float(tax_data.median())),
                    round(float(tax_data.min())),
                    round(float(tax_data.max()))
                ]
        
        # 2. Create data frame where Space > 800, ordered by decreasing Price
        space_filtered = data_partial[data_partial['Space'] > 800.0].copy()
        space_filtered = space_filtered.sort_values('Price', ascending=False)
        
        # 3. Calculate number of observations where Lot >= 4th quantile
        # Only consider rows with valid Lot values for this calculation
        lot_valid = data_partial['Lot'].dropna()
        lot_q4 = lot_valid.quantile(0.75)  # 4th quantile is 75th percentile
        num_observations = int(len(lot_valid[lot_valid > lot_q4]))
        
        # 4. Fit linear regression model
        # Apply listwise deletion for regression model (complete cases only)
        data_for_model = self.__listwise_deletion(data_partial)
        
        # Prepare features (all variables except Price)
        feature_columns = ['Bedroom', 'Space', 'Room', 'Lot', 'Tax', 'Bathroom', 'Garage', 'Condition']
        
        # Reset index and convert to numpy arrays
        data_for_model = data_for_model.reset_index(drop=True)
        X = data_for_model[feature_columns].values  # Use .values to get numpy array
        y = data_for_model['Price'].values
        
        # Fit the model
        model = LinearRegression()
        model.fit(X, y)
        
        # Create model parameters dictionary with exact order
        model_parameters = {'Intercept': float(model.intercept_)}
        for i, feature in enumerate(feature_columns):
            model_parameters[feature] = float(model.coef_[i])
        
        # 5. Make prediction for specific house
        # House specs: 3 bedrooms, 1500 sq ft space, 8 rooms, lot width 40, $1000 tax, 
        # 2 bathrooms, 1 garage space, bad condition (0)
        # Order: ['Bedroom', 'Space', 'Room', 'Lot', 'Tax', 'Bathroom', 'Garage', 'Condition']
        house_features = np.array([[3.0, 1500.0, 8.0, 40.0, 1000.0, 2.0, 1.0, 0.0]])
        
        price_prediction = float(model.predict(house_features)[0])
        
        # Return the required dictionary structure
        result = {
            'summary_dict': {
                'statistics': tax_stats,
                'data_frame': space_filtered,
                'number_of_observations': num_observations
            },
            'regression_dict': {
                'model_parameters': model_parameters,
                'price_prediction': price_prediction
            }
        }
        
        return result
    
    def __listwise_deletion(self, data: pd.DataFrame):
        return data.dropna() 