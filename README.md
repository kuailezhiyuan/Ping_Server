# ping_server
一个用来检测丢包率的小程序，通过ping来实现

##配置config.json
host里可添加多个服务器信息，
SCKEY是Sever酱推送信息到微信，详情查看<http://www.kpro.xyz/archives/89>
times是ping的次数10
loss是丢包率超过多少通过Sever酱推送报警

可通过Crontab定时执行
