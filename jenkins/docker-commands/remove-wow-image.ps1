# Check if the container exists
$containerExists = docker ps -a --format "{{.Image}}" | Where-Object { $_ -like "*world-of-games*" }

if ($containerExists) {
    docker rm -f wow-app
	docker images | Where-Object { $_.Repository -like "*world-of-games*" } | ForEach-Object { docker rmi $_.ID }
}
