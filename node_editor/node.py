from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from node_editor.pin import Pin
from node_editor.gui.node_graphics import Node_Graphics
from node_editor.common import Node_Status
from node_editor.PinUtils import PinType

class Node(Node_Graphics):
    data = None
    
    def __init__(self):
        super().__init__()

    # Override me
    def init_widget(self):
        pass

    def compute(self):
        return

    def execute(self):
        # Get the values from the input pins
        self.execute_inputs()

        # Compute the value
        self.compute()

        # execute nodes connected to output
        self.execute_outputs()

    def execute_inputs(self):
        for input in self.get_inputs():
            self.execute_input(input)
            
    def execute_outputs(self):
        for output in self.get_outputs():
            self.execute_output(output)
            
    def execute_input(self, input_pin):
        #self.execute_pin(input_pin)
        return
           
    def execute_output(self, output_pin):
        if output_pin.pin_type == PinType.EXEC:
            output_pin.execute_connected()
    
    def delete(self):
        """Deletes the connection.

        This function removes any connected pins by calling :any:`Port.remove_connection` for each pin
        connected to this connection. After all connections have been removed, the stored :any:`Port`
        references are set to None. Finally, :any:`QGraphicsScene.removeItem` is called on the scene to
        remove this widget.

        Returns:
            None
        """

        to_delete = [pin.connection for pin in self._pins if pin.connection]
        for connection in to_delete:
            connection.delete()

        self.scene().removeItem(self)

    def get_pin(self, name):
        for pin in self._pins:
            if pin.name == name:
                return pin
            
    def get_inputs(self):
        pin_inputs = []
        for pin in self._pins:
            if not pin.is_output:
                pin_inputs.append(pin)
        return pin_inputs
    
    def get_outputs(self):
        pin_outputs = []
        for pin in self._pins:
            if pin.is_output:
                pin_outputs.append(pin)
        return pin_outputs

    def add_pin(self, name, is_output=False, pin_type = PinType.BASE):
        """
        Adds a new pin to the node.

        Args:
            name (str): The name of the new pin.
            is_output (bool, optional): True if the new pin is an output pin, False if it's an input pin. Default is False.
            flags (int, optional): A set of flags to apply to the new pin. Default is 0.
            ptr (Any, optional): A pointer to associate with the new pin. Default is None.

        Returns:
            None: This method doesn't return anything.

        """
        pin = Pin(self, self.scene())
        pin.is_output = is_output
        pin.set_name(name)
        pin.node = self
        pin.set_type(pin_type)

        self._pins.append(pin)

    def select_connections(self, value):
        """
        Sets the highlighting of all connected pins to the specified value.

        This method takes a boolean value `value` as input and sets the `_do_highlight` attribute of all connected pins to
        this value. If a pin is not connected, this method does nothing for that pin. After setting the `_do_highlight`
        attribute for all connected pins, the `update_path` method is called for each connection.

        Args:
            value: A boolean value indicating whether to highlight the connected pins or not.

        Returns:
            None.
        """

        for pin in self._pins:
            if pin.connection:
                pin.connection._do_highlight = value
                pin.connection.update_path()
    
    def get_data(self):
        return self.data
