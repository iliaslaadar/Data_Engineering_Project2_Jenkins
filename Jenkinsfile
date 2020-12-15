pipeline{
    agent any
    stages{
        stage('TEST') {
            steps{
                echo 'Test the app:'
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
