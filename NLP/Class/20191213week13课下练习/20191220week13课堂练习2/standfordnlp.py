from stanfordcorenlp import StanfordCoreNLP

sentence = '我爱你.'

with StanfordCoreNLP(r'/usr/local/Cellar/stanford-corenlp/3.9.1/libexec', lang='zh') as nlp:
    print ('Tokenize:', nlp.word_tokenize(sentence))
    print ('Part of Speech:', nlp.pos_tag(sentence))
    print ('Named Entities:', nlp.ner(sentence))
    print ('Constituency Parsing:', nlp.parse(sentence))#语法树
    print ('Dependency Parsing:', nlp.dependency_parse(sentence))#依存句法