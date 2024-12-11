from enum import Enum

class TextType(Enum):
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    IMAGE = "image"
    LINK = "link text"
    NORMAL = "normal text"


class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, another):
        return (
            self.text == another.text and
            self.text_type == another.text_type and
            self.url == another.url
                )
        
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")

