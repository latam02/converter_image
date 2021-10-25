pipeline {
  agent any
  stages {
    stage('UnitTest') {
      agent {
        docker {
          image 'python:3.8-slim'
        }

      }
      steps {
        sh 'ls -la'
        sh 'pip --version'
        sh 'pip freeze'
      }
    }

  }
}