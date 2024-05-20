from node_editor.node import Node
from PySide6 import QtWidgets
from Example_Project.common_widgets import TextLineEdit
from node_editor.PinUtils import PinType
import requests

class API_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "API"
        self.type_text = "Getter"
        self.set_color(title_color=(0, 128, 0))

            
        self.add_pin(name="Ex In", is_output=False, pin_type=PinType.EXEC)
        self.add_pin(name="Ex Out", is_output=True, pin_type=PinType.EXEC)
        self.add_pin(name="Data", is_output=True)

        self.build()

    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.url_text_edit = TextLineEdit()
        self.url_text_edit.setText("https://pokeapi.co/api/v2/pokemon")
        layout.addWidget(self.url_text_edit)
        
        self.widget.setLayout(layout)
        
        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget()
        
    def compute(self):
        text = self.url_text_edit.text()
        
        self.response = requests.get(url = text)
        self.data = self.response.json()
        