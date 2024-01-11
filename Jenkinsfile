pipeline {
    agent any

    environment {
        // Define las variables de entorno necesarias
        DOCKER_IMAGE = 'cisquito/cc-proyectopatitas-tests:latest'
    }

    // Condicional para ejecutar solo cuando proviene de GitHub Actions
    when {
        expression { env.GITHUB_ACTIONS == 'true' }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    // Construir la imagen de Docker
                    docker.build(env.DOCKER_IMAGE)
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Ejecutar las pruebas con pytest dentro del contenedor Docker
                    docker.image(env.DOCKER_IMAGE).inside {
                        sh 'pip install -r requirements.txt'
                        sh 'pytest'
                    }
                }
            }
        }
    }
}
