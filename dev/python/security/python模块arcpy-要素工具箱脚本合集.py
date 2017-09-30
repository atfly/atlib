
# 导入模块和env
import arcpy
from arcpy import env 
# 定义工作空间
env.workspace = "C:/data"
# 以上几步在其他工具中将省略
# 输入及输出文件路径及名称，无路径默认在工作空间
inFeatures = "parks.shp" 
outFeatureClass = "c:/output/output.gdb/parks_pt"  
# 第三个参数（可选）（"CENTROID"，"INSIDE"）(Boolean)
arcpy.FeatureToPoint_management(inFeatures, outFeatureClass, "INSIDE") 
# （略）
# 设置输入和输出要素
inFeatures = "majorrds.shp"
outFeatureClass = "c:/output/output.gdb/majorrds_midpt"
# 转换
# 第三个参数（可选）指定输出点的创建位置，可以为"ALL","MID","START","END","BOTH_ENDS","DANGLE"
arcpy.FeatureVerticesToPoints_management(inFeatures, outFeatureClass, "MID")
sfaffg
# 导入模块和env
import arcpy
from arcpy import env 
# 定义工作空间
env.workspace = "C:/data"
# 以上几步在其他工具中将省略
# 输入及输出文件路径及名称，无路径默认在工作空间
inFeatures = "parks.shp" 
outFeatureClass = "c:/output/output.gdb/parks_pt"  
# 第三个参数（可选）（"CENTROID"，"INSIDE"）(Boolean)
arcpy.FeatureToPoint_management(inFeatures, outFeatureClass, "INSIDE") 