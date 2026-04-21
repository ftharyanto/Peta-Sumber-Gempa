# Peta Sumber Gempa Indonesia 2024

Aplikas berbasis Django dan Leaflet.js untuk menampilkan data sesar aktif dan subduksi dari PusGeN 2024.

Repository: [https://github.com/ftharyanto/Peta-Sumber-Gempa](https://github.com/ftharyanto/Peta-Sumber-Gempa)

## Fitur
- Visualisasi garis sesar (Shallow Crustal) dan subduksi.
- Interaktif: Klik pada garis untuk melihat nama sumber gempa.
- Desain premium dengan tema Dark Matter.

## Cara Menjalankan Lokal (Leluasa)

1. Pastikan Docker dan Docker Compose sudah terinstal.
2. Jalankan perintah berikut:
   ```bash
   docker-compose up --build
   ```
3. Buka browser dan akses [http://localhost:9004](http://localhost:9004).

## Jalankan dari GitHub Container Registry (GHCR)

Jika image sudah di-upload ke GHCR, Anda bisa menjalankannya langsung tanpa membangun dari source:

1. Pull image terbaru:
   ```bash
   docker pull ghcr.io/ftharyanto/peta-sumber-gempa:latest
   ```
2. Jalankan kontainer pada port 9004:
   ```bash
   docker run -d -p 9004:8000 --name fault-map ghcr.io/ftharyanto/peta-sumber-gempa:latest
   ```

## Cara Update (Repull) Image

Jika ada pembaruan pada repositori, gunakan langkah berikut untuk memperbarui image lokal Anda:

1. Stop dan hapus kontainer yang sedang berjalan:
   ```bash
   docker stop fault-map
   docker rm fault-map
   ```
2. Pull image terbaru dari GHCR:
   ```bash
   docker pull ghcr.io/ftharyanto/peta-sumber-gempa:latest
   ```
3. Jalankan kembali kontainer:
   ```bash
   docker run -d -p 9004:8000 --name fault-map ghcr.io/ftharyanto/peta-sumber-gempa:latest
   ```
## Sumber Data
- **PusGeN 2024**: [https://ciptakarya.pu.go.id/produk-kegempaan](Pusat Studi Gempa Nasional 2024)

## Tech Stack
- **Backend**: Django & `pyshp`
- **Frontend**: Leaflet.js & Vanilla CSS
- **Deployment**: Docker & GitHub Actions
