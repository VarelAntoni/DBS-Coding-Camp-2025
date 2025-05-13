import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.extract import extract_fashion_data
import pandas as pd
from utils.load import save_to_csv
import os

def test_save_to_csv_creates_file(tmp_path):
    df = pd.DataFrame([{"Title": "X", "Price": 100, "Rating": 4.5, "Colors": 3, "Size": "M", "Gender": "Men", "Timestamp": "2025-05-13"}])
    file_path = tmp_path / "test_output.csv"
    save_to_csv(df, file_path)
    
    assert os.path.exists(file_path)
    assert file_path.read_text().startswith("Title,Price,Rating")
