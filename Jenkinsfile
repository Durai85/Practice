pipeline {
    agent any

    environment {
        IMAGE_NAME      = "todo-app"
        DOCKER_HUB_USER = "durai85"
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Durai85/Practice.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKER_HUB_USER/$IMAGE_NAME:latest .'
            }
        }

        stage('Push to Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                      docker push $DOCKER_HUB_USER/$IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                  docker stop myapp-container || true
                  docker rm myapp-container || true
                  docker run -d --name myapp-container -p 5000:5000 $DOCKER_HUB_USER/$IMAGE_NAME:latest
                '''
            }
        }
    }
}