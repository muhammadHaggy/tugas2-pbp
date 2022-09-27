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