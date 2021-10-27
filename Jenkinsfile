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
          sh 'python -m pytest ./convert_image/test/test_convert_image.py'
          // sh 'python -m pytest --html=report.html --self-contained-html'
          sh 'python -m pytest --html=../../report.html -s'
          sh 'ls -ls'
        }
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: '**', followSymlinks: false
    }
  }
}