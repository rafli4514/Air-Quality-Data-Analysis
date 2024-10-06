# Air Quality Dataset data analisis

## Deskripsi
Proyek ini adalah dashboard analisis polusi udara yang dibuat menggunakan Python dan Streamlit. Dashboard ini bertujuan untuk menampilkan tren polusi udara dari tahun ke tahun, 
lonjakan polusi sepanjang hari, serta hubungan antara kondisi cuaca (suhu, curah hujan, kecepatan angin) dengan tingkat polusi udara. Dengan menggunakan dataset yang memuat 
informasi kualitas udara, kami memberikan visualisasi yang dapat membantu memahami pola dan hubungan yang mempengaruhi kualitas udara.

## Struktur Direktori
- /data: berisi dataset yang digunakan dalam proyek ini dengan format file .csv.
- /dashboard: berisi dashboard.py yang digunakan untuk membuat dashboard dari hasil analisis data
- air_quality.ipynb: file yang digunakan untuk melakukan analisis data

## Langkah Instalasi
1. Clone repository ini ke komputer lokal menggunakan perintah:

```
git clone https://github.com/rafli4514/Air-Quality-Data-Analysis.git
```
 
2. Pastikan env python sudah terinstall library-library yang diperlukan sesuai dengan versinya. jika belum
   kamu dapat menginstallnya dengan perintah

```
pip install streamlit
pip install -r requirements.txt
```

## Cara menjalankan
1. Masuk kedalam direktori dashboard:
   ```
   cd Air-Quality-Data-Analysis/dashboard
   streamlit run dashboard.py
   ```
