
properties([  githubProjectProperty(displayName: 'CHECKOUT WOG from git', 
                                    projectUrlStr: 'https://github.com/idubi/WorldOfGame/',
                                    description:  'CHECKOUT WOG from git'), 
              
              parameters([string(defaultValue: 'idubi_github', description: 'the credentials to login to github', name: 'github_credentials_id'),
                        string(defaultValue: 'https://github.com/idubi/WorldOfGame/', description: 'the github repo', name: 'github_repository_url'), 
                        string(defaultValue: 'jenkins', description: 'github branch to checkut', name: 'github_branch'), 
                        string(defaultValue: 'Jenkinsfile', description: 'the jenkinsfile script  file name to execute ', name: 'script_file')
                      ])
              ])
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: "*/${params.github_branch}"]], 
                    userRemoteConfigs: [[
                        url: '${github_repository_url}',
                        credentialsId: '${github_credentials_id}'
                    ]]
                ])
            }
        }

      

    // post {
    //     // Post-build actions
    // }
}
}