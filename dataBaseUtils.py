import sqlite3


class DataBase:

    def __init__(self):
        self.DATABASE = './data/newsData.db'
        self.TABLENAME = 'newsClassified'
        self.DATAROWS = 0

    def changeDatabase(self, dbDir):
        self.DATABASE = dbDir

    def getDATAROWS(self):
        dbConn = sqlite3.connect(self.DATABASE)
        dbCursor = dbConn.cursor()
        self.DATAROWS = dbCursor.execute("SELECT count(*) FROM newsClassified;").fetchone()[0]
        dbConn.close()

    def dataBaseInit(self):
        dbConn = sqlite3.connect(self.DATABASE)
        dbCursor = dbConn.cursor()
        createTableSQL = '''CREATE TABLE IF NOT EXISTS `newsClassified` (
                      `id` int(11) NOT NULL,
                      `predictChannel` varchar(255) DEFAULT NULL,
                      `channelName` varchar(255) DEFAULT NULL,
                      `title` varchar(255) NOT NULL,
                      `content` text,
                      PRIMARY KEY (`title`));'''
        dbCursor.execute(createTableSQL)
        self.getDATAROWS()
        dbConn.commit()
        dbConn.close()

    def dataInsert(self, predictChannel, channelName, title, content):
        dbConn = sqlite3.connect(self.DATABASE)
        dbCursor = dbConn.cursor()

        try:
            self.getDATAROWS()
            rowInsert = "INSERT INTO newsClassified (id, predictChannel, channelName, title, content) \
                        VALUES (" + str(self.DATAROWS + 1) + ", '" + predictChannel + "', '" + channelName + "', '" + title + "', '" + content + "')"
            dbCursor.execute(rowInsert)
            print("第 " + str(self.DATAROWS + 1) + " 条新闻已入库！", predictChannel + ": " + title)
            dbConn.commit()

        except Exception as e:
            print("该新闻入库失败，原因是:", e)

        dbConn.close()

    def dataQuery(self, keyword=""):
        dbConn = sqlite3.connect(self.DATABASE)
        dbCursor = dbConn.cursor()

        dataQuery = "SELECT * FROM " + self.TABLENAME + " WHERE predictChannel LIKE '%" + keyword + "%' OR channelName LIKE '%" + keyword + "%' \
                     OR title LIKE '%" + keyword + "%' OR content LIKE '%" + keyword + "%'"
        dataList = dbCursor.execute(dataQuery).fetchall()

        dbConn.close()
        return dataList

    def dataClear(self):
        dbConn = sqlite3.connect(self.DATABASE)
        dbCursor = dbConn.cursor()

        deleteDataFromTable = "DELETE FROM " + self.TABLENAME
        dbCursor.execute(deleteDataFromTable)

        dbConn.commit()
        dbConn.close()


if __name__ == '__main__':
    db = DataBase()
    db.dataBaseInit()
    db.dataClear()
