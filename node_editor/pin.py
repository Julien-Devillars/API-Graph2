from node_editor.gui.pin_graphics import Pin_Graphics


class Pin(Pin_Graphics):
    def __init__(self, parent, scene):
        super().__init__(parent, scene)

        self.name = None
        self.node = None
        self.connection = None

    def set_execution(self, execution):
        self.execution = execution
        super().set_execution(execution)
        
    def set_execute(self, execute):
        self.inner_execute = execute
        
    def execute(self):
        if(self.inner_execute is None):
            return
        self.inner_execute()

    def set_name(self, name):
        self.name = name
        super().set_name(name)

    def clear_connection(self):
        if self.connection:
            self.connection.delete()
            
    def get_connected_pin(self):
        if self.connection :
            if self.connection.start_pin == self :
                return self.connection.end_pin
            return self.connection.start_pin
        
    def get_connected_node(self):
        connected_pin = self.get_connected_pin()
        if not connected_pin:
            return None
        return connected_pin.node
    
    def execute_connected(self):
        connected_node = self.get_connected_node()
        if not connected_node:
            return
        connected_node.execute()

    def can_connect_to(self, pin):
        if not pin:
            return False
        if pin.node == self.node:
            return False

        return self.is_output != pin.is_output

    def is_connected(self):
        return bool(self.connection)

    def get_data(self):
        # Get a list of nodes in the order to be computed. Forward evaluation by default.
        def get_node_compute_order(node, forward=False):
            # Create a set to keep track of visited nodes
            visited = set()
            # Create a stack to keep track of nodes to visit
            stack = [node]
            # Create a list to store the evaluation order
            order = []

        # Get the next nodes that this node is dependent on
        def get_next_input_node(node):
            pass

        # Get the next nodes that is affected by the input node.
        def get_next_output_node(node):
            pass

        # if pin isn't connected, return it current data

        # get the evalutation order of the owning node of the pin

        # loop over each node and process it

        # return the pin's data
