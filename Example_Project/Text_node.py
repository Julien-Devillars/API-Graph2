from node_editor.node import Node
from PySide6 import QtWidgets
from PySide6 import QtCore
from Example_Project.common_widgets import TextLineEdit
from node_editor.PinUtils import PinType

class Text_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Text"
        self.type_text = "Utils Nodes"
        self.set_color(title_color=(155, 155, 155))

        self.add_pin(name="Data", is_output=True, pin_type=PinType.BASE)

        self.build()

    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.text_edit = TextLineEdit()
        layout.addWidget(self.text_edit)
        self.widget.setLayout(layout)
        self.text_edit.textChanged.connect(self.execute)
        
        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget()
    
    def compute(self):
        text = self.text_edit.text()
        self.data = text