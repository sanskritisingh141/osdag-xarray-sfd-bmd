import xarray as xr
import plotly.graph_objects as go
from pathlib import Path
import sys

print("Task-2 started")

# ---------------- PATH SETUP ----------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Allow importing node.py
sys.path.append(str(DATA_DIR))

from node import nodes  # ✅ correct now

# ---------------- LOAD DATA ----------------
ds = xr.open_dataset(DATA_DIR / "screening_task.nc")

# ---------------- GIRDER DEFINITIONS ----------------
girders = {
    "Girder 1": {
        "elements": [13, 22, 31, 40, 49, 58, 67, 76, 81],
        "nodes": [1, 11, 16, 21, 26, 31, 36, 41, 46, 6]
    },
    "Girder 2": {
        "elements": [14, 23, 32, 41, 50, 59, 68, 77, 82],
        "nodes": [2, 12, 17, 22, 27, 32, 37, 42, 47, 7]
    },
    "Girder 3": {
        "elements": [15, 24, 33, 42, 51, 60, 69, 78, 83],
        "nodes": [3, 13, 18, 23, 28, 33, 38, 43, 48, 8]
    },
    "Girder 4": {
        "elements": [16, 25, 34, 43, 52, 61, 70, 79, 84],
        "nodes": [4, 14, 19, 24, 29, 34, 39, 44, 49, 9]
    },
    "Girder 5": {
        "elements": [17, 26, 35, 44, 53, 62, 71, 80, 85],
        "nodes": [5, 15, 20, 25, 30, 35, 40, 45, 50, 10]
    }
}

# ---------------- HELPER FUNCTIONS ----------------
def get_node_coords(node_id):
    return nodes[node_id]  # (x, y, z)

def get_force_values(elements, component):
    values = []
    for e in elements:
        elem = ds["forces"].sel(Element=e)
        values.append(elem.sel(Component=f"{component}_i").item())
        values.append(elem.sel(Component=f"{component}_j").item())
    return values

# ---------------- BASE BRIDGE GEOMETRY ----------------
fig_sfd = go.Figure()
fig_bmd = go.Figure()

for girder_name, data in girders.items():
    xs, ys, zs = [], [], []

    for node in data["nodes"]:
        x, y, z = get_node_coords(node)
        xs.append(x)
        ys.append(y)
        zs.append(z)

    # Bridge wireframe
    fig_sfd.add_trace(
        go.Scatter3d(
            x=xs, y=ys, z=zs,
            mode="lines+markers",
            name=girder_name,
            line=dict(width=4, color="gray")
        )
    )

    fig_bmd.add_trace(
        go.Scatter3d(
            x=xs, y=ys, z=zs,
            mode="lines+markers",
            name=girder_name,
            line=dict(width=4, color="gray")
        )
    )

print("✅ Bridge wireframe created")

# ---------------- 3D SFD ----------------
SCALE = 0.002

for girder_name, data in girders.items():
    xs, ys, zs = [], [], []

    shear_vals = get_force_values(data["elements"], "Vy")

    for i, node in enumerate(data["nodes"]):
        x, y, z = get_node_coords(node)
        xs.append(x)
        ys.append(y + shear_vals[i] * SCALE)
        zs.append(z)

    fig_sfd.add_trace(
        go.Scatter3d(
            x=xs, y=ys, z=zs,
            mode="lines",
            name=f"{girder_name} - SFD"
        )
    )

fig_sfd.update_layout(
    title="3D Shear Force Diagram (SFD)",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Shear Force (scaled)",
        zaxis_title="Z"
    ),
    template="plotly_white",
    scene_camera=dict(
    eye=dict(x=1.5, y=1.5, z=1.2)
)

)

fig_sfd.write_html(OUTPUT_DIR / "task2_3d_sfd.html")
print("✅ 3D SFD generated")

# ---------------- 3D BMD ----------------
for girder_name, data in girders.items():
    xs, ys, zs = [], [], []

    moment_vals = get_force_values(data["elements"], "Mz")

    for i, node in enumerate(data["nodes"]):
        x, y, z = get_node_coords(node)
        xs.append(x)
        ys.append(y + moment_vals[i] * SCALE)
        zs.append(z)

    fig_bmd.add_trace(
        go.Scatter3d(
            x=xs, y=ys, z=zs,
            mode="lines",
            name=f"{girder_name} - BMD"
        )
    )

fig_bmd.update_layout(
    title="3D Bending Moment Diagram (BMD)",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Bending Moment (scaled)",
        zaxis_title="Z"
    ),
    template="plotly_white"
)

fig_bmd.write_html(OUTPUT_DIR / "task2_3d_bmd.html")
print("✅ 3D BMD generated")

