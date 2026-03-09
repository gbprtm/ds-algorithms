## Merge Sort

**Merge Sort** adalah algoritma *sorting* yang dikenal karena efisiensi dan stabilitasnya.
Algoritma ini menggunakan konsep **Divide and Conquer**, yaitu membagi masalah menjadi bagian yang lebih kecil, menyelesaikannya secara rekursif, lalu menggabungkannya kembali menjadi solusi yang terurut.

### Cara Kerja

Merge Sort mengurutkan sebuah array `A[0..n-1]` dengan langkah-langkah berikut:

1. Membagi array menjadi dua bagian:

   * `A[0..(n/2)-1]`
   * `A[(n/2)..n-1]`
2. Mengurutkan kedua bagian tersebut secara rekursif.
3. Menggabungkan kedua bagian yang telah terurut menjadi satu array yang terurut.

### Pseudocode

```
MERGESORT(A)

if n > 1
    bagi A menjadi B dan C
    MERGESORT(B)
    MERGESORT(C)
    MERGE(B, C, A)
```

### Kompleksitas Algoritma

Kompleksitas waktu Merge Sort adalah:

```
Θ(n log n)
```

### Analisis Rekurensi (Master Theorem)

Persamaan rekurensi Merge Sort:

```
T(n) = aT(n/b) + f(n)
```

Dengan nilai:

```
a = 2
b = 2
f(n) = n
```

Sehingga:

```
T(n) = 2T(n/2) + n
```

Hitung nilai:

```
c = log_b(a)
c = log₂(2) = 1
```

Maka:

```
n^(log_b a) = n¹ = n
```

Karena:

```
f(n) = n
```

maka menurut **Master Theorem**:

```
T(n) = Θ(n log n)
```
### Hubungan Pengulangan (Recurrence Relation) Merge Sort

Relasi perulangan dari algoritma **Merge Sort** dapat dituliskan sebagai berikut:

```
T(n) =
    Θ(1)              jika n = 1
    2T(n/2) + Θ(n)    jika n > 1
```

Penjelasan:

* **T(n)** mewakili total waktu yang dibutuhkan algoritma untuk mengurutkan array dengan ukuran `n`.
* **2T(n/2)** mewakili waktu yang dibutuhkan untuk mengurutkan dua bagian array secara rekursif.
  Karena array dibagi menjadi dua bagian dengan ukuran masing-masing `n/2`, maka terdapat dua pemanggilan rekursif.
* **Θ(n)** mewakili waktu yang dibutuhkan untuk **menggabungkan (merge)** dua bagian array yang telah terurut.

---

### Analisis Kompleksitas Merge Sort

#### Kompleksitas Waktu

* **Kasus Terbaik (Best Case)** :
  `O(n log n)` — terjadi ketika array sudah terurut atau hampir terurut.

* **Kasus Rata-rata (Average Case)** :
  `O(n log n)` — terjadi ketika data dalam array berada dalam urutan acak.

* **Kasus Terburuk (Worst Case)** :
  `O(n log n)` — terjadi ketika array berada dalam urutan terbalik.

Merge Sort memiliki kompleksitas waktu yang sama pada ketiga kasus tersebut karena proses pembagian dan penggabungan array selalu dilakukan dengan cara yang sama.
