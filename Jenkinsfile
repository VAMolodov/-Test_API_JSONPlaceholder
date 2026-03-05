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
                // 1. Принудительно удаляем старый контейнер, если он остался от прошлого раза
                sh 'docker rm -f test-container || true'
                
                // 2. Запускаем тесты (без маппинга -v)
                sh 'docker run --name test-container my-api-tests pytest --alluredir=allure-results || true'
                
                // 3. Копируем папку с результатами
                sh 'docker cp test-container:/app/allure-results ./'
                
                // 4. Удаляем временный контейнер
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
