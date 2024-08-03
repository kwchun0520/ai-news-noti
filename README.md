# ai-news-noti

add to .env
```
TELEGRAM_TOKEN=_TELEGRAM_TOKEN_
CHAT_ID=_CHAT_ID_
AWS_ACCOUNT_ID=_AWS_ACCOUNT_ID_
REGION=_REGION_
DRY=0
```


pre-steps
## create iam role
``` bash
./create-iam-role.sh
```


simple deploy 
``` bash
./deploy.sh __FUNCTION_NAME__
```


schedule
``` bash
./schedule.sh __FUNCTON_NAME__
```

invoke
``` bash
./invoke.sh __FUNCTION_NAME__
