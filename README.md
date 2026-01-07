# FAQ Bansos AI Telegram Bot

## Deskripsi Project
Project ini merupakan pengembangan **Chatbot FAQ Bansos berbasis Artificial Intelligence (AI)** yang terintegrasi dengan **Telegram**. Chatbot dirancang untuk membantu masyarakat dalam memperoleh informasi terkait bantuan sosial (Bansos) secara cepat, konsisten, dan akurat, khususnya untuk pertanyaan yang sering berulang (Frequently Asked Questions).

Sistem ini memanfaatkan pendekatan **Natural Language Processing (NLP)** serta **semi-learning**, sehingga chatbot tidak hanya menjawab pertanyaan berdasarkan data yang telah tersedia, tetapi juga mampu mencatat pertanyaan baru untuk pengembangan basis pengetahuan secara bertahap dan terkontrol.

---

## Latar Belakang
Layanan bantuan sosial sering kali menghadapi permasalahan berupa:
1. Banyaknya pertanyaan berulang dari masyarakat.
2. Keterbatasan petugas dalam melayani pertanyaan secara real-time.
3. Perbedaan cara masyarakat menyampaikan pertanyaan meskipun memiliki maksud yang sama.

Oleh karena itu, diperlukan sebuah solusi berbasis AI yang mampu:
- Memahami variasi bahasa alami masyarakat,
- Memberikan jawaban sesuai ketentuan resmi,
- Tetap menjaga akurasi dan akuntabilitas informasi publik.

---

## Tujuan Pengembangan
Tujuan dari pengembangan chatbot ini adalah:
1. Menyediakan media layanan informasi Bansos yang mudah diakses melalui Telegram.
2. Mengurangi beban layanan manual akibat pertanyaan berulang.
3. Meningkatkan kualitas pelayanan publik dengan respon yang cepat dan konsisten.
4. Menerapkan pendekatan AI yang aman melalui mekanisme semi-learning.
5. Menyediakan sistem yang dapat dikembangkan secara berkelanjutan.

---

## Ruang Lingkup Sistem
Ruang lingkup sistem chatbot ini meliputi:
- Menjawab pertanyaan FAQ Bansos berdasarkan dokumen resmi.
- Mendukung variasi kalimat pengguna menggunakan NLP similarity.
- Mencatat pertanyaan baru yang belum terjawab.
- Tidak menghasilkan jawaban di luar basis pengetahuan yang disetujui.
- Terintegrasi dengan Telegram Bot API.

---

## Arsitektur Sistem
Secara umum, arsitektur sistem terdiri dari:
1. **User (Telegram)**  
   Pengguna mengirimkan pertanyaan melalui aplikasi Telegram.

2. **Telegram Bot**  
   Menerima pesan dan meneruskannya ke sistem AI.

3. **AI Engine**  
   - Pencocokan berbasis keyword  
   - Perhitungan similarity berbasis NLP  
   - Penentuan jawaban atau pencatatan pertanyaan baru

4. **Knowledge Base (FAQ Data)**  
   Basis data FAQ yang disusun dari dokumen resmi.

5. **Semi-Learning Log**  
   Penyimpanan pertanyaan baru untuk pengembangan selanjutnya.

---

## Pendekatan Artificial Intelligence
Project ini menggunakan pendekatan AI sebagai berikut:

### 1. Keyword Matching
Pertanyaan pengguna dicocokkan dengan kata kunci yang telah ditentukan pada setiap intent FAQ.

### 2. NLP Similarity
Menggunakan model *sentence embedding multilingual* untuk mengukur kemiripan makna antara pertanyaan pengguna dan data FAQ.

### 3. Semi-Learning
Jika sistem tidak menemukan jawaban yang sesuai:
- Pertanyaan tidak dijawab secara spekulatif.
- Pertanyaan disimpan ke dalam file log (`new_questions.json`).
- Admin dapat meninjau dan menambahkan jawaban secara manual.

Pendekatan ini memastikan chatbot tetap aman dan sesuai dengan prinsip layanan publik.

---

## Fitur Utama
- Chatbot Telegram berbasis AI
- Dukungan bahasa alami (NLP)
- Jawaban fleksibel berdasarkan kata kunci dan makna
- Semi-learning (belajar dari pertanyaan pengguna)
- Aman untuk layanan publik
- Mudah dikembangkan

---

## TIM PENGEMBANG
FADLY FERDIANSYAH KURNIA
SALSABILA TASYA RAMADHANI SUWETY

---



