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
        withEnv(["HOME=${env.WORKSPCE}"]) {
          sh 'pip install --user -r requirements.txt'
        }
      }
    }

  }
}