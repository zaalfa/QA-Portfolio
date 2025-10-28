# 🧩 Portofolio Quality Assurance (QA) – Portal Alumni Universitas Brawijaya

## 1. Informasi Proyek

**Judul Proyek:** Portal Alumni Universitas Brawijaya  
**Peran:** QA Tester (Manual Testing) & Project Responsible  
**Periode:** 2023  
**Metode Pengembangan:** Waterfall  
**Jenis Pengujian:** White Box Testing dan Black Box Testing

---

## 2. Deskripsi Proyek

Portal Alumni Universitas Brawijaya merupakan website yang dikembangkan untuk memfasilitasi komunikasi antar alumni, menampilkan informasi lowongan kerja, aktivitas alumni, serta profil alumni berprestasi.

Dalam proyek ini saya berperan sebagai **QA tester sekaligus penanggung jawab proyek**. Saya terlibat langsung mulai dari perencanaan sistem, pengembangan antarmuka, hingga pengujian fungsionalitas untuk memastikan setiap fitur berjalan sesuai kebutuhan pengguna.  
Meskipun pengembangan dilakukan dalam waktu terbatas, proses QA tetap diterapkan secara sistematis untuk menjamin keandalan dan konsistensi fungsi website.

---

## 3. Tujuan Testing

- Memastikan seluruh fitur berjalan sesuai kebutuhan pengguna (requirement).
- Memverifikasi bahwa sistem tidak memiliki error logika maupun fungsional.
- Menjamin kualitas produk sebelum tahap finalisasi dan dokumentasi laporan proyek.

---

## 4. Jenis Pengujian

- **White Box Testing** – menggunakan metode _Basis Path Testing_ untuk menguji jalur logika program dan memastikan kompleksitas eksekusi sesuai standar.
- **Black Box Testing** – menguji fungsionalitas sistem berdasarkan kebutuhan pengguna tanpa melihat kode sumber, fokus pada input–output.

---

## 5. Contoh Test Case

| No  | Skenario Uji           | Langkah Uji                                                                           | Data Uji                    | Hasil yang Diharapkan                                                    | Hasil Aktual | Status |
| --- | ---------------------- | ------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------ | ------------ | ------ |
| 1   | Login Admin            | 1. Buka halaman login<br>2. Masukkan username dan password valid<br>3. Klik **Login** | Username dan password valid | Dashboard admin tampil                                                   | Sesuai       | ✅     |
| 2   | Tambah Data Alumni     | 1. Login sebagai admin<br>2. Klik **Tambah Data**<br>3. Isi form dan submit           | Data alumni valid           | Pesan _"Data berhasil ditambahkan!"_ muncul                              | Sesuai       | ✅     |
| 3   | Tambah Data Kosong     | 1. Login sebagai admin<br>2. Klik **Tambah Data** tanpa mengisi form                  | Form kosong                 | Pesan _"Harap diisi"_ muncul                                             | Sesuai       | ✅     |
| 4   | Input Link Tidak Valid | 1. Login sebagai admin<br>2. Tambah artikel alumni dengan link salah                  | URL tidak valid             | Pesan _"Link berita tidak valid. Harap masukkan URL yang benar."_ muncul | Sesuai       | ✅     |
| 5   | Akses Halaman DPKA UB  | 1. Buka halaman utama<br>2. Klik tautan layanan karir                                 | —                           | Sistem mengarahkan ke halaman resmi DPKA UB                              | Sesuai       | ✅     |

---

## 6. Hasil Pengujian

Berdasarkan hasil pengujian _White Box_ dan _Black Box_, seluruh fitur yang diimplementasikan berjalan dengan baik dan memenuhi spesifikasi kebutuhan.  
Tidak ditemukan bug fungsional maupun struktural selama proses pengujian.  
Semua test case mendapatkan hasil **“Valid”** sesuai laporan akhir proyek.

Pengujian dilakukan secara manual menggunakan browser (**Google Chrome**), dengan verifikasi data melalui **PHPMyAdmin** untuk memastikan konsistensi antara front-end dan database.

---

## 7. Tools yang Digunakan

- **Browser:** Google Chrome
- **Local Server:** XAMPP
- **Database Management:** PHPMyAdmin
- **Documentation:** Microsoft Excel (Test Case & QA Report)
- **Code Editor:** Visual Studio Code

---

## 8. Kesimpulan

Proyek ini menjadi pengalaman berharga dalam menerapkan proses _Quality Assurance_ secara menyeluruh — mulai dari pembuatan test case, pelaksanaan pengujian manual, hingga dokumentasi hasil uji.  
Seluruh pengujian menunjukkan bahwa sistem berfungsi dengan baik tanpa bug, serta telah memenuhi kebutuhan pengguna dan spesifikasi teknis yang ditetapkan.  
Melalui proyek ini, saya mengasah kemampuan analisis sistem, ketelitian dalam verifikasi hasil, dan komunikasi efektif dengan tim developer untuk menjaga kualitas produk perangkat lunak.
