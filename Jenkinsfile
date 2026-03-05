

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
        stage('Clear old results') {
            steps {
                // Полностью чистим папку перед новым запуском
                sh 'rm -rf allure-results && mkdir allure-results'
                sh 'chmod 777 allure-results' 
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
                // запускаем тесты
                sh 'docker run --rm -v $(pwd)/allure-results:/app/allure-results my-api-tests pytest --alluredir=/app/allure-results --clean-alluredir'
            }
        }
    }

    post {
        always {

            // Генерируем отчет
            sh 'docker run --rm -v $(pwd):/work busybox chown -R 1000:1000 /work/allure-results || true'
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
