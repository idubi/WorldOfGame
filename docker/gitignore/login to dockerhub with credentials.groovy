pipeline {
	agent  {
					label "win-agent"
	}                                   
	environment {
		DOCKERHUB_CREDENTIALS = credentials('idubi_dockerhub')
	}                
	stages {
	  stage('login to dockerhub') {
			steps   {
				 
					powershell("""
								# this 2 solutions raise a warning to avoid insecure environment . 
								#   --> however : sicne this is executed inside own computer or insid DMZ behind firewall 
								#       this is good for my needs. 
								#       in linux I would use --password-stdin and use 1 quoteted mark for groovy interpulation 
								#       for more security , but this is not the case. 
								#   --> we use powershall for environmental restricrtions
								#   
								#'echo DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR'
								docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW 
							""")
			
				
				}    
		}
	}
	post{
			always('logout from dockerhub') {
												powershell("""
												#  docker logout
														""")      
			}
		}   
}						
	