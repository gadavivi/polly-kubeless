# polly-kubeless
Text to speech converter using aws-polly and Kubeless

# Deploy

1. First create a kubernetes cluster with ingress (up to the "Deploy Kubeless" section) - [Running FaaS on Kubernetes Cluster on AWS using Kubeless](https://aws.amazon.com/blogs/opensource/running-faas-on-kubernetes-cluster-on-aws-using-kubeless/)
2. install the [serverless framework](https://serverless.com/framework/docs/providers/kubeless/guide/installation/):
3. install kafka:
```
$ export RELEASE=$(curl -s https://api.github.com/repos/kubeless/kubeless/releases/latest | grep tag_name | cut -d '"' -f 4)
$ kubectl create -f https://github.com/kubeless/kubeless/releases/download/$RELEASE/kafka-zookeeper-$RELEASE.yaml
```
4.run to create the stack:
```
$ git clone https://github.com/gadavivi/polly-kubeless.git
$ cd polly-kubeless
$ serverless deploy -s dev
```