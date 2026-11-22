import pandas as pd

# Memuat dataset Chess dari Kaggle (games.csv)
df = pd.read_csv("games.csv")

# 1. Melihat 5 baris data teratas dan terbawah
print("=== 5 DATA TERATAS ===")
print(df.head())

print("\n=== 5 DATA TERBAWAH ===")
print(df.tail())

# 2. Melihat ukuran data (jumlah baris & kolom) serta nama kolom
print("\n=== UKURAN DATA (BARIS, KOLOM) ===")
print(df.shape)

print("\n=== NAMA KOLOM ===")
print(df.columns.tolist())

# 3. Melihat tipe data setiap kolom dan informasi non-null
print("\n=== INFO TIPE DATA & NON-NULL ===")
print(df.info())

# 4. Mengecek jumlah missing value (data kosong) per kolom
print("\n=== JUMLAH MISSING VALUE PER KOLOM ===")
print(df.isnull().sum())

# 5. Mengecek jumlah baris duplikat (keseluruhan & berdasarkan id pertandingan)
print("\n=== JUMLAH BARIS DUPLIKAT ===")
print("Duplikat penuh:", df.duplicated().sum())
if "id" in df.columns:
  print(
      "Duplikat berdasarkan kolom 'id':", df.duplicated(subset=["id"]).sum()
  )

# 6. Statistik deskriptif untuk kolom numerik (rating, turns, dsb.)
print("\n=== STATISTIK DESKRIPTIF (NUMERIK) ===")
print(df.describe())

# 7. Mengecek nilai unik pada kolom kategorikal penting di data chess
kolom_kategorikal = ["winner", "victory_status", "rated", "opening_name"]
for col in kolom_kategorikal:
  if col in df.columns:
    print(f"\n=== DISTRIBUSI NILAI '{col}' (TOP 10) ===")
    print(df[col].value_counts(dropna=False).head(10))
