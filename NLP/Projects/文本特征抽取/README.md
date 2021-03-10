## 文本特征抽取项目 ##

**项目名称：** 完整版本文本特征抽取

**项目要求：**[详情参见本链接](https://github.com/superxiaoqiang/blcu_py_nlp/blob/master/ch11_Python_Advanced6_NLP_1.md)

**项目功能：**

类似于 Coh-Metrix 的简略版 Mini-Metrix

#### Coh-Metrix功能分析 ####
- Descriptive模块（描述性指标）
  - DESPC（段落数）
  - DESSC（句子数）
  - DESWC（字数）
  - DESPL（平均段落长度）
  - DESPLd（段落平均长度的标准差）
  - DESSL（句子平均长度）
  - DESSLd（句子平均长度的标准差）
  - DESWLsy（单词的平均音节数）
  - DESWLsyd（单词的平均音节数的标准差）
  - DESWLlt（单词中的平均字母数）
  - DESWLltd（单词平均字母数的标准偏差）
- Text Easability Principal Component Scores模块（文本易用性）
  - PCNARz（叙述性）叙述性文本讲述故事
  - PCNARp
  - PCSYNz（语法简洁性）文本中句子包含较少单词并使用更为简单、熟悉的句法结构的程度。
  - PCSYNp
  - PCCNCz（单词具体性）具体有意义的单词
  - PCCNCp
  - PCREFz（参照凝聚力）高凝聚力的文本集中体现思想，低凝聚力的文本通常更难以处理
  - PCREFp
  - PCDCz（深度内聚）因果关系和逻辑关系
  - PCDCp
  - PCVERBz（动词衔接）文本中动词重叠的程度
  - PCVERBp
  - PCCONNz（连接性）文本中包含明确的对抗性，加性和比较性连接词以表达文本中的关系的程度
  - PCCONNp
  - PCTEMPz（时间）包含更多关于时间性的线索并且具有更一致的时间性（即时态，方面）的文本更易于处理和理解
  - PCTEMPp
- Referential Cohesion（参照内聚）本地句子或共指之间内容词的重叠
  - CRFNO1（相邻名词重叠）
  - CRFNOa（全局重叠）
  - CRFAO1（参数重叠）当一个句子中的名词与另一句子中的相同名词（单数或复数形式）重叠时，就会发生参数重叠
  - CRFAOa
  - CRFSO1
  - CRFSOa
  - CRFCWO1（内容词重叠）句子对之间重叠的显式内容词的比例
  - CRFCWO1d
  - CRFCWOa
  - CRFCWOad
  - CRFANP1（照应重叠）成对句子之间的前向重叠
  - CRFANPa
- Latent Semantic Analysis（潜在语义分析）提供了句子之间或段落之间语义重叠的度量
  - LSASS1（LSA相邻）
  - LSASS1d
  - LSASSp
  - LSASSpd
  - LSAPP1
  - LSAPP1d
  - LSAGN
  - LSAGNd
- Lexical Diversity（词汇多样性）
  - LDTTRc（令牌比率）
  - LDTTRa（键入所有单词的标记率）
  - LDMTLDa（MTLD词汇多样性度量）
  - LDVOCDa（VOC词汇多样性）
- Connectives（连接词）连接词在概念和子句之间的紧密联系的建立中起着重要作用
  - CNCAll（所有连接词）
  - CNCCaus（因果连接词）
  - CNCLogic（逻辑连接词）
  - CNCADC（对比性连接词）
  - CNCTemp
  - CNCTempx（拓展的实践性连接词）
  - CNCAdd（加法连接词）
  - CNCPos（积极性）
  - CNCNeg（消极性）
- Situation Model（情况模型）使用情境模型
  - SMCAUSv（因果动词的发生率）
  - SMCAUSvp（因果内容）
  - SMINTEp
  - SMCAUSr
  - SMINTEr 
  - SMCAUSlsa
  - SMCAUSwn
  - SMTEMP
- Syntactic Complexity（句法复杂性）
  - SYNLE（主要动词之前的词）
  - SYNNP（每个NP的修饰词）
  - SYNMEDpos（这是根据部分语音标签计算出的相邻句子之间的平均最小编辑距离得分）
  - SYNMEDwrd（这是从单词计算出的相邻句子之间的最小编辑距离得分）
  - SYNMEDlem（这是引理中相邻句子之间的最小编辑距离得分。）
  - SYNSTRUTa（语法结构相似性相邻）
  - SYNSTRUTt（语法结构相似性全部为01）
- Syntactic Pattern Density（句法模式密度）
  - DRNP（名词短语发生率）
  - DRVP（动词短语发生率）
  - DRAP（副词短语发生率）
  - DRPP（介词短语发生率）
  - DRPVAL
  - DRNEG（否定表达发生率）
  - DRGERUND（动名词发生率）
  - DRINF（不定式发生率）
- Word Information
  - WRDNOUN（名词出现的分数）
  - WRDVERB（动词出现的分数）
  - WRDADJ（形容词出现的分数）
  - WRDADV（副词出现的分数）
  - WRDPRO（人称代词）
  - WRDPRP1s（第一人称代词单数）
  - WRDPRP1p（第一人称代词复数）
  - WRDPRP2（第二人称代词）
  - WRDPRP3s（第三人称代词单数）
  - WRDPRP3p（第三人称代词复数）
  - WRDFRQc（内容词的平均词频）
  - WRDFRQa（所有词的平均单词频率）
  - WRDFRQmc（句子中品骏最小单词频率）
  - WRDAOAc（获取年龄）
  - WRDFAMc（成年人对于单词的熟悉程度）
  - WRDCNCc（具体性）一个单词具体程度和抽象程度的指标
  - WRDIMGc（想象力）
  - WRDMEAc（意义）
  - WRDPOLc（一词多义的数量）
- Readability
  - Flesch Reading Ease：RDFRE（Flesch Reading Ease公式的输出是0到100之间的数字，得分越高表示阅读越容易。平均文档的Flesch Reading Ease分数在6到70之间）
  - RDFKGL（这个更常见的Flesch-Kincaid年级水平公式将“阅读难易度分数”转换为美国年级学校水平。数字越高，阅读文本越困难。等级范围为0到12。）
  
### 第一阶段：Descriptive模块 ###

**项目成员：**
- 段落处理及其描述：杨澜
- 句子处理及其描述：张伊晗
- 单词处理及其描述：杨瑞霞
要求：中文英文皆可处理

**文件构成：**

| 文件名| 函数名 | 说明 | 
| :--- | :--- | :--- | 
| Descriptive_Paragraph | 1.DESPC（段落数）2.DESPL（平均段落长度）3.DESPLd（段落平均长度的标准差） | 参考官方网页 |
| Descriptive_sentence | 1.DESSC（句子数）2.DESSL（句子平均长度）3.DESSLd（句子平均长度的标准差）| 参考官方网页 |
| Descriptive_words | 1.DESWC（字数）2.DESWLlt（单词中的平均字母数）3.DESWLltd（单词平均字母数的标准偏差） | 参考官方网页 |
| main.py | 主函数 | 读取文章，可通过段落数，句子数和单词数对齐进行描述，输出上述指标到txt文件对描述结果进行保存 |

**目前遇到的问题**
无法使用该项目的网络版，不知道输出结果格式。
