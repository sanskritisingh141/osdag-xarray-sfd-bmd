import xarray as xr
import plotly.graph_objects as go
from pathlib import Path
import os

print("🚀 Task-1 started")

# --------- BULLETPROOF PATH SETUP ----------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

print("BASE_DIR:", BASE_DIR)
print("DATA_DIR:", DATA_DIR)

OUTPUT_DIR.mkdir(exist_ok=True)

# --------- LOAD DATASET ----------
ds = xr.open_dataset(DATA_DIR / "screening_task.nc")

OUTPUT_DIR = Path("../outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

central_elements = [15, 24, 33, 42, 51, 60, 69, 78, 83]

Mz_vals, Vy_vals, x_axis = [], [], []
counter = 0

for e in central_elements:
    elem = ds["forces"].sel(Element=e)

    Mz_vals += [
        elem.sel(Component="Mz_i").item(),
        elem.sel(Component="Mz_j").item()
    ]

    Vy_vals += [
        elem.sel(Component="Vy_i").item(),
        elem.sel(Component="Vy_j").item()
    ]

    x_axis += [counter, counter + 1]
    counter += 1

# BMD
bmd = go.Figure(go.Scatter(x=x_axis, y=Mz_vals, mode="lines+markers"))
bmd.update_layout(
    title="BMD – Central Longitudinal Girder",
    xaxis_title="Element sequence",
    yaxis_title="Mz",
    template="plotly_white"
)
bmd.write_html("../outputs/task1_bmd.html")

# SFD
sfd = go.Figure(go.Scatter(x=x_axis, y=Vy_vals, mode="lines+markers"))
sfd.update_layout(
    title="SFD – Central Longitudinal Girder",
    xaxis_title="Element sequence",
    yaxis_title="Vy",
    template="plotly_white"
)
sfd.write_html("../outputs/task1_sfd.html")

print("Task-1 HTML files generated in outputs/")