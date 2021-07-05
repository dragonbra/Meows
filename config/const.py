import os


class Const:
    # root dir
    # PROJECT_PATH = 'D:\\GitHub\\NewsClassifier'
    PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

    # about database
    DATABASE_NAME = 'Classified_News.db'
    TABLE_NAME = 'news'
    DATABASE_PATH = PROJECT_PATH + '\\resources\\database\\' + DATABASE_NAME

    # about model
    MODEL_NAME = 'model_13.bin'
    MODEL_DICT_NAME = 'roberta_wwm_vocab.txt'
    MODEL_PATH = PROJECT_PATH + '\\resources\\model\\' + MODEL_NAME
    MODEL_DICT_PATH = PROJECT_PATH + '\\resources\\model\\' + MODEL_DICT_NAME

    # about examples
    DEFAULT_FILE_PATH = PROJECT_PATH + '\\resources\\example\\'

    # about images
    TAB_ICON_DIR = PROJECT_PATH + '\\resources\\images\\tabicons\\'
    CHANNEL_IMG_DIR = PROJECT_PATH + '\\resources\\images\\channels\\'
    LOGO_IMG_PATH = PROJECT_PATH + '\\resources\\images\\logo\\Meows_Alter.png'
    LOGO_ICON_PATH = PROJECT_PATH + '\\resources\\images\\logo\\Meows.ico'
    MASK_IMG_PATH = PROJECT_PATH + '\\resources\\images\\mask\\皮卡丘.png'


class ConstDictionary:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can not change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError("const name %s is not all upper" % name)
        self.__dict__[name] = value

