# Peta Sumber Gempa Indonesia 2024

Aplikas berbasis Django dan Leaflet.js untuk menampilkan data sesar aktif dan subduksi dari PusGeN 2024.

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

1. Pull image terbaru (ganti `<username>` dan `<repository>` sesuai akun GitHub Anda):
   ```bash
   docker pull ghcr.io/<username>/<repository>:latest
   ```
2. Jalankan kontainer pada port 9004:
   ```bash
   docker run -d -p 9004:8000 --name fault-map ghcr.io/<username>/<repository>:latest
   ```

## Struktur Data
- **Sesar**: Atribut `Name` (diambil dari `PusGeN2024_Shallow_Crustal_v5_12.shp`).
- **Subduksi**: Atribut `TrenchName` (diambil dari `2024_Subduction trench_v2.shp`).

## Tech Stack
- **Backend**: Django & `pyshp`
- **Frontend**: Leaflet.js & Vanilla CSS
- **Deployment**: Docker & GitHub Actions
