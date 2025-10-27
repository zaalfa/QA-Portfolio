# 🧪 QA Automation Portfolio - Selenium Practice Testing

## 📘 Overview

Proyek ini merupakan bagian dari portofolio QA Automation yang dibuat untuk mendemonstrasikan kemampuan dalam:

- Membuat test case manual dan otomatis
- Menggunakan Selenium WebDriver untuk pengujian web
- Melakukan verifikasi hasil dengan screenshot otomatis

Website yang diuji: https://practicesoftwaretesting.com

---

## 🎯 Test Plan

### Tujuan

Melakukan pengujian otomatis terhadap fitur **Login Page** untuk memastikan bahwa sistem dapat:

- Menerima kredensial yang valid (positive test)
- Menolak kredensial yang tidak valid (negative test)

### Lingkup

| Jenis Test    | Keterangan                                 |
| ------------- | ------------------------------------------ |
| Functional    | Login form & validasi input                |
| Positive Case | Login menggunakan email dan password valid |
| Negative Case | Login menggunakan password salah           |

### Tools & Environment

| Komponen | Versi / Detail    |
| -------- | ----------------- |
| Bahasa   | Python 3.9        |
| Library  | Selenium 4.36     |
| Browser  | Google Chrome 141 |
| Driver   | ChromeDriver 141  |
| OS       | Windows 10        |
| IDE      | VS Code           |

---

## 🧩 Test Cases

| ID    | Test Case     | Tujuan                                                  | Langkah                                                                                                             | Data Input                                                 | Hasil Diharapkan                               |
| ----- | ------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------- |
| TC001 | Login Valid   | Memastikan login berhasil dengan kredensial benar       | 1. Buka halaman utama <br> 2. Klik **Sign In** <br> 3. Masukkan email dan password valid <br> 4. Klik **Login**     | Email: `zalfarmdhni@gmail.com` <br> Password: `Test01-123` | Pengguna diarahkan ke halaman **My Account**   |
| TC002 | Login Invalid | Memastikan sistem menolak login dengan kredensial salah | 1. Buka halaman utama <br> 2. Klik **Sign In** <br> 3. Masukkan email valid & password salah <br> 4. Klik **Login** | Email: `zalfarmdhni@gmail.com` <br> Password: `Salah123`   | Muncul pesan error “Invalid email or password” |

---

## ⚙️ Automation Implementation

### Struktur Folder

```
selenium_practice_testing/
│
├── drivers/
│   └── chromedriver.exe
│
├── screenshots/
│   ├── login_failed.png
│   └── login_success.png
│
└── tests/
    ├── test_login_valid.py
    └── test_login_invalid.py
```

## 🧾 Test Results

### TC001 - Login Valid ✅

**Status:** Passed  
**Bukti Screenshot:**  
![Login Success](../selenium_practice_testing/screenshots/login_success.png)

---

### TC002 - Login Invalid ❌

**Status:** Passed (menampilkan pesan error sesuai ekspektasi)  
**Bukti Screenshot:**  
![Login Failed](../selenium_practice_testing/screenshots/login_failed.png)

---

## 🧠 Summary

- Automation berjalan sesuai rencana dan berhasil menguji fitur login.
- Hasil test menunjukkan sistem bekerja sesuai ekspektasi untuk input valid dan invalid.
- Script menggunakan **explicit wait** untuk stabilitas dan **screenshot otomatis** untuk dokumentasi hasil.

### Potensi Pengembangan

- Menambahkan automation untuk fitur Register & Logout.
- Mengintegrasikan hasil test dengan `pytest-html` untuk laporan otomatis.
- Menambahkan CI/CD pipeline (misalnya GitHub Actions) agar test berjalan otomatis setiap kali commit.

---

🧑‍💻 **Dibuat oleh:** T. Zalfa Ramadhani
📅 **Tahun:** 2025  
📍 **Tujuan:** Portofolio QA Automation berbasis Selenium.
