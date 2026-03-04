def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Example cleaning steps
    data = data.dropna()  # Remove missing values
    data = data.drop_duplicates()  # Remove duplicates
    # Add more cleaning steps as necessary
    return data

def save_processed_data(data, output_path):
    data.to_csv(output_path, index=False)