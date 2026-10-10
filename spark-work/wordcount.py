from pyspark.sql import SparkSession

# 1. Inisialisasi SparkSession dengan menunjuk ke Spark Master klaster
spark = SparkSession.builder \
    .appName("AnalisisStatistikBigData") \
    .master("spark://spark:7077") \
    .getOrCreate()

sc = spark.sparkContext

# (Sisa kode pembacaan HDFS dan statistik tetap sama seperti sebelumnya)
file_path = "hdfs://namenode:9000/bigdata/bigdata.txt"
lines = sc.textFile(file_path)

total_lines = lines.count()
words = lines.flatMap(lambda line: line.lower().split())
total_words = words.count()
total_letters = lines.map(lambda line: sum(1 for c in line if c.isalpha())).sum()
total_digits = lines.map(lambda line: sum(1 for c in line if c.isdigit())).sum()

pairs = words.map(lambda word: (word, 1))
word_counts = pairs.reduceByKey(lambda a, b: a + b)
top_10 = word_counts.sortBy(lambda x: x[1], ascending=False).take(10)

print("\n================ STATISTIK DATASET HDFS ================")
print(f"Total Baris    : {total_lines}")
print(f"Total Kata     : {total_words}")
print(f"Total Huruf    : {total_letters}")
print(f"Total Angka    : {total_digits}")
print("=======================================================")

print("\n========== 10 KATA TERBANYAK ==========")
for word, count in top_10:
    print(f"{word} \t-> {count} kemunculan")
print("=======================================\n")

spark.stop()
