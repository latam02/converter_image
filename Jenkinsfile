pipeline {
  agent any
  environment {
    SONAR_TOKEN=credentials('sonar_token')
    DOCKER_USER='christc'
    DOCKER_PASSWORD=credentials('docker_password')
    IMAGE_NAME='convert_image'
    TAG_VERSION='1.0'
  stages {
    stage('UnitTest') {
      agent {
        docker {
          image 'python:3.8.12'
        }
      }
      steps {
        withEnv(["HOME=${env.WORKSPCE}"]) {
          sh 'pip install --upgrade pip'
          sh 'pip install --user -r requirements.txt'
          // sh 'python -m pytest --html=report.html --self-contained-html'
          sh 'python -m pytest -r ./convert_image/test/test_convert_image.py'
          sh 'python -m pytest --html=./report.html -s'
          sh 'ls -la'
        }
      }
      post {
        always {
          sh 'ls -la'
          archiveArtifacts artifacts: 'report.html', followSymlinks: false
        }
      }
    }
    stage('CodeQuality') {
      steps {
        sh "/var/jenkins_home/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner   -Dsonar.organization=latam02ci   -Dsonar.projectKey=converterimage   -Dsonar.sources=.   -Dsonar.host.url=https://sonarcloud.io"
      }
    }
    stage('QualityGates') {
      steps {
        sh 'echo get the compute results: Failed/Passed for your scanned project'
      }
    }
    stage('Package'){
      steps {
        sh 'docker build -t ${IMAGE_NAME}:${TAG_VERSION} .'
      }
    }
    stage('Publish'){
      steps {
        sh 'docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD}'
        sh 'docker tag ${IMAGE_NAME}:${TAG_VERSION} christc/${IMAGE_NAME}:${TAG_VERSION}'
        sh 'docker push christc/${IMAGE_NAME}:${TAG_VERSION}'
      }
    }
    stage('Deploy'){
      steps {
        sh 'echo deploy'
      }
    }
  }
}
