# Cash Register

## 📌 О проекте
**Cash Register** — это Django-приложение, имитирующее работу кассового аппарата.


### Методы API

#### 1. **Генерация QR-кода для чека**

**Эндпоинт:** `/api/receipts/qr/`  
**Метод:** `POST`  
**Описание:** Принимает список ID товаров и генерирует QR-код, который содержит ссылку на PDF-файл чека.

#### Пример запроса:
```json
{
  "items": [1, 2, 3]
}
```
**items:** Список ID товаров, которые были приобретены в чеке.

#### Пример ответа:
```json
{
  "qr_code": "/media/receipts/qr-1_2025-03-01_12h00m00s.png"
}
```
**qr_code:** Ссылка на сгенерированный QR-код для чека. При сканировании QR-кода будет открыта ссылка на PDF-файл чека.

## 🚀 Запуск проекта

### 1️⃣ Клонирование репозитория
```sh
git clone <URL_РЕПОЗИТОРИЯ>
cd cash_register
```

### 2️⃣ Создание виртуального окружения и установка зависимостей
```sh
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate    # Для Windows
pip install -r requirements.txt
```

### 3️⃣ Создание `.env` файла
Создайте файл `.env` на основе `.env.example`:
```sh
cp .env.example .env
```
Заполните переменные в `.env`.

### 4️⃣ Применение миграций и создание суперпользователя
```sh
python manage.py migrate
python manage.py createsuperuser
```
Заполните данные (email, пароль) и подтвердите.

### 5️⃣ Запуск проекта
```sh
python manage.py runserver
```

### 6️⃣ Открытие проекта
- Админ-панель: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
