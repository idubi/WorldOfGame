helm repo add jenkins https://charts.jenkins.io
helm repo add ngrok https://ngrok.github.io/kubernetes-ingress-controller
helm repo update
docker run --net=host -it -e NGROK_AUTHTOKEN=2BsrQx17WJ65dtFrpOnbpwJ9GOa_6foW4pMD8WXui74TfJKv5 --name ngrok ngrok/ngrok:latest http 8777

