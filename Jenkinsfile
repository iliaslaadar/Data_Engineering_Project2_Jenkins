pipeline{
    agent any
    stages{
        stage('BUILD') {
            steps{
                echo 'Run the app:'
                sh 'docker build -t projet_tweet .'
            }
        }
        stage('RUN') {
            steps{
                echo 'Run the app:'
                sh 'docker run -it -d -p 5000:5000 --name projet_tweet_c projet_tweet'
            }
        }
        stage('TEST') {
            steps{
                echo 'Test the app:'
                sh 'python3 Integration_test.py'
                sh 'python3 Unit_test.py'
            }
        }
        stage('STOP') {
            steps{
                script{
                    
                }
            }
        }
    }
}
