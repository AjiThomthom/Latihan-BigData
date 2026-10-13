// ==========================================
// TUGAS INDIVIDU BIG DATA - PERTEMUAN 4
// Studi Kasus: Monitoring Sensor IoT
// Database: NoSQL (MongoDB)
// ==========================================

// 1. Inisialisasi Database dan Collection
use iot_monitoring;
db.createCollection("sensor_data");

// 2. Insert Data Contoh (Minimal 10 Dokumen)
db.sensor_data.insertMany([
  {
    sensor_id: "ESP32_01",
    lokasi: "Plant_Cikarang_A",
    timestamp: "2026-10-13T08:00:00Z",
    metrik: { suhu_celcius: 28.5, kelembapan_persen: 65 },
    status: "NORMAL"
  },
  {
    sensor_id: "ESP32_01",
    lokasi: "Plant_Cikarang_A",
    timestamp: "2026-10-13T09:00:00Z",
    metrik: { suhu_celcius: 36.2, kelembapan_persen: 58 },
    status: "WARNING"
  },
  {
    sensor_id: "ESP32_02",
    lokasi: "Plant_Cikarang_B",
    timestamp: "2026-10-13T08:00:00Z",
    metrik: { suhu_celcius: 24.1, kelembapan_persen: 70 },
    status: "NORMAL"
  },
  {
    sensor_id: "ESP32_02",
    lokasi: "Plant_Cikarang_B",
    timestamp: "2026-10-13T09:00:00Z",
    metrik: { suhu_celcius: 41.8, kelembapan_persen: 45 },
    status: "CRITICAL"
  },
  {
    sensor_id: "ESP32_03",
    lokasi: "Server_Room_Bekasi",
    timestamp: "2026-10-13T08:00:00Z",
    metrik: { suhu_celcius: 19.5, kelembapan_persen: 50 },
    status: "NORMAL"
  },
  {
    sensor_id: "ESP32_03",
    lokasi: "Server_Room_Bekasi",
    timestamp: "2026-10-13T09:00:00Z",
    metrik: { suhu_celcius: 20.0, kelembapan_persen: 52 },
    status: "NORMAL"
  },
  {
    sensor_id: "ESP32_04",
    lokasi: "Plant_Cikarang_A",
    timestamp: "2026-10-13T10:00:00Z",
    metrik: { suhu_celcius: 37.0, kelembapan_persen: 55 },
    status: "WARNING"
  },
  {
    sensor_id: "ESP32_05",
    lokasi: "Warehouse_Bekasi",
    timestamp: "2026-10-13T08:30:00Z",
    metrik: { suhu_celcius: 27.0, kelembapan_persen: 68 },
    status: "NORMAL"
  },
  {
    sensor_id: "ESP32_05",
    lokasi: "Warehouse_Bekasi",
    timestamp: "2026-10-13T09:30:00Z",
    metrik: { suhu_celcius: 28.1, kelembapan_persen: 66 },
    status: "NORMAL"
  },
  {
    sensor_id: "ESP32_06",
    lokasi: "Plant_Cikarang_B",
    timestamp: "2026-10-13T10:00:00Z",
    metrik: { suhu_celcius: 43.5, kelembapan_persen: 40 },
    status: "CRITICAL"
  }
]);

// 3. Operasi Read (Filtering & Querying)
// A. Mencari sensor dengan suhu >= 35 Celcius
db.sensor_data.find({ "metrik.suhu_celcius": { $gte: 35 } }).pretty();

// B. Mencari sensor berdasarkan lokasi
db.sensor_data.find({ lokasi: "Plant_Cikarang_A" });

// 4. Operasi Update
// Mengubah status ESP32_01 pada jam 09:00 menjadi CRITICAL
db.sensor_data.updateOne(
  { sensor_id: "ESP32_01", timestamp: "2026-10-13T09:00:00Z" },
  { $set: { status: "CRITICAL" } }
);

// 5. Operasi Delete
// Menghapus data sensor anomali ESP32_06
db.sensor_data.deleteOne({ sensor_id: "ESP32_06" });

// 6. Operasi Aggregation
// Menghitung rata-rata suhu dan jumlah pembacaan per lokasi
db.sensor_data.aggregate([
  {
    $group: {
      _id: "$lokasi",
      rata_rata_suhu: { $avg: "$metrik.suhu_celcius" },
      total_bacaan: { $sum: 1 }
    }
  }
]);
