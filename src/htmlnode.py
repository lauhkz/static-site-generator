class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("html: Method not implemented")

    def props_to_html(self):
        if self.props is None:
            raise ValueError("html: No props given")

        props = self.props
        prop_str = ''

        for prop in props:
            prop_str += f' {prop}="{props[prop]}"'

        return prop_str
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return self.value
        if self.value is None:
            raise ValueError("invalid html: no value given")
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        props = self.props_to_html()
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
