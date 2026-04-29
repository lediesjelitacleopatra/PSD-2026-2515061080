# Implementasi Singly Linked List pada Sistem Daftar Tugas Mahasiswa
Program ini merupakan implementasi struktur data Singly Linked List menggunakan bahasa Python dengan studi kasus daftar tugas mahasiswa. Program ini berfungsi untuk membantu mahasiswa dalam mencatat tugas yang harus dikerjakan, menampilkan daftar tugas yang masih aktif, serta menghapus tugas yang telah selesai dikerjakan. Dengan adanya program ini, pengguna dapat mengelola daftar tugas secara lebih teratur dan sistematis.

Struktur data yang digunakan adalah Singly Linked List, yaitu kumpulan node yang saling terhubung melalui pointer `next`, di mana setiap node menyimpan satu data berupa nama tugas. Program memiliki tiga fungsi utama, yaitu menambahkan tugas baru ke dalam daftar, menampilkan seluruh daftar tugas secara berurutan, dan menghapus tugas pertama yang dianggap sudah selesai. Linked List dipilih karena jumlah tugas bersifat dinamis, sehingga data dapat ditambah dan dihapus dengan mudah tanpa harus menentukan kapasitas penyimpanan di awal.
## Source Code

<img width="658" height="180" alt="image" src="https://github.com/user-attachments/assets/0a1b5cb0-958e-4282-9783-7d1fda1f4596" />

Pertama, saya membuat class Node. Class ini digunakan untuk menyimpan setiap data tugas. Di dalam class Node terdapat method __init__ yang berfungsi sebagai constructor. Pada bagian ini, parameter tugas digunakan untuk menerima input nama tugas dari pengguna. Kemudian self.tugas digunakan untuk menyimpan nama tugas tersebut, sedangkan self.next digunakan sebagai penunjuk ke node berikutnya. Nilai awalnya adalah None karena node baru belum terhubung dengan node lain.

<img width="510" height="118" alt="image" src="https://github.com/user-attachments/assets/d3ff10c3-790b-437d-acde-f312bdf9ef87" />

Selanjutnya saya membuat class LinkedList. Class ini berfungsi untuk mengatur seluruh daftar tugas mahasiswa. Pada bagian constructor, terdapat self.start yang digunakan untuk menyimpan node pertama dari linked list. Nilai awalnya None karena saat program dimulai daftar tugas masih kosong.

<img width="789" height="395" alt="Screenshot 2026-04-29 211430" src="https://github.com/user-attachments/assets/7dee8426-a7cc-4b63-b6cc-75a3725be1b0" />

Kemudian terdapat fungsi tambah_tugas(). Fungsi ini digunakan untuk menambahkan tugas baru ke dalam daftar. 

`tambah_tugas(self, tugas)` merupakan fungsi yang digunakan untuk menambahkan tugas baru ke dalam linked list. Fungsi ini menerima parameter `tugas`, yaitu nama tugas yang akan dimasukkan ke dalam daftar.

`new_node = Node(tugas)` digunakan untuk membuat node baru dari class `Node`. Node ini akan menyimpan data berupa nama tugas yang diinput oleh pengguna.

`if self.start is None:` digunakan untuk mengecek apakah linked list masih kosong atau belum memiliki data. Variabel `self.start` berfungsi sebagai penunjuk node pertama dalam linked list. Jika nilainya `None`, berarti belum ada tugas yang tersimpan.

`self.start = new_node` berfungsi untuk menjadikan node baru sebagai node pertama ketika linked list masih kosong. Karena belum ada data sebelumnya, maka tugas pertama yang dimasukkan akan langsung disimpan pada posisi awal list.

`else:` digunakan ketika linked list sudah memiliki data, sehingga node baru tidak bisa langsung menjadi node pertama dan harus ditempatkan di bagian akhir.

`current = self.start` digunakan untuk membuat variabel bantu bernama `current` yang berfungsi menelusuri linked list mulai dari node pertama tanpa mengubah posisi `self.start`.

`while current.next is not None:` digunakan sebagai perulangan untuk mencari node terakhir pada linked list. Selama node saat ini masih memiliki node berikutnya, maka program akan terus berpindah ke node selanjutnya.

`current = current.next` berfungsi untuk memindahkan posisi `current` ke node berikutnya sampai menemukan node terakhir.

`current.next = new_node` digunakan untuk menghubungkan node terakhir dengan node baru, sehingga tugas baru berhasil ditambahkan di bagian akhir daftar tugas.

`print(f"Tugas '{tugas}' berhasil ditambahkan.")` berfungsi untuk menampilkan pesan bahwa tugas yang dimasukkan telah berhasil disimpan ke dalam linked list.

<img width="912" height="251" alt="image" src="https://github.com/user-attachments/assets/2261eed2-27d4-4422-8e60-190a232d9b57" />

Berikutnya ada fungsi hapus_tugas(). Fungsi ini digunakan untuk menghapus tugas pertama dari daftar, karena diasumsikan tugas pertama adalah tugas yang paling dulu harus diselesaikan.

`hapus_tugas(self)` merupakan fungsi yang digunakan untuk menghapus tugas pertama dari linked list.

`if self.start is None:` digunakan untuk mengecek apakah daftar tugas masih kosong. Jika `self.start` bernilai `None`, berarti tidak ada node atau tugas yang tersimpan dalam linked list.

`print("Tidak ada tugas dalam daftar!")` berfungsi untuk menampilkan pesan kepada pengguna bahwa tidak ada tugas yang bisa dihapus karena daftar masih kosong.

`else:` dijalankan jika linked list memiliki data, sehingga proses penghapusan dapat dilakukan.

`tugas_selesai = self.start.tugas` digunakan untuk menyimpan nama tugas pertama sebelum node tersebut dihapus. Hal ini dilakukan agar nama tugas yang selesai masih bisa ditampilkan kepada pengguna.

`self.start = self.start.next` berfungsi untuk menghapus node pertama dengan cara memindahkan posisi `self.start` ke node berikutnya. Karena `self.start` selalu menunjuk node pertama, maka ketika dipindahkan, node pertama sebelumnya otomatis terhapus dari daftar.

`print(f"Tugas '{tugas_selesai}' telah selesai dan dihapus.")` digunakan untuk menampilkan informasi bahwa tugas pertama telah selesai dikerjakan dan berhasil dihapus dari linked list.

<img width="680" height="422" alt="image" src="https://github.com/user-attachments/assets/538000af-d3c2-4bd7-9e69-d0514667069f" />

Selanjutnya terdapat fungsi tampilkan_tugas(). Fungsi ini digunakan untuk menampilkan seluruh daftar tugas mahasiswa.
Fungsi ini membantu pengguna melihat tugas apa saja yang masih ada dalam daftar.

`if self.start is None:` digunakan untuk mengecek apakah linked list kosong atau tidak memiliki data. Jika `self.start` bernilai `None`, berarti belum ada tugas yang tersimpan.

`print("Daftar tugas kosong.")` berfungsi untuk menampilkan pesan bahwa tidak ada tugas dalam daftar, sehingga tidak ada data yang bisa ditampilkan.

`return` digunakan untuk menghentikan fungsi agar program tidak melanjutkan proses ke bagian berikutnya, karena linked list masih kosong.

`print("\nDaftar Tugas Mahasiswa:")` digunakan untuk menampilkan judul daftar tugas agar output terlihat lebih jelas dan rapi.

`current = self.start` berfungsi untuk membuat variabel bantu bernama `current` yang digunakan untuk menelusuri linked list mulai dari node pertama tanpa mengubah posisi asli `self.start`.

`nomor = 1` digunakan untuk memberikan nomor urut pada setiap tugas yang ditampilkan agar daftar lebih terstruktur dan mudah dibaca.

`while current is not None:` digunakan sebagai perulangan untuk menampilkan semua node dalam linked list. Perulangan akan terus berjalan selama masih ada node yang tersisa.

`print(f"{nomor}. {current.tugas}")` berfungsi untuk menampilkan nomor urut beserta nama tugas yang tersimpan pada setiap node.

`current = current.next` digunakan untuk memindahkan posisi `current` ke node berikutnya agar seluruh data dapat ditampilkan sampai node terakhir.

`nomor += 1` berfungsi untuk menambahkan nomor urut setiap kali program berpindah ke tugas berikutnya, sehingga urutan daftar tetap sesuai.

<img width="777" height="430" alt="image" src="https://github.com/user-attachments/assets/e622d787-6214-4ffb-a3a0-468a811313db" />

<img width="676" height="394" alt="image" src="https://github.com/user-attachments/assets/1e85ef72-1db7-437f-b623-338551b9ae59" />

Terakhir terdapat fungsi main() sebagai fungsi utama program.

`main()` merupakan fungsi utama yang digunakan untuk menjalankan seluruh program. Fungsi ini mengatur alur program mulai dari menampilkan menu, menerima input pengguna, hingga memanggil fungsi-fungsi lain seperti menambah tugas, menghapus tugas, dan menampilkan daftar tugas.

`daftar_tugas = LinkedList()` digunakan untuk membuat object dari class `LinkedList`. Object ini akan digunakan untuk menyimpan seluruh data tugas mahasiswa selama program berjalan.

`while True:` digunakan untuk membuat perulangan tanpa batas agar program terus berjalan sampai pengguna memilih untuk keluar dari program.

`print("SISTEM DAFTAR TUGAS MAHASISWA")` berfungsi untuk menampilkan judul utama program agar pengguna mengetahui bahwa program yang dijalankan adalah sistem daftar tugas mahasiswa.

`print("1. Tambah Tugas")` digunakan untuk menampilkan pilihan menu pertama, yaitu menambahkan tugas baru ke dalam daftar.

`print("2. Hapus Tugas Pertama")` digunakan untuk menampilkan pilihan menu kedua, yaitu menghapus tugas pertama yang dianggap sudah selesai.

`print("3. Tampilkan Daftar Tugas")` digunakan untuk menampilkan pilihan menu ketiga, yaitu melihat seluruh daftar tugas yang tersimpan.

`print("4. Keluar")` digunakan untuk menampilkan pilihan menu keempat, yaitu menghentikan program.

`pilihan = input("Masukkan pilihan: ")` berfungsi untuk menerima input dari pengguna mengenai menu mana yang ingin dipilih.

`if pilihan == "1":` digunakan untuk mengecek apakah pengguna memilih menu pertama, yaitu menambah tugas.

`tugas = input("Masukkan nama tugas: ")` berfungsi untuk meminta pengguna memasukkan nama tugas yang ingin ditambahkan.

`daftar_tugas.tambah_tugas(tugas)` digunakan untuk memanggil fungsi `tambah_tugas()` agar tugas baru dapat disimpan ke dalam linked list.

`elif pilihan == "2":` digunakan untuk mengecek apakah pengguna memilih menu kedua, yaitu menghapus tugas pertama.

`daftar_tugas.hapus_tugas()` berfungsi untuk memanggil fungsi `hapus_tugas()` agar tugas pertama dapat dihapus dari daftar.

`elif pilihan == "3":` digunakan untuk mengecek apakah pengguna memilih menu ketiga, yaitu menampilkan seluruh daftar tugas.

`daftar_tugas.tampilkan_tugas()` digunakan untuk memanggil fungsi `tampilkan_tugas()` agar semua tugas yang tersimpan dapat ditampilkan ke layar.

`elif pilihan == "4":` digunakan untuk mengecek apakah pengguna memilih menu keluar dari program.

`print("Program selesai.")` berfungsi untuk menampilkan pesan bahwa program telah selesai dijalankan.

`break` digunakan untuk menghentikan perulangan `while True`, sehingga program akan berhenti.

`else:` dijalankan jika pengguna memasukkan pilihan yang tidak sesuai dengan menu yang tersedia.

`print("Pilihan tidak valid!")` berfungsi untuk menampilkan pesan kesalahan agar pengguna mengetahui bahwa input yang dimasukkan salah.

## Output Program

<img width="513" height="164" alt="image" src="https://github.com/user-attachments/assets/bb9ad459-d740-4035-8e5f-4397afcec9ee" />

Saat program pertama kali dijalankan, yang muncul adalah judul program yaitu Sistem Daftar Tugas Mahasiswa. Setelah itu program menampilkan empat pilihan menu utama, yaitu tambah tugas, hapus tugas pertama, tampilkan daftar tugas, dan keluar dari program.

<img width="591" height="240" alt="image" src="https://github.com/user-attachments/assets/be4c6cac-dc92-46d7-a69d-eb3379f345ae" />

Jika pengguna memilih angka 1, maka program akan meminta input nama tugas yang ingin ditambahkan. Setelah nama tugas dimasukkan, program akan menampilkan pesan bahwa tugas berhasil ditambahkan.

<img width="647" height="213" alt="image" src="https://github.com/user-attachments/assets/d81dbb86-5072-4fb9-882e-94d6fddd7668" />

Jika pengguna memilih angka 2, maka program akan menghapus tugas pertama dalam linked list. Jika daftar masih kosong, program akan menampilkan pesan bahwa tidak ada tugas dalam daftar.

<img width="621" height="275" alt="image" src="https://github.com/user-attachments/assets/fb39be60-797a-4fac-ab09-6f1d4cdd0b95" />

Jika pengguna memilih angka 3, maka program akan menampilkan seluruh daftar tugas yang sudah tersimpan secara berurutan mulai dari tugas pertama hingga terakhir.

<img width="554" height="188" alt="image" src="https://github.com/user-attachments/assets/16636b29-972a-4ae3-b54f-8b83a73559c7" />

Jika pengguna memilih angka 4, maka program akan berhenti dan menampilkan pesan “Program selesai.”

<img width="436" height="184" alt="image" src="https://github.com/user-attachments/assets/0cb30c33-e4c1-4dc1-9359-d2df0ef86e41" />

Jika pengguna memasukkan angka atau pilihan yang tidak tersedia pada menu, misalnya angka 5 atau huruf lain selain pilihan yang sudah disediakan, maka program akan masuk ke bagian else dan menampilkan pesan bahwa pilihan tidak valid.

<img width="539" height="183" alt="image" src="https://github.com/user-attachments/assets/529a1c7d-4afe-4875-b4ca-6134c2a2d580" />

Jika pengguna memilih menu hapus tugas pertama, tetapi daftar tugas masih kosong atau belum ada data yang tersimpan, maka program akan menampilkan pesan bahwa tidak ada tugas dalam daftar. Hal ini terjadi karena linked list masih kosong, sehingga program tidak dapat menghapus node pertama.

<img width="478" height="187" alt="image" src="https://github.com/user-attachments/assets/365ace16-7a74-41d9-9ddc-9f7bb91443ae" />

Jika pengguna memilih menu tampilkan daftar tugas, tetapi belum ada tugas yang dimasukkan, maka program akan menampilkan pesan bahwa daftar tugas kosong.
Output ini menunjukkan bahwa belum ada node atau data tugas yang tersimpan di dalam linked list, sehingga tidak ada data yang dapat ditampilkan.

## Link YouTube 
https://youtu.be/pEFlpWnIE_c
