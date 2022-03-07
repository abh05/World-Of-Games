pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                git 'https://github.com/abh05/World-Of-Games/'
            }
        }
        stage('Build') {
            steps {
               sh 'sudo docker-compose build'
            }
        }
        stage('Run') {
            steps {
               echo 'Running container image...'
               sh 'echo \'{32}\' > scores.txt'
               sh 'sudo docker-compose down && sudo docker-compose up -d'
               sh 'sudo docker cp scores.txt score-srv:/app'
            }
        }
           stage('Test') {
            steps {
                sh 'echo a'
            }
        }
    }
}