# Portofolio Quality Assurance (QA) - Portal Alumni Universitas Brawijaya

## 1. Informasi Proyek
**Judul Proyek:** Portal Alumni Universitas Brawijaya  
**Peran:** Quality Assurance (Manual Testing)  
**Periode:** 2023  
**Metode Pengembangan:** Waterfall  
**Jenis Pengujian:** White Box Testing dan Black Box Testing

## 2. Deskripsi Proyek
Proyek ini merupakan pengembangan website Portal Alumni Universitas Brawijaya yang bertujuan untuk memfasilitasi pertukaran informasi di kalangan alumni, menyediakan data lowongan kerja, artikel aktivitas alumni, serta profil alumni berprestasi. Website ini dirancang menggunakan pendekatan Object Oriented Programming (OOP) dan diuji menggunakan metode Waterfall. Saya berperan sebagai Quality Assurance untuk memastikan setiap fitur berfungsi sesuai dengan kebutuhan pengguna.

## 3. Tujuan Testing
Melakukan pengujian untuk memastikan seluruh fungsi aplikasi berjalan sesuai dengan requirement, mendeteksi bug, dan memberikan laporan hasil pengujian yang dapat digunakan tim developer untuk melakukan perbaikan.

## 4. Jenis Pengujian
- **White Box Testing** – menggunakan metode Basis Path Testing untuk menganalisis logika program dan kompleksitas jalur eksekusi.  
- **Black Box Testing** – melakukan pengujian fungsionalitas berdasarkan kebutuhan pengguna tanpa melihat kode sumber.

## 5. Contoh Test Case

| No | Skenario Uji | Langkah Uji | Data Uji | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|--------------|-------------|----------|------------------------|--------------|--------|
| 1 | Login Admin | 1. Buka halaman login<br>2. Masukkan username dan password valid<br>3. Klik Login | Username dan password valid | Dashboard admin tampil | Sesuai | ✅ |
| 2 | Tambah Data Alumni | 1. Login sebagai admin<br>2. Klik 'Tambah Data'<br>3. Isi form dan submit | Data alumni valid | Pesan 'Data berhasil ditambahkan' muncul | Sesuai | ✅ |
| 3 | Tambah Data Kosong | 1. Login sebagai admin<br>2. Klik 'Tambah Data' tanpa isi form | Form kosong | Pesan 'Harap diisi' muncul | Sesuai | ✅ |

## 6. Hasil Pengujian
Dari hasil pengujian yang dilakukan, seluruh fungsi utama berjalan sesuai kebutuhan pengguna. Tiga bug fungsional ditemukan selama tahap pengujian dan telah diperbaiki oleh tim developer. Proses testing dilakukan secara manual menggunakan browser (Google Chrome), PHPMyAdmin untuk verifikasi data backend, serta dokumentasi test case dan bug report menggunakan Microsoft Excel.

## 7. Tools yang Digunakan
- Browser (Google Chrome)  
- XAMPP (Local Server)  
- PHPMyAdmin (Database Management)  
- Microsoft Excel (Test Case dan Bug Report)  
- Visual Studio Code (Editor Kode)

## 8. Kesimpulan
Melalui proyek ini, saya mempraktikkan proses Quality Assurance secara menyeluruh mulai dari pembuatan test case, pelaksanaan pengujian fungsional dan struktural, hingga dokumentasi hasil uji. Pengalaman ini mengasah kemampuan saya dalam analisis sistem, ketelitian, serta komunikasi dengan tim developer untuk memastikan kualitas perangkat lunak.

