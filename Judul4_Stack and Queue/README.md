# Implementasi Stack Linked List pada Sistem Riwayat Browser

Program ini merupakan implementasi struktur data Stack menggunakan Linked List dengan studi kasus sistem riwayat browser. Program ini dibuat untuk menyimpan halaman website yang pernah dibuka oleh pengguna, melihat website terakhir yang dikunjungi, menampilkan seluruh riwayat website, serta menghapus website terakhir dari riwayat browser.

Struktur data yang digunakan adalah Stack Linked List dengan konsep LIFO (Last In First Out), yaitu data yang terakhir masuk akan menjadi data pertama yang keluar. Pada program ini, setiap website disimpan dalam node linked list, di mana website yang terakhir dibuka akan berada di posisi paling atas stack. Struktur data stack dipilih karena sesuai dengan cara kerja fitur back pada browser, yaitu halaman terakhir yang dibuka akan menjadi halaman pertama yang keluar saat pengguna kembali ke halaman sebelumnya.

## Source Code

<img width="477" height="130" alt="image" src="https://github.com/user-attachments/assets/b245236e-5aa2-40ce-8512-fb90d83cff04" />

Pertama, saya membuat class `Node`. Class ini digunakan untuk menyimpan data website pada setiap node linked list.

`def __init__(self, website):` merupakan constructor yang digunakan untuk menerima input nama website.

`self.website = website` digunakan untuk menyimpan nama website ke dalam node.

`self.next = None` digunakan sebagai pointer untuk menghubungkan node ke node berikutnya.

<img width="454" height="114" alt="image" src="https://github.com/user-attachments/assets/9355af38-786f-492e-8524-e9f092a86d5a" />

Selanjutnya saya membuat `class StackLinkedList` yang digunakan untuk mengatur seluruh data stack.
`def __init__(self):` merupakan constructor class stack.

`self.top_ptr = None` digunakan sebagai penunjuk data paling atas dalam stack. Nilai awal None menandakan stack masih kosong.

<img width="414" height="96" alt="image" src="https://github.com/user-attachments/assets/895b24f0-0198-45ea-bb8a-10d563b32454" />

Berikutnya terdapat fungsi is_empty() yang digunakan untuk mengecek apakah stack kosong.

`return self.top_ptr is None` akan menghasilkan nilai True jika stack kosong dan False jika stack memiliki data.

<img width="887" height="257" alt="image" src="https://github.com/user-attachments/assets/8e7a088f-855f-4e82-9170-0013038551c2" />

Selanjutnya terdapat fungsi push() yang digunakan untuk menambahkan website baru ke dalam stack.

`new_node = Node(website)` digunakan untuk membuat node baru yang berisi nama website.

`new_node.next = self.top_ptr` digunakan untuk menghubungkan node baru ke data teratas sebelumnya.

`self.top_ptr = new_node` digunakan untuk menjadikan node baru sebagai data paling atas stack.

`print(f"Website '{website}' berhasil ditambahkan ke riwayat browser.")` digunakan untuk menampilkan pesan bahwa website berhasil ditambahkan.

<img width="844" height="324" alt="image" src="https://github.com/user-attachments/assets/4d47944e-177d-4bab-ab80-9057970d964f" />

Berikutnya terdapat fungsi `pop()` yang digunakan untuk menghapus website terakhir dari stack.

`if self.is_empty():` digunakan untuk mengecek apakah stack kosong.

`print("Riwayat browser kosong")` digunakan untuk menampilkan pesan jika tidak ada data yang bisa dihapus.

`temp = self.top_ptr` digunakan untuk menyimpan data website paling atas sebelum dihapus.

`print(f"Website '{temp.website}' berhasil dihapus dari riwayat.")` digunakan untuk menampilkan website yang dihapus.

`self.top_ptr = self.top_ptr.next` digunakan untuk memindahkan posisi top ke node berikutnya sehingga data teratas sebelumnya terhapus dari stack.

<img width="762" height="208" alt="image" src="https://github.com/user-attachments/assets/a79c6dda-5036-4aba-944e-cc9d20ad6423" />

Selanjutnya terdapat fungsi `peek()` yang digunakan untuk melihat website terakhir yang dibuka.

`if self.is_empty():` digunakan untuk mengecek apakah stack kosong.

`print(f"Website terakhir dibuka: {self.top_ptr.website}")` digunakan untuk menampilkan data website yang berada di posisi paling atas stack.

<img width="653" height="411" alt="image" src="https://github.com/user-attachments/assets/4d3d0976-27e9-4f73-8e28-bccb97f49211" />

Berikutnya terdapat fungsi `display()` yang digunakan untuk menampilkan seluruh isi stack.

`if self.is_empty():` digunakan untuk mengecek apakah stack kosong.

`print("\nRiwayat Browser (Terbaru ke Terlama):")` digunakan untuk menampilkan judul output.

`current = self.top_ptr` digunakan sebagai variabel bantu untuk menelusuri stack dari data teratas.

`nomor = 1` digunakan untuk memberikan nomor urut pada setiap website.

`while current is not None:` digunakan untuk melakukan perulangan sampai node terakhir.

`print(f"{nomor}. {current.website}")` digunakan untuk menampilkan nomor urut dan nama website.

`current = current.next` digunakan untuk berpindah ke node berikutnya.

`nomor += 1` digunakan untuk menambahkan nomor urut.

<img width="685" height="501" alt="image" src="https://github.com/user-attachments/assets/b66d5576-583d-498b-9862-92fd2359b10c" />

<img width="581" height="358" alt="image" src="https://github.com/user-attachments/assets/fc346fbf-8f51-4bc7-82c5-5b38ca33e270" />

<img width="508" height="284" alt="image" src="https://github.com/user-attachments/assets/2e2b38d4-2dfc-479c-be77-c6832de564bb" />

Terakhir terdapat fungsi `main()` yang digunakan sebagai fungsi utama program.

`stack = StackLinkedList()` digunakan untuk membuat object stack.

`while pilih != 5:` digunakan untuk menjalankan program terus-menerus sampai pengguna memilih keluar.

Bagian ini digunakan untuk menampilkan menu utama program.

`pilih = int(input("Pilih menu: "))` digunakan untuk menerima input pilihan menu dari pengguna.

`if pilih == 1:` digunakan ketika pengguna ingin menambahkan website baru.

`website = input("Masukkan nama website: ")` digunakan untuk menerima input nama website.

`stack.push(website)` digunakan untuk memanggil fungsi push.

`elif pilih == 2:` digunakan ketika pengguna ingin menghapus website terakhir.

`stack.pop()` digunakan untuk memanggil fungsi pop.

`elif pilih == 3:` digunakan ketika pengguna ingin melihat website terakhir yang dibuka.

`stack.peek()` digunakan untuk memanggil fungsi peek.

`elif pilih == 4:` digunakan ketika pengguna ingin menampilkan seluruh riwayat browser.

`stack.display()` digunakan untuk memanggil fungsi display.

`elif pilih == 5:` digunakan untuk keluar dari program.

`print("Program selesai.")` digunakan untuk menampilkan pesan saat program dihentikan.

`else:` digunakan jika pengguna memasukkan pilihan yang tidak tersedia.

`print("Pilihan tidak valid!")` digunakan untuk menampilkan pesan kesalahan input.

## Output Program

<img width="405" height="190" alt="image" src="https://github.com/user-attachments/assets/0d55982d-8a69-4cbf-a8d5-150fe948d22f" />

Saat program pertama kali dijalankan, pengguna akan melihat menu utama yang berisi pilihan untuk membuka website, menghapus website terakhir, melihat website terakhir yang dibuka, menampilkan seluruh riwayat browser, dan keluar dari program.

<img width="629" height="272" alt="image" src="https://github.com/user-attachments/assets/aa681f22-7e94-4a1f-b15c-231013862e97" />

Jika pengguna memilih menu buka website, maka program akan meminta input nama website, kemudian website tersebut akan masuk ke dalam stack dan menjadi data paling atas.

<img width="507" height="287" alt="image" src="https://github.com/user-attachments/assets/2d23b808-9549-4875-bf70-353c35441aa9" />

Jika pengguna memilih menu tampilkan riwayat browser, maka seluruh data website akan ditampilkan mulai dari website terbaru hingga website terlama sesuai konsep stack.

<img width="368" height="79" alt="image" src="https://github.com/user-attachments/assets/6d0fbda4-721b-4aa1-b213-aac189dd6699" />

Jika pengguna memilih menu lihat website terakhir, maka program akan menampilkan website yang berada di posisi paling atas stack.

<img width="546" height="282" alt="image" src="https://github.com/user-attachments/assets/f686d04d-161d-4910-8108-83ff30b96216" />

Jika pengguna memilih menu hapus website terakhir, maka website paling atas akan dihapus terlebih dahulu karena stack menggunakan konsep LIFO (Last In First Out).

<img width="386" height="278" alt="image" src="https://github.com/user-attachments/assets/7873de52-0f9e-447a-bda5-277ccc80a27a" />

Jika stack kosong dan pengguna mencoba menghapus atau melihat website terakhir, maka program akan menampilkan pesan “Riwayat browser kosong”.

<img width="401" height="284" alt="image" src="https://github.com/user-attachments/assets/10fe7111-dbaa-4120-af7b-6225a67fded9" />

Jika pengguna memasukkan pilihan menu yang tidak tersedia, maka program akan menampilkan pesan “Pilihan tidak valid!”.

<img width="463" height="243" alt="image" src="https://github.com/user-attachments/assets/19d4e524-48dd-4889-9153-dba2ad20e762" />

Program akan berhenti ketika pengguna memilih menu keluar dan akan menampilkan pesan “Program selesai”.
