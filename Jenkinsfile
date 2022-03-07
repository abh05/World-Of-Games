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
                sh 'echo \'{32}\' > scores.txt'
                sh 'sudo docker-compose build'
            }
        }
        stage('Run') {
            steps {
               echo 'Running the container image...'
               echo 'Making a dummy score file'
               sh 'sudo docker-compose down && sudo docker-compose up -d'
            }
        }
           stage('Test') {
            steps {
                sh 'echo a'
            }
        }
    }
}