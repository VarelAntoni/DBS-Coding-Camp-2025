# Laporan Proyek Machine Learning - Muhammad Varel Antoni

## Project Overview

Rekomendasi musik telah menjadi fitur penting dalam industri streaming modern seperti Spotify, YouTube Music, dan Apple Music. Seiring bertambahnya jumlah lagu secara eksponensial, pengguna menghadapi tantangan dalam menemukan musik yang sesuai dengan preferensi mereka. Untuk itu, dibutuhkan sistem rekomendasi yang dapat memberikan saran lagu secara relevan dan personal.

Menurut [Schedl et al., 2015](https://ieeexplore.ieee.org/document/7120121), sistem rekomendasi musik dapat meningkatkan kepuasan pengguna dan engagement secara signifikan. Dalam proyek ini, dikembangkan sistem rekomendasi musik menggunakan dua pendekatan: **Content-Based Filtering** dan **Collaborative Filtering**, berdasarkan dataset Spotify yang diambil dari [Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset).

## Business Understanding

Sistem rekomendasi yang efektif dapat meningkatkan retensi pengguna dan waktu penggunaan aplikasi, sekaligus memberikan pengalaman yang lebih personal dan menyenangkan.

### Problem Statements

- Bagaimana merekomendasikan lagu yang mirip dengan lagu favorit pengguna berdasarkan karakteristik audio?
- Bagaimana memprediksi lagu yang belum pernah didengar oleh pengguna, tetapi kemungkinan besar akan disukai?

### Goals

- Menghasilkan daftar lagu mirip secara konten dengan lagu favorit pengguna.
- Mengembangkan sistem prediksi lagu baru berdasarkan pola rating dari pengguna lain.

### Solution Statements

- Menggunakan **Content-Based Filtering** dengan pendekatan **cosine similarity** antar fitur audio (danceability, energy, valence, dll).
- Menerapkan **Collaborative Filtering** menggunakan algoritma **KNNBasic** dari library `Surprise` untuk mempelajari interaksi user-item.

## Data Understanding

Dataset digunakan berasal dari: [Spotify Tracks Dataset - Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)  
Jumlah lagu dalam dataset asli >300.000, tetapi diambil **20.000 sampel** untuk efisiensi komputasi.

### Fitur-Fitur Utama:
- `track_id`: ID unik setiap lagu
- `track_name`: judul lagu
- `artists`: nama artis
- `danceability`, `energy`, `valence`, `tempo`, `acousticness`, `instrumentalness`: fitur numerik dari audio
- `track_genre`: genre dari lagu

Dataset memiliki beberapa missing value dan duplikat, khususnya pada kolom `Unnamed: 0` dan beberapa ID track, yang telah dibersihkan sebelum modeling.

## Data Preparation

Langkah-langkah yang dilakukan sebelum pelatihan model:
1. Sampling 20.000 lagu dari dataset utama.
2. Menghapus kolom tidak relevan (`Unnamed: 0`) dan nilai kosong.
3. Menghapus duplikat berdasarkan `track_id`.
4. Normalisasi fitur numerik (`danceability`, `energy`, dll) menggunakan `StandardScaler`.
5. Simulasi interaksi pengguna:
   - Dibuat 50 user fiktif
   - Setiap user memberikan rating 10–30 lagu secara acak dengan skor 1–5

Langkah ini penting agar data yang digunakan bersih, terstruktur, dan dapat digunakan untuk dua jenis pendekatan filtering.

## Modeling

### Content-Based Filtering

Model content-based menghitung cosine similarity antar lagu berdasarkan fitur audio. Fungsi `recommend_tracks(track_name)` digunakan untuk menghasilkan rekomendasi berdasarkan kemiripan konten lagu.

**Hasil:**

![Content-Based Filtering](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/content-based_filtering.png?raw=true)

**Visualisasi:**

![Content-Based Visualized](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/content-based_visualized.png?raw=true)

---

### Collaborative Filtering

Menggunakan `KNNBasic` dari Surprise untuk membuat prediksi rating lagu-lagu yang belum didengarkan oleh user, kemudian memilih lagu dengan estimasi tertinggi.

**Hasil:**

![Collaborative Filtering](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/collaborative_filtering.png?raw=true)

**Visualisasi:**

![Collaborative Visualized](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/collaborative_visualized.png?raw=true)

---

### Combine Filtering

Menggabungkan hasil dari dua pendekatan untuk dilihat dalam satu tabel:

**Hasil:**

![Combine Filtering](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/combine_filtering.png?raw=true)

---

### Compare Filtering

Perbandingan jumlah hasil rekomendasi dari masing-masing pendekatan:

**Visualisasi:**

![Compare Filtering](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/compare_filtering.png?raw=true)

## Evaluation

Evaluasi dilakukan menggunakan dua pendekatan:

- **Content-Based**: dievaluasi secara kualitatif (genre/artis serupa)
- **Collaborative Filtering**: dievaluasi secara kuantitatif menggunakan RMSE

Tambahan metrik:
- **Precision@5**: Mengukur berapa banyak lagu yang relevan dari 5 lagu yang direkomendasikan
- **Recall@5**: Mengukur berapa banyak lagu relevan dari total lagu yang disukai user yang berhasil direkomendasikan

**Hasil Precision dan Recall:**

![Precision & Recall](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/precision_recall.png?raw=true)

---

## Kesimpulan

Sistem rekomendasi ini membuktikan bahwa pendekatan berbasis konten dapat memberikan hasil yang cepat dan konsisten, terutama untuk lagu-lagu dengan fitur audio yang dominan. Sementara itu, pendekatan collaborative filtering lebih personal karena mempertimbangkan preferensi pengguna lain, tetapi membutuhkan cukup banyak data interaksi pengguna. Kedua pendekatan saling melengkapi dan idealnya dapat digabungkan dalam sistem produksi untuk meningkatkan akurasi dan relevansi rekomendasi.

---
