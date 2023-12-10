# Check if the container exists
$containerExists = docker ps -a --format "{{.Image}}" | Where-Object { $_ -like "*world-of-games*" }
if ($containerExists) {
    docker rm -f wow-app
	docker rmi -f $(docker images 'world-of-games' -q)
}

$repoExists = docker images 'idubi/world-of-games' 
if ($repoExists) {
    docker rmi -f $(docker images 'idubi/world-of-games' -q)    <# Action to perform if the condition is true #>
}
