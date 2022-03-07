pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/abh05/World-Of-Games.git/')])
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