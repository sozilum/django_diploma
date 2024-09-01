

### Интернет-магазин

Шаблон интернет магазина с фикстурами для тестирования проекта

## Как поднять проект

### 1. Установка зависимостей

1. Установите [Poetry](https://python-poetry.org/):
   ```bash
   pip install poetry
   ```
2. Запустите виртуальную среду Poetry:
   ```bash
   poetry shell
   ```
3. Установите все необходимые зависимости:
   ```bash
   poetry install
   ```

### 2. Подготовка репозитория

1. Установите Git, если он ещё не установлен:
   ```bash
   sudo apt install git
   ```
2. Инициализируйте репозиторий Git:
   ```bash
   git init
   ```
3. Клонируйте проект:
   ```bash
   git clone <URL_Вашего_Репозитория>
   ```
4. Перейдите в директорию проекта:
   ```bash
   cd diploma
   ```

### 3. Настройка данных и базы

1. Загрузите начальные данные:
   ```bash
   python manage.py loaddata fixtures/main_data.json
   ```
2. Примените миграции Django:
   ```bash
   python manage.py migrate
   ```

### 4. Установка и настройка фронтенда

#### Установите фронтенд:
    ```bash
    pip install diploma-frontend-0.6_corrected.tar.gz
    ```

### 5. Запуск проекта

#### Запустите сервер:
    ```bash
    python manage.py runserver
    ```

Теперь ваш проект запущен и доступен по адресу `http://127.0.0.1:8000/`. 

