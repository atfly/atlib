
# -*- coding: utf-8 -*-

from xml.dom import minidom

def list2xml(list):
    """
    在需要时调用此方法，传入List，返回Document对象

    """
    doc = minidom.Document()
    root = doc.createElement("list")

    for entity in list:
        element = get_element(entity, doc)
        root.appendChild(element)
    doc.appendChild(root)

    return doc

def get_element(entity, doc):
    element_name = entity.__class__.__name__
    element = doc.createElement(element_name)
    map = entity.__dict__
    it = map.iterkeys()

    for i in it:
        if i.startswith("_"):
            pass
        else:
           element.appendChild(get_sub_element(doc = doc, element_name = i, text_value = map.get(i))) 

    return element

def get_sub_element(doc, element_name, text_value):
    element = doc.createElement(element_name)

    try:
            text_node = doc.createTextNode(text_value)
            element.appendChild(text_node)
    except Exception:
            text_node = doc.createTextNode(str(text_value))
            element.appendChild(text_node)
    return element
