# Implementasi Sequential Search untuk Pencarian Kata dalam Kalimat

Program ini dibuat untuk mencari suatu kata tertentu dalam sebuah kalimat yang dimasukkan oleh pengguna. Program akan menghitung berapa kali kata tersebut muncul serta menampilkan posisi indeks kemunculan kata dalam kalimat tersebut.

Algoritma yang digunakan dalam program ini adalah Sequential Search (Linear Search), yaitu metode pencarian dengan cara memeriksa setiap elemen secara berurutan dari awal hingga akhir. Sebelum proses pencarian dilakukan, program terlebih dahulu menghapus tanda baca agar hasil pencarian lebih akurat.

## Source Code

<img width="928" height="458" alt="image" src="https://github.com/user-attachments/assets/ef37d344-b62b-494f-a621-7da0da6909e5" />

`import string`
digunakan untuk mengimpor modul `string` yang tersedia di Python.`string.punctuation` berisi kumpulan karakter tanda baca seperti koma (,), titik (.), tanda seru (!), dan lain-lain. Modul ini digunakan dalam program untuk membantu proses penghapusan tanda baca pada kalimat.

`Fungsi sequential_search_kata(kalimat, target)` merupakan fungsi yang digunakan untuk mencari kata tertentu di dalam sebuah kalimat menggunakan metode Sequential Search.

Fungsi ini menerima dua parameter, yaitu `kalimat` sebagai input berupa teks yang akan dicari, dan `target` sebagai kata yang ingin ditemukan dalam kalimat tersebut.

`kalimat = kalimat.translate(str.maketrans('', '', string.punctuation))`
digunakan untuk menghapus seluruh tanda baca yang terdapat dalam kalimat, seperti koma, titik, dan tanda lainnya. Hal ini dilakukan agar proses pencarian menjadi lebih akurat, karena tanda baca dapat menyebabkan kata dianggap berbeda.

`kata_list = kalimat.split()`
digunakan untuk memecah kalimat menjadi beberapa kata dan menyimpannya dalam bentuk list. Setiap kata akan menjadi elemen dalam list tersebut sehingga dapat diakses satu per satu.

`count = 0`
digunakan untuk menyimpan jumlah kemunculan kata yang dicari dalam kalimat.

`indeks = []`
digunakan untuk menyimpan posisi atau indeks dari setiap kata yang ditemukan.

`for i in range(len(kata_list)):`
digunakan untuk melakukan pencarian secara berurutan (sequential) terhadap setiap kata dalam list, dimulai dari indeks pertama hingga terakhir.

`if kata_list[i].lower() == target.lower():`
digunakan untuk membandingkan setiap kata dengan target. Method `.lower()` digunakan agar perbandingan tidak membedakan huruf besar atau kecil.

`count += 1`
digunakan untuk menambah jumlah kemunculan setiap kali kata yang dicari ditemukan.

`indeks.append(i)`
digunakan untuk menyimpan indeks dari kata yang ditemukan ke dalam list indeks.

`return count, indeks`
digunakan untuk mengembalikan hasil pencarian berupa jumlah kemunculan dan posisi indeks kata.

<img width="865" height="408" alt="image" src="https://github.com/user-attachments/assets/8a90f1a2-e979-4c04-b3d1-452965166fab" />

`def main():` 
Fungsi `main()` merupakan fungsi utama yang digunakan untuk menjalankan program.

`kalimat = input("Masukkan sebuah kalimat: ")`dan `target = input("Masukkan kata yang ingin dicari: ")`
digunakan untuk menerima input dari pengguna berupa kalimat dan kata yang ingin dicari.

`count, indeks = sequential_search_kata(kalimat, target)`
digunakan untuk memanggil fungsi pencarian dan menyimpan hasilnya ke dalam variabel `count` dan `indeks`.

`print(f"\nKalimat: {kalimat}")`
digunakan untuk menampilkan kembali kalimat yang telah diinput oleh pengguna.

`if count > 0:`
digunakan untuk mengecek apakah kata ditemukan dalam kalimat.

Jika kondisi bernilai benar, maka program akan menjalankan:
`print(f"Kata '{target}' ditemukan sebanyak {count} kali.")
dan
print(f"Terdapat pada indeks: {indeks}")
yang berfungsi untuk menampilkan jumlah kemunculan dan posisi kata.

Jika kondisi bernilai salah, maka program akan menjalankan:
`print(f"Kata '{target}' tidak ditemukan.")`
yang berfungsi untuk menampilkan bahwa kata tidak ditemukan.

<img width="419" height="75" alt="image" src="https://github.com/user-attachments/assets/0e158fb4-b8a3-4040-b3d5-fe7c0483e98b" />

`if __name__ == "__main__":`
digunakan untuk memastikan bahwa fungsi main() hanya dijalankan ketika file program dieksekusi secara langsung.
