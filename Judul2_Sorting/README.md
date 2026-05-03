# Implementasi Bubble Sort pada Sistem Playlist Lagu Favorit Berdasarkan Jumlah Diputar

Program ini merupakan implementasi algoritma Bubble Sort menggunakan bahasa Python dengan studi kasus playlist lagu favorit berdasarkan jumlah diputar. Program ini dibuat untuk membantu pengguna dalam mencatat daftar lagu beserta jumlah pemutarannya, kemudian mengurutkan lagu dari yang paling sering diputar hingga yang paling sedikit diputar.

Algoritma yang digunakan adalah Bubble Sort, yaitu metode pengurutan dengan cara membandingkan dua elemen yang bersebelahan lalu menukarnya jika urutannya belum sesuai. Pada program ini, pengurutan dilakukan secara descending berdasarkan jumlah diputar, sehingga lagu dengan jumlah pemutaran tertinggi akan berada di urutan pertama.

## Source Code

<img width="745" height="250" alt="image" src="https://github.com/user-attachments/assets/b4c4cf84-5f4e-42c0-b351-8dd6dafadc6c" />

`def bubble_sort_playcount(lagu, n):` merupakan fungsi yang digunakan untuk mengurutkan data lagu berdasarkan jumlah diputar menggunakan algoritma Bubble Sort. Fungsi ini menerima parameter `lagu` sebagai list data lagu dan `n` sebagai jumlah data lagu.

`for i in range(n - 1):` digunakan untuk mengatur jumlah tahap perulangan utama dalam Bubble Sort. Karena proses sorting dilakukan secara bertahap, maka diperlukan sebanyak `n - 1` tahap agar seluruh data terurut sempurna.

`for j in range(n - i - 1):` digunakan untuk melakukan perbandingan antar elemen yang bersebelahan. Nilai `- i` digunakan karena pada setiap tahap, data terbesar sudah berada di posisi yang benar sehingga tidak perlu dibandingkan lagi.

`if lagu[j]["diputar"] < lagu[j + 1]["diputar"]:` digunakan untuk mengecek apakah jumlah diputar pada posisi sekarang lebih kecil daripada posisi berikutnya. Karena pengurutan dilakukan secara descending, maka jika nilai kiri lebih kecil, kedua data harus ditukar.

`temp = lagu[j]` digunakan untuk menyimpan sementara data lagu pada posisi saat ini agar datanya tidak hilang saat proses pertukaran.

`lagu[j] = lagu[j + 1]` berfungsi untuk memindahkan data lagu berikutnya ke posisi sekarang.

`lagu[j + 1] = temp` digunakan untuk menempatkan data lama yang sudah disimpan di variabel `temp` ke posisi berikutnya

<img width="925" height="155" alt="image" src="https://github.com/user-attachments/assets/5a44400f-bc36-4759-92d5-f7b5ec00622d" />

Berikutnya terdapat fungsi `tampilkan_lagu()`, yang digunakan untuk menampilkan seluruh daftar playlist lagu yang telah dimasukkan.

`def tampilkan_lagu(lagu):` merupakan fungsi yang digunakan untuk menampilkan semua data lagu yang tersimpan di dalam list.

`print("DAFTAR PLAYLIST LAGU FAVORIT")` berfungsi untuk menampilkan judul output agar hasil terlihat lebih rapi dan mudah dipahami.

`for i in range(len(lagu)):` digunakan untuk melakukan perulangan sebanyak jumlah data lagu yang tersimpan di dalam list.

`print(f"{i+1}. {lagu[i]['judul']} - {lagu[i]['diputar']}x diputar")` digunakan untuk menampilkan nomor urut, judul lagu, dan jumlah lagu diputar dari setiap data lagu.

<img width="682" height="387" alt="image" src="https://github.com/user-attachments/assets/296363be-4964-47bd-ba92-ca3a58df2fd9" />

Selanjutnya terdapat fungsi `main()`, yaitu fungsi utama yang menjalankan seluruh program.

`def main():` merupakan fungsi utama yang digunakan untuk menjalankan seluruh alur program.

`lagu = []` digunakan untuk membuat list kosong yang akan menyimpan seluruh data lagu yang diinput oleh pengguna.

`try:` digunakan untuk mengantisipasi kesalahan input agar program tidak langsung error.

`n = int(input("Masukkan jumlah lagu: "))` digunakan untuk menerima input jumlah lagu yang ingin dimasukkan oleh pengguna.

`except ValueError:` digunakan untuk menangani kesalahan jika pengguna memasukkan input selain angka.

`print("Input tidak valid!")` berfungsi untuk menampilkan pesan kesalahan jika input tidak sesuai.

`return` digunakan untuk menghentikan program jika terjadi kesalahan input.

`for i in range(n):` digunakan untuk melakukan input data lagu sebanyak jumlah yang telah dimasukkan sebelumnya.

`print(f"\nInput data lagu ke-{i+1}")` berfungsi untuk menampilkan urutan input lagu agar lebih jelas.

`judul = input("Judul lagu: ")` digunakan untuk menerima input nama atau judul lagu dari pengguna.


<img width="609" height="383" alt="image" src="https://github.com/user-attachments/assets/4318be3c-80ee-4133-99b8-4e286869974b" />

`while True:` digunakan agar program terus meminta input jumlah diputar sampai pengguna memasukkan angka yang valid.

`try:` digunakan kembali untuk menangani kemungkinan kesalahan input.

`diputar = int(input("Jumlah diputar: "))` digunakan untuk menerima input jumlah lagu diputar dalam bentuk angka.

`break` digunakan untuk menghentikan perulangan jika input sudah benar.

`except ValueError:` digunakan jika pengguna memasukkan input selain angka.

`print("Masukkan angka yang valid!")` berfungsi untuk memberi tahu pengguna agar memasukkan angka yang benar.

`data_lagu = {"judul": judul, "diputar": diputar}` digunakan untuk menyimpan data lagu dalam bentuk dictionary agar setiap lagu memiliki dua informasi, yaitu judul lagu dan jumlah diputar.

`lagu.append(data_lagu)` berfungsi untuk menambahkan data lagu ke dalam list utama.


<img width="920" height="333" alt="image" src="https://github.com/user-attachments/assets/f903372e-3649-43d4-91b7-9c2dd986c1a4" />

`print("\nData sebelum diurutkan:")` digunakan untuk menampilkan daftar lagu sebelum proses sorting dilakukan.

`tampilkan_lagu(lagu)` digunakan untuk memanggil fungsi tampilan agar seluruh data lagu dapat dilihat sebelum diurutkan.

`bubble_sort_playcount(lagu, n)` digunakan untuk memanggil fungsi Bubble Sort agar data lagu diurutkan berdasarkan jumlah diputar.

`print("\nHasil setelah diurutkan (Bubble Sort - Paling Banyak Diputar):")` berfungsi untuk menampilkan hasil akhir setelah proses sorting selesai.

`tampilkan_lagu(lagu)` digunakan kembali untuk menampilkan data lagu yang sudah terurut.

`if __name__ == "__main__":` digunakan untuk memastikan bahwa fungsi `main()` hanya berjalan saat file Python dijalankan secara langsung, bukan saat dipanggil dari file lain.

`main()` berfungsi untuk memulai seluruh program.

## Output

<img width="401" height="210" alt="image" src="https://github.com/user-attachments/assets/ff33f24b-fc59-4cc5-9798-2c479acc9608" />

Saat program pertama kali dijalankan, pengguna akan diminta memasukkan jumlah lagu yang ingin disimpan ke dalam playlist. Input ini digunakan untuk menentukan berapa banyak data lagu yang akan dimasukkan ke dalam program.

Setelah itu, program akan meminta pengguna mengisi data setiap lagu, yaitu judul lagu dan jumlah diputar. Proses ini dilakukan berulang sesuai jumlah lagu yang telah dimasukkan sebelumnya.


<img width="470" height="141" alt="image" src="https://github.com/user-attachments/assets/aec7eb10-3915-48e5-af0d-0f1c411cb9e2" />

Setelah semua data lagu selesai diinput, program akan menampilkan daftar lagu sebelum dilakukan proses pengurutan. Data masih ditampilkan sesuai urutan saat pertama kali dimasukkan oleh pengguna.

<img width="714" height="136" alt="image" src="https://github.com/user-attachments/assets/ffac1c51-68e3-44d4-9ae5-840459aff264" />

Selanjutnya program menjalankan algoritma Bubble Sort untuk mengurutkan data berdasarkan jumlah diputar secara descending, yaitu dari lagu yang paling sering diputar hingga yang paling sedikit diputar.

Dari output tersebut dapat dilihat bahwa lagu dengan jumlah pemutaran tertinggi akan berada di urutan pertama. Hal ini membuktikan bahwa algoritma Bubble Sort berhasil bekerja sesuai tujuan program, yaitu mengurutkan playlist lagu favorit berdasarkan jumlah diputar tanpa error
