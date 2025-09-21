from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi driver Chrome
driver = webdriver.Chrome()

# Buka halaman web Anda
# Jika halaman Anda lokal, gunakan 'file:///path/to/your/file.html'
# Jika online, gunakan 'https://www.example.com'
driver.get("https://rantai-diva.streamlit.app/")

# Tunggu sampai elemen ada di halaman
# Ini penting untuk halaman dinamis yang memuat konten belakangan
try:
    # Gunakan selector CSS untuk menemukan elemen div yang Anda berikan
    # Kelas-kelas dipisahkan dengan titik (.)
    # Elemen ini unik dan spesifik
    css_selector = "div.absolute.bottom-0.left-1\\/4.z-10.-translate-x-1\\/2"
    
    # Tunggu maksimal 10 detik hingga elemen terlihat
    element_to_hide = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )
    
    print("Elemen ditemukan.")

    # Sembunyikan elemen dengan menjalankan JavaScript
    # Ini mengubah properti CSS 'display' menjadi 'none'
    driver.execute_script("arguments[0].style.display = 'none';", element_to_hide)
    
    print("Elemen telah disembunyikan.")

    # Biarkan browser terbuka sebentar untuk observasi
    time.sleep(5)
    
except Exception as e:
    print(f"Terjadi kesalahan: {e}")

finally:
    # Tutup browser
    driver.quit()
