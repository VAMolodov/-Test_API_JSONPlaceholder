pipeline {
    //  На чем запускать (any - на любом свободном сервере/агенте)
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Скачиваем код из Git (настройки возьмутся из интерфейса Jenkins)
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Собираем образ
                sh 'docker build --no-cache -t my-api-tests .'
            }
        }

        stage('Run API Tests') {
            steps {
                // 1. Запускаем контейнер БЕЗ маппинга -v, но даем ему имя 'test-container'
                // Используем || true, чтобы билд не падал до того, как мы заберем отчеты
                sh 'docker run --name test-container my-api-tests pytest --alluredir=allure-results || true'
                
                // 2. Копируем папку с результатами ИЗ контейнера в Jenkins Workspace
                sh 'docker cp test-container:/app/allure-results ./'
                
                // 3. Удаляем временный контейнер
                sh 'docker rm test-container'
            }
        }

    }

    post {
        always {

            // Генерируем отчет
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
