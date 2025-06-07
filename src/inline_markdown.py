import re
from textnode import TextType, TextNode

def text_to_textnodes(text):
    nodes = [TextNode(str(text), TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

    print(new_nodes)
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_text = node.text
        images = extract_markdown_images(node_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for img in images:
            sections = node_text.split(f"![{img[0]}]({img[1]})", 1)
            if len(sections) != 2:
                raise Exception("this is not right friend")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_text = node.text
        links = extract_markdown_links(node_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = node_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise Exception("this is not right friend")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes

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
