# Cash Register

## 📌 О проекте
**Cash Register** — это Django-приложение, имитирующее работу кассового аппарата.

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
- Главная страница: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Админ-панель: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 🔧 Основные команды
Остановка сервера:
```sh
CTRL+C
```
Очистка базы данных:
```sh
python manage.py flush
```
Просмотр логов:
```sh
python manage.py runserver
```

