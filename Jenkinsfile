pipeline{
    agent any
    stages{
        stage('APP') {
            steps{
                echo 'Run the app:'
                sh 'python3 app.py &'
                sh "sleep 10"
            }
        }
        stage('TEST') {
            steps{
                echo 'Test the app:'
                sh 'python3 Integration_test.py'
                sh 'python3 Unit_test.py'
            }
        }
        stage('MERGE') {
            steps{
                sh 'git checkout main'
                sh 'git checkout -b release/v3'
                sh 'git push'
                sh 'git merge develop'
            }
        }
    }
}
