import pandas as pd

if __name__ == '__main__':
    channelNameList = []
    newsTitleList = []
    newsContentList = []
    try:
        dataFile = pd.read_csv('D:\\GitHub\\NewsClassifier\\resources\\example\\traindata.csv', error_bad_lines=False)
        dataTable = dataFile.values
        for dataRow in dataTable:
            # dataRow = dataTable[_]
            # dataRow[0] = content
            # dataRow[1] = channelName
            # dataRow[2] = title
            try:
                newsContent = dataRow[1]
                channelName = dataRow[0]
                newsTitle = newsContent[0:20]

                newsContentList.append(newsContent)
                channelNameList.append(channelName)
                newsTitleList.append(newsTitle)

            except Exception as e:
                print(e)
                continue
    except Exception as e:
        print(e)
        pass

    output_excel = {'content': newsContentList, 'channelName': channelNameList, 'title': newsTitleList}
    output = pd.DataFrame(output_excel)
    output.to_csv('./data.csv', index=False, encoding="utf_8_sig", header=None)
