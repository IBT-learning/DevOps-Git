pipeline {
    agent any

    stages {
        stage('Hello') {
            steps { 
                echo "hello"
            }
        }
        stage('Git clone') {
            steps {
                echo 'cloning from github'
                git branch: 'main', changelog: false, credentialsId: 'ibt', poll: false, url: 'https://github.com/IBT-learning/DevOps-Git.git'
            }
        }
        stage('Git verify') {
            steps {
                sh 'ls -lrt' 
            }
        }
    }
}
