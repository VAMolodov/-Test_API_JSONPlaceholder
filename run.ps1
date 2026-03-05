# Сборка образа (опционально, можно закомментировать если не менял код)
# docker build -t my-api-tests .

# Запуск тестов
docker run --rm -v "${PWD}/allure-results:/app/allure-results" my-api-tests pytest --alluredir=allure-results --clean-alluredir

# Открытие отчета
allure serve allure-results
