import jieba.analyse
import codecs
import re
import time

## 去除停用词的2个函数
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [
        line.strip() for line in open(filepath, "r", encoding="utf-8").readlines()
    ]
    return stopwords


# 对句子去除停用词
def movestopwords(sentence):
    stopwords = stopwordslist("./stopwords/s1.txt")  # 这里加载停用词的路径
    stopwords.append(stopwordslist("./stopwords/s2.txt"))
    stopwords.append(stopwordslist("./stopwords/s3.txt"))
    stopwords.append(stopwordslist("./stopwords/s4.txt"))

    outstr = ""
    for word in sentence:
        if word not in stopwords:
            if word != "\t" and "\n":
                outstr += word
                # outstr += " "
    return outstr


# 以写的方式打开原始的简体中文语料库
f = codecs.open("zhwiki_chs.txt", "r", encoding="utf8")
# 将分完词的语料写入到 wiki_chs_seg.txt文件中
target = codecs.open("wiki_chs_seg.txt", "w", encoding="utf8")

print("open files")
line_num = 1
line = f.readline()

# 循环遍历每一行，并对这一行进行分词操作
# 如果下一行没有内容的话，就会readline会返回-1，则while -1就会跳出循环

# stopwords = stopwordslist('./stopwords/百度停用词表.txt')  # 这里加载停用词的路径
stopwords = stopwordslist("./stopwords/s1.txt")  # 这里加载停用词的路径
stopwords.append(stopwordslist("./stopwords/s2.txt"))
stopwords.append(stopwordslist("./stopwords/s3.txt"))
stopwords.append(stopwordslist("./stopwords/s4.txt"))

while line:
    print("---- processing ", line_num, " article----------------\n")
    # print(line)
    # print('===start===')
    # time.sleep(5)

    for i in re.sub("[a-zA-Z0-9]", "", line).split(" "):
        # print('===sub===\n', i)
        if i != "":
            line_seg = jieba.cut(i)
            # print('===segs===\n', line_seg)
            listcontent = ""
            for word in line_seg:
                if word in stopwords or word == "\n" or word == "\t":
                    continue
                listcontent += word
                listcontent += " "

            # print('===words===\n', listcontent)
            if listcontent != "":
                listcontent += "\n"
                target.writelines(listcontent)

    # print("去除停用词前：", line_seg)
    # print("去除停用词后：", listcontent)

    line_num = line_num + 1
    line = f.readline()

# 关闭两个文件流，并退出程序
f.close()
target.close()
exit()

