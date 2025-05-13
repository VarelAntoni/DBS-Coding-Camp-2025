import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.extract import extract_fashion_data
from bs4 import BeautifulSoup

def test_extract_valid_html():
    html = """
    <div class="collection-card">
        <div class="product-details">
            <h3 class="product-title">Product Test</h3>
            <div class="price-container">
                <span class="price">$99.99</span>
            </div>
            <p>Rating: ⭐ 4.5 / 5</p>
            <p>3 Colors</p>
            <p>Size: M</p>
            <p>Gender: Unisex</p>
        </div>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    card = soup.find('div', class_='collection-card')
    result = extract_fashion_data(card)
    assert result["Title"] == "Product Test"
    assert "$" in result["Price"]
    assert "Rating" in result
