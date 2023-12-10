#!bin/sh
cd /var/jenkins-agent
curl -sO http://host.docker.internal:8080/jnlpJars/agent.jar
nohup java -jar agent.jar -url http://host.docker.internal:8080/ -secret a75e3766f4de975c4f4c5561eae36a3bf854f43c41baa3a33ed05084447a2cae -name "docker-agent" -workDir "/var/jenkins-agent" > agent_logs.txt &
cd -


