# Contoh Penggunaan Symbolab

Dokumen ini berisi berbagai contoh penggunaan Symbolab untuk berbagai jenis soal matematika.

## 1. Aljabar

### Penyederhanaan Ekspresi
```
Menu: 1 (Aljabar)
Pilih: 1 (Sederhanakan)

Input: (x+1)^2 - x^2
Output: 2*x + 1

Input: (2*x + 3)*(x - 1)
Output: 2*x^2 + x - 3
```

### Faktorisasi
```
Menu: 1 (Aljabar)
Pilih: 2 (Faktorisasi)

Input: x^2 - 4
Output: (x - 2)*(x + 2)

Input: x^2 - 5*x + 6
Output: (x - 3)*(x - 2)

Input: x^3 - 1
Output: (x - 1)*(x^2 + x + 1)
```

### Ekspansi
```
Menu: 1 (Aljabar)
Pilih: 3 (Expand)

Input: (x+2)^3
Output: x^3 + 6*x^2 + 12*x + 8

Input: (x+y)^2
Output: x^2 + 2*x*y + y^2
```

### Menyelesaikan Persamaan
```
Menu: 1 (Aljabar)
Pilih: 4 (Selesaikan persamaan)

Input: x^2 - 5*x + 6
Variabel: x
Output: x = [2, 3]

Input: 2*x + 5
Variabel: x
Output: x = [-5/2]

Input: x^2 - 2
Variabel: x
Output: x = [-sqrt(2), sqrt(2)]
```

## 2. Trigonometri

### Penyederhanaan
```
Menu: 2 (Trigonometri)
Pilih: 1 (Sederhanakan)

Input: sin(x)^2 + cos(x)^2
Output: 1

Input: sin(2*x)
Output: 2*sin(x)*cos(x)

Input: cos(2*x)
Output: -sin(x)^2 + cos(x)^2
```

### Hitung Nilai
```
Menu: 2 (Trigonometri)
Pilih: 2 (Hitung nilai)

Fungsi: sin
Nilai: pi/4
Output: sqrt(2)/2 = 0.7071

Fungsi: cos
Nilai: pi/3
Output: 1/2 = 0.5

Fungsi: tan
Nilai: pi/4
Output: 1
```

## 3. Turunan (Derivative)

### Turunan Pertama
```
Menu: 3 (Turunan)

Input: x^3 + 2*x^2 + x
Variabel: x
Orde: 1
Output: dy/dx = 3*x^2 + 4*x + 1

Input: sin(x)
Variabel: x
Orde: 1
Output: dy/dx = cos(x)

Input: e^x
Variabel: x
Orde: 1
Output: dy/dx = exp(x)
```

### Turunan Kedua
```
Menu: 3 (Turunan)

Input: x^4
Variabel: x
Orde: 2
Output: d²y/dx² = 12*x^2

Input: sin(x)
Variabel: x
Orde: 2
Output: d²y/dx² = -sin(x)
```

## 4. Integral

### Integral Tak Tentu
```
Menu: 4 (Integral)
Pilih: 1 (Tak tentu)

Input: x^2 + 2*x
Variabel: x
Output: ∫(x^2 + 2*x) dx = x^3/3 + x^2 + C

Input: sin(x)
Variabel: x
Output: ∫sin(x) dx = -cos(x) + C

Input: 1/x
Variabel: x
Output: ∫(1/x) dx = log(x) + C
```

### Integral Tentu
```
Menu: 4 (Integral)
Pilih: 2 (Tentu)

Input: x^2
Variabel: x
Batas bawah: 0
Batas atas: 1
Output: ∫[0 to 1] x^2 dx = 1/3

Input: sin(x)
Variabel: x
Batas bawah: 0
Batas atas: pi
Output: ∫[0 to π] sin(x) dx = 2
```

## 5. Limit

### Limit Mendekati Titik
```
Menu: 5 (Limit)

Input: sin(x)/x
Variabel: x
Menuju: 0
Output: lim (x → 0) sin(x)/x = 1

Input: (x^2 - 1)/(x - 1)
Variabel: x
Menuju: 1
Output: lim (x → 1) (x^2-1)/(x-1) = 2
```

### Limit Tak Hingga
```
Menu: 5 (Limit)

Input: 1/x
Variabel: x
Menuju: oo
Output: lim (x → ∞) 1/x = 0

Input: (2*x^2 + 3*x)/(x^2 + 1)
Variabel: x
Menuju: oo
Output: lim (x → ∞) = 2
```

## 6. Matriks

### Determinan
```
Menu: 6 (Matriks)
Pilih: 1 (Determinan)

Baris: 2
Kolom: 2
Baris 1: 1, 2
Baris 2: 3, 4
Output: Determinan = -2

Baris: 3
Kolom: 3
Baris 1: 1, 0, 2
Baris 2: -1, 3, 1
Baris 3: 2, 1, 0
Output: Determinan = -13
```

### Inverse Matriks
```
Menu: 6 (Matriks)
Pilih: 2 (Inverse)

Baris: 2
Kolom: 2
Baris 1: 4, 7
Baris 2: 2, 6
Output: 
Matrix([
  [ 3/5, -7/10],
  [-1/5,  2/5 ]
])
```

### Eigenvalue & Eigenvector
```
Menu: 6 (Matriks)
Pilih: 3 (Eigenvalue)

Baris: 2
Kolom: 2
Baris 1: 4, 2
Baris 2: 1, 3
Output:
Eigenvalues: {2: 1, 5: 1}
Eigenvectors:
  λ = 2, v = [-2, 1]
  λ = 5, v = [1, 1]
```

### Transpose
```
Menu: 6 (Matriks)
Pilih: 4 (Transpose)

Baris: 2
Kolom: 3
Baris 1: 1, 2, 3
Baris 2: 4, 5, 6
Output:
Matrix([
  [1, 4],
  [2, 5],
  [3, 6]
])
```

### Perkalian Matriks
```
Menu: 6 (Matriks)
Pilih: 5 (Perkalian)

Matriks A:
Baris: 2, Kolom: 2
Baris 1: 1, 2
Baris 2: 3, 4

Matriks B:
Baris: 2, Kolom: 2
Baris 1: 5, 6
Baris 2: 7, 8

Output: A × B =
Matrix([
  [19, 22],
  [43, 50]
])
```

## 7. Persamaan Diferensial

### Orde Pertama
```
Menu: 7 (Persamaan Diferensial)

Input: f(x).diff(x) - f(x)
Output: Eq(f(x), C1*exp(x))
(Solusi: y = C₁eˣ)

Input: f(x).diff(x) + 2*f(x)
Output: Eq(f(x), C1*exp(-2*x))
(Solusi: y = C₁e⁻²ˣ)
```

### Orde Kedua
```
Menu: 7 (Persamaan Diferensial)

Input: f(x).diff(x, 2) + f(x)
Output: Eq(f(x), C1*sin(x) + C2*cos(x))
(Solusi: y = C₁sin(x) + C₂cos(x))
```

## Tips Penggunaan

1. **Perkalian**: Selalu gunakan `*` untuk perkalian
   - Benar: `2*x`
   - Salah: `2x`

2. **Pangkat**: Gunakan `^` atau `**`
   - Benar: `x^2` atau `x**2`
   - Salah: `x2`

3. **Konstanta Matematika**:
   - π (pi): gunakan `pi`
   - e: gunakan `e` atau `E`
   - ∞ (infinity): gunakan `oo`

4. **Fungsi Trigonometri**:
   - sin, cos, tan, asin, acos, atan
   - sinh, cosh, tanh (hiperbolik)

5. **Fungsi Logaritma**:
   - ln(x): gunakan `log(x)`
   - log₁₀(x): gunakan `log(x, 10)`

6. **Akar**:
   - √x: gunakan `sqrt(x)`
   - ∛x: gunakan `x**(1/3)` atau `cbrt(x)`

## Keyboard Shortcuts

- `Ctrl+C`: Keluar dari program
- `Enter`: Lanjutkan ke menu berikutnya

---

Untuk bantuan lebih lanjut, pilih menu `9` (Bantuan) di program utama.
