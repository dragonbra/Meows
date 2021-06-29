import os


class Const:
    # root dir
    PROJECT_PATH = 'D:\\GitHub\\NewsClassifier'

    # about database
    DATABASE_NAME = 'newsData.db'
    TABLE_NAME = 'newsClassified'
    DATABASE_PATH = PROJECT_PATH + '\\resources\\database\\' + DATABASE_NAME

    # about model
    MODEL_NAME = 'ClassifyModel.bin'
    MODEL_DICT_NAME = 'roberta_wwm_vocab.txt'
    MODEL_PATH = PROJECT_PATH + '\\resources\\model\\' + MODEL_NAME
    MODEL_DICT_PATH = PROJECT_PATH + '\\resources\\model\\' + MODEL_DICT_NAME

    # about examples
    DEFAULT_FILE_PATH = PROJECT_PATH + '\\examples\\'

    # about images
    LOGO_IMG_PATH = PROJECT_PATH + '\\resources\\images\\logo\\Meows.png'
    LOGO_ICON_PATH = PROJECT_PATH + '\\resources\\images\\logo\\Meows.ico'


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

