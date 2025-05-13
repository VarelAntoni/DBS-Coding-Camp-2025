import pandas as pd

def save_to_csv(df, filename):
    try:
        df.to_csv(filename, index=False)
        print(f"✅ Data berhasil disimpan ke: {filename}")
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan ke CSV: {e}")


def save_to_postgresql(df, table_name, conn_string):
    try:
        from sqlalchemy import create_engine
        engine = create_engine(conn_string)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"✅ Data berhasil disimpan ke tabel PostgreSQL: {table_name}")
    except Exception as e:
        print(f"[ERROR] Gagal simpan ke PostgreSQL: {e}")


def save_to_google_sheets(df, spreadsheet_id, worksheet_name, credentials_json):
    try:
        import gspread
        from google.oauth2.service_account import Credentials

        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(credentials_json, scopes=scopes)
        client = gspread.authorize(creds)

        sheet = client.open_by_key(spreadsheet_id)
        worksheet = sheet.worksheet(worksheet_name)

        worksheet.clear()
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

        print(f"✅ Data berhasil disimpan ke Google Sheets: {worksheet_name}")
    except Exception as e:
        print(f"[ERROR] Gagal simpan ke Google Sheets: {e}")
