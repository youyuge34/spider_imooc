#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-08-17 10:23
# @Author  : YouSheng
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collectData(self, parsedData):
        if (parsedData is not None):
            self.datas.append(parsedData)

    def output(self):
        try:
            fout = open('output.html', 'w')
            fout.write('<html>')
            fout.write('<body>')
            # 数据集输出成表格形式
            fout.write('<table>')

            for data in self.datas:
                fout.write('<tr>')
                fout.write('<td>%s</td>' % data['url'].encode('utf-8'))
                fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
                fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
                fout.write('</tr>')

            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')
            fout.close()
        except IOError as e:
            print e.message

