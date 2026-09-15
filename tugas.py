produk = {
    "nama": "Iphone 20 pro max 5tb",
    "harga": 999999,
    "stok": 5
}

while True:
    print("\nMenu Produk")
    print("1. Tampilkan data")
    print("2. Tambah kategori")
    print("3. Ubah harga")
    print("4. Hapus kategori")
    print("5. Keluar")

    pilihan = input("Pilih menu yang ada di atas (1-5): ")

    # 1. Tampilkan data
    if pilihan == "1":
        print("\nData Produk")
        print("Nama  :", produk["nama"])
        print("Harga :", produk["harga"])
        print("Stok  :", produk["stok"])

        if "kategori" in produk:
            print("Kategori :", produk["kategori"])

    # 2. Tambah kategori
    elif pilihan == "2":
        kategori = input("Masukkan kategori produk: ")
        produk["kategori"] = kategori
        print("\nKategori berhasil ditambahkan.")

    # 3. Ubah harga
    elif pilihan == "3":
        harga_baru = int(input("Masukkan harga baru: "))
        produk["harga"] = harga_baru
        print("\nHarga berhasil diubah.")

    # 4. Hapus kategori
    elif pilihan == "4":
        if "kategori" in produk:
            del produk["kategori"]
            print("\nKategori berhasil dihapus.")
        else:
            print("\nData kategori belum ada.")

    # 5. Keluar
    elif pilihan == "5":
        print("\nTerima Kasih dan datang kembali.")
        break

    # Jika input tidak valid
    else:
        print("\nPilihan tidak valid.")

print("\nData Produk Akhir")
print(produk)