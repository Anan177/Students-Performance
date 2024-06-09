# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Mereka telah menyediakan dataset yang dapat Anda unduh melalui tautan berikut: [students' performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/). Selain itu, mereka juga meminta Anda untuk membuatkan dashboard agar mereka mudah dalam memahami data dan memonitor

### Permasalahan Bisnis
Institusi pendidikan memiliki peran yang sangat penting dalam membentuk masa depan generasi muda. Salah satu indikator keberhasilan institusi pendidikan adalah jumlah lulusan yang berhasil menyelesaikan pendidikannya. Namun, Jaya Jaya Institut menghadapi masalah serius dengan tingginya angka dropout mahasiswa. Tingginya angka dropout ini tidak hanya merugikan mahasiswa secara individu, tetapi juga mempengaruhi reputasi dan performa institusi secara keseluruhan.

Dropout rate yang tinggi dapat berdampak negatif pada beberapa aspek, antara lain:
- Reputasi Institusi: Tingkat dropout yang tinggi dapat mencoreng reputasi Jaya Jaya Institut sebagai lembaga pendidikan yang berkualitas, sehingga dapat   mengurangi daya tarik bagi calon mahasiswa baru.
- Kerugian Finansial: Setiap mahasiswa yang dropout merupakan kerugian finansial bagi institusi karena biaya yang telah dikeluarkan untuk merekrut dan - - mendidik mahasiswa tersebut tidak dapat dikembalikan.
- Kinerja Akademik: Tingginya angka dropout dapat menurunkan kinerja akademik institusi dan mengurangi jumlah lulusan yang siap memasuki dunia kerja, yang pada akhirnya berdampak pada kontribusi institusi terhadap masyarakat.

Alasan mahasiswa melakukan dropout bisa sangat bervariasi, mulai dari kesulitan akademik, masalah keuangan, kurangnya dukungan sosial, hingga ketidakpuasan dengan program studi yang diambil. Oleh karena itu, penting bagi Jaya Jaya Institut untuk dapat mengidentifikasi mahasiswa yang berisiko tinggi untuk melakukan dropout sedini mungkin dan menyediakan intervensi yang tepat untuk mengurangi risiko tersebut.

### Cakupan Proyek

1.	Penggunaan data dari dataset Jaya Jaya Institut untuk melakukan eksplorasi data, analisis statistik, dan preprocessing data untuk memahami distribusi,mengidentifikasi, dan mencari hubungan antara variabel-variabel yang relevan dengan tingkat dropout mahasiswa.

2.	Pembuatan model prediktif dengan beberapa algoritma machine learning (Random Forest, Logistic Regression, atau Gradient Boosting) dan melakukan evaluasi untuk menentukan model terbaik untuk memprediksi status mahasiswa.

3.  Pembuatan dashboard interaktif yang menyajikan informasi mengenai performa mahasiswa dan faktor-faktor relevan yang mempengaruhi tingkat dropout rate, untuk tujuan monitoring dan intervensi Awal.

Batasan Proyek:
- Keterbatasan Data: Ketersediaan kuantitas dan kualitas data yang ada akan membatasi sejauh mana analisis dan prediksi dapat dilakukan.
- Scope Analisis: Analisis difokuskan pada parameter-parameter yang ada dalam dataset, serta lebih difokuskan untuk megindentifikasi fitur penting untuk pembuatan model prediktif.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup Environtment:

Sebelum menjalankan skrip Python, pastikan sudah memiliki lingkungan yang sesuai dengan dependensi yang diperlukan. Langkah-langkah setup environment dapat dilakukan sebagai berikut:
1. Instalasi Python: Pastikan telah menginstal Python. 
2. Penyesuaian direktori, penyiapan virtual environtment dan instalasi dependensi: Instal paket-paket yang diperlukan dengan menjalankan perintah berikut di terminal atau command prompt:
```
mkdir proyek_student_dropout
cd proyek_student_dropout
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Business Dashboard
link: https://lookerstudio.google.com/reporting/862175d1-35c4-4513-8f69-6afb9d918e1a

Dashboard yang telah dibuat, disesuaikan dengan analisis dan fitur penting yang didapat saat melakukan analisis dan pemodelan, sehingga dirasa dapat memonitor dan memberi informasi penting yang berkaitan dengan student's dropout rate. Berikut penjelasan mengenai parameter-paramter pada dashboard:

1. Score card Student Count: Total seluruh mahasiswa yang telah meninggalkan institusi pendidikan (graduate dan dropout). 

2. Score card Dropout: Total mahasiswa dropout, Merupakan salah satu indikator utama dalam kasus ini, apabila nilainya semakin kecil akan semakin baik.

3. Score card Dropout Rate: Persentase jumlah dropout terhadap jumlah mahasiswa yang telah meninggalkan institusi pendidikan secara keseluruhan (Student Count). Merupakan indikator utama yang perhatikan di kasus ini, semakin rendah nilainya akan semakin baik.

4. Score card Avg Enrollment Age: Rataan dari usia mahasiswa pada saat pendaftaran. Indikator untuk menilai kebanyakan mahasiswa dropout berada pada kisaran berapa. Dapat di analisis lebih lanjut dengan grafik Age group.

5. Score card Avg Total Semester Grade: Rataan dari nilai seluruh semester pada mahasiswa. Indikator untuk menilai kebanyakan mahasiswa saat ini berada pada semester grade tinggi atau rendah. Dapat di analisis lebih lanjut dengan grafik Status by Avg Semester Grade.

6. Score card Avg Admission Grade: Nilai rataan dari nilai penerimaan mahasiswa. Indikator untuk menilai kebanyakan mahasiswa saat ini berada pada admission grade tinggi atau rendah. Dapat di analisis lebih lanjut dengan grafik Status by Admission Grade.

7. Grafik Status by Enrollment Age: Pengelompokan mahasiswa graduate dan dropout berdasarkan 5 rentang usia pendaftaran. Untuk mengetahui lebih jelas bagaimana persebaran usia pendaftaran dari mahasiswa dropout dan graduate.

8. Grafik Status by Admission Grade: Pengelompokan mahasiswa berdasarkan rentang nilai penerimaan mereka. Pada grafik ini dapat diketahui proporsi/persentase dropout dan gradute untuk masing-masing rentang nilai.

9. Grafik Status by Avg Total Semester Grade: Pengelompokan mahasiswa berdasarkan rentang rataan nilai semester mereka. Pada grafik ini dapat diketahui proporsi/persentase dropout dan gradute untuk masing-masing rentang nilai.

10. Pie Marital status dan Gender: Memberikan informasi proporsi, jumlah, dan persentase terkait gender dan marital status dari mahsiswa. Selain memonitor, dapat menjadi pedoman untuk solusi yang sesuai untuk mengurangi dropout rate agar sesuai demografi mahasiswa.

11. Tabel Dropout rate by Course: Memperlihatkan course dengan dropout rate tertinggi beserta dengan jumlah mahasiswa, serta persentase dari mahasiswa pemilik beasiswa dan mahasiswa dengan bayaran terkini. Selain untuk memonitor, dapat digunakan untuk mengidentifikasi prioritas Course yang harus diutamakan. Biasanya peringkat tertinggilah yang harus diutamakan, akan tetapi bila course di isi oleh sedikit mahasiswa, maka juga perlu ada perhatian lebih karena pengurangan 1 orang saja dapat berdampak lebih signifikan.

12. Grafik line Avg Total Semester Grade by Course: Memberikan informasi nilai rataan seluruh semester untuk mahasiswa gradute dan dropout, dan diurutkan berdasarkan Course dengan dropout rate tertinggi.

13. Check box Fees UptoDate dan Scholarship : Untuk memilih apakah hanya ingin menampilkan mahasiswa dengan fees uptodate saja atau mahasiswa dengan kepemilikan beasiswa saja, beserta sebalaiknya. Dapat memberi infromasi lain terkait bagaimana pengaruhnya terhadap parameter lainnya. Untuk kembali menampilkan kedua jenis dapat meriset checkbox

## Menjalankan Sistem Machine Learning
1. Pastikan mempunyai struktur direktori yang mencakup hal-hal berikut:
```
directory/
├── model
├── app.py
├── image.jpg
├── data_preprocessing.py
└── prediction.py
```
2. Anda dapat menjalankan skrip app.py dengan menggunakan IDE seperti PyCharm atau VSCode, Kemudian jalankan skrip tersebut dengan menekan tombol "Run" atau "Execute":

```
streamlit run app.py
or
python -m streamlit run app.py
```

3. Masuk ke tab student prediction dan masukan input data mahasiswa sesuai permintaan kemudian klik button "predict"

link: https://students-performance-chn2jtty949mbusdky2mzv.streamlit.app/

## Conclusion
- Berdasarkan dataset yang diberikan dengan pemfokusan untuk mendeteksi mahasiswa dropout, secara singkat menghasilkan kesimpulan sebagai berikut:

    1. Secara umum pendeteksian mahasiswa dropout dapat diketahui secara jelas berdasarkan beberapa parameter numerik di tiap semesternya, seperti jumlah unit kurikuler (Curricular units) yang dikreditkan, didaftarkan, dinilai, dan disetujui mahasiswa pada semester pertama dan kedua. Mahasiswa yang berpotensi dropout akan memiliki nilai-nilai yang lebih kecil dibanding mahasiswa graduate. Selain itu, nilai masuk mahasiswa yang semakin kecil (admission grade), serta umur saat penerimaan (age at enrollment) yang semakin tinggi juga meningkatkan potensi dropout.

    2. Faktor lain yang berpengaruh secara kuat dalam potensi dropout adalah biaya yang uptodate (tuition fees uptodate) atau kepemilikan beasiswa beasiswa (scholarship). Meski bisa dikatakan hanya sebagian kecil mahasiswa, akan tetapi mahasiswa dengan biaya yang tidak uptodate akan sangat berpotensi melakukan dropout, serta mahasiswa yang memiliki beasiswa berkemungkinan sangat kecil untuk melakukan dropout.

    3. Berdasarkan Course yang diambil mahasiswa, nilai dropout rate memiliki variansi yang sangat tinggi. Variansi tinggi ini memungkinkan pemfokusan pada course-course tertentu yang dianggap paling bermasalah pada kasus ini. Berbagai Course juga pastinya memiliki standar Curricular units yang berbeda-beda sehingga tidak dapat dibandingkan antar coursenya. Seperti contoh Course Animation dan Multimedia Design memiliki nilai Curricular units grade yang sangat kecil dibanding course lainnya. Selain itu, dapat diketahui pula beberapa Course yang memiliki total mahasiswa rendah cenderung memiliki dropout rate tinggi, serta cenderung memiliki persentase mahasiswa dengan biaya uptodate rendah dan beasiswa yang sangat kecil.

    4. Informasi lain yang dapat memberi informasi tambahan adalah sebagian besar mahasiswa yang memiliki hubungan (non-single) lebih rawan melakukan dropout dibandingkan dengan yang single. Selain itu berdasarkan gender, laki-laki memiliki kecenderungan potensi dropout yang lebih tinggi.

- Pembuatan model menggunakan algoritma Random Forest menghasilkan model yang baik dan dapat digunakan untuk memprediksi status mahasiswa berdasarkan beberapa fitur/variabel yang ada dalam dataset. Peningkatan dan pemeliharaan kemampuan model dapat menjadi opsi yang bagus, terutama jika menggunakan dataset yang lebih banyak atau data yang lebih terbarukan.

- Dashboard memiliki beberapa informasi yang dapat dimonitor terkait dropout rate di perusahaan ini. Dimana seperti yang telah diketahui masalah utama dari dropout ini dapat diketahui dengan parameter numerik seperti nilai semester, nilai penerimaan, umur saat penerimaan, rataan nilai total semester, serta pembagiannya pada Course tertentu. Selain itu informasi tambahan juga dapat dikaitkan dengan Gender dan Marital status.

### Rekomendasi Action Items

Beberapa rekomendasi action items yang dapat dilakukan perusahaan guna menyelesaikan permasalahan dropout di institusi ini adalah sebagai berikut.

- action item 1
    Melihat permasalahan umum dropout di institusi ini yang berkaitan erat dengan parameter numerik curicural units, terutama nilai semester (grade). Maka disarankan untuk melakukan sosialisasi terkait kebutuhan curicural units, program peningkatan peningkatan pembelajaran khusus, program remedial, serta program pendampingan dan mentoring akademik yang dapat dilakukan oleh senior maupun alumni. Selain itu untuk permasalahan pola dropout rate yang tinggi berada pada mahasiswa dengan nilai masuk (admission grade) yang rendah, dapat di atasi dengan batasan dan standar nilai masuk.
- action item 2
    Melihat bahwa pola dropout rate yang tinggi berada pada mahasiswa dengan umur penerimaan (age at enrollment) yang tinggi. Maka dapat melakukan program layanan konseling khusus untuk mahasiswa berumur >25 tahun untuk membantu mahasiswa senior menghadapi stres, kecemasan, atau masalah pribadi lainnya yang dapat mempengaruhi performa akademik mereka. Selain itu juga dapat dilakukan usaha preventif untuk membatasi umur masuk calon mahasiswa.
- action item 3
    Berupaya untuk meningkatkan persentase biaya terkini (tuition fees uptodate) sampai pada 100%, serta meningkatkan kapasitas program beasiswa agar dapat menampung lebih banyak mahasiswa. Tentunya hal ini juga harus disesuaikan dengan Course yang ada.
- action item 4
    Melakukan penyeseuaian kurikulum dan beban akademik untuk masing-masing Course, terutama yang memiliki dropout rate tinggi. Untuk memastikan bahwa beban akademik tidak terlalu berat dan materi yang diajarkan relevan serta bermanfaat. Selain itu, juga dapat menawarkan fleksibilitas dalam pemilihan unit kurikulum, memungkinkan mahasiswa untuk mengatur beban akademik mereka sesuai dengan kapasitas pribadi.
- action item 5
    Monitoring dan Intervensi Awal dengan menggunakan informasi lewat dashboard dan memanfaatankan model untuk memprediksi secara cepat mahasiswa yang beresiko dropout. 