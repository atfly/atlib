
from xml.dom import minidom

try:
    xmlfile = open("path.xml", "a+")
    #xmldoc = minidom.parse( sys.argv[1])
    xmldoc = minidom.parse(xmlfile)
except :
    #updatelogger.error( "Can't parse Xml File." )
    sys.exit(0)

ClientOutputPath = xmldoc.getElementsByTagName('D')[0].attributes['path'].value

OutputPath = xmldoc.getElementsByTagName('h')[0].attributes['path'].value

BasePath = xmldoc.getElementsByTagName('th')[0].attributes['path'].value

ToolPath = xmldoc.getElementsByTagName('ub')[0].attributes['path'].value

ToolPath_2 = xmldoc.getElementsByTagName('ub')[1].attributes['path'].value

ClientOutputPath.replace( "\\", "\\\\" )

OutputPath.replace( "\\", "\\\\" )

BasePath.replace( "\\", "\\\\" )

#www.iplaypy.com

ToolPath.replace( "\\", "\\\\" )

print ClientOutputPath

print OutputPath

print BasePath

print ToolPath

print ToolPath_2

