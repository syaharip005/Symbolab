
Program pembantu matematika lengkap untuk mahasiswa dan pelajar Indonesia. Mendukung berbagai operasi matematika dari Aljabar hingga Persamaan Diferensial.

## ✨ Fitur

- **Aljabar**: Penyederhanaan, faktorisasi, ekspansi, dan penyelesaian persamaan
- **Trigonometri**: Simplifikasi dan perhitungan nilai trigonometri
- **Turunan/Derivative**: Menghitung turunan pertama, kedua, dan seterusnya
- **Integral**: Integral tak tentu dan integral tentu
- **Limit**: Menghitung limit fungsi
- **Matriks**: Determinan, inverse, eigenvalue, eigenvector, transpose, dan perkalian
- **Persamaan Diferensial**: Menyelesaikan persamaan diferensial
- **Riwayat**: Menyimpan riwayat perhitungan

## 🚀 Instalasi

### Prasyarat
- Python 3.7 atau lebih tinggi

### Langkah Instalasi

1. Clone repository ini:
```bash
git clone https://github.com/syaharip005/Symbolab.git
cd Symbolab
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Cara Penggunaan

Jalankan program dengan perintah:
```bash
python symbolab.py
```

Atau di Linux/Mac (jika sudah chmod +x):
```bash
./symbolab.py
```

### Menu Utama

Setelah menjalankan program, Anda akan melihat menu:

```
============================================================
    SYMBOLAB - AI MATH SOLVER UNTUK INDONESIA
============================================================

Pilih jenis operasi matematika:
1. Aljabar (persamaan, penyederhanaan, faktorisasi)
2. Trigonometri (sin, cos, tan, simplifikasi)
3. Turunan/Derivative (dy/dx)
4. Integral (∫)
5. Limit (lim)
6. Matriks (determinan, inverse, eigenvalue)
7. Persamaan Diferensial
8. Lihat Riwayat
9. Bantuan
0. Keluar
```

Pilih menu sesuai operasi yang ingin dilakukan.

## 📖 Contoh Penggunaan

### 1. Aljabar

**Sederhanakan ekspresi:**
```
Pilih menu: 1
Pilih operasi: 1
Masukkan ekspresi: (x+1)^2 - x^2
Hasil: 2*x + 1
```

**Faktorisasi:**
```
Pilih menu: 1
Pilih operasi: 2
Masukkan ekspresi: x^2 - 4
Hasil faktorisasi: (x - 2)*(x + 2)
```

**Selesaikan persamaan:**
```
Pilih menu: 1
Pilih operasi: 4
Masukkan persamaan: x^2 - 5*x + 6
Selesaikan untuk variabel: x
Solusi: x = [2, 3]
```

### 2. Trigonometri

**Sederhanakan:**
```
Pilih menu: 2
Pilih operasi: 1
Masukkan ekspresi: sin(x)^2 + cos(x)^2
Hasil: 1
```

**Hitung nilai:**
```
Pilih menu: 2
Pilih operasi: 2
Fungsi: sin
Nilai: pi/4
sin(pi/4) = sqrt(2)/2 = 0.7071067811865475
```

### 3. Turunan

```
Pilih menu: 3
Masukkan fungsi: x^3 + 2*x^2 + x
Turunan terhadap variabel: x
Orde turunan: 1
dy/dx = 3*x^2 + 4*x + 1
```

### 4. Integral

**Integral tak tentu:**
```
Pilih menu: 4
Pilih jenis: 1
Masukkan fungsi: x^2 + 2*x
Integralkan terhadap variabel: x
∫(x^2 + 2*x) dx = x^3/3 + x^2 + C
```

**Integral tentu:**
```
Pilih menu: 4
Pilih jenis: 2
Masukkan fungsi: x^2
Integralkan terhadap variabel: x
Batas bawah: 0
Batas atas: 1
∫[0 to 1] (x^2) dx = 1/3
Nilai numerik: 0.333333333333333
```

### 5. Limit

```
Pilih menu: 5
Masukkan fungsi: sin(x)/x
Variabel: x
Limit menuju: 0
Arah: (tekan enter)
lim (x → 0) sin(x)/x = 1
```

### 6. Matriks

**Determinan matriks 2x2:**
```
Pilih menu: 6
Pilih operasi: 1
Jumlah baris: 2
Jumlah kolom: 2
Baris 1: 1, 2
Baris 2: 3, 4
Determinan = -2
```

**Eigenvalue:**
```
Pilih menu: 6
Pilih operasi: 3
Jumlah baris: 2
Jumlah kolom: 2
Baris 1: 4, 2
Baris 2: 1, 3
Eigenvalues: {2: 1, 5: 1}
```

### 7. Persamaan Diferensial

```
Pilih menu: 7
Masukkan persamaan diferensial: f(x).diff(x) - f(x)
Solusi: Eq(f(x), C1*exp(x))
```

## 📝 Catatan Penting

- **Perkalian**: Gunakan `*` untuk perkalian eksplisit, contoh: `2*x` bukan `2x`
- **Pangkat**: Gunakan `^` atau `**`, contoh: `x^2` atau `x**2`
- **Pi**: Gunakan `pi` untuk π
- **Infinity**: Gunakan `oo` untuk ∞
- **Fungsi Trigonometri**: sin, cos, tan, asin, acos, atan
- **Fungsi Logaritma**: log (ln), log(x, 10) untuk log basis 10
- **Konstanta**: e untuk bilangan Euler

## 🛠️ Teknologi

- **Python 3**: Bahasa pemrograman utama
- **SymPy**: Library matematika simbolik untuk Python

## 👨‍💻 Kontributor

- Achmad Syarifudin (syaharip005)

## 📄 Lisensi

MIT License - lihat file [LICENSE](LICENSE) untuk detail lengkap.

## 🙏 Terima Kasih

Terima kasih telah menggunakan Symbolab! Semoga membantu dalam pembelajaran matematika Anda.

---

**Selamat Belajar Matematika! 🎓📐**
