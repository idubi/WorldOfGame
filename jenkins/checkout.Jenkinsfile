
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
                    branches: [[name: "*/main"]], 
                    userRemoteConfigs: [[
                        url: 'https://github.com/idubi/WorldOfGame/',
                        credentialsId: 'idubi_github'
                    ]]
                ])
            }
        }
         stage('Build Docker Image') {
            steps {
                script {
                    // Navigate to the directory containing your Dockerfile
                    dir('.') {
                        // Build a Docker image using the Dockerfile
                        bat 'docker build -t WORLD_OF_GAMES .'
                    }
                }
            }
        }
          stage('Run Docker Container') {
            steps {
                script {
                    // Run a Docker container from the previously built image
                    bat 'docker run -d --name wow-app WORLD_OF_GAMES'
                }
            }
        }
        

      

    // post {
    //     // Post-build actions
    // }
}
}