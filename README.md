# 爬取笔趣阁小说

## 功能说明

脚本能够爬取[笔趣阁(http://www.biquge.la/)](http://www.biquge.la/)的所有小说.

爬取的时候,需要输入爬取的书本ID和爬取方式.

## 相关依赖

脚本依赖的第三方库为`BeautifulSoup`和`requests`.如果你的电脑没有安装,请打开终端,执行以下命令:

* 安装BS4

`pip install beautifulsoup4`

* 安装解析器

`pip install lxml`

* 安装requests

`pip install requests`

如果安装报错权限不足,请在命令前加上`sudo`

## 书本ID

书本ID的获取方式如下图

![书本ID](http://7xsgl3.com1.z0.glb.clouddn.com//201609041556.png )

笔趣阁中每本书都会有书本ID,此为必填项,**填错有可能导致程序无法运行**

## 爬取方式

两种方式各有优缺点,请使用者自行选择

* 慢速爬取

慢速爬取为单线程爬取,且每次爬取会停止1秒钟,这种方式爬取能够保证爬取内容的顺序是按照书本顺序来执行,并且不容易出现空内容,网页无法爬取等bug.

* 快速爬取

快速爬取使用多线程爬取,开启4个线程进行爬取数据,这种方式爬取速度快,但偶尔会出现解码错误等bug,并且这种方式会导致顺序错乱.

## 爬取结果

爬取后的结果会按照章节的名称放在脚本的当前目录中

## 日志记录

所有爬取动作都会在日中中以Debug的方式记录.

>Sun, 04 Sep 2016 16:00:12 connectionpool.py[line:387] DEBUG "GET /book/21065/7913976.html HTTP/1.1" 200 None
Sun, 04 Sep 2016 16:00:12 connectionpool.py[line:387] DEBUG "GET /book/21065/7913979.html HTTP/1.1" 200 10889
Sun, 04 Sep 2016 16:00:12 connectionpool.py[line:387] DEBUG "GET /book/21065/7913981.html HTTP/1.1" 200 9299
Sun, 04 Sep 2016 16:00:12 connectionpool.py[line:387] DEBUG "GET /book/21065/7913983.html HTTP/1.1" 200 11299
Sun, 04 Sep 2016 16:00:13 connectionpool.py[line:207] INFO Starting new HTTP connection (1): www.biquge.la
Sun, 04 Sep 2016 16:00:13 connectionpool.py[line:207] INFO Starting new HTTP connection (1): www.biquge.la
Sun, 04 Sep 2016 16:00:13 connectionpool.py[line:207] INFO Starting new HTTP connection (1): www.biquge.la
Sun, 04 Sep 2016 16:00:13 connectionpool.py[line:207] INFO Starting new HTTP connection (1): www.biquge.la

爬取失败的网页也会在此记录,可以查看到爬取失败的原因以及爬取失败的网页地址

## 效果演示

![爬取效果演示](http://7xsgl3.com1.z0.glb.clouddn.com//201609041601.png )

![爬取效果演示](http://7xsgl3.com1.z0.glb.clouddn.com//201609041603.png )
