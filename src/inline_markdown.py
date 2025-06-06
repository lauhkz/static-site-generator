import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    splitted_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            splitted_nodes.append(node)
            continue

        node_text = node.text
        splitted_text = node_text.split(delimiter)

        if len(splitted_text) % 2 == 0:
            raise ValueError("unmatching delimiter")

        temp_list = []
        for i in range(len(splitted_text)):
            if splitted_text[i] == "":
                continue
            if i % 2 == 0:
                temp_list.append(TextNode(splitted_text[i], TextType.TEXT))
            else:
                temp_list.append(TextNode(splitted_text[i], text_type))
            
        splitted_nodes.extend(temp_list)
    return splitted_nodes


def extract_markdown_images(text):
    # images
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    # regular links
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
