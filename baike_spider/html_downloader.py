#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-08-17 10:23
# @Author  : YouSheng
import urllib2
class HtmlDownloader(object):
    def download(self, url):
        req = urllib2.Request(url)
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
        else:
            return response.read()



