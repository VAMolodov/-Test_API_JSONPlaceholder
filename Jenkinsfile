

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
        stage('Prepare') {
            steps {
                // Создаем папку заранее силами Jenkins
                sh 'mkdir -p allure-results'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Собираем образ
                sh 'docker build -t my-api-tests .'
            }
        }

        stage('Run API Tests') {
            steps {
                // запускаем тесты
                sh 'docker run --rm -v $(pwd)/allure-results:/app/allure-results my-api-tests pytest --alluredir=allure-results --clean-alluredir'
            }
        }
    }

    post {
        always {
            sh 'docker run --rm -v $(pwd):/work busybox chown -R 1000:1000 /work/allure-results || true'
            // Генерируем отчет
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
