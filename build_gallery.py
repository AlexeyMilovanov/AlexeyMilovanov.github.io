import os

# 1. Настройки
GALLERY_DIR = "gallery"
OUTPUT_FILE = "photos.html"

# Проверяем, существует ли папка с фотографиями
if not os.path.exists(GALLERY_DIR):
    os.makedirs(GALLERY_DIR)
    print(f"📁 Создана папка '{GALLERY_DIR}'. Положите туда фотографии!")

# 2. Ищем все картинки в папке gallery
valid_extensions = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
image_files = [f for f in os.listdir(GALLERY_DIR) if os.path.splitext(f)[1].lower() in valid_extensions]

# Сортируем по имени (чтобы порядок на сайте был предсказуемым)
image_files.sort()

# 3. HTML Шаблон (Верхняя часть: стили, шапка и начало галереи)
html_top = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photos - Alexey Milovanov</title>
    <style>
        :root {
            --primary-color: #2c3e50;
            --accent-color: #2980b9;
            --bg-color: #e8ecef;
            --text-color: #333;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 10px;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 10px;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
            align-items: start;
        }
        .gallery img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            transition: transform 0.2s;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .gallery img:hover {
            transform: scale(1.03);
        }
    </style>
</head>
<body>
    <div class="container">
        <nav style="text-align: center; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 1px solid #ccc;">
            <a href="index.html" style="margin: 0 15px; color: #2c3e50; text-decoration: none;">Home</a>
            <a href="photos.html" style="margin: 0 15px; font-weight: bold; color: #2980b9; text-decoration: none;">Photos</a>
        </nav>
        <div class="gallery">
"""

# 4. HTML Шаблон (Нижняя часть: закрывающие теги)
html_bottom = """        </div>
    </div>
</body>
</html>"""

# 5. Генерируем серединку с тегами <img>
html_images = ""
for img in image_files:
    # Прописываем путь к картинке: gallery/имя_файла.jpg
    html_images += f'            <img src="{GALLERY_DIR}/{img}" alt="{img}">\n'

# 6. Собираем всё вместе и записываем в файл photos.html
full_html = html_top + html_images + html_bottom

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(full_html)

print(f"✅ Готово! Файл {OUTPUT_FILE} успешно сгенерирован/обновлен.")
print(f"📸 Добавлено фотографий в галерею: {len(image_files)}")