# Laporan Proyek Machine Learning - Muhammad Varel Antoni

## Domain Proyek

**Diabetes Prediction** adalah proyek yang bertujuan untuk mengklasifikasikan risiko diabetes pada pasien berdasarkan atribut kesehatan seperti usia, tekanan darah, kadar glukosa, dan faktor lainnya. Deteksi dini diabetes sangat penting untuk mencegah komplikasi yang lebih serius dan menurunkan beban pada sistem layanan kesehatan.

Masalah ini penting diselesaikan karena:

- Dapat membantu diagnosis dini dan pengobatan yang lebih tepat.
- Mengurangi beban rumah sakit melalui prediksi otomatis berbasis data.
- Meningkatkan efisiensi layanan kesehatan dengan sistem prediksi berbasis ML.

**Rubrik/Kriteria Tambahan (Opsional)**:

**Referensi:**  
Dataset: [https://www.kaggle.com/datasets/marshalpatel3558/diabetes-prediction-dataset-legit-dataset](https://www.kaggle.com/datasets/marshalpatel3558/diabetes-prediction-dataset-legit-dataset)

## Business Understanding

### Problem Statements

- Bagaimana cara mengklasifikasikan seseorang berisiko diabetes berdasarkan atribut seperti BMI, tekanan darah, dan riwayat keluarga?
- Algoritma machine learning apa yang paling efektif untuk memprediksi risiko diabetes secara otomatis?

### Goals

- Mengembangkan model klasifikasi yang mampu memprediksi risiko diabetes (Yes, No, Possible).
- Membandingkan performa berbagai algoritma klasifikasi untuk menentukan model terbaik.

### Solution Statements

- Mengajukan tiga solusi dengan menggunakan:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - XGBoost Classifier
- Menggunakan metrik evaluasi: accuracy, precision, recall, dan F1-score.
- Memilih model terbaik berdasarkan performa pada data uji.
- Model yang overfit akan diidentifikasi berdasarkan gap akurasi train dan test.

## Data Understanding

Dataset berisi data kesehatan dan demografis dari pasien untuk prediksi diabetes.

Dataset diambil dari Kaggle:  
[https://www.kaggle.com/datasets/marshalpatel3558/diabetes-prediction-dataset-legit-dataset](https://www.kaggle.com/datasets/marshalpatel3558/diabetes-prediction-dataset-legit-dataset)

Dataset memiliki 1000 baris dan 14 kolom. data juga tergolong bersih karena tidak memiliki missing value dan data duplikat.

### Variabel-variabel

- `ID`: Nomor identifikasi unik untuk setiap pasien
- `No_Pation`: Nomor pasien (mungkin internal atau administratif)
- `Gender`: Jenis kelamin pasien (F/M)
- `AGE`: Umur pasien
- `Urea`, `Cr`: Parameter fungsi ginjal
- `HbA1c`: Indikator kontrol gula darah jangka panjang
- `Chol`, `TG`, `HDL`, `LDL`, `VLDL`: Profil lipid
- `BMI`: Indeks massa tubuh
- `CLASS`: Label target untuk klasifikasi diabetes:
  - `Y`: Yes (positif diabetes)
  - `N`: No (negatif diabetes)
  - `P`: Possible (kemungkinan diabetes)


### Visualisasi Distribusi Label

Terdapat ketidakseimbangan distribusi kelas dengan dominasi kelas "Y", disertai pembersihan spasi dan penyesuaian kapitalisasi.

## Data Preparation

### Langkah-langkah data preparation

1. **pembersihan string**: Mengganti label f menjadi F
2. **Outlier Handling**: Menghapus data ekstrem berdasarkan IQR.
3. **Standardization**: Menstandardisasi fitur numerik menggunakan `StandardScaler`.
4. **Encoding**: Label target dan fitur kategorikal diubah menggunakan `LabelEncoder`.
5. **Train-test split**: Data dibagi 80% training, 20% testing.

### Alasan tahapan dilakukan

- Standardisasi penting untuk model seperti SVM.
- Encoding diperlukan untuk input model ML.
- Outlier bisa mengganggu model prediktif.
- Split data mencegah overfitting dan memastikan evaluasi objektif.

## Modeling

### Algoritma yang digunakan

1. **Logistic Regression**
   Logistic Regression adalah model klasifikasi linier yang digunakan untuk memprediksi probabilitas keanggotaan suatu kelas. Model ini bekerja dengan memetakan kombinasi linier dari fitur input ke dalam rentang probabilitas (antara 0 dan 1) menggunakan fungsi sigmoid (pada kasus biner) atau fungsi softmax (untuk multikelas). Model ini memaksimalkan log-likelihood, yaitu kemungkinan observasi data berdasarkan distribusi Bernoulli atau multinomial.
   
   Parameter Kunci: random_state=42, max_iter=200.
3. **Support Vector Machine (SVM)**
   Support Vector Machine adalah algoritma klasifikasi yang bekerja dengan mencari hyperplane (garis pemisah dalam ruang fitur) terbaik yang memisahkan data antar kelas dengan margin terbesar. Titik-titik data yang berada paling dekat dengan hyperplane disebut support vectors dan menjadi penentu utama dalam pembentukan batas keputusan.
   
   Parameter Kunci: kernel='linear', random_state=42.
5. **XGBoost**
   XGBoost adalah algoritma berbasis gradient boosting, yang membangun model secara berurutan. Setiap pohon keputusan yang baru akan mencoba memperbaiki kesalahan prediksi dari pohon sebelumnya dengan meminimalkan loss function menggunakan gradien dari error.
   
   Parameter Kunci: objective='multi:softmax', num_class=3, eval_metric='mlogloss', random_state=42, use_label_encoder=False.

### Visualisasi akurasi train vs test

Ketiga model menunjukkan akurasi training dan testing mendekati sempurna , menandakan dataset bersih dan model sangat mampu memisahkan kelas.

## Evaluation

### Metrik yang digunakan

- **Accuracy**: proporsi prediksi yang benar.
- **Precision**: mengukur seberapa akurat model saat memprediksi kelas positif.
- **Recall**: mengukur seberapa banyak kelas positif yang berhasil teridentifikasi.
- **F1-Score**: keseimbangan antara precision dan recall.

### Formula

- Accuracy = (TP + TN) / (TP + TN + FP + FN)
- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1 Score = 2 * (Precision * Recall) / (Precision + Recall)

### Hasil Proyek

- Logistic Regression
  - Accuracy : 0.9206
  - Precision: 0.9033
  - Recall   : 0.9206
  - F1-Score : 0.9106

- Support Vector Machine (SVM)
  - Accuracy : 0.9444
  - Precision: 0.9451
  - Recall   : 0.9444
  - F1-Score : 0.9446

- XGBoost
  - Accuracy : 0.9921
  - Precision: 0.9921
  - Recall   : 0.9921
  - F1-Score : 0.9917
    
## Summary

Model ini dikembangkan untuk memprediksi risiko diabetes (Yes, No, Possible), sebagai upaya mendukung deteksi dini dalam dunia medis. Evaluasi model menunjukkan bahwa:
- Semua problem statement terjawab:
  - Model berhasil mengklasifikasikan risiko dengan sangat baik.
  - Tiga model diuji dan dibandingkan untuk memilih yang paling andal.
- Goals proyek tercapai:
  - Akurasi tinggi (hingga 99%) menunjukkan model sangat layak diterapkan.
- Solusi yang dihasilkan berdampak:
  - Model XGBoost dapat membantu pengambilan keputusan medis secara otomatis.
  - Dengan recall 99%, potensi kesalahan dalam melewatkan kasus diabetes sangat kecil, sehingga bisa membantu mencegah keterlambatan penanganan.

---

**---Ini adalah bagian akhir laporan---**
