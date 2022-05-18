import re
import os
import json
from args_parse import parser
from nltk.corpus import words

patent_begin_pos = re.compile(r'<DOCUMENT file="FAMPAT">')
patent_end_pos = re.compile(r'</DOCUMENT>')

title_start_pos = re.compile(r'<TI>')
title_end_pos = re.compile(r'</TI>')

abstract_start_pos = re.compile(r'<AB original="(?P<patent_num>\S+)">')
abstract_end_pos = re.compile(r'</AB>')

claims_start_pos = re.compile(r'<CLMS original="(?P<patent_num>\S+)">')
claims_end_pos = re.compile(r'</CLMS>')

desc_start_pos = re.compile(r'<DESC original="(?P<patent_num>\S+)">')
desc_end_pos = re.compile(r'</DESC>')


def get_title(patent_string):
    """ Return the title content and its end position in a string """

    start_idx = title_start_pos.search(patent_string)
    end_idx = title_end_pos.search(patent_string)

    if not start_idx:
        return "", patent_string
    title_text = patent_string[start_idx.end():end_idx.start()].replace('\n', ' ')\
        .replace('\t', ' ').replace('<br />', ' ')
    return title_text, patent_string[end_idx.end():]

def get_abstract(patent_string):
    """ Return the title content and its end position in a string """

    start_idx = abstract_start_pos.search(patent_string)  # , pos=start_pos)
    # print("start_idx:", start_idx)
    end_idx = abstract_end_pos.search(patent_string)  # , pos=start_pos)
    # print("end_idx:", end_idx)

    if not start_idx:
        return None, "", patent_string
    abstract_text = patent_string[start_idx.end():end_idx.start()].replace('\n', ' ')\
        .replace('\t', ' ').replace('<br />', ' ')
    patent_num = start_idx.group('patent_num')
    return patent_num, abstract_text, patent_string[end_idx.end():]


def separate_claim(claims):
    """ Returns separated claims as dictionary with claim index as key and claim as value"""

    reg_string = r"^(\d+)\. |[\n]+(\d+)\. "
    reg_exp = re.compile(reg_string)
    all_claims = {}
    start = -1
    m = None
    # Separate the claims based on chosen regex pattern
    for m in reg_exp.finditer(claims):
        if start == -1:
            start = m.start(0)
            continue
        else:
            claim = claims[start: m.start(0)].strip()
            # print("Current Claim:", claim)
            claim_reg_exp = re.search(r'^(?P<idx>\d+)\. ', claim)
            claim_id = claim_reg_exp.group('idx')
            all_claims[int(claim_id)] = claim[claim_reg_exp.end():]
            start = m.start(0)
    if m:
        claim = claims[m.start(0): ].strip()
        # print("Current Claim:", claim)
        claim_reg_exp = re.search(r'^(?P<idx>\d+)\. ', claim)
        claim_id = claim_reg_exp.group('idx')
        all_claims[int(claim_id)] = claim[claim_reg_exp.end():]

    return all_claims


def get_claims(patent_string):
    """ Returns separated claims as dictionary"""

    # print(patent_string[:80])

    start_idx = claims_start_pos.search(patent_string)  # , pos=start_pos)
    # print("start_idx:", start_idx)
    end_idx = claims_end_pos.search(patent_string)  # , pos=start_pos)
    # print("end_idx:", end_idx)

    if not start_idx:
        return None, "", patent_string

    patent_num = start_idx.group('patent_num')
    claims_string = patent_string[start_idx.end(): end_idx.start()].replace("<br />", "\n").replace('\t', ' ')
    # print(claims_string[:50])
    # print(claims_string[-50:])

    separated_claims = separate_claim(claims_string)
    # print("separated_claims:", separated_claims)
    return patent_num, separated_claims, patent_string[end_idx.end():]


def get_desc(patent_string):
    """ Returns cleaned and separated """
    # print("*** In descriptions ***")
    # print(patent_string[:80])

    start_idx = desc_start_pos.search(patent_string)  # , pos=start_pos)
    # print("start_idx:", start_idx)
    end_idx = desc_end_pos.search(patent_string)  # , pos=start_pos)
    # print("end_idx:", end_idx)

    if not start_idx:
        return None, "", patent_string

    desc_patent_num = start_idx.group('patent_num')
    desc_string = patent_string[start_idx.end(): end_idx.start()].replace('\t', ' ')

    # print(desc_string[:80])
    # print(desc_string[-80:])
    return desc_patent_num, desc_string, patent_string[end_idx.end():]

def is_english(sentence):
    """ Returns true if at least one word in the sentence is english"""
    found = False
    for word in sentence.split():
        if len(word) > 1 and word.lower() in words.words():
            found = True
            break
    return found


def get_all_headers(desc_content, headers_dict):
    """ This is used to get headers from Orbit files """
    header_string = re.compile(r'^[A-Z ]+\.*$')
    tag_string = re.compile(r'<br />')

    start = 0

    for m in tag_string.finditer(desc_content):
        content = desc_content[start: m.start(0)].strip()
        # print(content)
        if header_string.match(content) and is_english(content):
            # print(content)
            headers_dict[content] = 1 + headers_dict.get(content, 0)
        start = m.end(0)
    return headers_dict


def parse_xml(xml_file, num_patents, possible_headers):
    """ Parse xml file to extract patent content in """
    patents_count = 0
    headers = {}
    # Read the file content
    with open(xml_file, 'r', encoding='utf-8') as f:
        xml_content = f.read()
        f.close()
    print(xml_content[:100], flush=True)
    for patent_start in patent_begin_pos.finditer(xml_content):
        # print("==========  PROCESSING A NEW PATENT  ===============")
        patents_count += 1
        # Extract content related to one patent & process ir
        patent_end = patent_end_pos.search(xml_content, patent_start.end())
        patent_content = xml_content[patent_start.end(): patent_end.start()]
        # print(patent_content[:50], '\n', patent_content[-50:])

        # Get title
        title, patent_content = get_title(patent_content)
        # print("TITLE:", title)

        # Get abstract
        ab_patent_num, abstract, patent_content = get_abstract(patent_content)
        # print("PATENT_NUM:", ab_patent_num, "\nABSTRACT:", abstract)

        # Get claims
        cl_patent_num, all_claims, patent_content = get_claims(patent_content)
        # print("All Separated claims:", all_claims)

        if not (ab_patent_num or cl_patent_num):
            # print("ERROR in getting patent number")
            # break
            pass

        # Description (too complicated to
        ds_patent_num, desc_string, patent_content = get_desc(patent_content)
        possible_headers = get_all_headers(desc_string, possible_headers)

        if patents_count == num_patents:
            break
    print('Number of patents processed', patents_count)
    return possible_headers


if __name__ == '__main__':
    if os.path.exists('possible_headers.json'):
        with open('possible_headers.json', 'r') as f:
            possible_headers = json.load(f)
            f.close()
    else:
        possible_headers = {}
    args = parser.parse_args()
    input_file = args.input_file
    num_patents = args.num_patents

    # possible_headers = parse_xml(
    #     input_file,
    #     num_patents,
    #     possible_headers)

    dir_path = "C:/Users/kumar/Projects/GraphemeLabs/testcases/"
    projects_list = [filename for filename in os.listdir(dir_path)
                     if re.match(r'Project \d{1,3}.xml', filename)]
    print(projects_list)
    for project in projects_list:
        print(f"Reading Project {project}")
        possible_headers = parse_xml(
            os.path.join(dir_path, project),
            num_patents,
            possible_headers)
        # break
    print(possible_headers)
    with open('possible_headers.json', 'w') as f:
        json.dump(possible_headers, f)
