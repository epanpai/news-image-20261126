# Build log — news-image-20261126

Bounty "Sum up 26 November's world news in one image", dibuka
2026-11-26T00:00:00Z (26 Nov 07:00 WIB), tutup 2026-11-28T00:00:00Z
(28 Nov 07:00 WIB). Hadiah $100 untuk 50 besar (juara 1 $20, juara 2
$12, juara 3 $6), escrow terdanai ($100, held 100.000.000 base units),
tanpa entry fee, harness program/v1. Sesi builder ini dimulai 26 Nov
~00:18 UTC — SETELAH buka (00:00Z), jadi thinking_in_window terpenuhi.

## Riset berita 26 Nov 2026 (browser.search, 26 Nov ~00:15–00:20 UTC)

Sumber: Reuters, CNN, Devdiscourse (Reuters summary), Libre News,
SelfStudys, Jagran Josh, SimpleLife.news (agregasi AP/Reuters/AFP).

1. KOREA UTARA (LEAD) — Kim Jong Un memeriksa fasilitas produksi
   bahan nuklir dan riset senjata, memerintahkan penyebaran senjata
   nuklir taktis yang lebih luas di berbagai domain; status Korea Utara
   sebagai negara senjata nuklir "absolutely inviolable"; "Our nuclear
   capability is now a reality." (KCNA, dilaporkan Kamis 26 Nov;
   Reuters/CNN).
2. LUAR ANGKASA — Astronot pertama Pakistan, Muhammad Zeeshan Ali,
   bergabung dengan stasiun luar angkasa Tiangong China lewat
   Shenzhou-24 — astronot asing pertama di Tiangong (headline 26 Nov).
3. PERDAGANGAN — AS mengusulkan tarif baru untuk 14 mitra dagang
   melawan overcapacity; China paling keras; Taiwan 15%; pasar Asia
   merosot (Reuters summary 26 Nov; konferensi pers Taiwan 26 Nov).
4. UKRAINA — Ukraina menyerang pangkalan udara besar Rusia,
   merusak lima pesawat; puluhan negara mendesak Rusia menghentikan
   dugaan penggunaan agen anti-huru-hara (Reuters summary 26 Nov).
5. ASTEROID — Gambar close-up pertama terungkap dari asteroid yang
   sengaja ditabrak untuk menguji pertahanan Bumi (Jagran Josh 26 Nov).
6. BANGLADESH — Upah minimum pekerja garmen naik 36% (headline 26 Nov).
7. Ticker: Kolombia 10 tahun perjanjian damai; Lebanon buka bandara
   internasional kedua; Korea Utara perintahkan Swiss tutup kantor
   diplomatiknya di Pyongyang; angka Rusia sendiri: hampir 500.000
   tewas di perang Ukraina; Gukesh vs Sindarov di Kejuaraan Catur
   Dunia, Jenewa; India Constitution Day; CEO Flipkart mundur Desember.

## Desain gambar (1024x1024, halaman depan koran)

- Masthead "THE WORLD IN ONE DAY" + "THURSDAY, 26 NOVEMBER 2026".
- Lead: Korea Utara — panel gelap marun, siluet rudal + awan jamur,
  kutipan Kim "Our nuclear capability is now a reality."
- Kolom kanan: luar angkasa (Tiangong) + tarif AS (grafik turun).
- Tiga panel: Ukraina / asteroid / Bangladesh.
- Ticker: Kolombia, Lebanon, Swiss–Pyongyang, angka korban Rusia,
  catur dunia, Constitution Day India.
- gen_image.py (PIL, hanya untuk build lokal) menggambar entry.png.
  main.py (stdlib saja) memvalidasi PNG lalu menyalin
  assets/entry.png ke /output/entry.png dan memverifikasi salinan
  byte-identik.

## Build
