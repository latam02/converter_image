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
          sh 'ls -la'
          sh 'pip install --user -r requirements.txt'
          sh 'python -m pytest ./convert_image/test/test_convert_image.py'
        }
      }
    }
  }

  post {
    always {
      archiveArtifacts 'dir1/reports/report.html'
    }
  }
}