pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"

                bat "docker build -t kubedemoapp:v1 ."
            }
        }

        stage('Docker Login') {
            steps {

                bat 'docker login -u tejaswini022 -p ashwini@2005'

            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {

                echo "Push Docker Image to Docker Hub"

                bat "docker tag kubedemoapp:v1 tejaswini022/kubeimage1:latest"

                bat "docker push tejaswini022/kubeimage1:latest"

            }
        }

        stage('Deploy to Kubernetes') {
            steps {

                echo "Deploy to Kubernetes"

                bat 'kubectl apply -f deployment.yaml --validate=false'

                bat 'kubectl apply -f service.yaml'

            }
        }
    }

    post {

        success {
            echo "Pipeline completed successfully!"
        }

        failure {
            echo "Pipeline failed!"
        }
    }
}