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
               sh 'pip uninstall --yes urllib3'
               sh 'pip install urllib3==1.22'
               sh 'sudo docker-compose build'
            }
        }
        stage('Run') {
            steps {
               echo 'Running container image...'
               sh 'echo \'32\' > Score.txt'
               sh 'sudo docker-compose down && sudo docker-compose up -d'
               sh 'sudo docker cp Score.txt score-srv:/app'
            }
        }
        stage('Test') {
            steps {
               echo 'testing the score server...'
                 sh 'pip install -r requirements.txt'
                 sh 'python3 Tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
               echo 'uploading docker'
            }
        }
    }
}