#coding:utf-8
import os,sys,time,json,urllib
path=os.path.split(os.path.realpath(sys.argv[0]))[0]

def load_config():
    jo=json.load(open(path+'/config.json'))
    return jo

def ping_sever(j):
    url=j['url']
    h='='*21+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'='*21+'\n' #log首行
    t='='*61+'\n'# log 尾行
    command = 'ping '+url+' -c '+str(jo['times'])  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.readlines()  # 读取命令行的输出到一个list
    if len(info)<2:
        return
    if j['log']:
        s = h
        for line in info:  # 按行遍历
            line = line.strip('\r\n')
            s = s + line + '\n'
        s=s+t
        w_log(s,'all-'+j['name']+'.log')
    s =h
    for l in info[-2:]:
        s=s+l
    s=s+t
    w_log(s,'ping-'+j['name']+'.log')
    return info[-2:]

def w_log(date,file):
    f=open(path+'/log/'+file,'a')
    f.write(date)
    f.close()

def send(text,desp):
    SCKEY=jo['SCKEY']
    text=urllib.quote(text.encode('utf-8'))
    desp=urllib.quote(desp.encode('utf-8'))
    urllib.urlopen('http://sc.ftqq.com/'+SCKEY+'.send?text='+text+'&desp='+desp)


jo=load_config()
for l in jo['host']:
    try:
        list_ping = ping_sever(l)
        str_ping_loss = list_ping[0].split(', ')[2]
        int_ping_loss = int(str_ping_loss[:str_ping_loss.find('%')])  # 获取丢包率
        if int_ping_loss > l['loss']:
            send(l['name'] + u'-丢包率过高', u'丢包率为' + str(int_ping_loss)+'%')
    except:
        send(l['name'] + u'-无法ping通', u'请检查设置，地址为 '+l['url'])