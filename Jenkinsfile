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
<<<<<<< HEAD
        sh 'whoami'
        sh 'pip -r install requirements.txt'
=======
        sh 'ls -la'
        sh 'pip --version'
        sh 'pip install requirements.txt'
        sh 'python -m pytest ./convert_image/test/test_convert_image.py'
>>>>>>> 4c4cadeb266facedf9b6a423540303e7e431ddce
      }
    }

  }
}