from pyspark.sql import SparkSession

# 1. Inisialisasi SparkSession (Driver Program)
spark = SparkSession.builder \
    .appName("LatihanWordCount") \
    .master("local[*]") \
    .getOrCreate()

sc = spark.sparkContext

# 2. Tahap Input (Membaca file)
lines = sc.textFile("data_latihan.txt")

# 3. Tahap Transformation (Lazy Evaluation)
# a. Tokenisasi: memecah kalimat menjadi kata
words = lines.flatMap(lambda line: line.lower().split())

# b. Mapping: mengubah kata menjadi (kata, 1)
pairs = words.map(lambda word: (word, 1))

# c. Agregasi: menjumlahkan angka berdasarkan kata yang sama
word_counts = pairs.reduceByKey(lambda a, b: a + b)

# Mengurutkan berdasarkan frekuensi terbanyak (opsional untuk mempermudah baca)
sorted_counts = word_counts.sortBy(lambda x: x[1], ascending=False)

# 4. Tahap Action (Memicu Eksekusi)
print("\n--- HASIL PEMROSESAN SPARK ---")
hasil = sorted_counts.collect()

for word, count in hasil:
    print(f"{word} : {count}")
print("------------------------------\n")

spark.stop()
