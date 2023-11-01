pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Check out code from the GitHub repository
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']], // Specify the branch you want to checkout
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: '']], // Leave empty to checkout to the workspace root
                    submoduleCfg: [],
                    userRemoteConfigs: [[
                        url: 'https://github.com/idubi/WorldOfGame', // Replace with your GitHub repository URL
                        credentialsId: 'jenkins-login@idubi' // Replace with your GitHub credentials ID
                    ]]
                ])
            }
        }
        
        stage('Build') {
            steps {
                // Add build steps here
            }
        }
        
        // Add more stages as needed for your build and deployment process
    }
}
