import pandas as pd
from utils.extract import scrape_fashion
from utils.transform import transform_data, transform_to_DataFrame
from utils.load import save_to_csv, save_to_postgresql, save_to_google_sheets


def main():
    BASE_URL = 'https://fashion-studio.dicoding.dev/page{}'

    # === EXTRACT ===
    all_data = scrape_fashion(BASE_URL, max_page=50)
    if not all_data:
        print("[INFO] Tidak ada data yang berhasil diambil.")
        return

    # === TRANSFORM ===
    df = transform_to_DataFrame(all_data)
    df = transform_data(df, exchange_rate=16000)
    if df.empty:
        print("[INFO] Data kosong setelah transformasi.")
        return

    # === EVALUASI SINGKAT ===
    print(f"\n✅ Total data bersih: {len(df)}")
    print(df.head())
    print(df.dtypes)

    # === LOAD ===
    # 1. Simpan ke CSV
    save_to_csv(df, "fashion_products.csv")

    # 2. Simpan ke PostgreSQL
    conn_string = "postgresql://developer:supersecretpassword@localhost:5432/fashiondb"
    save_to_postgresql(df, "fashion_products", conn_string)

    # 3. Simpan ke Google Sheets
    spreadsheet_id = "1FFadMEugsDg-GES8v_ObUO4O9z2zl74xAiDXQI9kFVI"
    worksheet_name = "fashiondb"
    credentials_path = "google-sheets-api.json"  

    save_to_google_sheets(df, spreadsheet_id, worksheet_name, credentials_path)


if __name__ == '__main__':
    main()
