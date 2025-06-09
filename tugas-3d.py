import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# Fungsi untuk menggambar kubus
def draw_cube(ax, origin, size, color):
    x, y, z = origin
    dx, dy, dz = size
    v = np.array([
        [x, y, z], [x+dx, y, z], [x+dx, y+dy, z], [x, y+dy, z],
        [x, y, z+dz], [x+dx, y, z+dz], [x+dx, y+dy, z+dz], [x, y+dy, z+dz]
    ])
    faces = [[v[i] for i in face] for face in [[0,1,2,3], [4,5,6,7], [0,1,5,4],
                                               [2,3,7,6], [1,2,6,5], [0,3,7,4]]]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, edgecolors='black', linewidths=0.5))

# Fungsi untuk menggambar kubus bergaris biru-putih
def draw_striped_cube(ax, origin, size, stripes=6, color1='white', color2='royalblue'):
    x, y, z = origin
    dx, dy, dz = size
    stripe_height = dz / stripes
    for i in range(stripes):
        z_start = z + i * stripe_height
        color = color1 if i % 2 == 0 else color2
        draw_cube(ax, (x, y, z_start), (dx, dy, stripe_height), color)

# Gambar wajah ekspresi sedih
def draw_face_sad(ax, center):
    x, y, z = center
    ax.plot([x-0.3], [y+1.9], [z+1.5], 'ko', markersize=6)  # mata kiri
    ax.plot([x+0.3], [y+1.9], [z+1.5], 'ko', markersize=6)  # mata kanan
    theta = np.linspace(-np.pi/3, np.pi/3, 30)
    ax.plot(x + 0.4*np.sin(theta), [y+1.9]*30, z+1.0 - 0.3*np.cos(theta), 'k', linewidth=2)  # mulut sedih

# Setup visualisasi
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Fungsi animasi
def update(frame):
    ax.cla()

    # Kepala
    draw_cube(ax, origin=(1, 1, 6), size=(2, 2, 2), color='bisque')
    draw_face_sad(ax, center=(2, 1, 6))

    # Badan
    draw_striped_cube(ax, origin=(1, 1, 3), size=(2, 2, 3))

    # Tangan kiri dan kanan
    draw_striped_cube(ax, origin=(0, 1, 3), size=(1, 1.5, 3))
    offset = 0.3 * np.sin(frame * 0.2)
    draw_striped_cube(ax, origin=(3, 1, 3 + offset), size=(1, 1.5, 3))

    # Celana
    draw_cube(ax, origin=(1, 1, 0), size=(1, 1, 3), color='slateblue')
    draw_cube(ax, origin=(2, 1, 0), size=(1, 1, 3), color='slateblue')

    # Teks ucapan
    ax.text(0.5, 1, 8.5, "hay... 😔", color='blue', fontsize=14)

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.set_zlim(0, 9)
    ax.set_box_aspect([1, 1, 1])
    ax.set_title("karakter minecraft", fontsize=14)

# Jalankan animasinya
ani = FuncAnimation(fig, update, frames=60, interval=100)
plt.show()
