pipeline {
  agent any
  stages {
    stage('UnitTest') {
      agent {
        docker {
          image 'python:3.8.12'
        }

      }
      steps {
        sh 'whoami'
        sh 'pip -r install requirements.txt'
      }
    }

  }
}