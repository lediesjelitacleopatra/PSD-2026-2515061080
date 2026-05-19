# Implementasi Stack Linked List
# Studi Kasus: Sistem Riwayat Browser

class Node:
    def __init__(self, website):
        self.website = website
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top_ptr = None

    # Mengecek apakah stack kosong
    def is_empty(self):
        return self.top_ptr is None

    # Menambahkan website ke riwayat browser
    def push(self, website):
        new_node = Node(website)

        new_node.next = self.top_ptr
        self.top_ptr = new_node

        print(f"Website '{website}' berhasil ditambahkan ke riwayat browser.")

    # Menghapus website terakhir dari riwayat
    def pop(self):
        if self.is_empty():
            print("Riwayat browser kosong")
            return

        temp = self.top_ptr

        print(f"Website '{temp.website}' berhasil dihapus dari riwayat.")

        self.top_ptr = self.top_ptr.next

    # Melihat website terakhir yang dibuka
    def peek(self):
        if self.is_empty():
            print("Riwayat browser kosong")
            return

        print(f"Website terakhir dibuka: {self.top_ptr.website}")

    # Menampilkan seluruh riwayat browser
    def display(self):
        if self.is_empty():
            print("Riwayat browser kosong")
            return

        print("\nRiwayat Browser (Terbaru ke Terlama):")

        current = self.top_ptr
        nomor = 1

        while current is not None:
            print(f"{nomor}. {current.website}")
            current = current.next
            nomor += 1


def main():
    stack = StackLinkedList()

    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM RIWAYAT BROWSER ===")
        print("1. Buka Website")
        print("2. Hapus Website Terakhir")
        print("3. Lihat Website Terakhir")
        print("4. Tampilkan Riwayat Browser")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            website = input("Masukkan nama website: ")
            stack.push(website)

        elif pilih == 2:
            stack.pop()

        elif pilih == 3:
            stack.peek()

        elif pilih == 4:
            stack.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()