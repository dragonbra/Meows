import pandas as pd


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
    return newsTitle + newsContent


def channelNameWordToNum(channelNameList):
    targetDict = {"财经": 0, "房产": 1, "教育": 2, "科技": 3, "军事": 4, "汽车": 5, "体育": 6, "游戏": 7, "娱乐": 8, "其他": 9}
    size = len(channelNameList)
    for index in range(size):
        channelNameList[index] = targetDict[channelNameList[index]]
    return channelNameList


def readCorpus(filePath):
    """
    从excel文件中读取数据集
    数据集格式为：
    第一列 content 新闻文本
    第二列 channelName 新闻分类频道
    第三列 title 新闻标题
    :param filePath: 数据集所在路径，应该为.csv结尾
    :return: 两个列表，第一个为新闻内容的列表，第二个为新闻内容对应的分类，下标对应
    """
    channelNameList = []
    newsTitleList = []
    newsContentList = []

    try:
        dataFile = pd.read_excel(filePath, header=None)
        dataTable = dataFile.values
        for dataRow in dataTable:
            # dataRow[0] = content
            # dataRow[1] = channelName
            # dataRow[2] = title
            try:
                newsContent = dataRow[0]
                channelName = dataRow[1]
                newsTitle = dataRow[2]

                newsContentList.append(newsContent)
                channelNameList.append(channelName)
                newsTitleList.append(newsTitle)

            except Exception as e:
                print(e)
                continue

    except Exception as e:
        print(e)
        pass

    return channelNameList, newsTitleList, newsContentList
