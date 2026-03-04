

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
                sh 'docker build -t my-api-tests .'
            }
        }

        stage('Run API Tests') {
            steps {
                // Запускаем тесты и сохраняем результаты в папку проекта в Jenkins
                // --clean-alluredir очистит результаты прошлого запуска внутри контейнера
                sh 'docker run --rm -v ${WORKSPACE}/allure-results:/app/allure-results my-api-tests pytest --alluredir=allure-results --clean-alluredir'
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
