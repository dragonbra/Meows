import sqlite3
from config import Const


class DataBase:

    def __init__(self, DATABASE_PATH=Const.DATABASE_PATH, TABLE_NAME=Const.TABLE_NAME):
        self.DATABASE_PATH = DATABASE_PATH
        self.TABLE_NAME = TABLE_NAME
        self.dataBaseInit()
        self.DATA_ROWS = self.getDATA_ROWS()

    def getDATA_ROWS(self):
        dbConn = sqlite3.connect(self.DATABASE_PATH)
        dbCursor = dbConn.cursor()
        DATA_ROWS = dbCursor.execute("SELECT count(*) FROM " + self.TABLE_NAME + ";").fetchone()[0]
        dbConn.close()
        return DATA_ROWS

    def dataBaseInit(self):
        dbConn = sqlite3.connect(self.DATABASE_PATH)
        dbCursor = dbConn.cursor()
        createTableSQL = '''
                        CREATE TABLE IF NOT EXISTS `''' + self.TABLE_NAME + '''` (
                        `id` int(11) NOT NULL,
                        `predictChannel` varchar(255) DEFAULT NULL,
                        `channelName` varchar(255) DEFAULT NULL,
                        `title` varchar(255) NOT NULL,
                        `content` text,
                        PRIMARY KEY (`title`));
                        '''
        dbCursor.execute(createTableSQL)
        self.getDATA_ROWS()
        dbConn.commit()
        dbConn.close()

    def dataInsert(self, predictChannel, channelName, title, content):
        dbConn = sqlite3.connect(self.DATABASE_PATH)
        dbCursor = dbConn.cursor()

        try:
            self.DATA_ROWS = self.getDATA_ROWS()
            rowInsert = "INSERT INTO " + self.TABLE_NAME + " (id, predictChannel, channelName, title, content) \
                        VALUES (" + str(self.DATA_ROWS + 1) + ", '" + predictChannel + "', '" + channelName + "', '" + title + "', '" + content + "')"
            dbCursor.execute(rowInsert)
            # print("第 " + str(self.DATA_ROWS + 1) + " 条新闻已入库！", predictChannel + ": " + title)
            dbConn.commit()

        except Exception as e:
            # print("该新闻入库失败，原因是:", e)
            pass

        dbConn.close()

    def dataQuery(self, keyword=""):
        dbConn = sqlite3.connect(self.DATABASE_PATH)
        dbCursor = dbConn.cursor()

        dataQuery = "SELECT * FROM " + self.TABLE_NAME + " WHERE predictChannel LIKE '%" + keyword + "%' \
                     OR channelName LIKE '%" + keyword + "%' \
                     OR title LIKE '%" + keyword + "%'"
        dataList = dbCursor.execute(dataQuery).fetchall()

        dbConn.close()
        return dataList

    def dataQueryWrongResult(self, keyword=""):
        dbConn = sqlite3.connect(self.DATABASE_PATH)
        dbCursor = dbConn.cursor()

        dataQuery = "SELECT * FROM " + self.TABLE_NAME + " WHERE predictChannel <> channelName AND channelName in " \
                    "('财经', '房产', '教育', '科技', '军事', '汽车', '体育', '游戏', '娱乐', '其他')"
        dataList = dbCursor.execute(dataQuery).fetchall()

        dbConn.close()
        return dataList

    def dataQueryInChannelName(self, keyword=""):
        dbConn = sqlite3.connect(self.DATABASE_PATH)
        dbCursor = dbConn.cursor()

        dataQuery = "SELECT * FROM " + self.TABLE_NAME + " WHERE channelName LIKE '%" + keyword + "%';"
        dataList = dbCursor.execute(dataQuery).fetchall()

        dbConn.close()
        return dataList

    def dataClear(self):
        dbConn = sqlite3.connect(self.DATABASE_PATH)
        dbCursor = dbConn.cursor()

        deleteDataFromTable = "DELETE FROM " + self.TABLE_NAME
        dbCursor.execute(deleteDataFromTable)

        dbConn.commit()
        dbConn.close()


if __name__ == '__main__':
    db = DataBase()
    db.dataClear()
