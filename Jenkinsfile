pipeline{
    agent any

    stages{
        stage('now root'){
            steps{
                sh 'pwd'
            }
            post{
                success{
                    echo 'root search seccess'
                }
                failure{
                    echo 'root search faild'
                }
            }
        }
        stage('docker build'){
            steps{
                sh 'docker build -t test-build .'
            }
            post{
                success{
                    echo 'docker build seccess'
                }
                failure{
                    echo 'docker build faild'
                }
            }
        }
        stage('docker-compose'){
            steps{
                sh 'docker-compose up -d'
            }
            post{
                success{
                    echo 'docker-compose seccess'
                }
                failure{
                    echo 'docker-compose faild'
                }
            }
        }
    }
}