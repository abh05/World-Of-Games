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
                 sh 'pip3 install -r requirements.txt'
                 dir("/var/lib/jenkins/workspace/world-of-games/") {
                 sh """
                 sudo bash -c "echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list"
                 sudo apt -y update
                 sudo apt -y install google-chrome-stable
                 sudo apt-get install -yqq unzip curl
                 sudo wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
                 sudo unzip -o /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
                 """
                 }
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