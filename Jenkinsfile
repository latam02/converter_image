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
        sh 'pip install --user -r CONVERTER_IMAGE/requirements.txt'
        // sh 'python -m pytest --html=report.html --self-contained-html'
        dir('CONVERTER_IMAGE') {
          sh 'ls -la'
          sh 'python -m pytest -r ./convert_image/test/test_convert_image.py'
          sh 'python -m pytest --html=../../report.html -s'
        }
      }
      post {
        always {
          archiveArtifacts artifacts: 'report.html', followSymlinks: false
        }
      }
    }
    stage('CodeQuality') {
      steps {
        sh "/var/jenkins_home/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner   -Dsonar.organization=latam02ci   -Dsonar.projectKey=converterimage   -Dsonar.sources=.   -Dsonar.host.url=https://sonarcloud.io"
      }
    }
  }
}
