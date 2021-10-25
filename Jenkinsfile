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
        sh 'pip -r install requirements.txt'
        sh 'python -m pytest ./convert_image/test/test_convert_image.py'
      }
    }

  }
}