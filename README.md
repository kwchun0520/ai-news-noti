# ai-news-noti

This is a repo of sending news notification to Telegram using AWS lambda function.

Get start by

1. store telegram token and chat id into 2 key/value pairs in a secret in AWS secret manager

2. add to .env
```
TELEGRAM_TOKEN=_TELEGRAM_TOKEN_
CHAT_ID=_CHAT_ID_
AWS_ACCOUNT_ID=_AWS_ACCOUNT_ID_
AWS_TELEGRAM_SECRET_NAME=__AWS_TELEGRAM_SECRET_NAME_ON_SECRET_MANAGER__
AWS_TELEGRAM_SECRET_TELEGRAM_TOKEN_KEY=__AWS_TELEGRAM_SECRET_TELEGRAM_TOKEN_KEY__
AWS_TELEGRAM_SECRET_CHAT_ID_KEY= __AWS_TELEGRAM_SECRET_CHAT_ID_KEY__
REGION=_REGION_
DRY=0
```

pre-steps of using AWS lambda

a. You must create a AWS account and install AWS CLI on local
b. You must set AWS CLI configuration on local by
``` bash
aws configure
```
c. create iam role for lambda execution
``` bash
./create-iam-role.sh
```

deploy to AWS
``` bash
./deploy.sh __FUNCTON_NAME__
```

schedule AWS lambda function
``` bash
./schedule.sh __FUNCTON_NAME__
```


invoke the AWS lambda function
``` bash
./invoke.sh __FUNCTION_NAME__
```