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

- Menggunakan **Content-Based Filtering** dengan pendekatan **cosine similarity** antar fitur audio (`danceability`, `energy`, `valence`, dll).
- Menerapkan **Collaborative Filtering** menggunakan algoritma **KNNBasic** dari library `Surprise` untuk mempelajari interaksi user-item.

## Data Understanding

Dataset digunakan berasal dari: [Spotify Tracks Dataset - Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)  
Jumlah lagu dalam dataset asli lebih dari 300.000, namun diambil **20.000 sampel** untuk efisiensi komputasi.

### Fitur-Fitur Utama:
- `track_id`: ID unik setiap lagu
- `track_name`: Judul lagu
- `artists`: Nama artis
- `danceability`, `energy`, `valence`, `tempo`, `acousticness`, `instrumentalness`: Fitur numerik dari audio
- `track_genre`: Genre dari lagu

Dataset memiliki beberapa missing value dan duplikat, khususnya pada kolom `Unnamed: 0` dan beberapa `track_id`, yang telah dibersihkan sebelum modeling.

## Data Preparation

Langkah-langkah yang dilakukan sebelum pelatihan model:
1. Sampling 20.000 lagu dari dataset utama.
2. Menghapus kolom tidak relevan (`Unnamed: 0`) dan nilai kosong.
3. Menghapus duplikat berdasarkan `track_id`.
4. Normalisasi fitur numerik (`danceability`, `energy`, dll) menggunakan `StandardScaler`.
5. Simulasi interaksi pengguna:
   - Dibuat 50 user fiktif.
   - Setiap user memberikan rating 10–30 lagu secara acak dengan skor 1–5.

Langkah ini penting agar data yang digunakan bersih, terstruktur, dan dapat digunakan untuk dua jenis pendekatan filtering.

## Modeling

### Content-Based Filtering

**Tujuan:**  
Memberikan rekomendasi lagu berdasarkan kemiripan fitur-fitur audio dari lagu favorit pengguna.

**Metode:**  
Menggunakan cosine similarity antar vektor fitur numerik (`danceability`, `energy`, `valence`, dll). Cosine similarity mengukur sudut antara dua vektor dalam ruang berdimensi tinggi, yang digunakan untuk menentukan kemiripan antar lagu.

**Langkah-langkah:**
1. Normalisasi fitur audio menggunakan `StandardScaler`.
2. Hitung cosine similarity antara lagu input dan seluruh lagu lainnya.
3. Urutkan berdasarkan skor similarity tertinggi.
4. Ambil Top-N sebagai hasil rekomendasi.

**Visualisasi:**

- Cosine similarity:
  
  ![Content-Based Filtering](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/content-based_filtering.png?raw=true)

- Visualisasi distribusi fitur:

  ![Content-Based Visualized](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/content-based_visualized.png?raw=true)

**Kelebihan:**
- Tidak memerlukan data pengguna lain.
- Cocok untuk cold-start pengguna baru.

**Kekurangan:**
- Tidak mempertimbangkan selera kolektif.
- Terbatas pada fitur konten yang tersedia.

---

### Collaborative Filtering

**Tujuan:**  
Memprediksi lagu-lagu yang disukai pengguna berdasarkan pola rating dari pengguna lain.

**Metode:**  
Menggunakan pendekatan memory-based collaborative filtering dengan algoritma **KNNBasic** dari library `Surprise`. Metode ini membandingkan kemiripan antar item (lagu) berdasarkan rating yang diberikan oleh pengguna.

**Langkah-langkah:**
1. Bentuk matriks interaksi user-item dari hasil simulasi pengguna.
2. Latih model `KNNBasic` dengan cosine similarity (`user_based=False`).
3. Lakukan prediksi rating lagu yang belum dirating oleh user.
4. Ambil lagu dengan estimasi rating tertinggi sebagai rekomendasi.

**Visualisasi:**

- Prediksi rating lagu:

  ![Collaborative Filtering](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/collaborative_filtering.png?raw=true)

- Top-N rekomendasi hasil prediksi:

  ![Collaborative Visualized](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/collaborative_visualized.png?raw=true)

**Kelebihan:**
- Menghasilkan rekomendasi yang lebih personal.
- Menggunakan pola kolektif seluruh pengguna.

**Kekurangan:**
- Tidak cocok untuk pengguna baru atau lagu baru (cold-start).
- Bergantung pada data interaksi.

---

### Combine Filtering

**Tujuan:**  
Menggabungkan hasil dari content-based dan collaborative filtering untuk memperkaya kualitas rekomendasi.

**Metode:**  
Gabungkan daftar rekomendasi dari kedua pendekatan. Hasil bisa disortir berdasarkan skor gabungan, skor tertinggi, atau frekuensi kemunculan.

**Visualisasi:**

![Combine Filtering](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/combine_filtering.png?raw=true)

---

### Compare Filtering

Perbandingan dilakukan untuk mengetahui performa masing-masing pendekatan dalam hal jumlah rekomendasi dan variasinya.

**Visualisasi:**

![Compare Filtering](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/blob/main/Machine_Learning_Terapan/Proyek_Akhir/images/compare_filtering.png?raw=true)

---

## Evaluation

Evaluasi dilakukan untuk menilai efektivitas sistem rekomendasi berdasarkan dua pendekatan: Content-Based Filtering dan Collaborative Filtering.

### 1. Content-Based Filtering

Pendekatan ini dievaluasi secara **kualitatif** dengan memeriksa kesesuaian genre, artis, dan karakteristik audio antara lagu input dan lagu yang direkomendasikan. Selain itu, metrik berikut digunakan:

- **Precision@5**: Mengukur persentase lagu yang relevan dari 5 rekomendasi teratas.
- **Recall@5**: Mengukur seberapa banyak lagu relevan yang berhasil direkomendasikan dari total lagu yang disukai.

Hasil menunjukkan bahwa rekomendasi memiliki kemiripan tinggi terhadap lagu input, dengan Precision dan Recall yang cukup tinggi (Precision@5 ≈ 0.80, Recall@5 ≈ 0.67).

### 2. Collaborative Filtering

Evaluasi dilakukan secara **kuantitatif** menggunakan:

- **Root Mean Squared Error (RMSE)**: Mengukur rata-rata selisih kuadrat antara rating yang diprediksi dan aktual. Nilai RMSE yang diperoleh berada di kisaran **0.32 – 0.36**, menandakan performa prediksi yang baik.
- **Precision@5 dan Recall@5**: Diterapkan dengan membandingkan prediksi Top-5 lagu terhadap data rating asli pengguna.

### 3. Perbandingan

| Metode               | Evaluasi       | Skor Utama   | Kelebihan                                 | Kelemahan                              |
|---------------------|----------------|--------------|-------------------------------------------|----------------------------------------|
| Content-Based       | Precision@5    | ~0.80        | Stabil, cocok untuk pengguna baru         | Tidak mempertimbangkan perilaku user lain |
| Collaborative       | RMSE, P@5, R@5 | RMSE ~0.33   | Lebih personal dan adaptif                | Butuh data interaksi (cold-start issue) |

Gabungan kedua pendekatan menghasilkan sistem rekomendasi yang lebih seimbang antara relevansi konten dan preferensi pengguna.

## Kesimpulan

Sistem rekomendasi yang dikembangkan dalam proyek ini berhasil menunjukkan bahwa:

- **Content-Based Filtering** mampu memberikan hasil cepat dan konsisten, cocok untuk pengguna baru.
- **Collaborative Filtering** menghasilkan rekomendasi yang lebih personal berdasarkan perilaku pengguna lain.
- **Gabungan kedua metode** memberikan cakupan rekomendasi yang lebih kuat dan relevan.

Penerapan kedua pendekatan secara bersamaan dapat meningkatkan kualitas sistem rekomendasi dalam skenario dunia nyata.

---

