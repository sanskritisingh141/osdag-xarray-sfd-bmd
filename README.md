# Osdag Internship Screening Assignment  
## Visualization of Shear Force and Bending Moment Diagrams

This repository contains the solution for the **Osdag Internship Screening Assignment (Software Development)**.  
The task focuses on visualizing internal force results from an Xarray dataset using Python.

The implementation includes:
- **Task 1:** 2D Shear Force Diagram (SFD) and Bending Moment Diagram (BMD) for the central longitudinal girder.
- **Task 2:** 3D SFD and BMD visualizations for all longitudinal girders, similar to MIDAS-style post-processing.

## Project Structure

```
osdag-xarray-sfd-bmd/
│
├── data/
│   ├── screening_task.nc
│   └── node.py
│
├── src/
│   ├── task1_sfd_bmd.py
│   └── task2_3d_sfd_bmd.py
│
├── outputs/
│   ├── task1_bmd.html
│   ├── task1_sfd.html
│   ├── task2_3d_sfd.html
│   └── task2_3d_bmd.html
│
├── requirements.txt
├── report.pdf
└── README.md
```

## Requirements

- Python 3.10 or later  
- Required libraries are listed in `requirements.txt`

Install dependencies using:

`pip install -r requirements.txt`


## How to Run the Code

**Task 1: 2D SFD & BMD (Central Longitudinal Girder)**

Run the following command from the project root:

`python src/task1_sfd_bmd.py`


This generates:

- `outputs/task1_bmd.html`

- `outputs/task1_sfd.html`
##
**Task 2: 3D SFD & BMD (All Longitudinal Girders)**

Run the following command from the project root:

`python src/task2_3d_sfd_bmd.py`


This generates:

- `outputs/task2_3d_sfd.html`

- `outputs/task2_3d_bmd.html`


## Output Description

The generated HTML files are interactive and can be opened directly in any web browser.

Task-1 outputs show continuous 2D shear force and bending moment diagrams for the central girder.

Task-2 outputs show 3D shear force and bending moment distributions across all girders using vertical extrusion.


## Notes

The sign convention provided in the Xarray dataset is preserved without manual modification.

A uniform scaling factor is applied for clear visualization of 3D force diagrams.

Node coordinates are imported directly from a Python file (node.py) as provided in the task.


## Author
Sanskriti Singh
