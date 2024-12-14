import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_basic_LeafNode(self):
        node = LeafNode("p", "this is a paragraph")
        node = node.to_html()
        self.assertEqual(node, "<p>this is a paragraph</p>")

    def test_link_leafnode(self):
        node = LeafNode("a", "this is a link", {"href": "https://google.com"})
        node = node.to_html()
        self.assertEqual(node, '<a href="https://google.com">this is a link</a>')

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main
