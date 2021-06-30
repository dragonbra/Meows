import os
import pandas as pd

if __name__ == '__main__':
    filePath = 'D:\\训练集\\'
    files = os.listdir(filePath)

    channelNameList = []
    newsTitleList = []
    newsContentList = []

    dataTable = pd.DataFrame()
    for fileName in files:
        fileName = filePath + fileName
        try:
            dataFile = pd.ExcelFile(fileName)
            # 显示出读入excel文件中各个sheet表的名字
            sheet_names = dataFile.sheet_names

            sheetNames = dataFile.sheet_names

            for sheet in sheetNames:
                df_sheet = pd.read_excel(fileName, sheet_name=sheet, header=None)
                # print(len(df_sheet))
                dataTable = pd.concat([dataTable, df_sheet], ignore_index=True)
                # print(len(dataTable))

            print(len(dataTable))
            # dataTable.to_excel(fileName, index=False, encoding="utf_8_sig", header=None)
            # for dataRow in dataTable:
            #     # dataRow[0] = content
            #     # dataRow[1] = channelName
            #     # dataRow[2] = title
            #     # print(dataRow)
            #     try:
            #         newsContent = dataRow[0]
            #         channelName = dataRow[1]
            #         newsTitle = dataRow[2]
            #
            #         newsContentList.append(newsContent)
            #         channelNameList.append(channelName)
            #         newsTitleList.append(newsTitle)
            #
            #     except Exception as e:
            #         print(e)
            #         continue
        except Exception as e:
            print(e)
            pass
    try:
        print(len(newsTitleList))
        output_excel = {'content': newsContentList, 'channelName': channelNameList, 'title': newsTitleList}
        output = pd.DataFrame(output_excel)
        output.to_csv('./data.csv', index=False, encoding="utf_8_sig", header=None)
        dataTable.to_csv('./data.csv', index=False, encoding="utf_8_sig", header=None)
    except Exception as e:
        print(e)

