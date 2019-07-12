#! /bin/bash
# 提取文本
python3.7 process_wiki.py ./source/zhwiki-20190520-pages-articles2.xml-p162888p544640.bz2 ./source/zhwiki.txt
# 繁体字转简体字
opencc -i ./source/zhwiki.txt -o ./source/zhwiki_chs.txt -c t2s.json
# 分词
python3.7 WordSeg.py