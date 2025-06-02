# Laporan Proyek Machine Learning - Muhammad Varel Antoni

## Project Overview

Rekomendasi musik merupakan fitur penting dalam platform streaming modern seperti Spotify. Dengan jumlah lagu yang sangat besar, pengguna sering mengalami kesulitan menemukan lagu yang sesuai dengan selera mereka. Untuk itu, sistem rekomendasi dibutuhkan agar dapat menyarankan lagu yang relevan dan dipersonalisasi. Dalam proyek ini, kami membangun dua pendekatan utama: Content-Based Filtering dan Collaborative Filtering untuk merekomendasikan lagu dari dataset Spotify. Dataset diambil dari Kaggle: [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset), yang memuat lebih dari 300.000 lagu dengan fitur audio dan metadata.

## Business Understanding

Rekomendasi yang tepat dapat meningkatkan retensi pengguna dan pengalaman personalisasi. Tujuan dari proyek ini adalah mengembangkan sistem yang bisa menyarankan lagu-lagu yang relevan berdasarkan kesamaan konten dan perilaku pengguna.

### Problem Statements

- Bagaimana cara merekomendasikan lagu yang mirip dengan lagu favorit pengguna?
- Bagaimana sistem dapat memprediksi lagu yang belum pernah didengar pengguna, tetapi kemungkinan disukai?

### Goals

- Membangun sistem Content-Based Filtering yang merekomendasikan lagu serupa berdasarkan fitur audio.
- Mengembangkan sistem Collaborative Filtering yang memprediksi lagu berdasarkan interaksi pengguna.

### Solution Statements

- **Content-Based Filtering:** menggunakan cosine similarity pada fitur seperti danceability, energy, valence, dll.
- **Collaborative Filtering:** menggunakan algoritma KNNBasic dari Surprise untuk merekomendasikan lagu berdasarkan rating pengguna.

## Data Understanding

Dataset berasal dari Kaggle dan mencakup lebih dari 300.000 lagu. Dalam proyek ini, kami menggunakan 20.000 sampel untuk efisiensi memori di Google Colab.

Fitur utama:
- `track_id`: ID unik lagu
- `track_name`: judul lagu
- `artists`: artis pembuat
- `danceability`, `energy`, `valence`, `tempo`, dll: fitur numerik audio dari Spotify API
- `popularity`: seberapa populer lagu tersebut
- `track_genre`: genre dari lagu

Contoh eksplorasi awal:
- Kolom numerik dinormalisasi menggunakan `StandardScaler`
- Kolom `Unnamed: 0` dihapus
- Duplikasi dan missing value ditangani terlebih dahulu

## Data Preparation

Langkah-langkah yang dilakukan:
1. **Sampling data** sebanyak 20.000 lagu dari keseluruhan dataset.
2. **Menghapus kolom tidak relevan** seperti `Unnamed: 0`.
3. **Drop missing values** dan duplikat berdasarkan `track_id`.
4. **Normalisasi fitur numerik** dengan `StandardScaler`.
5. **Simulasi interaksi pengguna**: Membuat 50 pengguna fiktif yang merating 10–30 lagu acak dengan skor 1–5.

Proses ini penting agar model bisa mempelajari pola dari data bersih, terstruktur, dan terukur.

## Modeling

### Content-Based Filtering

Model ini menggunakan fitur audio seperti `danceability`, `energy`, `acousticness`, dll. Cosine similarity dihitung antar semua lagu, dan fungsi `recommend_tracks(track_name)` dibuat untuk memberikan 5 lagu yang paling mirip dengan input pengguna.

**Contoh kode:**

![Content-Based Filtering](Machine_Learning_Terapan/Proyek_Akhir/images/content-based_filtering.png)

**Visualisasi:**

![Content-Based Visualized](Machine_Learning_Terapan/Proyek_Akhir/images/content-based_visualized.png)

### Collaborative Filtering

Menggunakan `KNNBasic` dari Surprise (user-based). Dataset simulasi `df_ratings` digunakan sebagai input. Model memprediksi rating lagu-lagu yang belum dirating oleh user, dan mengembalikan lagu dengan skor tertinggi.

**Contoh kode:**

![Collaborative Filtering](Machine_Learning_Terapan/Proyek_Akhir/images/collaborative_filtering.png)

**Visualisasi:**

![Collaborative Visualized](Machine_Learning_Terapan/Proyek_Akhir/images/collaborative_visualized.png)

### Combine Filtering

Untuk menunjukkan kedua pendekatan secara berdampingan, hasil rekomendasi dari content-based dan collaborative digabung ke dalam satu tabel.

**Tabel Gabungan:**

![Combine Filtering](Machine_Learning_Terapan/Proyek_Akhir/images/combine_filtering.png)

### Compare Filtering

Perbandingan visual jumlah rekomendasi yang berasal dari masing-masing metode.

![Compare Filtering](Machine_Learning_Terapan/Proyek_Akhir/images/compare_filtering.png)

## Evaluation

Evaluasi dilakukan secara kualitatif untuk content-based (dengan melihat kemiripan fitur dan genre), serta secara kuantitatif untuk collaborative filtering menggunakan metrik RMSE.

Untuk mengukur efektivitas sistem, juga dihitung Precision@k dan Recall@k dari hasil rekomendasi.

**Visualisasi Precision & Recall:**

![Precision & Recall](Machine_Learning_Terapan/Proyek_Akhir/images/precision_recall.png)

---

## Kesimpulan

Proyek ini menunjukkan bagaimana dua pendekatan berbeda dalam sistem rekomendasi dapat saling melengkapi. Content-based cocok untuk memberikan lagu mirip dengan lagu yang disukai pengguna, sementara collaborative filtering membantu memberikan lagu baru yang mungkin disukai berdasarkan kesamaan selera dengan pengguna lain.

---

> _Catatan:_
> Anda dapat menjalankan proyek ini melalui file notebook utama `Proyek_Akhir_Machine_Learning.ipynb`. Dataset dan gambar-gambar berada di dalam struktur direktori `Proyek_Akhir/images/`.
