
# [**USGenerator**](https://github.com/AgileRE-2023/USGenerator/)

<br />
<p align="center">
<img src="https://drive.google.com/uc?id=1WN6fC9X13gEjRKOts5--9lD71xAwtoCi">
</p>
<br />

Aplikasi ini memanfaatkan teknik *Natural Language Processing (NLP)* untuk mengotomatiskan pembuatan User Stories dari sebuah paragraf. Dengan menggunakan kerangka kerja *Django*, proyek ini menyediakan solusi web yang memungkinkan pengguna untuk dengan cepat dan konsisten menghasilkan User Story Scenarios. Pendekatan ini menyederhanakan proses tersebut, memastikan efisiensi waktu dalam penyusunan User Stories, sambil menjamin konsistensi dan hasil yang terstandarisasi. Pada akhirnya, ini meningkatkan praktik-praktik yang praktis dalam pengembangan produk dan layanan.


## Cara Instalasi 🚩

Instruksi berikut adalah cara menginstal aplikasi dalam sesi terminal, berikut adalah langkah-langkahnya :

#### 1.) Lakukan clone pada *repository*

```sh
  git clone https://github.com/AgileRE-2023/USGenerator.git
```

#### 2.) Masuk ke folder project USGenerator

```sh
  cd USGenerator
```

#### 3.) Masuk ke folder usg

```sh
  cd usg
```

#### 4.) Lakukan instalasi modul-modul yang digunakan

```sh
  pip install -r requirements.txt
```

#### 5.) Buat migrasi untuk membuat database

```sh
  python manage.py makemigrations
```
```sh
  python manage.py migrate
```

#### 6.) Jalankan aplikasi USGenerator

```sh
  python manage.py runserver
```

#### 7.) Akses aplikasi web di browser

```sh
  http://127.0.0.1:8000/
```


## Cara Penggunaan 📝
Untuk panduan lengkap mengenai prosedur penggunaan aplikasi dapat dilihat dari informasi berikut :

#### Registrasi
1. Tekan tombol **Sign up** pada halaman *Login*
2. Pada halaman *Registration*, isilah seluruh form dengan informasi yang diperlukan
3. Kemudian tekan tombol **Sign Up**

#### Sign In
1. Pada halaman *Login*, masukkan Email dan Password
2. Centang bagian **Remember Me** jika ingin akun diingat (opsional)
3. Kemudian tekan tombol **Sign In**

#### Membuat Projek User Story
1. Pada halaman *Dashboard*, tekan tombol "**+ add**" pada bagian atas list project untuk masuk ke halaman *Input User Story*
2. Masukkan informasi yang dibutuhkan berupa project title dan teks paragraf User Story
3. Kemudian tekan tombol **Generate**
4. Setelah di Generate, anda akan melihat hasil output User Story yang anda masukkan
5. Jika ingin mengubah hasil User Story, edit isi paragraf pada bagian input paragraf, lalu tekan tombol **Update** setelah merubah isi paragrafnya

#### Membuat User Story Scenario
1. Pada halaman *Input User Story* sebelumnya, tekan salah satu output User Story yang akan digunakan untuk masuk ke halaman *Input Scenario*
2. Pada halaman *Input Scenario*, Masukkan informasi yang dibutuhkan berupa title dan teks paragraf User Story Scenario
3. Kemudian tekan tombol **Generate**
4. Setelah proses generate selesai, hasil dari User Story Scenario yang telah dimasukkan akan ditampilkan.
5. Jika ingin mengubah hasil User Story Scenario, edit isi paragraf pada bagian input paragraf, lalu tekan tombol **Update** setelah merubah isi paragrafnya

#### Mengedit List Project
1. Pada halaman *Dashboard*, terdapat list projek User Story yang sudah dibuat
2. Tekan tombol **View** pada bagian Result untuk melihat informasi projek
3. Tekan icon **trash** pada bagian Action untuk menghapus projek dari list

#### Mengedit User Profile
1. Pada halaman *User Profile*, tekan tombol **Edit Profile** untuk mengubah data diri pengguna (Full Name, Email, dan Phone Number)
2. Kemudian tekan tombol **Save Changes** setelah merubah data diri pengguna

#### Reset Password
1. Pada halaman *Sign In*, tekan tombol **Forgot Password** untuk masuk ke halaman *Forgot Password*
2. Masukkan email aktif yang ingin diganti passwordnya pada kolom inputan
3. Tekan tombol **Send**
4. Buka history email anda dan carilah kiriman email dari website USGenerator
5. Klik tautan yang telah dikirim pada email tersebut
6. Masukkan kata sandi baru anda pada halaman *Reset Password* lalu tekan tombol SAVE



## Informasi Lainnya 📍

#### Anggota Proyek
Anggota pada proyek pengerjaan aplikasi USGenerator terdiri dari 10 orang, meliputi :

1. Nora Tamima Anggraini
2. Calvin Immanuel Siringoringo
3. Shabrina Al Khansa Putri S.
4. Rishad Safranatha
5. Darfito Danurdoro
6. Reyhan Eldwin Maulana
7. Aryasaty Kirana Tungga M.
8. Zidan Maulana Ramadhan
9. Ferry Triwantono
10. Rafly Gymnastiar Z.

#### Tanggal Rilis
Tanggal 5 Januari 2024

#### Kontak
Informasi kontak setiap anggota lebih detail dapat dilihat di bawah ini :
1. Nora Tamima Anggraini : ntamimaa@gmail.com
2. Calvin Immanuel Siringoringo : calvinsiringoringo03@gmail.com
3. Shabrina Al Khansa Putri S. : shabrinaal10@gmail.com 
4. Rishad Safranatha : safranatha@gmail.com
5. Darfito Danurdoro :  darfito.jkt2003@gmail.com
6. Reyhan Eldwin Maulana : reyhaneldwin31@gmail.com
7. Aryasaty Kirana Tungga M. : aryasatykiranaa@gmail.com
8. Zidan Maulana Ramadhan : zidanmaulanar@gmail.com
9. Ferry Triwantono : triwan98@gmail.com
10. Rafly Gymnastiar Z. : rafly.gymnastiar7c@gmail.com 

## Lisensi 🧾
Copyright © 2024 Universitas Airlangga

