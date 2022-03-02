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
                sh 'sudo docker-compose up '
            }
        }
           stage('Test') {
            steps {
                sh 'echo a'
            }
        }
    }
}