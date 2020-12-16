pipeline{
	agent any
  stages {
    stage('RUN'){
      steps{
        script{
          sh 'python3 app.py &'
	  			sh 'sleep 5'
        }
      }  
    }
    stage('TEST'){
      steps{
        script{
          if (env.BRANCH_NAME == 'feature_app') {
            //sh 'python3 Integration_test.py'
						sh 'python3 Unit_test.py'
          }
        }
      }
    }
    stage('PUSH'){
      steps{
        script{
          if (env.BRANCH_NAME == 'develop') {
            echo 'Push to release'
						bat 'git merge feature_app'
          }
        }  
      }
    }
    stage('ACCEPTANCE'){
      steps{
        script{
          if (env.BRANCH_NAME == 'release/v2' ) {
            input 'Push to main ?'
          }
        }
      }
    }
    stage('MERGE'){
      steps{
        script{
          if (env.BRANCH_NAME == 'release/v2') {
            echo 'Merge to main'
          }
        }
      }
    }
  }
}
