pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}/my_temp_project/src"
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    echo "🛠 Cleaning workspace..."
                    sh 'rm -rf my_temp_project'
                    
                    echo "📥 Cloning repository..."
                    sh 'git clone https://github.com/Saiganesh-0918/my_temp_project.git my_temp_project'

                    echo "✅ Repository cloned successfully!"
                    sh 'ls -la my_temp_project'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "📦 Installing dependencies..."
                    sh 'pip install --break-system-packages pytest'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "🚀 Running tests..."
                    sh '''
                        cd my_temp_project
                        export PYTHONPATH=$WORKSPACE/my_temp_project/src
                        echo "PYTHONPATH is now set to: $PYTHONPATH"
                        pytest tests/ --capture=tee-sys
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check the logs for details."
        }
    }
}

