pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
                git 'https://github.com/abh05/World-Of-Games.git'
            }
        }
        stage('Build Image testjenkins_score-srv') {
            steps {
               sh 'pip uninstall --yes urllib3'
               sh 'pip install urllib3==1.22'
               sh 'sudo docker-compose build'
            }
        }
        stage('Run container image') {
            steps {
               echo 'Running container image...'
               sh 'echo \'32\' > Score.txt'
               sh 'sudo docker-compose down && sudo docker-compose up -d'
               sh 'sudo docker cp Score.txt score-srv:/app'
            }
        }
        stage('Score-srv Selenium Test on Ubuntu 18.04') {
            steps {
               echo 'testing the score server...'
                 sh 'pip3 install -r requirements.txt'
                 sh 'sudo apt-get install chromium-chromedriver=99.0.4844.51-0ubuntu0.18.04.1'
                 sh 'chmod 777 Tests/chromedriver'
                 sh 'python3 Tests/e2e.py'
               script {
                   echo "${currentBuild.currentResult}"
               }
            }
            post {
                failure {
                    echo "${currentBuild.currentResult}"
                    echo "Test Failed - will not upload image"
                }
            }
        }
        stage('Finalize upload image to Docker-Hub and delete container') {
            steps{
                 echo "upload image"
                    sh 'sudo docker stop score-srv'
                    sh 'sudo docker rm score-srv'
                 echo 'docker push <username/testjenkins_score-srv>'
            }
            post {
                always {
                    cleanWs()
                }
            }
        }
    }
}