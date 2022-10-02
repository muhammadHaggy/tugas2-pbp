# To Do List App
https://tugas-pbp.herokuapp.com/todolist/

## Kegunaan csrf_token pada Template
CSRF token kepanjangannya Cross Site Request Forgery. Token ini berguna untuk menjamin bahwa form yang dapat disubmit adalah form yang memang berasal dari website itu sendiri. Tanpa token tersebut dalam suatu form yang disubmit, Django secara default akan menolaknya. Hal ini dapat mencegah pihak ketiga untuk menambahkan form tidak dikenal dalam sebuah website.

## Pembuatan Form Secara Manual
Pembuatan form secara manual dapat menggunakan html saja. Langkah-langkahnya:
1. Buat tag dan endtag form
2. Di dalamnya, buat pertanyaan form dalam html tag label, dan input dalam html tag input dengan attribut type dan id yang sesuai untuk setiap pertanyaan
3. Tambahkan input dengan tipe submit atau button dengan tipe submit di akhir form

## Alur Data
Pengguna mengisi form lalu mengklik tombol submit. Lalu browser akan mensubmit http request yang biasanya bertipe POST membawa data-data yang dimasukkan user. Jika CSRF token sesuai, maka server akan memvalidasi masukan pada form. Jika lolos validasi, server akan menyimpan data tersebut ke dalam database. Lalu, server akan meredirect user ke url show_todolist, lalu view akan menampilkan data yang sudah diupdate melalui template yang ada.

## Implementasi Pembuatan App Todolist
Saya menjalankan perintah python manage.py startapp todolist. Setelah itu, saya tambahkan app baru itu ke dalam installed apps di project folder.

## Implementasi Routing Todolist
Saya menyertakan mywatchlist.urls ke dalam urls.py pada direktori project folder, yaitu pada url 'todolist/'. Lalu saya mulai mengisi urls.py pada app mywatchlist, yang pertama adalah url '' yang menampilkan list dari task, yang kedua adalah url 'register/' untuk mendaftar user baru, 'logout/' untuk logout dari current user, 'login/' untuk masuk ke user yang sudah terdaftar, 'create-task/' untuk menambahkan task baru, 'delete-task' untuk menghapus task, dan 'toggle-task' untuk mengubah status dari sebuah task.

## Implementasi registrasi

Saya menggunakan UserCreationForm yang ada di django untuk membuat form registrasi. Pada template, saya hanya perlu memasukkan UserCreationForm dan button untuk submit data dalam tag form.

## Implementasi login

Saya menggunakan template dan module view dari tutorial untuk implementasi fungsi login.

## Implementasi logout

Saya menggunakan fungsi bawaan logout pada django, lalu meredirect user ke halaman login.

## Implementasi halaman utama todolist
Pada halaman pertama todolist, saya menggunakan tabel untuk menampilkan detail dari setiap task serta tombol toggle dan delete task. Saya juga menambahkan tombol create task di atas tabel dan tombol logout pada bawah tabel.

## Implementasi Form Pembuatan Task
Saya menggunakan ModelForm untuk memetakan model dan fieldnya ke form yang sesuai. Lalu, saya mengkonversi masukan user ke objek Task. Objek itu kita simpan dalam database untuk ditampilkan di halaman index.

## Implementasi Model Watchlist
Saya membuat sebuah class model bernama Task yang berisi atribut:
* user, sebuah field foreign key yang merepresentasikan user yang membuat task tersebut.
* date, sebuah datefield yang merepresentasikan tanggal dibuatnya task tersebut.
* title, sebuah charfield (menampung String pendek) yang merepresentasikan judul task.
* review, sebuah textfield (menampung string panjang) yang merepresentasikan pendapat pribadi saya terhadap film/series tersebut.
* description, sebuah textfield yang merepresentasikan deskripsi task.
* is_finished, sebuah field boolean yang merepresentasikan status task.

## Perbedaan Inline, Internal, dan External CSS
Inline CSS adalah penambahan CSS attribut pada tiap html tag yang ingin dikustomisasi. Dengan Inline CSS, kita dapat secara cepat memasukkan styling ke dalam html page, hal ini sangat berguna ketika kita ingin mengetes dan melihat perubahan dengan cepat. Namun, menambahkan attribut CSS ke tiap html tag memakan waktu dan dapat membuat file html kita sulit untuk dibaca.

Internal CSS adalah penambahan CSS dalam tag style di dalam bagian head html. Dengan internal CSS, kita bisa menggunakan fitur class dan ID selector yang tidak tersedia pada inline CSS. Namun, untuk website yang punya banyak file html, menambahkan internal css ke tiap file menghabiskan banyak waktu dan melanggar prinsip "Do not repeat yourself".

External CSS adalah penambahan CSS dengan cara menghubungkan html file di website kita dengan suatu file .css external. Metode ini sangat efisien untuk website-webisite besar karena dengan mengubah satu file saja, kita bisa mengubah styling pada banyak html yang terhubung. Namun, ada resiko halaman web tidak akan ditampilkan dengan baik sampai file CSS external dimuat.

## Tag HTML 5

### nav
Mendefinisikan bagian navigasi dari sebuah website. Nav biasanya berisi link ke bagian lain dari website.

### article
Mendefinisikan bagian dari web yang membentuk bagian independen, seperti artikel, postingan blog, dll.

### dialog
Tag dialog memunculkan dialog box kepada user. Cocok untuk penggunaan seperti peringatan yang bisa diabaikan.

### embed
Tag embed dapat digunakan untuk memasukkan aplikasi eksternal seperti konten audio dan video ke dalam web kita.




## Tipe-Tipe CSS Selector
### Universal Selector
Memilih semua elemen html. Syntax: *

### Type Selector
Memilih semua elemen node namenya sesuai. Contoh: type selector p akan memilih semua elemen <p>

### Class Selector
Memilih semua elemen yang punya attribut class yang sesuai. Contoh: .card akan memilih semua elemen yang punya class card

### ID Selector
Memilih sebuah elemen berdasarkan nilai attribut idnya. Misalnya: #user akan memilih elemen yang punya id "user".

### Attribut selector
Memilih semua elemen yang punya attribut. Contoh: [href] akan memilih semua elemen yang punya attribut href. 

## Implementasi Kustomisasi Login, Register, dan Create-task
Untuk semua halaman dalam app todolist kita menerapkan sebuah navbar yang disebelah kirinya bertuliskan "Signed in as username" jika sudah login dan "Not logged in" jika belum login. Di tengah-tengah navbar bertuliskan nama app yaitu todolist memanfaatkan tag brand. Di sebelah kanan navbar terdapat action button yang berbeda-beda tiap halaman, pada halaman login action buttonnya menuju ke halaman register, pada halaman register action buttonnya menuju ke halaman login, sedangkan pada halaman index todolist action buttonnya menuju ke halaman create-task dan logout user.

Pada semua halaman kita letakkan semua widget dalam container agar lebih rapi. Pada halaman login, saya memasukkan form dalam sebuah flex yang memposisikan item di tengah. Lalu saya memasukkan control group dan control class pada tiap input form untuk memanfaatkan default layout dari bootstrap. Pada halaman register, saya memanfaatkan layout form default dari bootstrap dengan cara mengiterasi tiap field pada form dan mengintegrasikannya dengan control class dari bootstrap. Saya juga melakukan hal yang sama pada halaman create-task.

## Implementasi halaman utama todolist
Saya meletakkan semua card task dalam suatu container. Setiap card berisi header yang merepresentasikan status dari tugas. Lalu body dari card diisi dengan judul task dan deskripsi dari task dengan tulisan yang lebih kecil. Body card juga diisi dua button action di sebelah kanan bawah yang masing-masing berfungsi untuk merubah status dari task dan menghapus task. Setiap card berisi footer yang merepresentasikan tanggal pembuatan dari tiap task.

## Implementasi responsiveness
Untuk implementasi responsiveness saya menggunakan sistem grid dari Bootstrap. Saya gunakan row dari bootstrap di luar iterasi tiap task. Lalu saya tambahkan card dengan col-lg-5 yang berarti pada checkpoint large, ubah ukuran kolum menjadi 5/12 dari lebar container. Hal ini hanya akan berlaku pada breakpoint large keatas. Yang berarti tampilannya pada breakpoint large kebawah hanyalah satu card per row, sedangkan pada breakpoint large keatas dua card per row.

Kita juga menerapkan beberapa checkpoint pada form login yaitu col-sm-8 col-md-6 col-lg-3. Pada checkpoint small, lebar form adalah 8/12, pada checkpoint medium 6/12, dan pada checkpoint large 3/12. Hal ini mencegah ukuran form yang tidak proporsional. Hal yang sama juga diterapkan pada halaman register dan create-task.

## Implementasi hover animation
Implementasi dengan internal CSS menggunakan selector class card. Animasi yang diterapkan adalah memperbesar ukuran kartu 5%. 