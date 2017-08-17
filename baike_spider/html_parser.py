#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-08-17 10:23
# @Author  : YouSheng

import re
from bs4 import BeautifulSoup
import urlparse


class HtmlParser(object):
    def parse(self, url, html):
        """
        html页面解析
        :param url:
        :param html:
        :return: 新的待爬url列表，有用的数据集
        """
        if url is None or html is None:
            return

        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        newUrls = self._getNewUrls(url, soup)
        newData = self._getNewData(url, soup)
        return newUrls, newData

    def _getNewUrls(self, page_url, soup):
        mUrlSet = set()
        # <a target="_blank" href="/item/C/7252092" data-lemmaid="7252092">C</a>
        links = soup.find_all('a', href=re.compile(r'/item/(.*)'))
        for link in links:
            newHref = link['href']
            mUrlSet.add(urlparse.urljoin(page_url, newHref))
        return mUrlSet

    def _getNewData(self, url, soup):
        dataDict = {"url" : str(url).strip()}
        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        if title.get_text() is not None:
            dataDict['title'] = title.get_text()
        else:
            dataDict['title'] = 'title is none'

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary = soup.find('div',class_='lemma-summary')
        if summary.get_text() is not None:
            dataDict['summary'] = summary.get_text()
        else:
            dataDict['summary'] = 'summary is None'
        return dataDict