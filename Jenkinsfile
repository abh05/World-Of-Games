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
               echo 'Running the container image...'
               echo 'Making a dummy score file'
               sh 'echo \'{32}\' > dummy_scores.txt'
               sh 'docker-compose up -d'
               sh 'docker-compose cp dummy_scores.txt score-srv:scores.txt'
               sh 'docker-compose build'
            }
        }
           stage('Test') {
            steps {
                sh 'echo a'
            }
        }
    }
}