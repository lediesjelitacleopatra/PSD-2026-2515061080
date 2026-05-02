# Implementasi Bubble Sort pada Sistem Playlist Lagu Favorit Berdasarkan Jumlah Diputar

Program ini merupakan implementasi algoritma Bubble Sort menggunakan bahasa Python dengan studi kasus playlist lagu favorit berdasarkan jumlah diputar. Program ini dibuat untuk membantu pengguna dalam mencatat daftar lagu beserta jumlah pemutarannya, kemudian mengurutkan lagu dari yang paling sering diputar hingga yang paling sedikit diputar.

Algoritma yang digunakan adalah Bubble Sort, yaitu metode pengurutan dengan cara membandingkan dua elemen yang bersebelahan lalu menukarnya jika urutannya belum sesuai. Pada program ini, pengurutan dilakukan secara descending berdasarkan jumlah diputar, sehingga lagu dengan jumlah pemutaran tertinggi akan berada di urutan pertama.

## Source Code

<img width="745" height="250" alt="image" src="https://github.com/user-attachments/assets/b4c4cf84-5f4e-42c0-b351-8dd6dafadc6c" />

bubble_sort_playcount(lagu, n) merupakan fungsi yang digunakan untuk mengurutkan data lagu berdasarkan jumlah diputar menggunakan algoritma Bubble Sort. Pengurutan dilakukan secara descending, yaitu dari lagu yang paling banyak diputar ke yang paling sedikit diputar.

for i in range(n - 1): digunakan untuk mengatur jumlah tahap perulangan utama. Karena Bubble Sort membandingkan data secara bertahap, maka dibutuhkan sebanyak n - 1 tahap untuk memastikan semua data sudah terurut.

for j in range(n - i - 1): digunakan untuk melakukan perbandingan antar elemen yang bersebelahan. Nilai - i digunakan karena setiap tahap, data terbesar sudah berada di posisi yang benar sehingga tidak perlu dibandingkan lagi.

if lagu[j]["diputar"] < lagu[j + 1]["diputar"]: digunakan untuk mengecek apakah jumlah diputar pada posisi sekarang lebih kecil daripada posisi berikutnya. Karena program menggunakan descending, maka jika data kiri lebih kecil, keduanya harus ditukar.

temp = lagu[j] digunakan untuk menyimpan sementara data lagu pada posisi saat ini agar tidak hilang saat proses pertukaran.

lagu[j] = lagu[j + 1] berfungsi untuk memindahkan data lagu berikutnya ke posisi sekarang.

lagu[j + 1] = temp digunakan untuk menempatkan data lama yang sudah disimpan di temp ke posisi berikutnya. Proses ini disebut swap atau pertukaran data.
