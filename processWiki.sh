#! /bin/bash
# 提取文本
python3.7 process_wiki.py zhwiki-20190520-pages-articles2.xml-p162888p544640.bz2 zhwiki.txt
# 繁体字转简体字
opencc -i zhwiki.txt -o zhwiki_chs.txt -c t2s.json
# 分词
python3.7 WordSeg.py