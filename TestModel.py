from gensim.models import Word2Vec
from six import iteritems, itervalues, string_types
import logging

word2vec_model = Word2Vec.load('wiki_chs.model')
logger = logging.getLogger()

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
   

testwords = ['1', '2', '上海', 'China', 'War', '足球', '中国', 'football', '西门子', 'city', '耳朵', 'as', 'good', 'well', 'done', 'sea', 'full']
for i in testwords:
    
    try:
        res = word2vec_model.wv.most_similar(i, topn=5)
        print (i)
        print (res)
        pass
    except BaseException as identifier:
        print('got error!', i, ', exp:', identifier)
        pass
    else:
        print('got pass!', i)
        pass
    
sim1 = word2vec_model.wv.similarity(u'男朋友', u'女朋友')
sim2 = word2vec_model.wv.similarity(u'学弟', u'学长')
sim3 = word2vec_model.wv.similarity(u'美国', u'中国')
sim4 = word2vec_model.wv.similarity(u'计算机', u'线程')
print(sim1)
print(sim2)
print(sim3)
print(sim4)
