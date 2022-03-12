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
        stage('Test Ubuntu 18.04') {
            steps {
               echo 'testing the score server...'
                 sh 'pip3 install -r requirements.txt'
                 sh 'sudo apt-get install chromium-chromedriver=99.0.4844.51-0ubuntu0.18.04.1'
                 sh 'chmod 777 Tests/chromedriver'
                 sh 'python3 Tests/e2e.py'
            }
            post{
                success {
                }
                failure {
                    script{
                        error "Failed, exiting now..."
                    }
                }
        }
        stage('Finalize') {
            steps{
                script {
                       if (currentBuild.result == "FAILURE"){
                            echo "The Test stage is fail. The Image didn`t pushed"
                            currentStage.result = "FAILURE"
                       }
                       else{
                            echo "upload image"
                       }
                 }
            }
            post {
                always {
                    cleanWs()
                }
            }
        }
    }
}