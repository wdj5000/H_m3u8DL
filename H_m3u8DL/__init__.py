import json,sys,os
import time,base64
from H_m3u8DL import parser,download,merge,delFile,idm5,decrypt
from argparse import ArgumentParser

version_now = '0.1.9'

def m3u8download(m3u8url, title='',base_uri_parse='',threads=16, key=None, iv=None, method=None, work_dir='./Downloads', headers=None,enable_del=True,merge_mode=3,proxy=None):

    # 构造m3u8下载信息
    # list: m3u8url = [{'m3u8url':m3u8url,'title':title},{'m3u8url':m3u8url,'title':title}]

    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030532) Edg/100.0.4896.60',
            'Cookie': '',
            'Connection': 'close'
        }
    if type(proxy) == str:
        proxies = {'http':proxy}
    elif type(proxy) == json:
        proxies = proxy
    else:
        proxies = None
    if '.mp4' in m3u8url and 'm3u8' not in m3u8url:
        idm5.download(url=m3u8url, save_name=title if '.mp4' in title else title + '.mp4')

    else:
        if type(m3u8url) == list:
            for info in m3u8url:

                m3u8download(m3u8url=info['m3u8url'], title=info['title'],base_uri_parse=info['base_uri_parse'],enable_del=info['enable_del'],merge_mode=info['merge_mode'],headers=info['headers'],work_dir=info['work_dir'],method=info['method'],key=info['key'],proxy=info['proxy'])

            sys.exit(0)
        # dir: m3u8url = r'c:\windows\'

        elif os.path.isdir(m3u8url):
            for root, dirs, files in os.walk(m3u8url):
                for f in files:
                    file = os.path.join(root, f)
                    if os.path.isfile(file):
                        if file.split('.')[-1] == 'm3u8':
                            m3u8download(m3u8url=file,key=key,title=title,base_uri_parse=base_uri_parse,enable_del=enable_del,merge_mode=merge_mode,headers=headers,work_dir=work_dir,method=method,proxy=proxies)
            sys.exit(0)
        # txt 文件中 title,m3u8url  一行一个链接
        elif os.path.isfile(m3u8url):
            if m3u8url[-4:] == '.txt':
                with open(m3u8url,'r',encoding='utf-8') as f:
                    m3u8texts = f.read()
                list_m3u8text = m3u8texts.split('\n')
                for m3u8text in list_m3u8text:
                    m3u8texts = m3u8text.split(',')
                    title = m3u8texts[0]
                    m3u8url = m3u8texts[1]
                    if len(m3u8texts) >= 3:
                        key = m3u8texts[2]
                    m3u8download(m3u8url=m3u8url,key=key,title=title,base_uri_parse=base_uri_parse,enable_del=enable_del,merge_mode=merge_mode,headers=headers,work_dir=work_dir,method=method,proxy=proxies)
                sys.exit(0)
        WideVine = ['SAMPLE-AES-CTR', 'cbcs', 'SAMPLE-AES']

        title, durations, count, temp_dir, data, method,enable_del,merge_mode,key = parser.Parser(m3u8url, title,base_uri_parse,method=method, key=key, iv=iv,work_dir=work_dir, headers=headers,enable_del=enable_del,merge_mode=merge_mode).run()

        tm = time.strftime("%H:%M:%S", time.gmtime(durations))
        print(title, tm,f'method:{method}')
        segments = json.loads(data)['segments']

        infos = []
        for segment in segments:
            name = segment['title'] + '.ts'
            info1 = {
                'title': temp_dir + '/video/' + name,
                'link': segment['uri'],
                'proxies':proxies
            }

            if 'key' in segment or method != None:

                info1['method'] = method
                if method == 'copyrightDRM':
                    info1['key'] = key
                    info1['iv'] = key

                    decrypt.decrypt_copyrightDRM(m3u8url,title,key)
                    print('调用执行完成')
                    sys.exit(0)

                elif method in WideVine:
                    info1['key'] = key
                    info1['iv'] = key
                else:
                    info1['key'] = base64.b64decode(segment['key']['uri'])
                    info1['iv'] = bytes.fromhex(segment['key']['iv'])
            infos.append(info1)

        download.FastRequests(infos, threads=threads, headers=headers).run()  # 下载

        # 下载完成，开始合并

        merge.Merge(temp_dir, mode=merge_mode)

        if method in WideVine:
            decrypt.decrypt2(temp_dir, key)
        # 删除多余文件
        if enable_del:
            delFile.del_file(temp_dir)
        print()

def main(argv=None):
    parser = ArgumentParser(
        prog=f"version {version_now}",
        description=("一个python写的m3u8流视频下载器,适合全平台,https://github.com/hecoter/H_m3u8DL")
    )

    parser.add_argument("m3u8url", default='', help="链接、本地文件链接、文件夹链接、txt文件")
    parser.add_argument("-title", default='', help="视频名称")
    parser.add_argument("-base_uri_parse", default='', help="解析时的baseuri")
    parser.add_argument("-threads", default=16, help='线程数')
    parser.add_argument("-key", default=None, help='key')
    parser.add_argument("-iv", default=None, help='iv')
    parser.add_argument("-method", default=None, help='解密方法')
    parser.add_argument("-work_dir", default='./Downloads', help='工作目录')
    parser.add_argument("-headers", default=None, help='请求头')
    parser.add_argument("-enable_del", default=True, help='下载完删除多余文件')
    parser.add_argument("-merge_mode", default=3, help='1:二进制合并，2：二进制合并完成后用ffmpeg转码，3：用ffmpeg转码')
    parser.add_argument("-proxy", default=None, help='代理：127.0.0.1:8888')
    args = parser.parse_args(argv)

    if args.m3u8url == '':
        parser.print_help()
    else:
        m3u8download(m3u8url=args.m3u8url, title=args.title, base_uri_parse=args.base_uri_parse, threads=args.threads, key=args.key, iv=args.iv, method=args.method,work_dir=args.work_dir, headers=args.headers, enable_del=args.enable_del, merge_mode=args.merge_mode, proxy=args.proxy)


if __name__ == '__main__':
    main()
    # m3u8download(m3u8url='https://hls.videocc.net/4adf37ccc0/a/4adf37ccc0342e919fef2de4d02b473a_3.m3u8',key='910d9a4a6c86d450d29b3a6a4eca3fd3',work_dir='工作目录',enable_del=False,proxy='127.0.0.1')


