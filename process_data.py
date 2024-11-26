def preprocess_data(df):
    # Convert timestamp to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Any additional preprocessing like handling missing data can be done here
    return df

cleaned_data = preprocess_data(climate_df)
print(cleaned_data)
