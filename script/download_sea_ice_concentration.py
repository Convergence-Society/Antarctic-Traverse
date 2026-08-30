from pathlib import Path
import earthaccess

DATA_DIR = Path("data/raw/nasa/sea-ice-concentration")
DATA_DIR.mkdir(parents=True, exist_ok=True)

earthaccess.login()

results = earthaccess.search_data(
    doi="10.5067/X5LG68MH013O",
    temporal=("2020-01-01", "2025-12-31"),
    bounding_box=(-180, -90, 180, -39),
)

print(f"Found {len(results)} files")

if not results:
    raise RuntimeError("No NSIDC-0079 V004 files found")

earthaccess.download(
    results,
    local_path=str(DATA_DIR),
)

print(f"Downloaded to: {DATA_DIR.resolve()}")