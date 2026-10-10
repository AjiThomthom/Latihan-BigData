import random
# ============================================================
# KOMPONEN KALIMAT: RED TEAM & BLUE TEAM
# ============================================================

# Subjek pelaku (Red Team, Blue Team, dan peran pendukung)
subjek_red = [
    "Tim red team", "Seorang peretas etis", "Anggota red team",
    "Operator red team", "Spesialis eksploitasi", "Peneliti offensive security",
    "Analis red team", "Seorang penetration tester", "Tim adversary emulation",
    "Konsultan red team", "Pemimpin red team", "Anggota purple team",
    "Spesialis social engineering", "Operator C2", "Pengembang payload",
    "Anggota tim exploit development", "Red teamer senior", "Junior red teamer"
]

subjek_blue = [
    "Tim blue team", "Analis SOC", "Insiden responder", "Analis threat hunting",
    "Administrator keamanan", "Anggota blue team", "Spesialis DFIR",
    "Analis malware", "Pemimpin blue team", "Anggota CSIRT",
    "Analis forensik digital", "Operator SIEM", "Threat intelligence analyst",
    "Security engineer", "Anggota tim deteksi", "Analis endpoint",
    "Pengelola firewall", "Administrator IAM", "Blue teamer senior",
    "Junior blue teamer", "SOC tier 1 analyst", "SOC tier 2 analyst",
    "SOC tier 3 analyst", "Incident handler"
]

subjek_netral = [
    "Organisasi", "Perusahaan", "Tim keamanan", "Manajemen", "Auditor keamanan",
    "Chief Information Security Officer", "Security architect", "Tim DevSecOps",
    "Tim kepatuhan", "Pengguna akhir", "Vendor keamanan", "Regulator",
    "Penyedia cloud", "Tim jaringan", "Tim aplikasi", "Tim operasi"
]

# Aksi Red Team (offensive)
aksi_red = [
    "melakukan reconnaissance terhadap target",
    "memetakan permukaan serangan organisasi",
    "menjalankan scanning port dengan Nmap",
    "mengidentifikasi kerentanan pada aplikasi web",
    "mengeksploitasi celah SQL injection",
    "menguji kekuatan kata sandi dengan brute force",
    "membuat payload reverse shell",
    "menyebarkan phishing email yang meyakinkan",
    "memanfaatkan misconfiguration pada server",
    "melakukan privilege escalation",
    "bergerak lateral di dalam jaringan",
    "mengambil alih akun administrator domain",
    "mengekstraksi kredensial dengan Mimikatz",
    "membangun command and control channel",
    "menjalankan serangan man-in-the-middle",
    "melakukan password spraying terhadap akun karyawan",
    "menyusup melalui supply chain perangkat lunak",
    "menguji ketahanan endpoint dengan malware simulasi",
    "melakukan serangan DDoS terkendali",
    "mengeksploitasi kerentanan zero-day",
    "memalsukan email dengan teknik spoofing",
    "memanfaatkan sesi yang tidak terkunci",
    "mencuri token autentikasi",
    "membuat backdoor yang sulit dideteksi",
    "melakukan persistence di sistem target",
    "menguji keamanan API dengan fuzzing",
    "memanfaatkan kesalahan konfigurasi cloud",
    "menjalankan teknik evasion terhadap antivirus",
    "melakukan dump memori untuk mencuri kredensial",
    "menguji kesadaran karyawan lewat simulasi vishing"
]

# Aksi Blue Team (defensive)
aksi_blue = [
    "mendeteksi aktivitas mencurigakan di jaringan",
    "menganalisis log dari SIEM",
    "melakukan threat hunting secara proaktif",
    "memblokir alamat IP berbahaya di firewall",
    "mengisolasi endpoint yang terinfeksi",
    "memulihkan sistem dari backup terbaru",
    "menambal kerentanan kritis dengan patch",
    "memperbarui signature IDS dan IPS",
    "mengaudit konfigurasi keamanan server",
    "menerapkan kebijakan least privilege",
    "mengaktifkan multi-factor authentication",
    "mengenkripsi data sensitif dengan AES-256",
    "memantau anomali pada lalu lintas keluar",
    "menganalisis malware di sandbox",
    "melakukan forensik pada endpoint yang terkena serangan",
    "mengumpulkan bukti digital dengan chain of custody",
    "mengimplementasikan segmentasi jaringan",
    "menerapkan model zero trust",
    "memverifikasi integritas file dengan hash SHA-256",
    "mengelola kunci kriptografi dengan HSM",
    "melatih karyawan tentang phishing",
    "menyusun playbook incident response",
    "menguji rencana disaster recovery",
    "memantau dark web untuk kebocoran data",
    "menggunakan honeypot untuk menjebak penyerang",
    "menganalisis perilaku pengguna dengan UEBA",
    "memperkuat konfigurasi endpoint dengan hardening",
    "mengelola akses berbasis peran di IAM",
    "mendeteksi lateral movement dengan EDR",
    "menggunakan threat intelligence untuk memperkuat pertahanan"
]

# Konteks / tujuan
konteks = [
    "untuk menguji kesiapan organisasi",
    "demi meningkatkan postur keamanan",
    "agar pertahanan berlapis dapat diuji",
    "guna menemukan celah sebelum penyerang nyata memanfaatkannya",
    "untuk memperkuat kolaborasi antara red dan blue team",
    "sehingga deteksi dini dapat ditingkatkan",
    "demi memenuhi standar ISO 27001 dan NIST",
    "agar kepatuhan terhadap PCI DSS tetap terjaga",
    "untuk melindungi data pelanggan",
    "sehingga kepercayaan publik tetap terjaga",
    "guna mencegah kerugian finansial",
    "demi menjaga reputasi perusahaan",
    "agar operasi bisnis tetap berjalan",
    "untuk mengurangi waktu deteksi dan respons",
    "sehingga biaya pemulihan dapat ditekan",
    "demi menciptakan budaya keamanan yang kuat",
    "agar seluruh tim memahami risiko nyata",
    "untuk menghadapi ancaman APT",
    "sehingga ransomware tidak berhasil masuk",
    "guna melindungi infrastruktur kritikal"
]

# Penutup / kesimpulan
penutup = [
    "Kolaborasi red dan blue team sangat penting.",
    "Pendekatan purple teaming mempercepat pembelajaran.",
    "Latihan ini harus dilakukan secara berkala.",
    "Hasilnya menjadi masukan berharga bagi manajemen.",
    "Ini adalah praktik terbaik industri keamanan siber.",
    "Setiap temuan harus ditindaklanjuti dengan cepat.",
    "Dokumentasi yang rapi memudahkan audit berikutnya.",
    "Peningkatan berkelanjutan adalah kunci keberhasilan.",
    "Budaya keamanan harus dibangun dari atas ke bawah.",
    "Investasi keamanan adalah investasi jangka panjang.",
    "Zero trust adalah arah masa depan keamanan.",
    "Otomatisasi membantu tetapi tetap butuh analis manusia.",
    "Threat intelligence memperkaya konteks serangan.",
    "Latihan ini memperkuat ketahanan organisasi.",
    "Pembelajaran dari setiap insiden sangat berharga.",
    "Purple teaming menjembatani dua perspektif berbeda.",
    "Deteksi dini menyelamatkan organisasi dari bencana.",
    "Respons cepat mengurangi dampak serangan.",
    "Keamanan adalah tanggung jawab bersama.",
    "Sinergi antar tim menciptakan pertahanan yang tangguh."
]

# ============================================================
# GENERATOR 10.000 KALIMAT
# ============================================================

TARGET = 10000
kalimat_set = set()
hasil = []

# Gabungkan semua subjek
semua_subjek = subjek_red + subjek_blue + subjek_netral

while len(hasil) < TARGET:
    # Pilih jenis kalimat: red, blue, atau kolaborasi
    tipe = random.choice(["red", "blue", "kolaborasi"])

    if tipe == "red":
        s = random.choice(subjek_red + subjek_netral)
        a = random.choice(aksi_red)
    elif tipe == "blue":
        s = random.choice(subjek_blue + subjek_netral)
        a = random.choice(aksi_blue)
    else:  # kolaborasi red & blue
        s = random.choice(semua_subjek)
        a = random.choice(aksi_red + aksi_blue)

    k = random.choice(konteks)
    p = random.choice(penutup)
    kalimat = f"{s} {a} {k}. {p}"

    if kalimat not in kalimat_set:
        kalimat_set.add(kalimat)
        hasil.append(kalimat)

# ============================================================
# TULIS KE FILE
# ============================================================
with open("bigdata.txt", "w", encoding="utf-8") as f:
    for kalimat in hasil:
        f.write(kalimat + "\n")

print(f"Berhasil membuat {len(hasil)} kalimat di bigdata.txt")

# Estimasi total kata
total_kata = sum(len(k.split()) for k in hasil)
print(f"Estimasi total kata: {total_kata}")
