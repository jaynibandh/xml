import argparse

parser = argparse.ArgumentParser(
    prog='patent_xml_parser.py',
    description='From Orbit XML result or patent search based on keywords, extract\
                each patent information, like patent-id, patent-no, title, abstract,\
                description and class numbers',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    allow_abbrev=True
)

parser.add_argument('--input_file', type=str, default=None,
                    help='XML file to parse and extract patents') #,
                    # required=True)
parser.add_argument('--num_patents', type=int, default=None,
                    help='Number of patents to parse.')
