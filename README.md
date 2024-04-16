PERSIAN README


**توضیحات:**

این یک برنامه‌ی ساده است که برای کار با شبکه‌های محلی (LAN) در سیستم عامل‌های مک و لینوکس طراحی شده است. با استفاده از این برنامه، می‌توانید به سادگی با دیگر دستگاه‌هایی که در همان شبکه قرار دارند، فایل‌های خود را به اشتراک بگذارید. به همین دلیل، این برنامه دارای قابلیت آپلود و دانلود فایل است. به طور خلاصه، با داشتن این برنامه، می‌توانید به راحتی و سرعت، فایل‌های خود را با دیگران به اشتراک بگذارید.


**توجه:** نحوه استفاده از برنامه در انتهای همین فایل نوشته شده است

**این برنامه تنها بر روی سیستم عامل‌های مک و لینوکس قابل اجرا است.**

**Description:**

This is a simple program designed for working with local area networks (LANs) on Mac and Linux operating systems. With this program, you can easily share your files with other devices that are on the same network. This program has the ability to upload and download files. In summary, with this program, you can easily and quickly share your files with others.

**Note:**

This program is only runable in Mac and Linux operating systems

---

## How to use Bagher | نحوه استفاده از باقر

Follow these steps to set up and run the Bagher web server:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mohsenFN/Bagher-webserver.git
   cd Bagher-webserver
   ```

2. **Run a Virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install requirements:**
   ```bash
   pip install -r requirements
   ```

4. **Take a Smoke Test:**
   ```bash
   python app.py run
   ```