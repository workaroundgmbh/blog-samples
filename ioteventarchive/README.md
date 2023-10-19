# IoT data event archive using Kinesis Firehose

This sample demonstrates the use of Kinesis Firehose triggered by EventBridge to 
archive IoT events received from AWS IoT Core. It is intended to demonstrate the 
blog post [Reducing scan archive storage costs by 95 % using Kinesis Data Firehose](https://engineering.proglove.com/).

TODO: update link above

## Deployment

As of now, deployment can be done using the [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
You will need write access to an AWS account.

Also, be aware that deploying this sample can incur costs in your account.

In preparation for the packaging step, you will need to create an S3 bucket in your account.
Please replace `MY-BUCKET` with a unique bucket name of your choice.

```bash
aws s3 mb MY-BUCKET
```

First, you will need to run

```bash
aws cloudformation package --template-file template.yaml --s3-bucket MY-BUCKET template.out
```

Then, to deploy the sample, run:

```bash
aws cloudformation deploy --template-file template.out --stack-name iot-sample --capabilities CAPABILITY_NAMED_IAM
```
