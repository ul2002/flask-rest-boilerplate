pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.7.2-slim' 
                }
            }
            steps {
                sh 'pip install -r requirements.txt' 
                sh 'python manage.py run'
            }
        }
    }
}