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
           stage('Test') {
            steps {
                sh 'echo a'
            }
        }
    }
}