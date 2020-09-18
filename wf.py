# -*- coding: utf-8 -*-
# word requency statistics


def textParse(bigString):
    listOfTokens = re.split(r"\w*", bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


if __name__ == '__main__':
    print("hello word")
    pass

