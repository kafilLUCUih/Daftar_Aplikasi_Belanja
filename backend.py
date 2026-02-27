import os

DATA_FILE = "daftar_belanja.txt"

def baca_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def simpan_data(daftar):
    with open(DATA_FILE, "w") as f:
        for item in daftar:
            f.write(f"{item}\n")

def tambah_item(item):
    daftar = baca_data()
    daftar.append(item)
    simpan_data(daftar)
    return f"✅ Item '{item}' berhasil ditambahkan."

def hapus_item(no):
    daftar = baca_data()
    if no < 1 or no > len(daftar):
        return "⚠️ Nomor item tidak valid."
    item = daftar.pop(no - 1)
    simpan_data(daftar)
    return f"✅ Item '{item}' berhasil dihapus."

def edit_item(no, nama_baru):
    daftar = baca_data()
    if no < 1 or no > len(daftar):
        return "⚠️ Nomor item tidak valid."
    lama = daftar[no - 1]
    daftar[no - 1] = nama_baru
    simpan_data(daftar)
    return f"✅ Item '{lama}' diganti menjadi '{nama_baru}'."

def cari_item(kata):
    daftar = baca_data()
    return [item for item in daftar if kata.lower() in item.lower()]