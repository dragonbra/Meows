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
        print("现在表中数据数量", self.DATAROWS)
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
                        VALUES (" + str(
                self.DATAROWS + 1) + ", '" + predictChannel + "', '" + channelName + "', '" + title + "', '" + content + "')"
            dbCursor.execute(rowInsert)
            dbConn.commit()
            print(rowInsert)

        except Exception as e:
            print(e)

        dbConn.close()

    def dataQuery(self):
        dbConn = sqlite3.connect(self.DATABASE)
        dbCursor = dbConn.cursor()

        dataQuery = "SELECT * from " + self.TABLENAME
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
    db.dataQuery()
