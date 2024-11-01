import cv2
import numpy as np

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Vértices del prisma triangular en coordenadas 3D
vertices = np.array([
    [-1, -1, -1],  # Base inferior
    [1, -1, -1],
    [0, 1, -1],
    [-1, -1, 1],   # Base superior
    [1, -1, 1],
    [0, 1, 1]
])

# Conexiones de los vértices para formar las aristas del prisma triangular
edges = [
    (0, 1), (1, 2), (2, 0),           # Base inferior
    (3, 4), (4, 5), (5, 3),           # Base superior
    (0, 3), (1, 4), (2, 5)            # Conexiones entre bases
]

def project_isometric(vertex):
    """Función para proyectar un punto 3D a 2D con proyección isométrica"""
    x, y, z = vertex
    x2D = x - z
    y2D = (x + 2 * y + z) / 2
    return int(x2D * 100 + WIDTH / 2), int(-y2D * 100 + HEIGHT / 2)

# Crear ventana
cv2.namedWindow("Prisma Triangular Isométrico")

while True:
    # Crear imagen negra para el fondo
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    # Dibujar aristas del prisma
    for edge in edges:
        pt1 = project_isometric(vertices[edge[0]])
        pt2 = project_isometric(vertices[edge[1]])
        cv2.line(frame, pt1, pt2, (255, 255, 255), 2)

    # Mostrar imagen
    cv2.imshow("Prisma Triangular Isométrico", frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()