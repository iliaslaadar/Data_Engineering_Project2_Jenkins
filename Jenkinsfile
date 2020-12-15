pipeline{
    agent any
    stages{
        stage('APP') {
            steps{
                echo 'Run the app:'
                sh 'python3 app.py &'
                sh "sleep 10"
                script{
                    env.BRANCH_NAME = 'feature_tests'
                    //sh 'git checkout feature_tests'
                    sh 'git remote update'
                    sh 'git fetch'
                    sh 'git checkout */feature_tests'
                }
                
                //script{env.BRANCH_NAME = 'feature_tests'}
            }
        }
        stage('TEST') {
            //when { triggeredBy 'APP' }
            when { environment name: 'BRANCH_NAME', value: 'feature_tests' }
            steps{
                echo 'Test the app:'
                sh 'python3 Integration_test.py'
                sh 'python3 Unit_test.py'
            }
        }
    }
}
