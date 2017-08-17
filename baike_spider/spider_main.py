#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-08-17 10:13
# @Author  : YouSheng

import url_manager
import html_downloader
import html_outputer
import html_parser


class SpiderMain(object):
    """
    爬虫的总调度器类
    """

    def __init__(self):
        """
        构造函数初始化URL管理器、下载器、解析器、输出器模块
        """
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        """
        爬虫的调度方法
        :param root_url:
        :return:
        """
        mCount = 1
        self.urls.addNewUrl(root_url)  # 添加新url
        while self.urls.hasNewUrl():  # 如果管理池中有新的url就进行爬
            try:
                newUrl = self.urls.getNewUrl()  # 获取新的url
                print 'craw %d : %s' % (mCount, newUrl)
                html = self.downloader.download(newUrl)  # 下载器下载得到html
                parsedUrls, parsedData = self.parser.parse(newUrl, html)  # 解析器解析html，得到更多的urls和有用的数据
                self.urls.addNewUrls(parsedUrls)  # 将解析出的urls添加进管理池中
                self.outputer.collectData(parsedData)  # 输出器记录下信息
                if (mCount == 10):
                    break
                mCount += 1
            except:
                print 'craw error'

        self.outputer.output()  # 输出结果


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python'
    mSpider = SpiderMain()
    mSpider.craw(root_url)
