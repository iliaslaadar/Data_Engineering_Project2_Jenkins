pipeline{
    agent any
    stages{
        stage('TEST') {
            steps{
                echo 'Run the app:'
                echo env.BRANCH_NAME
                sh 'python3 app.py &'
                sh "sleep 10"
            }
            BRANCH_NAME = 'feature_tests'
            when{
                expression{
                    BRANCH_NAME == 'feature_tests'
                }
            }
            steps{
                echo env.BRANCH_NAME
                echo 'Test the app:'
                //sh 'git checkout feature_tests'
                sh 'python3 Integration_test.py'
                sh 'python3 Unit_test.py'
            }
        }
        stage('STOP') {
            steps{
                echo 'Exit the app:'
                sh 'kill -INT $(lsof -t -i :5000)'
            }
        }
    }
}
