import csv
import xml.etree.ElementTree as ET
import os

annoDir = ('VOCLabels/')
destDir = ('SSDLabels/')

def parseXML(filename):
    tree = ET.parse(annoDir + filename)
    root = tree.getroot()
    for item in root.findall('object'):
        _class = -1
        minX = -1
        minY = -1
        maxY = -1
        maxX = -1
        for child in item:
            if child.tag == 'name':
                classTitle = child.text.encode('utf8')
                if str(classTitle) == "b'jabrapanacast'":
                    _class = 2
                elif str(classTitle) == "b'jabraspeak710'":
                    _class = 1
            if child.tag == 'bndbox':
                minX = int(child[0].text.encode('utf8'))
                minY = int(child[1].text.encode('utf8'))
                maxX = int(child[2].text.encode('utf8'))
                maxY = int(child[3].text.encode('utf8'))
        print("%s %s %s %s %s" % (_class, minX, minY, maxX, maxY))
        with open(destDir + filename[:-4]+".txt", "a+") as f:
            f.write("%d %d %d %d %d\n" % (_class, minX, minY, maxX, maxY))

for filename in os.listdir(annoDir):
    if filename.endswith(".xml"): parseXML(filename)