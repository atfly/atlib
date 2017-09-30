
    import os  
    from PIL import Image  
    import images2gif  

    def GetGifAnimationFromImages(targetGifFilePath, srcImageFilePaths, type = 0):  
        #用来合成的图片  
        images = []  
          
        #取得所有图片中最大长度（宽度、高度）  
        maxWidthAndHeight = 1  
        #最大宽度和高度  
        maxWidth = 1  
        maxHeight = 1  
        #取得图片按宽度从大到小排序的路径顺序  
        widthAndFilePaths = []  
        #取得图片按高度从大到小排序的路径顺序  
        heightAndFilePaths = []  
          
        for imageFilePath in srcImageFilePaths:  
            fp = open(imageFilePath, "rb")  
            width,height = Image.open(fp).size  
            widthAndFilePaths.append((width, imageFilePath))  
            heightAndFilePaths.append((height, imageFilePath))  
            maxWidth = max(maxWidth, width)  
            maxHeight = max(maxHeight, height)  
            fp.close()  
      
        maxWidthAndHeight = max(maxWidthAndHeight, maxWidth, maxHeight)  
              
        #降序排列  
        widthAndFilePaths.sort(key=lambda item: item[0], reverse=True)  
        heightAndFilePaths.sort(key=lambda item: item[0], reverse=True)  
          
        if type == 4 or type == 5:  
            #原图直接合成(按宽度排序)  
            if type == 4:  
                for widthAndFilePath in widthAndFilePaths:  
                    img = Image.open(widthAndFilePath[1])  
                    images.append(img)  
            #原图直接合成(按高度排序)  
            if type == 5:  
                for heightAndFilePath in heightAndFilePaths:  
                    img = Image.open(heightAndFilePath[1])  
                    images.append(img)  
#www.iplaypy.com

        else:  
            for imageFilePath in srcImageFilePaths:  
                fp = open(imageFilePath, "rb")  
                img = Image.open(fp)  
                width,height = img.size  
                #生成空的白色背景图片  
                if type == 0 or type == 2:    
                    #长方形  
                    imgResizeAndCenter = Image.new("RGB", [maxWidth,maxHeight], (255,255,255))  
                elif type == 1 or type == 3:  
                    #正方形  
                    imgResizeAndCenter = Image.new("RGB", [maxWidthAndHeight,maxWidthAndHeight], (255,255,255))  
      
                if type == 0:  
                    #宽度/最大宽度>=高度/最大高度，使用小的缩放比例  
                    if maxWidth / width >= maxHeight / height:  
                        resizeImg = img.resize((width * maxHeight / height, maxHeight),Image.ANTIALIAS)  
                        imgResizeAndCenter.paste(resizeImg, ((maxWidth - width * maxHeight / height)/ 2,0))  
                    else:  
                        resizeImg = img.resize((maxWidth, height * maxWidth / width),Image.ANTIALIAS)  
                        imgResizeAndCenter.paste(resizeImg, (0,(maxHeight - height * maxWidth / width)/ 2))  
                if type == 1:  
                    #宽度>=高度，按宽度缩放到最大长度  
                    if width >= height:  
                        resizeImg = img.resize((maxWidthAndHeight, height * maxWidthAndHeight / width),Image.ANTIALIAS)  
                        imgResizeAndCenter.paste(resizeImg, (0,(maxWidthAndHeight - height * maxWidthAndHeight / width)/ 2))  
                    else:  
                        resizeImg = img.resize((width * maxWidthAndHeight / height, maxWidthAndHeight),Image.ANTIALIAS)  
                        imgResizeAndCenter.paste(resizeImg, ((maxWidthAndHeight - width * maxWidthAndHeight / height)/ 2, 0))  
                elif type == 2:  
                    imgResizeAndCenter.paste(img, ((maxWidth - width) / 2,(maxHeight - height) / 2))  
                elif type == 3:  
                    imgResizeAndCenter.paste(img, ((maxWidthAndHeight - width) / 2,(maxWidthAndHeight - height) / 2))  
                      
        #        #保存缩放居中后的图片  
        #        imgResizeAndCenter.convert("RGB").save(os.path.dirname(imageFilePath) + os.sep + "ResizeAndCenter" + os.path.basename(imageFilePath), 'jpeg')  
                images.append(imgResizeAndCenter)  
                fp.close()  
              
        images2gif.writeGif(targetGifFilePath, images, duration=1, nq=0.1)  
      
    #取得目录下面的文件列表  
    def GetDirImageList(dir_proc, recusive = True):  
        resultList = []  

        for file in os.listdir(dir_proc):  
            if os.path.isdir(os.path.join(dir_proc, file)):  
                if (recusive):  
                    resultList.append(GetDirImageList(os.path.join(dir_proc, file), recusive))  
                continue  
      
            resultList.append(os.path.join(dir_proc, file))  
              
        return resultList  
      
    if __name__ == "__main__":  
        GetGifAnimationFromImages(r"D:\hecheng.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\c.jpg"])  
        GetGifAnimationFromImages(r"D:\hecheng1.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\b.jpg", r"D:\c.jpg"], 1)  
        GetGifAnimationFromImages(r"D:\hecheng2.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\c.jpg"], 2)  
        GetGifAnimationFromImages(r"D:\hecheng3.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\c.jpg"], 3)  
        GetGifAnimationFromImages(r"D:\hecheng4.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\c.jpg"], 4)  
        GetGifAnimationFromImages(r"D:\hecheng5.gif", [r"D:\a.jpg", r"D:\b.jpg", r"D:\c.jpg"], 5)  
          
        GetGifAnimationFromImages(r"D:\hechengTest.gif", GetDirImageList(r"D:\GifMarker"), type = 4)  