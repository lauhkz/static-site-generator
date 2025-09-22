from enum import Enum

from htmlnode import HTMLNode
from textnode import TextNode

class BlockType(Enum):
    PARAGRAPH = "paragraph text"
    HEADING = "heading text"
    CODE = "code text"
    QUOTE = "quote text"
    ULIST = "unordered text"
    OLIST = "ordered_list text"


def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    for block in blocks:
        block_type = block_to_block_type(block)
        print(f'block type: {block_type} block: {block}')
        if block_type == BlockType.CODE and block != "```":
            node = TextNode(block, TextType.CODE, None)

def block_to_block_type(block):
    print(f"original block: {block}")
    lines = block.split("\n")
    lines = [line.strip() for line in lines]
    print(f"lines splitted: {lines}")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_blocks(md):
    splitted = md.split("\n\n")
    clean_split = []
    for block in splitted:
        if block == "":
            continue
        block = block.strip()
        clean_split.append(block)
    return clean_split

