
#!/user/bin/python

import os
from datetime import date, datetime, timedelta
import shutil

import logging
import sys

class BkpDT:

    def __init__(self):
        self.exculdeFileExt = ['.lnk']
        self.logger = self.getLogger(sys.argv[0])
        self.backupFolder = '/'.join(['D:/BackupFiles', str(date.today())])


    def getLogger(self, carrier):
        logger = logging.getLogger(os.path.basename(carrier))
        logger.setLevel(logging.DEBUG)
        conlog = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(lineno)s - %(levelname)s - %(message)s")
        conlog.setFormatter(formatter)
        logger.addHandler(conlog)
        return logger

    def getFileInfo(self, file):
        fileInfo = {}
        FILE_STAT = os.stat(file)
        fileInfo['file_name'] = os.path.basename(file)
        fileInfo['file_size'] = os.path.getsize(file)
        fileInfo['modified_date'] = datetime.fromtimestamp(int(FILE_STAT.st_mtime))
        fileInfo['create_date'] = datetime.fromtimestamp(int(FILE_STAT.st_ctime))
        fileInfo['file_ext'] = os.path.splitext(file)[1]
        return fileInfo

    def isNeedBkp(self, fileInfo):#www.iplaypy.com
        today = datetime.today()
        if (fileInfo['file_ext'] not in self.exculdeFileExt) and (today - fileInfo['modified_date'] > timedelta(days = 1)):
            return True

    def createBkpFolder(self):
        if not os.path.exists(self.backupFolder):
            os.mkdir(self.backupFolder)


    def bkpFiles(self):
        files = os.listdir(os.getcwd())
        tf = handled = 0
        for i, file in enumerate(files):
            tf = i
            fileInfo = self.getFileInfo(file)
            if self.isNeedBkp(fileInfo):
                self.createBkpFolder()
                self.logger.debug('Moving file {0} to backup folder {1}'.format(fileInfo['file_name'], self.backupFolder))
                shutil.move(file, self.backupFolder)
                handled += 1
        self.logger.debug('Total {} files found, moved {} files to backup folder'.format(tf, handled))

os.chdir('C:/Documents and Settings/**/Desktop')
bkp = BkpDT()
bkp.bkpFiles()

