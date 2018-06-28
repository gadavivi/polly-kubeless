# polly-kubeless
Text to speech converter using aws-polly and Kubeless

#Deploy

First create a kubernetes cluster with ingress (follow up to "Deploy Kubeless" section) - [Running FaaS on Kubernetes Cluster on AWS using Kubeless](https://aws.amazon.com/blogs/opensource/running-faas-on-kubernetes-cluster-on-aws-using-kubeless/)

after installing the [serverless framework](https://serverless.com/framework/docs/providers/kubeless/guide/installation/):

run to create the stack:
```
$ git clone https://github.com/gadavivi/polly-kubeless.git
$ cd polly-kubeless
$ serverless deploy -s dev
```