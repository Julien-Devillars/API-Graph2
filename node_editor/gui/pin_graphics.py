from PySide6 import QtCore, QtGui, QtWidgets
from node_editor.PinUtils import PinType


class Pin_Graphics(QtWidgets.QGraphicsPathItem):
    def __init__(self, parent, scene):
        super().__init__(parent)

        self.radius_ = 5
        self.margin = 2

        self.pin_type = PinType.BASE

        path = QtGui.QPainterPath()

        path.addEllipse(-self.radius_, -self.radius_, 2 * self.radius_, 2 * self.radius_)

        self.setPath(path)

        self.setFlag(QtWidgets.QGraphicsPathItem.ItemSendsScenePositionChanges)
        self.font = QtGui.QFont()
        self.font_metrics = QtGui.QFontMetrics(self.font)

        self.pin_text_height = self.font_metrics.height()

        self.is_output = False
        self.margin = 2

        self.text_path = QtGui.QPainterPath()

    def set_type(self, type):
        if self.pin_type == PinType.BASE : return
        
        path = QtGui.QPainterPath()
        points = []
        
        if self.pin_type == PinType.EXEC:
            points.append(QtCore.QPointF(-6, -7))
            points.append(QtCore.QPointF(-6, 7))
            points.append(QtCore.QPointF(-2, 7))
            points.append(QtCore.QPointF(6, 0))
            points.append(QtCore.QPointF(-2, -7))
            points.append(QtCore.QPointF(-6, -7))
            path.addPolygon(QtGui.QPolygonF(points))
            self.setPath(path)
            
        if self.pin_type == PinType.MULTI:
            points.append(QtCore.QPointF(-4, -4))
            points.append(QtCore.QPointF(-4, 4))
            points.append(QtCore.QPointF(4, 4))
            points.append(QtCore.QPointF(4, -4))
            points.append(QtCore.QPointF(-4, -4))
            
        path.addPolygon(QtGui.QPolygonF(points))
        self.setPath(path)

    def set_name(self, name):
        nice_name = self.name.replace("_", " ").title()
        self.pin_text_width = self.font_metrics.horizontalAdvance(nice_name)

        if self.is_output:
            x = -self.radius_ - self.margin - self.pin_text_width
        else:
            x = self.radius_ + self.margin

        y = self.pin_text_height / 4

        self.text_path.addText(x, y, self.font, nice_name)

    def paint(self, painter, option=None, widget=None):
        if self.pin_type == PinType.EXEC:
            painter.setPen(QtCore.Qt.white)
        elif self.pin_type == PinType.MULTI:
            painter.setPen(QtCore.Qt.yellow)
        else:
            painter.setPen(QtCore.Qt.green)

        if self.is_connected():
            if self.pin_type == PinType.EXEC:
                painter.setBrush(QtCore.Qt.white)
            elif self.pin_type == PinType.MULTI:
                painter.setBrush(QtCore.Qt.yellow)
            else:
                painter.setBrush(QtCore.Qt.green)
        else:
            painter.setBrush(QtCore.Qt.NoBrush)

        painter.drawPath(self.path())

        # Draw text

        #if not self.pin_type:
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.white)
        painter.drawPath(self.text_path)

    def itemChange(self, change, value):
        if change == QtWidgets.QGraphicsItem.ItemScenePositionHasChanged and self.connection:
            self.connection.update_start_and_end_pos()

        return value
