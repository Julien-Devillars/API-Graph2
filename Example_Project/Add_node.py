from node_editor.node import Node
from node_editor.PinUtils import PinType


class Add_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Add"
        self.type_text = "Logic Nodes"
        self.set_color(title_color=(0, 128, 0))

        self.add_pin(name="Ex In", is_output=False, pin_type=PinType.EXEC)
        self.add_pin(name="Ex Out", is_output=True, pin_type=PinType.EXEC)

        self.add_pin(name="input A", is_output=False, pin_type=PinType.BASE)
        self.add_pin(name="input B", is_output=False, pin_type=PinType.BASE)
        
        self.add_pin(name="output", is_output=True, pin_type=PinType.BASE)
        self.build()


    def compute(self):
        pin_a = self.get_pin("input A")
        pin_b = self.get_pin("input B")
        if pin_a == None or pin_b == None: return
        
        node_a = pin_a.get_connected_node()
        node_b = pin_b.get_connected_node()
        if node_a == None or node_b == None: return
        
        data_a = node_a.get_data()
        data_b = node_b.get_data()
        
        self.data = int(data_a) + int(data_b)
        
    