pipeline{
  agent any
  stages {
    stage('Build the Flask application'){
      steps{
        script{
          if (env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'release/v2' ) {
            sh 'python3 app.py &'
          }
        }
      }  
    }
    stage('Testing'){
      steps{
        script{
          if (env.BRANCH_NAME == 'feature_app') {
            sh 'python3 Unit_test.py '
          }
          else {
              echo 'Should be in the unittest branch to do the test !'
          }
        }
      }
    }
    stage('Release'){
      steps{
        script{
          if (env.BRANCH_NAME == 'develop') {
            echo 'Push to release '
          }
          else if (env.BRANCH_NAME == 'release/v2') {
            echo 'Already in release'
          }
        }  
      }
    }
    stage('User acceptance for pushing to main'){
      steps{
        script{
          if (env.BRANCH_NAME == 'release/v2' ) {
            input 'Push to main ?'
          }
        }
      }
    }
    stage('Merging to main'){
      steps{
        script{
          if (env.BRANCH_NAME == 'release/v2') {
            echo 'Merge to main'
          }
        }
      }
    }
    stage('Docker images down'){
      steps{
        script{
          if (env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'release/v2' ) {
            input 'Stop the container'
            sh 'kill -INT $(lsof -t -i :5000)'
          }
        }
      }
    }
  }
}
