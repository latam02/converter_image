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
        sh '''python -m pytest ./convert_image/test/test_convert_image.py
'''
      }
    }

  }
}