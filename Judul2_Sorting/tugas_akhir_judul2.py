def bubble_sort_playcount(lagu, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Descending: dari yang paling banyak diputar
            if lagu[j]["diputar"] < lagu[j + 1]["diputar"]:
                temp = lagu[j]
                lagu[j] = lagu[j + 1]
                lagu[j + 1] = temp


def tampilkan_lagu(lagu):
    print("DAFTAR PLAYLIST LAGU FAVORIT")
    for i in range(len(lagu)):
        print(f"{i+1}. {lagu[i]['judul']} - {lagu[i]['diputar']}x diputar")


def main():
    lagu = []

    try:
        n = int(input("Masukkan jumlah lagu: "))
    except ValueError:
        print("Input tidak valid!")
        return

    for i in range(n):
        print(f"\nInput data lagu ke-{i+1}")

        judul = input("Judul lagu: ")

        while True:
            try:
                diputar = int(input("Jumlah diputar: "))
                break
            except ValueError:
                print("Masukkan angka yang valid!")

        data_lagu = {
            "judul": judul,
            "diputar": diputar
        }

        lagu.append(data_lagu)

    print("\nData sebelum diurutkan:")
    tampilkan_lagu(lagu)

    bubble_sort_playcount(lagu, n)

    print("\nHasil setelah diurutkan (Bubble Sort - Paling Banyak Diputar):")
    tampilkan_lagu(lagu)


if __name__ == "__main__":
    main()