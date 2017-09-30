

import win32file #导入方法模块  

sectorsPerCluster, bytesPerSector, numFreeClusters, totalNumClusters \
                   = win32file.GetDiskFreeSpace("c:\\")

print "FreeSpace:", \
      (numFreeClusters * sectorsPerCluster * bytesPerSector) /(1024 * 1024), \
      "MB"

