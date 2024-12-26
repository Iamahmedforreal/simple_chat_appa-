pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building the application...'
        bat 'docker build -t hello-world-app .'
      }
    }
    stage('Test') {
      steps {
        echo 'Testing the application...'
        bat 'python test_t.py' // Adjust for your Python version
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying the application (locally)...'
        bat 'docker run -d -p 82:82 hello-world-app'
      }
    }
  }
  post {
    success {
      echo 'Pipeline completed successfully!'
    }
    failure {
      echo 'Pipeline failed. Check the logs for details.'
    }
  }
}
