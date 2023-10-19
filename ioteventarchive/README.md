# IoT data event archive using Kinesis Firehose

This sample demonstrates the use of Kinesis Firehose triggered by EventBridge to 
archive IoT events received from AWS IoT Core. It is intended to demonstrate the 
blog post [Reducing scan archive storage costs by 95 % using Kinesis Data Firehose](https://engineering.proglove.com/blog/2023/10/18/reducing-scan-archive-storage-costs-by-95-percent-using-kinesis-data-frehose.html).

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

## Usage

In order to test the setup, you can simply use the AWS IoT Core test client in the AWS management web console.
The following link gets you there, please be aware that you may have to replace the region to suit yours - the sample 
uses `eu-west-1`: [https://eu-west-1.console.aws.amazon.com/iot/home?region=eu-west-1#/test](https://eu-west-1.console.aws.amazon.com/iot/home?region=eu-west-1#/test).

There, you can publish an IoT message to the IoT topic `iot/your-topic`, where you can choose anything you like for `your-topic`.

Then, you can go to the S3 buckeet created as part of the stack, and after one or two minutes, you should see data coming in.
