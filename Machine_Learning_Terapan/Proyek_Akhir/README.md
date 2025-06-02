# Laporan Proyek Machine Learning - Muhammad Varel Antoni

## Project Overview

Dalam era digital saat ini, platform streaming musik seperti Spotify memiliki jutaan lagu. Hal ini sering kali membuat pengguna merasa kewalahan dalam menemukan lagu yang sesuai dengan selera mereka. Oleh karena itu, sistem rekomendasi berperan penting dalam meningkatkan pengalaman pengguna dan menjaga loyalitas mereka. Berdasarkan studi oleh Ricci et al. (2015), sistem rekomendasi terbukti meningkatkan engagement dan retensi pengguna dalam platform berbasis konten digital. Proyek ini bertujuan membangun dua jenis sistem rekomendasi: Content-Based Filtering dan Collaborative Filtering, menggunakan dataset dari Kaggle yang berisi metadata dan fitur audio dari lebih dari 300.000 lagu Spotify [^1].

[^1]: M. Pandya, "Spotify Tracks Dataset", Kaggle, [Online]. Available: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

## Business Understanding

Sistem rekomendasi dapat memberikan dampak besar pada kepuasan pengguna dengan cara mengurangi beban pencarian dan meningkatkan personalisasi pengalaman.

### Problem Statements

- Bagaimana cara merekomendasikan lagu yang mirip dengan lagu favorit pengguna berdasarkan fitur audio?
- Bagaimana cara memprediksi lagu yang mungkin disukai pengguna meskipun belum pernah didengarkan sebelumnya?

### Goals

- Menghasilkan rekomendasi lagu serupa berdasarkan kemiripan fitur audio (content-based).
- Mengembangkan sistem yang dapat memberikan rekomendasi lagu berdasarkan preferensi pengguna lain (collaborative filtering).

### Solution Statements

- **Pendekatan 1:** Content-Based Filtering menggunakan cosine similarity antara fitur seperti `danceability`, `energy`, `valence`, `tempo`, dll.
- **Pendekatan 2:** Collaborative Filtering menggunakan algoritma `KNNBasic` dari pustaka `Surprise`, berdasarkan simulasi interaksi pengguna.

## Data Understanding

Dataset digunakan dari Kaggle dan memuat lebih dari 300.000 lagu. Untuk efisiensi, hanya digunakan 20.000 data lagu.

Link dataset: [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)

### Fitur utama pada dataset:
- `track_id`: ID unik lagu
- `track_name`: judul lagu
- `artists`: artis pembuat lagu
- `track_genre`: genre dari lagu
- `popularity`: tingkat popularitas
- Fitur audio seperti `danceability`, `energy`, `acousticness`, `valence`, `tempo`, `instrumentalness`, dll.

Dataset ini mengandung beberapa missing values dan duplikat yang dibersihkan pada tahap selanjutnya.

## Data Preparation

Langkah-langkah preprocessing dilakukan sebagai berikut:

1. **Sampling data:** Mengambil 20.000 lagu secara acak.
2. **Cleaning data:** Menghapus kolom tidak relevan seperti `Unnamed: 0`, menghapus duplikat berdasarkan `track_id`, dan menghapus missing values.
3. **Feature scaling:** Menormalkan fitur numerik menggunakan `StandardScaler`.
4. **Simulasi interaksi pengguna:** Membuat 50 user fiktif, masing-masing memberikan rating acak pada 10–30 lagu sebagai data training collaborative filtering.

Tahapan ini bertujuan memastikan data konsisten, relevan, dan siap diproses oleh algoritma pemodelan.

## Modeling

### Content-Based Filtering

Model menghitung cosine similarity antar lagu berdasarkan fitur audio. Hasil rekomendasi diperoleh dengan mengambil lagu dengan skor kemiripan tertinggi terhadap input.

**Hasil:**

![Content-Based Filtering](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/content-based_filtering.png?raw=true)

**Visualisasi:**

![Content-Based Visualized](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/content-based_visualized.png?raw=true)

### Collaborative Filtering

Model menggunakan `KNNBasic` dari `Surprise` dengan pendekatan user-based. Dataset yang disimulasikan menjadi matriks user-item untuk memprediksi rating lagu yang belum diberi rating.

**Hasil:**

![Collaborative Filtering](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/collaborative_filtering.png?raw=true)

**Visualisasi:**

![Collaborative Visualized](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/collaborative_visual
