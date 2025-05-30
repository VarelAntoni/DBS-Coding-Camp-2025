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

**Contoh output:**
Rekomendasi lagu mirip dengan *"I'm Ready - Radio Edit"*:
- B2B - James Hope-Tita Lau
- Push Me - Neopolitan
- etc.

### Collaborative Filtering

Menggunakan `KNNBasic` dari Surprise (user-based). Dataset simulasi `df_ratings` digunakan sebagai input. Model memprediksi rating lagu-lagu yang belum dirating oleh user, dan mengembalikan lagu dengan skor tertinggi.

**Contoh output:**
Rekomendasi untuk user_10:
- Psyche-Out - Meat Beat Manifesto
- Saku - Susumu Yokota
- etc.

## Evaluation

Untuk content-based, evaluasi dilakukan secara kualitatif (melihat kemiripan nama/artis/fitur lagu).
Untuk collaborative filtering, digunakan metrik RMSE dari Surprise:

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
