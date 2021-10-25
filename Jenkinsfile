pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo hello world'
      }
    }

    stage('Unit test') {
      steps {
        sh '''python -m pytest -vv --cov=app ./convert_image/test/test_convert_image.py
'''
      }
    }

  }
}