
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

      

    // post {
    //     // Post-build actions
    // }
}
}

