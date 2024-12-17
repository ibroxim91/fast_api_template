# 1. Rasmni tanlash
FROM python:3.11-slim

# 2. Ishlash papkasini yaratish va o'rnatish
WORKDIR /app

# 3. Talab qilingan fayllarni konteynerga nusxalash
COPY requirements.txt .

# 4. Kutubxonalarni o'rnatish
RUN pip install --no-cache-dir -r requirements.txt

# 5. Loyihani konteynerga nusxalash
COPY . .

# 6. Docker konteynerda ishlatiladigan portni sozlash
EXPOSE 8000

# 7. FastAPI ilovasini ishga tushirish
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
