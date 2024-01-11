pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'cisquito/cc-proyectopatitas-tests:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest'
                }
            }
        }
    }
}
