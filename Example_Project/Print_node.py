from node_editor.node import Node

class Print_Node(Node):
    
    PIN_EXEC_STR = "Ex in"
    PIN_DATA_STR = "Data"
    
    def __init__(self):
        super().__init__()

        self.title_text = "Print"
        self.type_text = "Utils Nodes"
        self.set_color(title_color=(160, 32, 240))

        self.add_pin(name = self.PIN_EXEC_STR, is_output=False, execution=True)
        self.add_pin(name = self.PIN_DATA_STR, is_output=False)
        
        self.build()

    def execute_input(self, input_pin):
        if input_pin.name != self.PIN_DATA_STR:
            return
        
        connected_pin = input_pin.get_connected_pin()
        if not connected_pin:
            return
        
        connected_node = connected_pin.node
        if not connected_node:
            return

        if connected_node.get_data is not None:
            self.data = connected_node.get_data()


    def compute(self):
        print(self.data)