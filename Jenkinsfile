pipeline{
    agent any
    stages{
//        stage('BUILD') {
//            steps{
//                echo 'Run the app:'
//                sh 'docker build -t project2 .'
//            }
//        }
        stage('RUN') {
                steps{
                    echo 'Test the app:'
                    sh 'docker run -p 5000:5000 project2'
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
