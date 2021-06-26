import torch
import traceback
from tqdm import tqdm
from bert_seq2seq.tokenizer import Tokenizer, load_chinese_base_vocab
from bert_seq2seq.utils import load_bert
import dataProcessUtils


# target = ["财经", "彩票", "房产", "股票", "家居", "教育", "科技", "社会", "时尚", "时政", "体育", "星座", "游戏", "娱乐"]
target = ["财经", "房产", "教育", "科技", "军事", "汽车", "体育", "游戏", "娱乐", "其他"]
targetDict = {"财经":0, "房产":1, "教育":2, "科技":3, "军事":4, "汽车":5, "体育":6, "游戏":7, "娱乐":8, "其他":9}

# data_path = "./corpus/新闻标题文本分类/Train.txt"
data_path = './corpus/新闻标题文本分类/news.xlsx'
sents_src, sents_tgt = dataProcessUtils.readCorpus(data_path)

size = len(sents_src)  # 75w新闻标题
totalNum = [0 for i in range(10)]
acNum = [0 for i in range(10)]
waNum = [0 for i in range(10)]
waDesNum = [0 for i in range(10)]

cls_model = "./state_dict/recentlyTrained.bin"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if __name__ == "__main__":
    vocab_path = "./state_dict/roberta_wwm_vocab.txt"  # roberta模型字典的位置
    model_name = "roberta"  # 选择模型名字
    # 加载字典
    word2idx = load_chinese_base_vocab(vocab_path, simplfied=False)
    tokenizer = Tokenizer(word2idx)
    # 定义模型
    bert_model = load_bert(word2idx, model_name=model_name, model_class="cls", target_size=len(target))
    bert_model.set_device(device)
    bert_model.eval()
    ## 加载训练的模型参数～
    bert_model.load_all_params(model_path=cls_model, device=device)

    for i in tqdm(range(size)):
        text = sents_src[i]
        ans = sents_tgt[i]

        totalNum[ans] += 1

        with torch.no_grad():
            text, text_ids = tokenizer.encode(text)
            text = torch.tensor(text, device=device).view(1, -1)
            try:
                res = torch.argmax(bert_model(text)).item()
                if res == ans:
                    acNum[ans] += 1
                else:
                    waNum[ans] += 1
                    waDesNum[res] += 1
                # if (acNum + waNum) % 2000 == 0:
                #     print()
                #     print("AC:", acNum)
                #     print("WA:", waNum)
            except:
                traceback.print_exc()

    print("Accuracy: ", sum(acNum), " / ", size)
    print(sum(acNum) / size)

    for i in range(10):
        totalNum[i] += 1
        print(target[i], " 该分类原有: ", totalNum[i])
        print("正确分类：",acNum[i],"错误分类：",waNum[i],"被错误分到此类：",waDesNum[i])
        print("该类recall：",acNum[i] / totalNum[i])
        print("该类precision：",acNum[i] / (acNum[i] + waDesNum[i]))
        print()