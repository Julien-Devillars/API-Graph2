from node_editor.node import Node
from node_editor.PinUtils import PinType

class Print_Node(Node):
    
    def __init__(self):
        super().__init__()

        self.title_text = "Print"
        self.type_text = "Utils Nodes"
        self.set_color(title_color=(160, 32, 240))

        self.add_pin(name = "Ex in", is_output=False, pin_type = PinType.EXEC)
        self.add_pin(name = "Data", is_output=False)
        
        self.build()

    def execute_inputs(self):
        
        data_pin = self.get_pin("Data")
        if not data_pin: return
        
        connected_node = data_pin.get_connected_node()
        if not connected_node: return

        if connected_node.get_data is not None:
            self.data = connected_node.get_data()

    def compute(self):
        print(self.data)