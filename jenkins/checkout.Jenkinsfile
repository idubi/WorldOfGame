
properties([  githubProjectProperty(displayName: 'CHECKOUT WOG from git', 
                                    projectUrlStr: 'https://github.com/idubi/WorldOfGame/'), 
              
              ])
pipeline {
    agent  {
                    label "win-agent"
                }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: "*/jenkins"]], 
                    userRemoteConfigs: [[
                        url: 'https://github.com/idubi/WorldOfGame/',
                        credentialsId: 'idubi_github'
                    ]]
                ])
            }
        }
        stage('clean local dockr if exist') {
            steps {
                powershell("""
                    .\\docker\\remove-wow-image.ps1
                """)
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Navigate to the directory containing your Dockerfile
                    dir('.') {
                        // Build a Docker image using the Dockerfile
                        bat 'docker build -t world-of-games .'
                    }
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Run a Docker container from the previously built image
                    bat 'docker run -d -p 8777:8777 --name wow-app world-of-games'
                }
            }
        }
        // stage('prepare for e2e test - install webdriver ') {
        //     steps {
        //         script {
        //             // Run a Docker container from the previously built image
        //             bat 'resources\\selenium\\chromedriver-win64\\chromedriver.exe'
        //             }
        //     }
        // }
        stage('E2E test on exported port') {
            steps {
                script {
                    // Run a Docker container from the previously built image
                    bat 'pip install selenium'
                    bat 'python ./tests/E2E_Score_Unites.py'
                }
            }
        }
    }
}