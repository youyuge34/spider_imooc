#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-08-17 10:23
# @Author  : YouSheng
class UrlManager(object):
    """
    Url管理器，维护两个url的列表
    """
    def __init__(self):
        self.newUrls = set()  # 待爬取的列表
        self.oldUrls = set()  # 爬取过的列表

    def addNewUrl(self, url):
        if url is None or url == '':
            return
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    def addNewUrls(self, parsedUrls):
        if parsedUrls is None or len(parsedUrls) == 0:
            return
        for url in parsedUrls:
            self.addNewUrl(url)

    def hasNewUrl(self):
        return len(self.newUrls) != 0

    def getNewUrl(self):
        newUrl = self.newUrls.pop()
        self.oldUrls.add(newUrl)
        return newUrl
