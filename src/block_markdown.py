from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph text"
    HEADING = "heading text"
    CODE = "code text"
    QUOTE = "quote text"
    ULIST = "unordered text"
    OLIST = "ordered_list text"


def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    html_string = ""
    for block in blocks:
        block_type = block_to_block_type(block)
        print(block_type)

def block_to_block_type(block):
    lines = block.split("\n")

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

