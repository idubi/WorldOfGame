# Check if the container exists
$containerExists = docker ps -a --format "{{.Image}}" | Where-Object { $_ -like "*world-of-games*" }
if ($containerExists) {
    docker rm -f wow-app
	docker rmi -f $(docker images 'idubi/world-of-games' -q)
}
