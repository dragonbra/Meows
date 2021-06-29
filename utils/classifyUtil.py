import torch
from bert_seq2seq.utils import load_bert
from bert_seq2seq.tokenizer import Tokenizer, load_chinese_base_vocab
from config import Const
from utils import dataProcUtil


class Classifier:
    """
    新闻分类器，读取预训练好的bert的model，用于预测该赛题的10分类
    """
    target = ["财经", "房产", "教育", "科技", "军事", "汽车", "体育", "游戏", "娱乐", "其他"]

    def __init__(self, MODEL_PATH=Const.MODEL_PATH, MODEL_DICT_PATH=Const.MODEL_DICT_PATH):
        self.MODEL_PATH = MODEL_PATH
        self.MODEL_DICT_PATH = MODEL_DICT_PATH
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print("当前设备使用:", self.device)

        # 加载字典
        self.word2idx = load_chinese_base_vocab(self.MODEL_DICT_PATH, simplfied=False)
        self.tokenizer = Tokenizer(self.word2idx)

        # 定义模型
        self.bert_model = load_bert(self.word2idx, model_name="roberta", model_class="cls",
                                    target_size=len(self.target))
        self.bert_model.set_device(self.device)
        self.bert_model.eval()

        # 加载训练的模型参数
        self.bert_model.load_all_params(model_path=self.MODEL_PATH, device=self.device)

        # 预测一次方便后续加速
        self.predict("Hello Meow")

    def predict(self, newsTextOri):
        newsTextList = dataProcUtil.newsCut(newsTextOri)
        other = 9
        resCountList = [0 for i in range(10)]

        for newsText in newsTextList:
            with torch.no_grad():
                newsTextPresentedInBert, newsTextIds = self.tokenizer.encode(newsText)
                newsTextPresentedInBert = torch.tensor(newsTextPresentedInBert, device=self.device).view(1, -1)
                try:
                    preRes = torch.argmax(self.bert_model(newsTextPresentedInBert)).item()
                    resCountList[preRes] += 1
                except Exception as e:
                    print(e)
                    resCountList[other] += 1

        maxCount = 0
        maxNum = 0
        res = 0
        for i in range(10):
            resCount = resCountList[i]
            if resCount > maxCount:
                res = i
                maxCount = resCount
                maxNum = 1
            elif resCount == maxCount:
                maxNum += 1

        return self.target[res]
