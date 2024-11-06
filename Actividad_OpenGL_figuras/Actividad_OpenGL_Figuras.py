import glfw
from OpenGL.GL import glClear, glClearColor, glBegin, glEnd, glVertex2f, glColor3f, GL_COLOR_BUFFER_BIT, GL_QUADS, GL_TRIANGLES, GL_LINES, glOrtho

def draw_square():
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Color rojo
    glVertex2f(-0.5,  0.5)  # Vértice superior izquierdo
    glVertex2f( 0.5,  0.5)  # Vértice superior derecho
    glVertex2f( 0.5, -0.5)  # Vértice inferior derecho
    glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
    glEnd()

def draw_triangle():
      glBegin(GL_TRIANGLES)
      glColor3f(0.0, 1.0, 0.0)  # Verde
      glVertex2f(-0.5, -0.4)    # Vértice inferior izquierdo
      glVertex2f(0.5, -0.4)     # Vértice inferior derecho
      glVertex2f(0.0, 0.5)      # Vértice superior
      glEnd()

def draw_line():
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex2f(-0.5,  -0.5)  # Vértice inicial
    glVertex2f( 0.5,  0.5)  # Vértice final
    glEnd()

def main():
    # Inicializar GLFW
    if not glfw.init():
        return

    # Crear la ventana con un contexto de OpenGL
    window = glfw.create_window(500, 500, "Cuadrado con GLFW", None, None)
    if not window:
        glfw.terminate()
        return

    # Hacer que el contexto de OpenGL sea actual para la ventana
    glfw.make_context_current(window)
    

    # Configurar la proyección ortográfica
    glOrtho(-1, 1, -1, 1, -1, 1)  # Configuración para un sistema de coordenadas 2D

    # Bucle principal
    while not glfw.window_should_close(window):
        # Limpiar el buffer de color
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar el cuadrado
        draw_square()

        # Intercambiar buffers y procesar eventos
        glfw.swap_buffers(window)
        glfw.poll_events()

    #Crear imagen para el triangulo
    windowt = glfw.create_window(500, 500, "Triangulo con GLFW", None, None)
    if not windowt:
        glfw.terminate()
        return
    
    # Hacer que el contexto de OpenGL sea actual para la ventana
    glfw.make_context_current(windowt)

    # Bucle principal triangulo
    while not glfw.window_should_close(windowt):
        # Limpiar el buffer de color
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar el triangulo
        draw_triangle()

        # Intercambiar buffers y procesar eventos
        glfw.swap_buffers(windowt)
        glfw.poll_events()

    
    #Crear imagen para la linea
    windowl = glfw.create_window(500, 500, "Linea con GLFW", None, None)
    if not windowl:
        glfw.terminate()
        return
    
    # Hacer que el contexto de OpenGL sea actual para la ventana
    glfw.make_context_current(windowl)

    # Bucle principal linea
    while not glfw.window_should_close(windowl):
        # Limpiar el buffer de color
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar el triangulo
        draw_line()

        # Intercambiar buffers y procesar eventos
        glfw.swap_buffers(windowl)
        glfw.poll_events()


    # Terminar GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()