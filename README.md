# python 多线程实例—简易的m3u8下载器

使用方式：

先pip 安装，pip install m3u8download-hecoter ，还要下载 ffmpeg 

然后 python 运行：

```
from m3u8download_hecoter import m3u8download
m3u8download(m3u8url='https://hls.videocc.net/4adf37ccc0/a/4adf37ccc0342e919fef2de4d02b473a_3.m3u8',title='9-第四节  民法典合同编及价格法（二）',work_dir='000',key='kQ2aSmyG1FDSmzpqTso/0w==',enable_del=False)

```



## 介绍

主要用来多线程下载文件，对m3u8链接进行了 解析、下载、解密、合并、删除等操作

支持windows,mac,linux

### 参数介绍

python 中使用时先安装m3u8download-hecoter : pip install m3u8download-hecoter

导入包：from m3u8download_hecoter import m3u8download

#### m3u8url (必填，其余参数全为非必填)

```
m3u8url = 'https://hls.cntv.myhwcdn.cn/asp/hls/2000/0303000a/3/default/363b41f09f6045a4ab95c7df387732bf/2000.m3u8'
 
 m3u8download(m3u8url)
```

#### title  

自定义视频名称

#### threads

线程数，默认16

#### key

视频解密时key，支持base64,hex格式，支持链接形式，支持本地文件链接形式

base64: 

```
m3u8download(m3u8url='https://hls.videocc.net/4adf37ccc0/a/4adf37ccc0342e919fef2de4d02b473a_3.m3u8',key='kQ2aSmyG1FDSmzpqTso/0w==')
```

hex:

```
m3u8download(m3u8url='https://hls.videocc.net/4adf37ccc0/a/4adf37ccc0342e919fef2de4d02b473a_3.m3u8',key='910d9a4a6c86d450d29b3a6a4eca3fd3')

```

链接：

```
key = 'http://******.key'
```

本地链接：

```
key = r"C:\Users\happy\Desktop\key.key"
```

#### iv

一般不需要自己填，自动解析，除非是 youku_AES

#### method

解密时对应的解密方法，当前支持 AES-128、SAMPLE-AES-CTR、KOOLEARN-ET、Widevine，一般不用更改，自动识别

```
m3u8download(m3u8url='https://hls.videocc.net/4adf37ccc0/a/4adf37ccc0342e919fef2de4d02b473a_3.m3u8',key='910d9a4a6c86d450d29b3a6a4eca3fd3',method='AES-128')
```

#### work_dir

工作目录，默认为当前目录下的 Downloads 文件夹

```
m3u8download(m3u8url='https://hls.videocc.net/4adf37ccc0/a/4adf37ccc0342e919fef2de4d02b473a_3.m3u8',key='910d9a4a6c86d450d29b3a6a4eca3fd3',work_dir='工作目录')
    
```

#### headers

自定义请求头，可以根据自己需要改

```
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030532) Edg/100.0.4896.60',
        'Cookie': '',
        'Connection': 'close',
        'referer':""
    }
    m3u8download(m3u8url='https://hls.videocc.net/4adf37ccc0/a/4adf37ccc0342e919fef2de4d02b473a_3.m3u8',key='910d9a4a6c86d450d29b3a6a4eca3fd3',work_dir='工作目录',headers=headers)

```

#### enable_del

删除除视频、音频之外的多余文件，默认为True，改为False之后可保留分片和解析的文件

```
m3u8download(m3u8url='https://hls.videocc.net/4adf37ccc0/a/4adf37ccc0342e919fef2de4d02b473a_3.m3u8',key='910d9a4a6c86d450d29b3a6a4eca3fd3',work_dir='工作目录',enable_del=False)
```

#### merge_mode

视频合并方式

```
merge_mode=1 为直接二进制合并
```

```
merge_mode=2 先二进制合并再 ffmpeg 转码
```

```
merge_mode=3 用ffmpeg 合并
```

默认为3

#### base_uri_parse

解析m3u8链接时用的网址前缀，一般可自动识别







