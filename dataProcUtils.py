import traceback

import pandas as pd
import torch
import tqdm
from bert_seq2seq.utils import load_bert
from bert_seq2seq.tokenizer import Tokenizer, load_chinese_base_vocab


def newsCut(text, length=500):
    """
    字符串分割，将字符串按某一长度进行分割
    :param text: 输入字符串
    :param length: 分割字符串长度
    :return: 分割成的字符串列表
    """
    textList = [text[i:i + length] for i in range(0, len(text), length)]
    return textList


def newsMerge(newsTitle, newsContent):
    return newsTitle + "。" + newsContent


def readCorpus(dataPath):
    """
    从excel文件中读取数据集
    数据集格式为：
    第一列 content 新闻文本
    第二列 channelName 新闻分类频道
    第三列 title 新闻标题
    :param dataPath: 数据集所在路径，应该为.csv结尾
    :return: 两个列表，第一个为新闻内容的列表，第二个为新闻内容对应的分类，下标对应
    """
    targetDict = {"财经": 0, "房产": 1, "教育": 2, "科技": 3, "军事": 4, "汽车": 5, "体育": 6, "游戏": 7, "娱乐": 8, "其他": 9}
    newsList = []
    newsClassList = []

    dataFile = pd.read_excel(dataPath)
    tables = dataFile.values
    for dataRow in tables:
        # dataRow[0] = content
        # dataRow[1] = channelName
        # dataRow[2] = title
        try:
            newsClass = targetDict[dataRow[1]]  # 将标签转化为对应的数字label

            newsText = str(dataRow[2]) + str(dataRow[0])
            newsText.strip()
            newsText = newsCut(newsText)

            for news in newsText:
                newsList.append(news)
                newsClassList.append(newsClass)

        except Exception:
            continue

    return newsList, newsClassList


class Classifier:
    """
    新闻分类器，读取预训练好的bert的model，用于预测该赛题的10分类
    """
    target = ["财经", "房产", "教育", "科技", "军事", "汽车", "体育", "游戏", "娱乐", "其他"]
    cls_model = "./model/ClassifyModel.bin"
    vocab_path = "./model/roberta_wwm_vocab.txt"  # roberta模型字典的位置
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def __init__(self):
        # 加载字典
        self.word2idx = load_chinese_base_vocab(self.vocab_path, simplfied=False)
        self.tokenizer = Tokenizer(self.word2idx)

        # 定义模型
        self.bert_model = load_bert(self.word2idx, model_name="roberta", model_class="cls",
                                    target_size=len(self.target))
        self.bert_model.set_device(self.device)
        self.bert_model.eval()

        # 加载训练的模型参数
        self.bert_model.load_all_params(model_path=self.cls_model, device=self.device)

        # 预测一次方便后续加速
        self.predict("Hello world.")

    def predict(self, newsTextOri):
        newsTextList = newsCut(newsTextOri)
        other = 9
        resCountList = [0 for i in range(10)]

        for newsText in newsTextList:
            with torch.no_grad():
                newsTextPresentedInBert, newsTextIds = self.tokenizer.encode(newsText)
                newsTextPresentedInBert = torch.tensor(newsTextPresentedInBert, device=self.device).view(1, -1)
                try:
                    preRes = torch.argmax(self.bert_model(newsTextPresentedInBert)).item()
                    resCountList[preRes] += 1
                except Exception:
                    resCountList[other] += 1

        maxCount = 0
        maxNum = 0
        res = 0
        for i in range(10):
            resCount = resCountList[i]
            if resCount > maxCount:
                res = i
                resCount = maxCount
                maxNum = 1
            elif resCount == maxCount:
                maxNum += 1

        return self.target[res]
