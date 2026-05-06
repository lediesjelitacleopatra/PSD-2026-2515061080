import string

def sequential_search_kata(kalimat, target):
    # hapus tanda baca
    kalimat = kalimat.translate(str.maketrans('', '', string.punctuation))

    kata_list = kalimat.split()
    count = 0
    indeks = []

    for i in range(len(kata_list)):
        if kata_list[i].lower() == target.lower():
            count += 1
            indeks.append(i)

    return count, indeks


def main():
    kalimat = input("Masukkan sebuah kalimat: ")
    target = input("Masukkan kata yang ingin dicari: ")

    count, indeks = sequential_search_kata(kalimat, target)

    print(f"\nKalimat: {kalimat}")

    if count > 0:
        print(f"Kata '{target}' ditemukan sebanyak {count} kali.")
        print(f"Terdapat pada indeks: {indeks}")
    else:
        print(f"Kata '{target}' tidak ditemukan.")


if __name__ == "__main__":
    main()