
def FMMSplit(sentence):
    'This is Forward Maximum Matching method.'

    MAXRANGE = 6

    splitedWords = []

    sentenceLength = sentence.__len__()

    finalPoint = sentenceLength - 1

    startPoint = 0

    endPoint = min(finalPoint, MAXRANGE - 1)
    #www.iplaypy.com

    while startPoint <= finalPoint:
        tempPoint = endPoint

        while tempPoint >= startPoint:
            subString = sentence[startPoint:tempPoint + 1]

            if ALLWORDS.has_key(subString):
                splitedWords.append(subString)
                break

            else:

                tempPoint -= 1           

        startPoint += 1

        endPoint = endPoint + 1 if endPoint + 1 <= finalPoint else endPoint

    return splitedWords