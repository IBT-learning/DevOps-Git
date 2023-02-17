pipeline {
    agent any
    parameters{
     string(name:'Branch_name', defaultValue:'main', description:'enter branch to build')
     choice(name: 'CHOICES', choices: ['one', 'two', 'three'], description: '')
    }

    stages {
        stage('Hello') {
            steps { 
                echo "hello"
            }
        }
        stage('Git clone') {
            steps {
                echo 'cloning from github'
                git branch: '$Branch_name', changelog: false, credentialsId: 'ibt', poll: false, url: 'https://github.com/IBT-learning/DevOps-Git.git'
            }
        }
        stage('Git verify') {
            steps {
                echo '$CHOICES'
            }
        }
        stage('Adding stage from jenkinsfile') {
        when{
            expression{
                BRANCH_NAME == 'main'
            }
        }
            steps {
                sh 'pwd' 
            }
        }
        stage('testing hooks') {
            steps {
                echo "it worked automatically"
            }
        }
    }
}
