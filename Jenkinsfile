pipeline{
    agent any
    stages{
        stage('APP') {
            steps{
                echo 'Run the app:'
                //sh 'git checkout feature_app'
                sh 'env.BRANCH_NAME'
                sh 'python3 app.py &'
                sh "sleep 10"
            }
        }
        stage('TEST') {
            steps{
                echo 'Test the app:'
                sh 'git checkout feature_tests'
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
