# Search Algoritma 

## Linear Search
- Linear Search, atau pencarian linear, adalah algoritma pencarian yang paling sederhana. Ini bekerja dengan cara memeriksa setiap elemen dalam kumpulan data secara berurutan hingga elemen yang dicari ditemukan atau sampai seluruh kumpulan data telah diperiksa. Proses pemeriksaan setiap elemen dilakukan dengan membandingkan secara berurutan.

- Misalkan nilai yang akan dicari adalah 90, maka akan dilakukan pencarian mulai dari elemen ke-1 index 0 hingga ketemu nilai yang dicari. 

- Proses mencarian dengan metode pencarian sequential (beruntun) ini selalu dimulai dari elemen ke-1 index 0, sehingga jika akan dilakukan pencarian kembali, proses pencarian akan diulangi lagi dengan melakukan pengecekan dari elemen ke-1.

Contoh : 
indeks = 0
ketemu = False
angkaCari = 90
angkaCari = data[indeks] => 90 = data[0] 90 = 72 (False) => indeks +=1 = 1
angkaCari = data[indeks] => 90 = data[1] => 90 = 85 (False) => indeks +=1 = 2
angkaCari = data[indeks] => 90 = data[2] => 90 = 60 (False) => indeks +=1 = 3
angkaCari = data[indeks] => 90 = data[3] => 90 = 90 (True) => Pencarian selesai
(ketemu=True), maka angkaCari berada pada indeks = 2

Dalam kompleksitas waktu dan ruang, Algoritma Linear Searching : 
- Kasus Terbaik (Best - Case)
- Kasus Terburuk (Worst - Case) = Jika pencarian dilakukan hingga akhir index
- Kasus Rata-Rata (Average- Case) = O(n) 

Waktu berjalannya algoritma tumbuh secara proporsional atau berbanding lurus dengan ukuran inputnya. Jika jumlah data (n) menjadi dua kali lipat, waktu yang dibutuhkan algoritma juga akan menjadi sekitar dua kali lipat


## Binary Searching
- Binary Searhing, merupakan metoda dalam    mencari data dengan membagi 2 atau pencarian dimulai dari index tengah. Dan membandingkan dengan data yang di cari.

- Data list pada Binary Search mengharuskan pengurutan dara terlebih dahulu sebelum memulai proses pencarian. Binary Searching lebih cepar dibandingkan Linear Searching karena dapat mereduksi jumlah elemen yang di cari sehingga iterasi yang dihasilkan lebih sedikit.

## Binary Search Algorithm

Langkah-langkah algoritma **Binary Search**:

1. Membaca data yang ada di dalam list. Jika data belum terurut, maka lakukan pengurutan terlebih dahulu.

2. Menentukan data yang akan dicari di dalam list.

3. Menentukan index tengah dengan rumus:

   ```
   mid = (index_awal + index_akhir) // 2
   ```

4. Bandingkan nilai yang dicari dengan nilai pada index tengah:

   * Jika **nilai yang dicari = nilai pada index tengah**, maka pencarian dihentikan karena data ditemukan.
   * Jika **nilai yang dicari > nilai pada index tengah**, maka pencarian dilakukan pada bagian kanan list dengan mengubah:

     ```
     index_awal = mid + 1
     ```
   * Jika **nilai yang dicari < nilai pada index tengah**, maka pencarian dilakukan pada bagian kiri list dengan mengubah:

     ```
     index_akhir = mid - 1
     ```

5. Hitung kembali index tengah:

   ```
   mid = (index_awal + index_akhir) // 2
   ```

6. Ulangi langkah perbandingan selama:

   ```
   index_awal <= index_akhir
   ```

   dan data belum ditemukan.
