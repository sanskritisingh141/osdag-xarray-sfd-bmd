import xarray as xr

# Load dataset
ds = xr.open_dataset("../data/results.nc")

print("=== DATASET SUMMARY ===")
print(ds)

print("\n=== DATA VARIABLES ===")
for var in ds.data_vars:
    print(var)

print("\n=== COORDINATES ===")
for coord in ds.coords:
    print(coord)

print("\n=== DIMENSIONS ===")
print(ds.dims)
