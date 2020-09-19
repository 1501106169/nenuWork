# -*- coding: utf-8 -*-
# word requency statistics
import re
import argparse
import os
import sys


'''read file content'''
def opentxt(filePath):
    with open(filePath, "r", encoding="utf-8") as file:
        txtStr = file.read()
    regEx = re.compile(u'\t|\n|\.|-|;|\)|\(|\?|"')      # genernal
    txtStr = re.sub(regEx, '', txtStr)
    return txtStr.lower().split()                       # translate lower


'''word frequency statistics and print sorted'''
def printsort(strList, isfile = True):
    strDict = { }                                       # storage word dict
    for str in strList:
        strDict[str] = strDict.get(str, 0) + 1
    strDictSort = sorted(strDict.items(), key = lambda item : item[1], reverse = True)
    print("total %d words \n" % len(strDictSort))
    # format output
    if(len(strDictSort) > 10):
        for i in range(10):
            print("{:5} {:5}".format(strDictSort[i][0], strDictSort[i][1]))
        if(isfile == False):
            print("----")
    else:
        for i in range(len(strDictSort)):
            print("{:5} {:5}".format(strDictSort[i][0], strDictSort[i][1]))
        if(isfile == False):
            print("----")
    return


'''isdir or isfile, return list'''
def filelist(filePath):
    # get file list
    if(os.path.isdir(filePath) == True):
        # filePath is folder
        return os.listdir(filePath)
        # fileName = os.listdir(filePath)
        # for i in range(len(fileName)):
            # fileName[i] = filePath + '\\' + fileName[i]
        # return fileName
    elif(os.path.isfile(filePath) == True):
        # filePath is file
        return [filePath]
    return


'''word frequency statistics'''
def wordStatistics(filePath):
    filePathList = filelist(filePath)
    if(os.path.isfile(filePath)):
        for file in filePathList:
            printsort(opentxt(file))
    else:
        for file in filePathList:
            print(file.split('.')[0])
            printsort(opentxt(filePath + '\\' + file), False)
    return


'''rediect word statistics'''
def redirect(strTxt):
    regEx = re.compile(u'\t|\n|\.|-|;|\)|\(|\?|"')      # genernal
    txtStr = re.sub(regEx, '', strTxt).lower().split()
    printsort(txtStr)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # nargs - 命令行参数应当消耗的数目。
    parser.add_argument("filePath", nargs = '?', help = "file or folder path")           # filePath, file or folder
    parser.add_argument('-s',nargs = '?', help = "file path")
    args = parser.parse_args()
    # wordStatistics(args.filePath)
    if ((args.s == None) and (args.filePath == None)):
        redi = sys.stdin.read()         # redirect
        redirect(redi)
        pass
    elif ((args.s == None) and (args.filePath != None)):
        wordStatistics(args.filePath)
        pass
    elif ((args.s != None) and (args.filePath == None)):
        wordStatistics(args.s)
        pass
    pass
