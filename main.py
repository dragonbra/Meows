import dataProcessUtils
from dataProcessUtils import Classifier
import torch
import time

if __name__ == "__main__":
    st = time.time()
    classifier = Classifier()
    print(time.time() - st)

    while True:
        text = input("news: ")
        if text == "q":
            break
        res = classifier.predict(text)
        print(res)

        continue