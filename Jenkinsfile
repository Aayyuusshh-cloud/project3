pipeline {
    agent any

    options {
        timestamps()
        ansiColor('xterm')
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }

    environment {
        APP_NAME = 'fastapi-crud-jwt'
        IMAGE = "fastapi-crud-jwt:build-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python & Dependencies') {
            steps {
                sh """
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    . .venv/bin/activate
                    pytest -q
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE} ."
            }
        }

        stage('Deploy (same EC2)') {
            steps {
                sh """
                    docker rm -f fastapi-prod || true
                    docker run -d --name fastapi-prod -p 80:8000 \\
                        -e SECRET_KEY=prod \\
                        ${IMAGE}


