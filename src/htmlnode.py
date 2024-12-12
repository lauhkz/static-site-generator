class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("html: Method not implemented")

    def props_to_html(self):
        if self.props == None:
            raise ValueError("html: No props given")

        props = self.props
        prop_str = ''

        for prop in props:
            prop_str += f' {prop}="{props[prop]}"'

        return prop_str
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

