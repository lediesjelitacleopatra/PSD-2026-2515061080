# Implementasi Singly Linked List
# Studi Kasus: Daftar Tugas Mahasiswa

class Node:
    def __init__(self, tugas):
        self.tugas = tugas
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    # Menambahkan tugas baru ke daftar
    def tambah_tugas(self, tugas):
        new_node = Node(tugas)

        if self.start is None:
            self.start = new_node
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = new_node

        print(f"Tugas '{tugas}' berhasil ditambahkan.")

    # Menghapus tugas pertama (yang sudah selesai)
    def hapus_tugas(self):
        if self.start is None:
            print("Tidak ada tugas dalam daftar!")
        else:
            tugas_selesai = self.start.tugas
            self.start = self.start.next
            print(f"Tugas '{tugas_selesai}' telah selesai dan dihapus.")

    # Menampilkan daftar tugas
    def tampilkan_tugas(self):
        if self.start is None:
            print("Daftar tugas kosong.")
            return

        print("\nDaftar Tugas Mahasiswa:")
        current = self.start
        nomor = 1

        while current is not None:
            print(f"{nomor}. {current.tugas}")
            current = current.next
            nomor += 1


def main():
    daftar_tugas = LinkedList()

    while True:
        print("SISTEM DAFTAR TUGAS MAHASISWA")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas Pertama")
        print("3. Tampilkan Daftar Tugas")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            tugas = input("Masukkan nama tugas: ")
            daftar_tugas.tambah_tugas(tugas)

        elif pilihan == "2":
            daftar_tugas.hapus_tugas()

        elif pilihan == "3":
            daftar_tugas.tampilkan_tugas()

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()