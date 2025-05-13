import pandas as pd

def transform_to_DataFrame(data):
    return pd.DataFrame(data)


def transform_data(df, exchange_rate=16000):
    try:
        dirty_patterns = {
            "Title": ["Unknown Product"],
            "Rating": ["Invalid Rating / 5", "Not Rated", None],
            "Price": ["Price Unavailable", None, ""]
        }

        for col, invalid_values in dirty_patterns.items():
            df = df[~df[col].isin(invalid_values)]

        df.dropna(inplace=True)

        # Clean Price
        df = df[df['Price'].str.strip() != '']
        df['Price'] = df['Price'].replace(r'[\$,]', '', regex=True).astype(float)
        df['Price'] = df['Price'] * exchange_rate  # float

        # Clean Rating
        df['Rating'] = df['Rating'].str.extract(r'([0-9.]+)').astype(float)

        # Clean Colors
        df['Colors'] = df['Colors'].str.extract(r'(\d+)').astype(int)

        # Clean Size & Gender
        df['Size'] = df['Size'].str.replace(r'Size:\s*', '', regex=True).astype('string')
        df['Gender'] = df['Gender'].str.replace(r'Gender:\s*', '', regex=True).astype('string')

        # Title
        df['Title'] = df['Title'].astype('string')

        # Timestamp (already string)
        df['Timestamp'] = df['Timestamp'].astype('string')

        df.drop_duplicates(inplace=True)
        df.reset_index(drop=True, inplace=True)

        return df

    except Exception as e:
        print(f"[ERROR] Transformasi gagal: {e}")
        return pd.DataFrame()
