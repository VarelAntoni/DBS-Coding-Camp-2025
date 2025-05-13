import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}


def fetching_content(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Gagal mengakses URL: {url} - {e}")
        return None


def extract_fashion_data(card):
    try:
        title_tag = card.find('h3', class_='product-title')
        price_tag = card.find('span', class_='price')
        p_tags = card.find_all('p')

        if not title_tag or not price_tag or len(p_tags) < 4:
            raise ValueError("Incomplete product data.")

        title = title_tag.text.strip()
        price = price_tag.text.strip()
        rating = p_tags[0].text.strip()
        colors = p_tags[1].text.strip()
        size = p_tags[2].text.strip()
        gender = p_tags[3].text.strip()
        timestamp = datetime.now().isoformat()

        return {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "Timestamp": timestamp
        }

    except Exception as e:
        print(f"[ERROR] Gagal ekstrak produk: {e}")
        return None



def scrape_fashion(base_url, start_page=1, max_page=50, delay=1):
    import time
    data = []

    try:
        for page_number in range(start_page, max_page + 1):
            url = base_url.format(page_number) if page_number > 1 else "https://fashion-studio.dicoding.dev"
            print(f"Scraping halaman: {url}")

            content = fetching_content(url)
            if content:
                soup = BeautifulSoup(content, "html.parser")
                cards = soup.find_all('div', class_='collection-card')

                for card in cards:
                    item = extract_fashion_data(card)
                    if item:
                        data.append(item)

                time.sleep(delay)
    except Exception as e:
        print(f"[ERROR] Kesalahan umum saat scraping: {e}")

    return data
