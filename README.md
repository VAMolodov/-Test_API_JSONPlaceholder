# 🚀 API Testing Project: JSONPlaceholder

Автоматизированное тестирование REST API сервиса JSONPlaceholder (https://jsonplaceholder.typicode.com) с использованием Python и Pytest.

## 📋 Описание проекта
Данный проект содержит набор интеграционных тестов для проверки эндпоинта `/posts`. Тесты охватывают основные CRUD-операции:
- Получение списка всех постов.
- Получение одного поста по ID.
- Создание нового поста (с последующим удалением).
- Обновление данных существующего поста (PUT).
- Удаление поста.


Создание виртуального окружение и установка зависимостей:

python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows

pip install -r requirements.txt


Запуск тестов:
Стандартный запуск (все тесты в проекте):
pytest

Подробный запуск (показывает названия каждого теста и статус):
pytest -v

Для запуска всех тестов и сбора данных для отчета:
pytest --alluredir=allure-results

Просмотр отчета Allure (Убедитесь, что Allure установлен в вашей системе)
allure serve allure-results



📂 Структура проекта

    tests/ — папка с тестами (GET, POST, PUT, DELETE).
    conftest.py — общие фикстуры (сессия, подготовка , очистка данных).
    data.py — базовые URL, тестовые данные и сценарии параметризации, JSON-схемы.
    requirements.txt — список необходимых библиотек.