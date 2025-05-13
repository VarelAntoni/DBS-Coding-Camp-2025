import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.extract import extract_fashion_data

import pandas as pd
from utils.transform import transform_data

def test_transform_data_structure():
    raw = [{
        "Title": "Test Shirt",
        "Price": "$100.00",
        "Rating": "Rating: ⭐ 4.0 / 5",
        "Colors": "2 Colors",
        "Size": "Size: L",
        "Gender": "Gender: Men",
        "Timestamp": "2025-05-13T18:00:00"
    }]
    df = pd.DataFrame(raw)
    transformed = transform_data(df)
    
    assert transformed["Price"].dtype == float
    assert transformed["Rating"].dtype == float
    assert transformed["Colors"].dtype == int
