pipeline {
    agent { docker { image 'python:3.6' } }
    stages {
        stage('build') {
            steps {
                sh 'python setup.py test'
            }
        }
    }
}
