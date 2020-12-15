
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
                //waitUntil {if (sh script: 'nc  0.0.0.0 5000 < /dev/null ; echo $?'==0) echo'waaw'}
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
