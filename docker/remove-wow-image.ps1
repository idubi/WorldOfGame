# Check if the container exists
$containerExists = docker ps -a --format "{{.Image}}" | Where-Object { $_ -eq "world-of-games" }

if ($containerExists) {
    docker rm -f wow-app
	docker rmi world-of-games
}
