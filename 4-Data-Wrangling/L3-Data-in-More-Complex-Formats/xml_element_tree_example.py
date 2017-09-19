import xml.etree.ElementTree as ET
import pprint

tree = ET.parse('exampleResearchArticle.xml')
root = tree.getroot()


print '\nChildren of root:'
for child in root:
    print child.tag
