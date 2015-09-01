#!/usr/bin/env python

class Paragraph(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            'ChildNodes': 'list[Paragraph]',
            'NodeId': 'str',
            'link': 'Link'

        }

        self.attributeMap = {
            'ChildNodes': 'ChildNodes','NodeId': 'NodeId','link': 'link'}       

        self.ChildNodes = None # list[ParagraphNode]
        self.NodeId = None # str
        self.link = None # Link
        
