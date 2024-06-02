# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Nah, sebagai calon data scientist masa depan Anda diminta untuk membantu Jaya Jaya Institut dalam menyelesaikan permasalahannya. Mereka telah menyediakan dataset yang dapat Anda unduh melalui tautan berikut: [students' performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md). Selain itu, mereka juga meminta Anda untuk membuatkan dashboard agar mereka mudah dalam memahami data dan memonitor performa siswa.

### Permasalahan Bisnis
Mengidentifikasi Faktor Penyebab Dropout: Menentukan faktor-faktor kunci yang berkontribusi terhadap dropout siswa. Ini melibatkan identifikasi pola dan korelasi dalam dataset yang dapat memprediksi apakah seorang siswa berisiko berhenti belajar.

Deteksi Dini Siswa Berisiko: Mengembangkan model prediktif yang dapat mendeteksi siswa yang berisiko berhenti belajar di awal perjalanan akademik mereka. Hal ini akan memungkinkan institusi untuk melakukan intervensi tepat waktu.

Meningkatkan Retensi Siswa: Memberikan wawasan dan rekomendasi yang dapat ditindaklanjuti berdasarkan analisis untuk meningkatkan tingkat retensi siswa. Ini bisa mencakup intervensi spesifik atau sistem dukungan untuk siswa yang berisiko.

Pemantauan Kinerja: Membuat dashboard yang memungkinkan institusi untuk memantau kinerja siswa secara real-time. Dashboard ini harus menampilkan metrik dan tren kunci terkait kinerja siswa dan tingkat dropout.

### Cakupan Proyek
1. Eksplorasi dan Persiapan Data:
    - Memuat dan memeriksa dataset untuk memahami strukturnya dan isinya.
2. Membersihkan data dengan menangani nilai yang hilang, outlier, dan ketidakkonsistenan.
•	Melakukan eksplorasi data (EDA) untuk mengidentifikasi fitur utama dan wawasan awal terkait kinerja siswa dan dropout.
•  Rekayasa Fitur:
•	Membuat fitur baru yang dapat membantu meningkatkan daya prediktif model. Ini bisa melibatkan penggabungan data, membuat istilah interaksi, atau mentransformasi fitur yang ada.
•  Pemodelan Prediktif:
•	Mengembangkan dan mengevaluasi berbagai model pembelajaran mesin untuk memprediksi dropout siswa. Ini bisa mencakup regresi logistik, pohon keputusan, random forests, atau gradient boosting machines.
•	Memilih model dengan kinerja terbaik berdasarkan akurasi, presisi, recall, F1-score, dan metrik relevan lainnya.
•  Pengembangan Dashboard:
•	Merancang dan mengimplementasikan dashboard menggunakan alat visualisasi yang sesuai (misalnya, Tableau, Power BI, atau alat berbasis Python seperti Dash atau Streamlit).
•	Memastikan dashboard ramah pengguna dan memberikan wawasan yang jelas tentang kinerja siswa, tingkat dropout, dan metrik kunci lainnya.
•  Rekomendasi dan Pelaporan:
•	Meringkas temuan dan memberikan rekomendasi yang dapat ditindaklanjuti kepada institusi berdasarkan analisis.
•	Menyiapkan laporan dan presentasi untuk mengkomunikasikan hasil dan nilai dashboard kepada pemangku kepentingan.

1. Penggunaan data dari dataset Jaya Jaya Maju untuk melakukan eksplorasi data, analisis statistik, dan pembuatan model prediktif.
2. Analisis faktor-faktor yang mempengaruhi attrition rate berdasarkan pengelompokan tertentu.
3. Pembuatan dashboard interaktif yang menyajikan informasi mengenai faktor-faktor relevan yang memengaruhi tingkat attriton rate.


### Persiapan

Sebelum menjalankan skrip Python, pastikan Anda memiliki lingkungan yang sesuai dengan dependensi yang diperlukan. Langkah-langkah setup environment dapat dilakukan sebagai berikut:
1. Instalasi Python: Pastikan Anda telah menginstal Python di komputer Anda. Anda bisa mengunduhnya dari situs resmi Python dan mengikuti petunjuk instalasinya.
2. Instalasi Package: Instal paket-paket yang diperlukan dengan menjalankan perintah berikut di terminal atau command prompt:
```
pip install pandas scikit-learn joblib
```

Menjalankan skrip:
1. Pastikan dataset mempunyai struktur dan fitur sesuai dengan dataset sekarang, serta sudah dibersihkan (tanpa missing value).
2. Anda dapat menjalankan skrip Python.py dengan menggunakan IDE seperti PyCharm atau VSCode, Kemudian jalankan skrip tersebut dengan menekan tombol "Run" atau "Execute"
3. Masukan direktori kerja anda (contoh: C:/Users/anan/mahir/New_folder)
4. Masukan nama dataset yang akan diprediksi label Attrition nya (contoh: employee_data.csv)
5. File hasil akan langsung tersimpan di direktor dengan nama hasil_prediksi.csv

Hal yang perlu diperhatikan:
1. Pastikan direktori sudah sesuai dengan lokasi model (.joblib) dan scaler (scaler.pkl)
2. Pastikan saat memasukan nama dataset menggunakan format akhir (.csv), serta dataset tersebut sudah ada dalam direktori

## Business Dashboard
link: https://lookerstudio.google.com/reporting/e8c69760-e127-4277-9175-6b0351f4824a

Dashboard yang telah dibuat, disesuaikan dengan analisis yang didapat dari dataset, sehingga dapat memonitor dan memberi informasi hal-hal penting yang berkaitan dengan Attrion rate. Berikut penjelasan mengenai parameter-paramter pada dashboard:

1. Score card Employee Count: Total seluruh karyawan di perusahaan saat ini (mengacu pada dataset bersih).

2. Score card Attrition: Total karyawan attrition yang meninggalkan perusahaan. Secara umum apabila nilainya kecil akan semakin baik.

3. Score card Attriton Rate: Persentase jumlah Attrition terhadap jumlah karyawan secara keseluruhan (Employee Count). Merupakan indikator utama yang perhatikan di kasus ini, semakin rendah nilainya akan semakin baik.

4. Score card Avg Age: Rataan dari usia karyawan yang meninggalkan perusahaan. Indikator untuk menilai kebanyakan karyawan yang meninggalkan perusahaan berada pada usia muda atau tua. Dapat di analisis lebih lanjut dengan grafik Age group

5. Score card Avg Monthly Income: Rataan dari usia karyawan yang meninggalkan perusahaan. Indikator untuk menilai kebanyakan karyawan yang meninggalkan perusahaan berada pada pendapatan bulanan tinggi atau rendah. Dapat di analisis lebih lanjut dengan grafik Monthly Income Group

6. Score card Avg Total Working Years: Nilai rataan dari usia karyawan yang meninggalkan perusahaan. Indikator untuk menilai seberapa lama pengalaman kerja karyawan yang meninggalkan perusahaan.

7. Grafik Attrition by Age: Pengelompokan karyawan yang meninggalkan perushaan berdasarkan 5 rentang usia. Tiap grup/rentang usia dapat di monitor secara terpisah untuk mengetahui kaitannya dengan parameter lain seperti monthly income, jobrole, gender, marital status, dan satisfaction level. Pemfokusan ini dapat berguna untuk menemukan solusi terbaik untuk mengurangi attrition di rentang usia tertentu.

8. Grafik Attrition by Monthly Income: Pengelompokan karyawan yang meninggalkan perusahaan berdasarkan rentang pendapatan bulanan mereka. Parameter ini berkorelasi dengan monthly income dan juga dapat dimonitor secara terpisah untuk tiap grupnya, serta dihubungkan terutama kaitannya dengan Job Role dan satisfaction. Semakin banyak karyawan attrition di grup monthly income rendah mengindikasikan karyawan yang menginkan pendapatan lebih kompetitif, ekspektasinya tidak terpenuhi, atau yang lainnya.

9. Grafik Attrition by Job Satisfaction: Pengelompokan karyawan yang meninggalkan perusahaan berdasarkan kategori kepuasannya terhadap pekerjaan. Dapat digunakan sebagai indikator penyebab attrition apabila kebanykan nilainya di kategori rendah, akan tetapi penilaian ini tidak selalu sesuai. Semakin banyak di kategori tinggi (high/very high) akan semakin baik.

10. Grafik Attrition by Environtment Satisfaction: Pengelompokan karyawan yang meninggalkan perusahaan berdasarkan kategori kepuasannya lingkungan kerja. Dapat digunakan sebagai indikator penyebab attrition kebanyakan nilainya di kategori rendah, akan tetapi penilaian ini tidak selalu sesuai. Semakin banyak di kategori tinggi (high/very high) akan semakin baik.

11. Tabel Top Attrition by Job Role: Memperlihatkan 5 Job Role dengan attrition rate tertinggi di perusahaan, beserta dengan jumlah karyawannya. Selain untuk memonitor, dapat digunakan untuk mengidentifikasi prioritas JobRole yang harus diutamakan. Biasanya peringkat tertinggilah yang harus diutamakan, akan tetapi bila Job Role di isi oleh sedikit karyawan, maka juga perlu ada perhatian lebih karena pengurangan 1 orang saja dapat berdampak lebih signifikan dari pada JobRole dengan total karyawan yang banyak.

12. Pie Attrition by gender dan marital status: Memberikan informasi proporsi, jumlah, dan persentase terkait gender dan marital status dari karyawan yang meinggalkan perusahaan. Selain memonitor, dapat menjadi pedoman untuk solusi yang sesuai untuk mengurangi attrition agar sesuai demografi karyawan, seperti kompensasi pernikahan, tunjangan, dan kebijakan terkait kesetaraan gender.

13. Filter Department: Opsional apabila ingin memfokuskan hanya pada department tertentu.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```
streamlit run genre_prediction_streamlit.py
or
python -m genre_prediction_streamlit.py

```
link:

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
