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
                    bat 'pip install -r requirements.txt'
                    bat 'pytest'
                }
            }
        }
    }
}
