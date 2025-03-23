import random
import datetime

barang_list = []

def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))

    barang = {
        "id": random.randint(1000, 9999),
        "nama": nama_barang,
        "jumlah": jumlah,
        "dipinjam": 0,
        "riwayat_peminjaman": []
    }

    barang_list.append(barang)
    print(f"Barang '{nama_barang}' berhasil ditambahkan!\n")

def pinjam_barang():
    if not barang_list:
        print("Belum ada barang yang tersedia.\n")
        return
    
    lihat_barang()
    id_barang = int(input("Masukkan ID barang yang ingin dipinjam: "))
    peminjam = input("Masukkan nama peminjam: ")
    jumlah_pinjam = int(input("Masukkan jumlah yang dipinjam: "))

    for barang in barang_list:
        if barang["id"] == id_barang:
            if barang["jumlah"] - barang["dipinjam"] >= jumlah_pinjam:
                barang["dipinjam"] += jumlah_pinjam
                barang["riwayat_peminjaman"].append({
                    "peminjam": peminjam,
                    "jumlah": jumlah_pinjam,
                    "tanggal": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                print(f"{jumlah_pinjam} {barang['nama']} berhasil dipinjam oleh {peminjam}!\n")
            else:
                print("Jumlah barang tidak mencukupi untuk dipinjam.\n")
            return
    
    print("ID barang tidak ditemukan.\n")

def lihat_barang():
    if not barang_list:
        print("Belum ada barang dalam inventaris.\n")
        return
    
    print("\nDaftar Barang di Inventaris:")
    for barang in barang_list:
        tersedia = barang["jumlah"] - barang["dipinjam"]
        print(f"[{barang['id']}] {barang['nama']} - Tersedia: {tersedia} (Total: {barang['jumlah']})")
        if barang["riwayat_peminjaman"]:
            print("   Riwayat Peminjaman:")
            for riwayat in barang["riwayat_peminjaman"]:
                print(f"   - {riwayat['peminjam']} ({riwayat['jumlah']} unit) pada {riwayat['tanggal']}")
    print()

def menu():
    while True:
        print("=== Sistem Peminjaman Barang ===")
        print("1. Tambah Barang")
        print("2. Pinjam Barang")
        print("3. Lihat Daftar Barang")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            pinjam_barang()
        elif pilihan == "3":
            lihat_barang()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem peminjaman barang.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.\n")

menu()
