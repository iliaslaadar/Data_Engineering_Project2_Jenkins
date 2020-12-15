pipeline{
    agent any
    stages{
        stage('APP') {
            steps{
                //BRANCH_NAME = 'feature_app'
                echo 'Run the app:'
                sh 'python3 app.py &'
                sh "sleep 10"
            }
        }
        stage('TEST') {
            //when { triggeredBy 'APP' }
            //when { environment name: 'DEPLOY_TO', value: 'production' }
            steps{
                echo 'Test the app:'
                sh 'python3 Integration_test.py'
                sh 'python3 Unit_test.py'
            }
        }
    }
}

