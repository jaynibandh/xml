import re
import xml.etree.ElementTree as ET
import xmltodict
from encodings import utf_8
import xml.etree.ElementTree as ET
from pprint import pprint
from args_parse import parser
from os import kill, remove
from pickle import NONE, TRUE
import csv
import string
from bs4 import BeautifulSoup
from os import remove
from pickle import NONE, TRUE
import xml.etree.ElementTree as ET
import re
import csv
import string
i=0
from bs4 import BeautifulSoup

count=0
#reg=regex(r'/n[A-Z][A-Z]')

#---------------------------------------------------------------------------------------#
#load all tags in heiracrhial manner innto a text file "j.txt"
#---------------------------------------------------------------------------------------#


k=[]
f=open("j","w",encoding="utf-8")
def perf_func(elem, func, level=0):
    func(elem,level)
    for child in list(elem):
        perf_func(child, func, level+1)



def print_level(elem,level):
    #print ('-'*level+elem.tag)
    #print(level)
    f.write("\n"+str(level)+" "+elem.tag)

  #k.append(('-'*level+elem.tag))
  #print(k)
  #return k

root = ET.parse('US2022030732A1.xml')
k=perf_func(root.getroot(), print_level)

f = open('j','r',encoding="utf_8")
separatoe=list(f.read().split("\n"))
o=[i.split(' ') for i in separatoe] 
#print(o)
r=0
while r<len(o):
    if r==len(o)-1:
        #print (o[r][0])
        break
    #print(o[r+1][0])
    #print(o[r+1][1])
    
    r=r+1
#print()
k=o[1][1]
#print(k)


#---------------------------------------------------------------------------------------#
#get count of tags .If any tag repeats only one instance is accepted
#---------------------------------------------------------------------------------------#

xmlTree = ET.parse('US2022030732A1.xml')

tags = {elem.tag for elem in xmlTree.iter()}
#print (tags)
j=("\n").join(tags)
#print(j)
ki=j.split()
#print(ki)
print(len(tags))
tree_root = xmlTree.getroot()
f = open("adult.txt", "w",encoding="utf-8")
print(tree_root.findall("patent-document"))


if len(tree_root):   
 print(len(tree_root))


#---------------------------------------------------------------------------------------#
#start of main working program
#---------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------#
#setting the regex for the iteration of start and end positionb tag
#---------------------------------------------------------------------------------------#


count=0
c=0
kil=ki[0]
#print(kill)

"""--input_file C:/Users/Jayanth/Downloads/check.xml --num_patents 1"""
patent_begin_pos = re.compile(rf"<{(o[1][1])}")
# the above regex is eqal to "<tag"
#if patent_begin_pos = re.compile(rf"<{(o[1][1])}>") was there then
 #the regex is "<tag> but if we have a tag in xml like <tag attrib="value" ....> 
 # then the regex chosen in line 108 fails
 #so do not use closing "">""
print(patent_begin_pos)
patent_end_pos = re.compile(rf"</{(o[1][1])}>")

#the below loop has to be tagggd and then can be use dtill then commented.
"""
while(r<len(o)):
 if r==len(o)-1:
        break
"""    
 #title_start_pos = re.compile(r'<TI>')
 #title_end_pos = re.compile(r'</TI>')

 #abstract_start_pos = re.compile(r'<AB original="(?P<patent_num>\S+)">')
 #abstract_end_pos = re.compile(r'</AB>')
cpc_start_pos=[]
cpc_end_pos=[]
cpc_start_pos[r] = re.compile(rf"<{(o[r+1][1])}>")
print(cpc_start_pos[r])
cpc_end_pos[r] = re.compile(rf"</{(o[r+1][1])}>")
 
r=r+1

#---------------------------------------------------------------------------------------#
# function definition to get data and load 
#---------------------------------------------------------------------------------------#
def get_title(patent_string):
    """ Return the title content and its end position in a string """

    start_idx = cpc_start_pos.search(patent_string)
    end_idx = cpc_end_pos.search(patent_string)

    if not start_idx:
        return "", patent_string
    title_text = patent_string[start_idx.end():end_idx.start()].replace('\n', ' ')\
        .replace('\t', ' ').replace('<br />', ' ').replace("<b>",' ').replace("</b>",' ').replace("<i>",' ').replace("</i>",' ')
    return title_text, patent_string[end_idx.end():]

#---------------------------------------------------------------------------------------#
# function definition to parse and display
#---------------------------------------------------------------------------------------#


def parse_xml(xml_file):
    patents_count = 0

    # Read the file content
    with open(xml_file, 'r', encoding='utf-8') as f:
        xml_content = f.read()
        #print(xml_content)
        f.close()
    possible_headers = {}
    with open('outpup1t', 'w', encoding='utf-8') as f:
     for patent_start in patent_begin_pos.finditer(xml_content):
        print("==========  PROCESSING A NEW PATENT  ===============")
        patents_count += 1
        # Extract content related to one patent & process ir
        patent_end = patent_end_pos.search(xml_content, patent_start.end())
        patent_content = xml_content[patent_start.end(): patent_end.start()]
        #print(patent_content[:50], '\n', patent_content[-50:])
        
        # Get title
        title, patent_content = get_title(patent_content)
        print("TITLE:", title)
        f.write(title)
        # Get abstract
        ab_patent_num, abstract, patent_content = get_abstract(patent_content)
        # print("PATENT_NUM:", ab_patent_num, "\nABSTRACT:", abstract)

        # Get claims
        cl_patent_num, all_claims, patent_content = get_claims(patent_content)
        # print("All Separated claims:", all_claims)
        
        cpc, patent_content = get_cpc(patent_content)
        print("CPC:\n", cpc)
        if not (ab_patent_num or cl_patent_num):
            # print("ERROR in getting patent number")
            # break
            pass
        
        print(title)
