
pipeline{
    agent any
    stages{
        stage('APP') {
            steps{
                echo 'Run the app:'
                sh 'python3 app.py &'
                sh 'sleep 10'
            }
        }
    }
}
