# Laporan Proyek Machine Learning - Muhammad Varel Antoni

## Domain Proyek

Wine Quality Classification merupakan proyek yang bertujuan untuk mengklasifikasikan kualitas wine berdasarkan sifat-sifat kimianya. Industri wine sangat bergantung pada kualitas produk mereka, yang dinilai melalui proses pengujian oleh ahli. Namun, proses ini membutuhkan waktu dan sumber daya manusia yang tidak sedikit. Oleh karena itu, penggunaan machine learning dapat membantu mempercepat proses klasifikasi kualitas wine berdasarkan data kimia yang dikumpulkan dari produk tersebut.
Masalah ini penting diselesaikan karena:

Dapat mengurangi ketergantungan pada penilai manusia (wine tasters).
Menyediakan proses penilaian yang konsisten dan dapat diskalakan.
Memberikan nilai tambah bagi produsen dalam mengontrol kualitas produksi.

**Rubrik/Kriteria Tambahan (Opsional)**:

Referensi:
Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Modeling wine preferences by data mining from physicochemical properties. Decision Support Systems, 47(4), 547-553. https://doi.org/10.1016/j.dss.2009.05.016

## Business Understanding
### Problem Statements
- Bagaimana cara mengklasifikasikan kualitas wine (low, medium, high) berdasarkan fitur kimiawi seperti fixed_acidity, residual_sugar, alcohol, dan density?
- Algoritma machine learning apa yang paling efektif untuk memprediksi kualitas wine secara otomatis?

### Goals
- Mengembangkan model klasifikasi yang mampu memprediksi apakah wine berkualitas rendah, sedang, atau tinggi berdasarkan fitur-fitur kimiawinya.
- Membandingkan performa berbagai algoritma klasifikasi untuk menemukan model terbaik berdasarkan metrik evaluasi.

### Solution Statements
- Mengajukan tiga solusi dengan menggunakan:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - XGBoost Classifier
- Menggunakan metrik evaluasi: accuracy, precision, recall, dan F1-score.
- Memilih model terbaik berdasarkan performa pada data uji.
- Model yang overfit akan diidentifikasi berdasarkan gap akurasi train dan test.

## Data Understanding
Dataset berisi 1000 data wine dengan 5 fitur dan label kualitas.
Dataset diambil dari kaggle (https://www.kaggle.com/datasets/sahideseker/wine-quality-classification/data)
Berikut hasil df.info(): 

### Variabel-variabel:
- fixed_acidity: keasaman tetap
- residual_sugar: gula sisa
- alcohol: kandungan alkohol
- density: kepadatan
- quality_label: kualitas wine (low, medium, high) — label target

### Visualisasi Distribusi Label:
Distribusi kategori cukup seimbang, meskipun kelas low sedikit lebih sedikit dibanding medium dan high.

## Data Preparation
### Langkah-langkah data preparation:
1. Encoding: Menggunakan LabelEncoder untuk mengubah kategori quality_label menjadi nilai numerik.
2. Standardization: Menstandardisasi fitur numerik menggunakan StandardScaler.
3. Train-test split: Data dibagi menjadi 80% untuk pelatihan dan 20% untuk pengujian.

### Alasan tahapan dilakukan:
- Encoding diperlukan agar label dapat diproses oleh algoritma ML.
- Standardisasi penting untuk algoritma seperti SVM yang sensitif terhadap skala fitur.
- Split data diperlukan agar evaluasi dilakukan secara objektif dan tidak bias.

## Modeling
### Algoritma yang digunakan:
1. Logistic Regression
  - Baseline model
  - Mudah diinterpretasi
2. Support Vector Machine (SVM)
  - Cocok untuk klasifikasi margin jelas
  - Komputasi lebih berat
3. XGBoost
  - Efisien, menangani data non-linear
  - Cenderung menghasilkan akurasi tinggi

### Visualisasi akurasi train vs test:
Seluruh model menunjukkan akurasi 100% pada train dan test, menandakan data sangat terstruktur, bersih dan sederhana.

## Evaluation
### Metrik yang digunakan:
- Accuracy: Total prediksi benar / total data
- Precision: Kemampuan model menghindari false positive
- Recall: Kemampuan model mendeteksi semua kasus positif
- F1-Score: Harmonic mean dari precision dan recall

### Formula:
- Accuracy = (TP + TN) / (TP + TN + FP + FN)
- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1 Score = 2 * (Precision * Recall) / (Precision + Recall)

### Hasil Proyek:
- Logistic Regression: Accuracy = 100%
- SVM: Accuracy = 100%
- XGBoost: Accuracy = 100%

**---Ini adalah bagian akhir laporan---**
