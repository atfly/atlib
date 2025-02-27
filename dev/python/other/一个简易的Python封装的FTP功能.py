
from ctypes import *
import os
import sys
import ftplib

class KANFtp:
    ftp = ftplib.FTP()
    bIsDir = False
    path = ""

    def __init__(self, host):
        self.ftp.connect( host )
            
    def Login(self, user, passwd ):
        self.ftp.login( user, passwd )
        print self.ftp.welcome

    def DownLoadFile( self, LocalFile, RemoteFile ):
        file_handler = open( LocalFile, 'wb' )
        self.ftp.retrbinary( "RETR %s" %( RemoteFile ), file_handler.write ) 
        file_handler.close()
        return True
    
    def UpLoadFile( self, LocalFile, RemoteFile ):
        if os.path.isfile( LocalFile ) == False:
            return False

        file_handler = open( LocalFile, "rb" )
        self.ftp.storbinary( 'STOR %s'%RemoteFile, file_handler, 4096 )

        file_handler.close()
        return True

    def UpLoadFileTree( self, LocalDir, RemoteDir ):
        if os.path.isdir( LocalDir ) == False:
            return False

        LocalNames = os.listdir( LocalDir )

        self.ftp.cwd( RemoteDir )

        for Local in LocalNames:
            src = os.path.join( LocalDir, Local)
            if os.path.isdir( src ):
                self.UpLoadFileTree( src, Local )
            else:
                self.UpLoadFile( src, Local )
                
        self.ftp.cwd( ".." )
        return
    
    def DownLoadFileTree( self, LocalDir, RemoteDir ):
        if os.path.isdir( LocalDir ) == False:
            os.makedirs( LocalDir )
        self.ftp.cwd( RemoteDir )

        RemoteNames = self.ftp.nlst()  

        for file in RemoteNames:
            Local = os.path.join( LocalDir, file )
            if self.isDir( file ):
                self.DownLoadFileTree( Local, file )                
            else:
                self.DownLoadFile( Local, file )
        self.ftp.cwd( ".." )
        return
    
    def show( self, list  ):
        result = list.lower().split( " " )

        if self.path in result and "<dir>" in result:
            self.bIsDir = True
     
    def isDir( self, path ):
        self.bIsDir = False
        self.path = path
        #this ues callback function ,that will change bIsDir value
        self.ftp.retrlines( 'LIST', self.show )

        return self.bIsDir

ftp = KANFtp('192.168.21.10')
ftp.Login('XXX','XXXX')

#www.iplaypy.com
#ftp.DownLoadFile('TEST.TXT', 'public\\hechangmin\\TEST.TXT')#ok
#ftp.UpLoadFile('TEST.TXT', 'public\\hechangmin\\TEST.TXT')#ok
#ftp.DownLoadFileTree('HECM', 'public\\hechangmin\\xxx\\')#ok
ftp.UpLoadFileTree('ts',"Public\\hechangmin\\testFTP" )
print "ok!"

