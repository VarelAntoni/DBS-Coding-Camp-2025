# Laporan Proyek Machine Learning - [Muhammad Varel Antoni]

## Project Overview

Rekomendasi film merupakan salah satu aplikasi machine learning yang sangat populer di platform streaming dan e-commerce media hiburan. Dengan jutaan film dan pengguna, memberikan rekomendasi yang relevan dan personal menjadi tantangan utama dalam meningkatkan pengalaman pengguna dan retensi pelanggan.

Dalam proyek ini digunakan dataset dari Kaggle: [Movie Recommendation System Dataset by parasharmanas](https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system), yang terdiri dari metadata film dan histori rating pengguna. Sistem rekomendasi dibangun dengan dua pendekatan utama: content-based filtering dan collaborative filtering berbasis embedding neural network.

Sistem rekomendasi ini bertujuan menyajikan film yang sesuai preferensi pengguna berdasarkan histori interaksi dan konten film, membantu mengatasi information overload.

Referensi:

- Ricci, F., Rokach, L., Shapira, B., & Kantor, P. B. (2011). *Recommender Systems Handbook*. Springer.

---

## Business Understanding

### Problem Statements

- Bagaimana membangun sistem rekomendasi film yang dapat menyesuaikan dengan preferensi, minat, atau perilaku pengguna?
- Bagaimana mengevaluasi kinerja dan hasil dari model dalam mengembangkan sistem rekomendasi film yang disesuaikan dengan preferensi, minat, atau perilaku pengguna?

### Goals

- Mengembangkan sistem rekomendasi yang dapat menyesuaikan preferensi pengguna.
- Mengevaluasi performa dua pendekatan (content-based dan collaborative) menggunakan metrik evaluasi yang relevan.

### Solution Approach

#### 1. Content-Based Filtering

- Menggunakan TF-IDF pada kolom `genres`.
- Menghitung cosine similarity antar film berdasarkan genre.
- Memberikan rekomendasi berdasarkan film yang memiliki kemiripan konten.

#### 2. Collaborative Filtering (Neural Network)

- Menggunakan embedding layer untuk user dan movie.
- Model prediksi rating berdasarkan representasi vektor user dan item.
- Optimizer: Adam, loss function: binary crossentropy.

---

## Data Understanding

Dataset berasal dari [Kaggle](https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system), terdiri dari dua file:

| File         | Deskripsi                                    |
|--------------|----------------------------------------------|
| `movies.csv` | ID film, judul film, dan genre               |
| `ratings.csv`| Interaksi user (userId, movieId, rating, timestamp) |

Dataset tidak memiliki missing values penting dan siap diproses.

---

## Data Preparation

Langkah-langkah preprocessing meliputi:

1. Ekstraksi tahun rilis dari `title`.
2. Penghapusan genre kosong atau “(no genres listed)”.
3. Encoding `userId` dan `movieId` menjadi index numerik.
4. Normalisasi rating ke rentang [0, 1].
5. Split data menjadi train dan validation.
6. Penerapan TF-IDF vectorization pada genre.

---

## Modeling

### 1. Content-Based Filtering

- Menggunakan TF-IDF vektorisasi pada genre.
- Menghitung cosine similarity antar film.
- Rekomendasi berdasarkan film yang mirip dengan film yang disukai pengguna.

Contoh output:
![Prediction Content-Based](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/raw/main/Machine_Learning_Terapan/Proyek_Akhir/images/prediction_content-based.png)

### 2. Collaborative Filtering 

- Embedding untuk user dan film.
- Model `RecommenderNet` dengan input user dan film encoded.
- Mengoutputkan prediksi rating menggunakan sigmoid.

Contoh output:
![Prediction Collaborative](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/raw/main/Machine_Learning_Terapan/Proyek_Akhir/images/prediction_collaborative.png)

---

## Evaluation

### 1. Content-Based Filtering

Evaluasi dilakukan menggunakan metrik:

- **Precision@10** – menghitung proporsi film yang direkomendasikan yang benar-benar relevan.

Visualisasi precision:
![Precision@10 Content-Based](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/raw/main/Machine_Learning_Terapan/Proyek_Akhir/images/Precision@10_content-based.png)

Visualisasi loss training:
![Loss Content-Based](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/raw/main/Machine_Learning_Terapan/Proyek_Akhir/images/Loss_content-based.png)

Visualisasi RMSE:
![RMSE Content-Based](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/raw/main/Machine_Learning_Terapan/Proyek_Akhir/images/RMSE-content_based.png)

**Interpretasi:**
- Precision mendekati 1 menandakan sistem menghasilkan rekomendasi yang sangat relevan.
- RMSE training yang rendah menunjukkan model bisa mempelajari pola rating dengan baik.

---

### 2. Collaborative Filtering

Evaluasi juga dilakukan dengan:

- **Precision@10** – relevansi top-N prediksi
- **Root Mean Squared Error (RMSE)** – untuk menghitung rata-rata deviasi prediksi rating terhadap nilai asli.

Visualisasi precision:
![Precision@10 Collaborative](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/raw/main/Machine_Learning_Terapan/Proyek_Akhir/images/Precision@10_collaborative.png)

Visualisasi loss training:
![Loss Collaborative](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/raw/main/Machine_Learning_Terapan/Proyek_Akhir/images/Loss-collaborative.png)

Visualisasi RMSE:
![RMSE Collaborative](https://github.com/VarelAntoni/DBS-Coding-Camp-2025/raw/main/Machine_Learning_Terapan/Proyek_Akhir/images/RMSE-collaborative.png)

**Interpretasi:**
- RMSE validasi rendah (~0.22) menunjukkan performa model yang baik dalam prediksi rating.
- Perbedaan train vs validation loss kecil, mengindikasikan tidak terjadi overfitting signifikan.

---

## Conclusion

- **Content-Based Filtering** unggul dalam cold-start user, menghasilkan rekomendasi berbasis kesamaan konten.
- **Collaborative Filtering** memberikan hasil lebih personal berdasarkan histori interaksi, cocok untuk pengguna dengan riwayat rating yang kaya.
- Kombinasi kedua pendekatan direkomendasikan untuk sistem rekomendasi yang optimal dalam skala besar.

