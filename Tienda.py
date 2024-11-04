import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFormLayout, QLineEdit, QStackedWidget, QMainWindow, QHBoxLayout,QTableWidget,QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QIcon

# Ventana para gestionar productos----

class VProductos(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel('Gestionar Productos')
        label.setAlignment(Qt.AlignCenter)  # esto es para  centrar el texto
        layout.addWidget(label)# esto es para agregar el label a la ventana

        # Formulario con campos de la ventana productos
        form_layout = QFormLayout()
        self.nombre_input = QLineEdit() # esto es para  crear un campo de texto
        self.nombre_input.setFixedSize(500, 40)# esto es para darle un tamaño a la caja de texto
        form_layout.addRow('Nombre del Producto:', self.nombre_input)# esto es para agragar el campo de texto al formulario
        self.precio_input = QLineEdit()
        self.precio_input.setFixedSize(500, 40)
        form_layout.addRow('Precio: $', self.precio_input)
        layout.addLayout(form_layout)# esto es para agregar el formulario a la ventana

        # Layout para los botones
        btn_layout = QHBoxLayout()
        btn_layout.setAlignment(Qt.AlignCenter)# esto centra los botones
        self.btn_add_product = QPushButton('Agregar') # esto es para crear un boton
        self.btn_add_product.setFixedSize(150, 40)# esto es para darle un tamaño al boton
        self.btn_edit_product = QPushButton('Editar')
        self.btn_edit_product.setFixedSize(150, 40)
        self.btn_del_product = QPushButton('Eliminar')
        self.btn_del_product.setFixedSize(150, 40)
        btn_layout.addWidget(self.btn_add_product)# esto es para  agregar el boton a la ventana
        btn_layout.addWidget(self.btn_edit_product)
        btn_layout.addWidget(self.btn_del_product)# 
        btn_layout.setContentsMargins(10, 10, 10, 10)
        btn_layout.setSpacing(60)#  esto es para darle un espacio entre los botones
        layout.addLayout(btn_layout)
        self.setLayout(layout)# 

        # Definir los estilos la ventana
        self.setStyleSheet("""
            QWidget {
                background-color:;
            }
            QLabel {
                color: white;
                font-size: 18px;
                font-weight: bold;
            }
            QLineEdit {
                padding: 10px;
                border-radius: 10px;
                border: 2px solid #918dd0 ;
                font-size: 16px;
            }               
            QPushButton {
                background-color: #918dd0;
                color: white;
                padding: 10px;
                border-radius: 10px;
                border: none;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #908af2;
            }
            QPushButton:pressed {
                background-color: #1a5276;
            }
        """)

class VVentas(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QWidget {
                background-color: #ceb2f9;  
            }
            QLabel {
                color: white;
                font-size: 18px;
                font-weight: bold;
            }
            QLineEdit {
                padding: 10px;
                border-radius: 10px;
                border: 2px solid #918dd0;
                font-size: 16px;
            }               
            QPushButton {
                background-color: #918dd0;
                color: white;
                padding: 10px;
                border-radius: 10px;
                border: none;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #908af2;
            }
            QPushButton:pressed {
                background-color: #1a5276;
             }
            
            QTableWidget {
            background-color: #ceb2f9 ;  
            color: white;  
            font-size: 16px;
            }
            QHeaderView::section {
            background-color: #918dd0;  
            color: white;  
            font-size: 16px;
            font-weight: bold;
            }
            QScrollBar:vertical {
            background: #918dd0;  
            width: 10px;
            }
            QScrollBar::handle:vertical {
            background: #918dd0; 
            min-height: 20px;
            border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            background: none;
            height: 0px;
            }
            """)

        l_principal = QHBoxLayout(self)

        seccion_venta = QVBoxLayout()
        
        titulo = QLabel("Punto de Venta")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        seccion_venta.addWidget(titulo)

        # tabla para los productos agregados a la venta
        self.tab_productos = QTableWidget(0, 4)
        self.tab_productos.setHorizontalHeaderLabels(["Código", "Producto", "Cantidad", "Precio"])
        self.tab_productos.setFixedHeight(200)
        seccion_venta.addWidget(self.tab_productos)
        l_precio = QHBoxLayout()
        
      
        self.btn_agr_producto = QPushButton("Agregar Producto")
        self.btn_agr_producto.setFixedSize(150, 40)
        l_precio.addWidget(self.btn_agr_producto)

   
        self.l_total = QLabel("Total: S/ 0.00")
        self.l_total.setStyleSheet("font-size: 16px; font-weight: bold; color: green;")
        self.l_total.setAlignment(Qt.AlignRight)
        l_precio.addWidget(self.l_total)

        
        seccion_venta.addLayout(l_precio)

        l_principal.addLayout(seccion_venta)

       
        seccion_detalles = QVBoxLayout()

     
        self.b_busqueda = QLineEdit()
        self.b_busqueda.setPlaceholderText("Buscar producto...")
        self.b_busqueda.setFixedHeight(40)  # aumenta la altura
        self.b_busqueda.setMinimumWidth(250)  
        self.b_busqueda.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        seccion_detalles.addWidget(self.b_busqueda)
        l_botones = QHBoxLayout()
        
        # boton para generar factura
        self.btn_g_factura = QPushButton("Generar Factura")
        self.btn_g_factura.setFixedSize(150, 40)
        l_botones.addWidget(self.btn_g_factura)

        # botpn para finalizar la venta
        self.btn_f_venta = QPushButton("Finalizar Venta")
        self.btn_f_venta.setFixedSize(150, 40)
        l_botones.addWidget(self.btn_f_venta)
        seccion_detalles.addLayout(l_botones)
        l_principal.addLayout(seccion_detalles)

# inicio----
class Inicio(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        label = QLabel('Bienvenido a la Administración de la Tienda')
        label.setAlignment(Qt.AlignCenter)  
        layout.addWidget(label)
        self.setLayout(layout)
        layout.addStretch()



class VPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('La Tiendita')
        self.setGeometry(100, 100, 800, 400)  # tamaño de la ventana

        self.setWindowIcon(QIcon("c:/Users/lenovo/Downloads/SVG/store.png"))  # Ruta al ícono
        layout = QVBoxLayout()    
        self.st_widget = QStackedWidget()
      
        #vistas
        self.v_inicio = Inicio()
        self.v_productos = VProductos()
        self.v_ventas = VVentas()

        
        self.st_widget.addWidget(self.v_inicio)
        self.st_widget.addWidget(self.v_productos)
        self.st_widget.addWidget(self.v_ventas)

        # layout para los botones
        botones_layout = QHBoxLayout()
        botones_layout.setContentsMargins(10, 10, 10, 10)  # margenes internos del layout (izquierda, arriba, derecha, abajo)
        botones_layout.setSpacing(90)  #

        self.setStyleSheet("background-color:  #dfddff;")
        self.btn_inicio = QPushButton('Inicio')
        self.btn_inicio.setFixedSize(150, 40)
        self.btn_inicio.setStyleSheet ("""
            QPushButton {
                background-color: #a39ef0 ;
                color: white;
                border: 2px solid #918dd0 ;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #908af2 ;
            }
            QPushButton:pressed {
                background-color: #7f78f0;
            }
        """)
        self.btn_inicio.clicked.connect(self.vista_inicio)        
        self.btn_productos = QPushButton('Productos')
        self.btn_productos.setFixedSize(150, 40)
        self.btn_productos.setStyleSheet ("""
            QPushButton {
                background-color: #a39ef0 ;
                color: white;
                border: 2px solid #918dd0 ;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #908af2 ;
            }
            QPushButton:pressed {
                background-color: #7f78f0;
            }
        """)
        self.btn_productos.clicked.connect(self.vista_productos)
        self.btn_ventas = QPushButton('Ventas')
        self.btn_ventas.setFixedSize(150, 40)
        self.btn_ventas.setStyleSheet ("""
            QPushButton {
                background-color: #a39ef0 ;
                color: white;
                border: 2px solid #918dd0 ;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #908af2 ;
            }
            QPushButton:pressed {
                background-color: #7f78f0;
            }
        """)
        self.btn_ventas.clicked.connect(self.vista_ventas)

        # añadir los botones al layout
        botones_layout.addStretch(1)
        botones_layout.addWidget(self.btn_inicio)
        botones_layout.addWidget(self.btn_productos)
        botones_layout.addWidget(self.btn_ventas)
        botones_layout.addStretch(1)

        # añadir el stacked_widget y el layout de botones al layout principal
        layout.addWidget(self.st_widget)
        layout.addLayout(botones_layout)

        # crear un widget central para la ventana principal
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # muetrar la pantalla de inicio por defecto
        self.vista_inicio()

    # funciones para mostrar las vistas
    def vista_inicio(self):
        self.st_widget.setCurrentIndex(0)

    def vista_productos(self):
        self.st_widget.setCurrentIndex(1)

    def vista_ventas(self):
        self.st_widget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # se crea y se muestra la ventana principal
    ventana = VPrincipal()
    ventana.show()

    sys.exit(app.exec_())
