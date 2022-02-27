pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                git 'https://github.com/abh05/World-Of-Games.git'
            }
        }
                stage('Build') {
            steps {
                bat 'docker-compose up'
            }
        }
    }
}