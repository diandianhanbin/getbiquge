# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : diandianhanbin@gmail.com
from bs4 import BeautifulSoup
import time
import requests
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
					datefmt='%a, %d %b %Y %H:%M:%S',
					filename='test.log',
					filemode='w')


def get_urls(url):
	"""
	从书本链接中获取文章详情的链接
	:param url: str, 书本的链接
	:return: list, 所有的章节url列表
	"""
	urls = []
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text, 'lxml')
	for x in soup.find_all('dd'):
		try:
			urls.append(url + x.a.get('href'))
		except Exception:
			logging.debug(x)
	return urls


def get_detail(charurl):
	"""
	从章节url中获取章节的内容
	:param charurl: 章节的url
	:return: None
	"""
	wb_data = requests.get(charurl)
	try:
		soup = BeautifulSoup(wb_data.text.encode('latin1').decode('gbk'), 'lxml')
		title = soup.find_all('div', class_='bookname')[0].find_all('h1')[0].text
		body = soup.find_all('div', id='content')[0].text
		print '======>>>>正在抓取{}的数据<<<========'.format(charurl)
		with open(title + '.txt', 'w') as f:
			f.write(title.encode('utf-8'))
			f.write('\n')
			for x in body.encode('utf-8').split('    '):
				if x == 'readx();':
					pass
				else:
					f.write(x)
					f.write('\n')
	except Exception as e:
		print '======>>>>{}的数据抓取失败<<<========'.format(charurl)
		logging.debug('网页解析失败: '+charurl)
		logging.debug(e)
	time.sleep(1)


def moreMulRun(bookurl):
	urls = get_urls(bookurl)
	pool = multiprocessing.Pool(processes=4)
	pool.map(get_detail, urls)


def slowRun(bookurl):
	for x in get_urls(bookurl):
		try:
			get_detail(x)
		except Exception as e:
			logging.debug('网页解析失败: ' + x)
		time.sleep(2)


if __name__ == '__main__':
	shuoming = '请选择想要爬取的类型:\n1.快速爬取(速度是慢速的4倍,偶尔出现内容爬取失败,顺序错乱等问题)\n2.慢速爬取(速度比较慢,爬取出错的情况较少,顺序不会错乱)\n'
	bookshuoming = '请输入书本的ID: \n'
	booknum = input(bookshuoming)
	runOperate = input(shuoming)
	url = 'http://www.biquge.la/book/{}/'.format(str(booknum))

	if runOperate == 1:
		moreMulRun(url)
	elif runOperate == 2:
		slowRun(url)
	else:
		print "输入错误,请检查输入的内容"