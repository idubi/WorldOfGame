# Set Docker Hub credentials
$DOCKER_HUB_USERNAME = "your_dockerhub_username"
$DOCKER_HUB_PASSWORD = "your_dockerhub_password"

# Set image name and tag
$IMAGE_NAME = "your-username/your-repo:your-tag"

# Build Docker image
docker build -t $IMAGE_NAME .

# Log in to Docker Hub
docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_PASSWORD

# Push Docker image to Docker Hub
docker push $IMAGE_NAME
