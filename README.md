# Analisis Data Chess dengan Pandas

Proyek ini berisi panduan setup lingkungan Python di VS Code serta skrip pengolahan awal dan analisis dataset **Chess Game Dataset (Lichess)** (`games.csv`) dari Kaggle menggunakan library `pandas`.

## Preview Infografis Panduan
![Infografis Cara Install Pandas dan Analisis Data Chess di VS Code](infografis_chess_pandas.jpg)

## Struktur File di Repository
- `cek_data.py` — Skrip untuk memeriksa struktur dataset, jumlah baris/kolom, tipe data, *missing value*, duplikat, statistik deskriptif, dan distribusi kolom utama.
- `analisis_chess.py` — Skrip untuk membersihkan duplikat berdasarkan `id` pertandingan dan menampilkan ringkasan pemenang, status kemenangan, pembukaan (*opening*) terpopuler, rata-rata rating, serta rata-rata jumlah giliran (*turns*).
- `infografis_chess_pandas.jpg` — Infografis 6 langkah instalasi `pandas` dengan *virtual environment* di VS Code untuk proyek data Chess.

## Preview Ringkasan Data & Analisis (`games.csv`)
Dataset Lichess pada `games.csv` memuat data pertandingan catur daring dengan kolom utama seperti:
- `id`: ID unik pertandingan
- `rated`: Status pertandingan *rated* atau *casual*
- `turns`: Jumlah giliran dalam satu pertandingan
- `victory_status`: Cara permainan berakhir (misalnya *mate*, *resign*, *outoftime*, *draw*)
- `winner`: Pemenang pertandingan (`white`, `black`, atau `draw`)
- `white_rating` & `black_rating`: Rating pemain Putih dan Hitam
- `opening_name`: Nama pembukaan catur yang dimainkan

### Contoh Output Pengecekan & Analisis (`cek_data.py` & `analisis_chess.py`)
```text
=== UKURAN DATA (BARIS, KOLOM) ===
(20058, 16)

=== DISTRIBUSI PEMENANG ===
white    10001
black     9107
draw       950

=== STATUS AKHIR PERTANDINGAN ===
resign       11147
mate          6325
outoftime     1680
draw           906

=== TOP 5 OPENING POPULER ===
Van't Kruijs Opening                             368
Sicilian Defense                                358
Sicilian Defense: Bowdler Attack               296
Scotch Game                                     271
French Defense: Knight Variation                271
