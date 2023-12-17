# World Of Games - DevOps 01052023 
delivered by **ido bistry**
---

project instructed of game code and deployment 
deploymnet done with docker jenkins. 

fror this deployment one must have Docker desktop
the deployment in docker installed

the deployment is relyinh on windows agent , but can be created with linux agent as well (with some code changes in the jenkinsfile)

in order to "test phase" to run - one must have selenium istalled aproperiate  for his chrome version, in the windows agent computer

**1**  . create a jenkins docker with colume directing to this folder : ***./jenkins/jenkins-data***
this volum contains all needed for jenkins allready install in order to load jenkins 
## 

    docker run -d -p 8080:8080 -p 8000:80 -p 50000:50000 -p 443:443 \
    	   --name jenkins --network jenkins-network --volume "D:\projects\WorldOfGame\jenkins\jenkins-data":/var/jenkins_home \ 
    	   --env JENKINS_USERNAME=admin --env JENKINS_PASSWORD=bitnami --env JENKINS_EMAIL=idubi.pro@gmail.com jenkins/jenkins:latest

- the user is created with admin/bitnami , but saved with admin/admin (after loading the volume iut is changed within volume congfiguration)
**user : admin/admin**



**2**  . for windws agent to run you will need to execite this 2 commands: 

    1. curl.exe -sO http://localhost:8080/jnlpJars/agent.jar
    2. java -jar agent.jar -url http://localhost:8080/ -secret 662069054a25e40cb0e83bc2af14418a2b4e3978296604d3cae07250e13c3741 -name "win-agent" -workDir "d:\jenkins_agent_executions\win-agent"
 
in oder to execute the deploymnent just go to : 
(after the setup this link will be availabele in created jenkins)
-   [deploy world-of-games](http://localhost:8080/job/world-of-games/job/deploy%20world-of-games/)
and execute deployment with parameters 

deployment parameters ar : 
1. the type of execution (can be VERSION < RELEASE and BUILD ) - the build is promoting each of the parts of the tagname accordingly 
2. numbet of images to leave in the dockerhub repository

since my  GIT repo and the DOCKER are private , the login credentials are encrypted as jenkins credentiols and the deployment read it while executions

the specific git repo is public, sicne you need to first clone this repo to get started, but on a production this would had been done on a different repo





# Deployment Process
the deployment process has this parts / stages   (see jenkinsfile): 
1. Clean Workspace - delete the workspace files from win agent
2. checkout from github - the main branch
3.  delete old docker container and image if existst - this is in the win agents docker client 
this is done by executing **powershell** code ([*remove-wow-image.ps1*](https://github.com/idubi/WorldOfGame/blob/main/jenkins/docker-commands/remove-wow-image.ps1))
4. Build Docker Image - this execute the [*Dockerfile*](https://github.com/idubi/WorldOfGame/blob/main/Dockerfile) from workspace home directory 
5. Run Docker Container - execue a docker container and point it to port :8777  in localhost
6. E2E test on exported port - execute with selenium (relying on selenium installed in your win client) e2e tests done with this file [*E2E_Score_Unites.py*](https://github.com/idubi/WorldOfGame/blob/main/tests/E2E_Score_Unites.py) in the GIT repo

current test is actually testing that the scores table was created with the deployment of the application

*(since we have piptest installed with [requirements.txt](https://github.com/idubi/WorldOfGame/blob/main/requirements.txt) then the tests should be working)*

7. login to dockerhub - using jenkins predefind credentials 
8. push to dockerhub - execute python code  ([*docker-hub-utils.py*](https://github.com/idubi/WorldOfGame/blob/main/docker/docker-hub-utils.py))  that does thissteps
 - [ ] get the last images inside docekr hub
 - [ ] increase the Version/Release/Build  numbet according to parameter
 - [ ] delete redubdent images from repository according to parameter, and latest version
 - [ ] push the created repo with created new tagname  and set it as latest


9. logout from dockerhub - this is done even if one of the previous steps is failed


