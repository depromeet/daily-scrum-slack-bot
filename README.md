# 데일리 스크럼 봇

### 개요
- 디프만 11기 활동 중 매일 아침 10시 데일리 스크럼 알림을 울리게 하기 위한 봇

### 실행 방법
[직접 실행]
```shell
$ python3 message.py
```
[Crontab]
```shell
0 10 * * * python3 message.py
```