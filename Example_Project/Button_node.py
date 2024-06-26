from PySide6 import QtWidgets

from node_editor.node import Node
from node_editor.PinUtils import PinType


class Button_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Button"
        self.type_text = "Inputs"
        self.set_color(title_color=(128, 0, 0))

        self.add_pin(name="Ex Out", is_output=True, pin_type=PinType.EXEC)

        self.build()

    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        btn = QtWidgets.QPushButton("Execute")
        btn.clicked.connect(self.btn_cmd)
        layout.addWidget(btn)
        self.widget.setLayout(layout)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget()

    def btn_cmd(self):
        self.execute()
