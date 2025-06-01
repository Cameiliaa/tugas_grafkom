from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0, 0, 0, 1) # Latar belakang hitam
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Menyesuaikan viewport agar ada ruang untuk 8 huruf berjejer (CAMEILIA)
    gluOrtho2D(-2.2, 2.2, -1.0, 1.0) # Adjusted viewport for 8 letters
    glMatrixMode(GL_MODELVIEW) # Pindah ke modelview matrix untuk transformasi

def draw_letter_Y(center_x, center_y, scale=1.0):
    """Menggambar huruf 'Y' di sekitar center_x, center_y dengan skala tertentu."""
    # Batang kiri atas
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.2 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.0 * scale), 0)
    glEnd()

    # Batang kanan atas
    glBegin(GL_QUADS)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.0 * scale), 0)
    glEnd()

    # Batang bawah
    glBegin(GL_QUADS)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.0 * scale), center_y + (-0.3 * scale), 0)
    glEnd()

def draw_letter_A(center_x, center_y, scale=1.0):
    """Menggambar huruf 'A' di sekitar center_x, center_y dengan skala tertentu."""
    # Kaki kiri
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.2 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (0.3 * scale), 0)
    glEnd()

    # Kaki kanan
    glBegin(GL_QUADS)
    glVertex3f(center_x + (0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.2 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.3 * scale), 0)
    glEnd()

    # Palang tengah
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.05 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.05 * scale), 0)
    glEnd()

# --- New Letter Drawing Functions for CAMEILIA ---
def draw_letter_C(center_x, center_y, scale=1.0):
    """Menggambar huruf 'C' di sekitar center_x, center_y dengan skala tertentu."""
    # Batang atas
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.2 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.2 * scale), center_y + (0.25 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (0.25 * scale), 0)
    glEnd()

    # Batang kiri
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.3 * scale), 0)
    glEnd()

    # Batang bawah
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.2 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.2 * scale), center_y + (-0.25 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (-0.25 * scale), 0)
    glEnd()

def draw_letter_M(center_x, center_y, scale=1.0):
    """Menggambar huruf 'M' di sekitar center_x, center_y dengan skala tertentu."""
    # Kaki kiri
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.2 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.2 * scale), center_y + (0.3 * scale), 0)
    glEnd()

    # Kaki kanan
    glBegin(GL_QUADS)
    glVertex3f(center_x + (0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.2 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.2 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (0.3 * scale), 0)
    glEnd()

    # Batang tengah kiri
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.15 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.3 * scale), 0)
    glEnd()

    # Batang tengah kanan
    glBegin(GL_QUADS)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (0.0 * scale), 0)
    glEnd()

def draw_letter_E(center_x, center_y, scale=1.0):
    """Menggambar huruf 'E' di sekitar center_x, center_y dengan skala tertentu."""
    # Batang vertikal
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.3 * scale), 0)
    glEnd()

    # Batang atas
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (0.25 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (0.25 * scale), 0)
    glEnd()

    # Batang tengah
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.025 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.025 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (-0.025 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.025 * scale), 0)
    glEnd()

    # Batang bawah
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (-0.25 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (-0.25 * scale), 0)
    glEnd()

def draw_letter_L(center_x, center_y, scale=1.0):
    """Menggambar huruf 'L' di sekitar center_x, center_y dengan skala tertentu."""
    # Batang vertikal
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.3 * scale), 0)
    glEnd()

    # Batang horizontal
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (-0.25 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (-0.25 * scale), 0)
    glEnd()

def draw_letter_I(center_x, center_y, scale=1.0):
    """Menggambar huruf 'I' di sekitar center_x, center_y dengan skala tertentu."""
    # Batang vertikal
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.025 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.025 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.025 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.025 * scale), center_y + (-0.3 * scale), 0)
    glEnd()

    # Batang atas
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.25 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.25 * scale), 0)
    glEnd()

    # Batang bawah
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (-0.25 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.25 * scale), 0)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    # Set the color to a "Camelia" RGB value (224, 60, 49)
    glColor3ub(224, 60, 49) 
    
    base_y = 0 # Posisi vertikal tengah huruf
    letter_spacing = 0.5 # Jarak antar huruf

    # Draw the word "CAMEILIA"
    draw_letter_C(-1.75 * letter_spacing, base_y, 0.7)
    draw_letter_A(-1.25 * letter_spacing, base_y, 0.7)
    draw_letter_M(-0.75 * letter_spacing, base_y, 0.7)
    draw_letter_E(-0.25 * letter_spacing, base_y, 0.7)
    draw_letter_I(0.25 * letter_spacing, base_y, 0.7) # First 'I'
    draw_letter_L(0.75 * letter_spacing, base_y, 0.7)
    draw_letter_I(1.25 * letter_spacing, base_y, 0.7) # Second 'I'
    draw_letter_A(1.75 * letter_spacing, base_y, 0.7)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1000, 400) # Increased window width for more letters
glutCreateWindow(b"Huruf CAMEILIA") # Judul window
init()
glutDisplayFunc(draw)
glutMainLoop()