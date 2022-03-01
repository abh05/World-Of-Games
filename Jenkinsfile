pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                git 'https://github.com/abh05/World-Of-Games.git'
            }
        }
        stage('Build and Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                sh 'e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                bat python 'docker-compose down'
            }
        }
    }
}