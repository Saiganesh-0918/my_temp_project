pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo " Cleaning workspace..."
                sh 'rm -rf my_temp_project'  // Remove old files if they exist
                
                echo " Cloning repository..."
                sh 'git clone https://github.com/Saiganesh-0918/my_temp_project.git'
                
                echo " Repository cloned successfully!"
                sh 'ls -la my_temp_project'  // List files to confirm cloning
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                echo " Setting up Python virtual environment..."
                sh '''
                    cd my_temp_project
                    python3 -m venv venv
                    . venv/bin/activate
                    echo " Virtual environment activated!"
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies..."
                sh '''
                    cd my_temp_project
                    source venv/bin/activate
                    pip install --break-system-packages -r requirements.txt
                    echo " Dependencies installed!"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo " Running tests..."
                sh '''
                    cd my_temp_project
                    source venv/bin/activate
                    export PYTHONPATH=$(pwd)/src
                    pytest tests/ --capture=tee-sys
                '''
            }
        }
    }

    post {
        success {
            echo " Pipeline completed successfully!"
        }
        failure {
            echo " Pipeline failed. Check the logs for details."
        }
    }
}

