# Toronto Climate Risk Assessment

## Objective & Value

This project develops a composite climate risk index for Toronto’s infrastructure by integrating climate projections and asset exposure data. The goal is to help city planners identify neighbourhoods or assets most vulnerable to climate hazards — extreme heat, heavy rainfall/flooding and freeze‑thaw cycles — so resources can be prioritized for resilience. By demonstrating geospatial analytics and climate science skills, the project shows how to translate scientific data into actionable insights for urban planning.

## Data Sources

- **Climate projections:** High‑resolution climate data from ClimateData.ca and other federal sources, including projected counts of extremely hot days, heavy precipitation events and freeze‑thaw cycles for mid‑century scenarios.
- **Historical climate & flood zones:** Floodplain maps and historical heat‑island data from the City of Toronto and the Toronto & Region Conservation Authority.
- **Infrastructure data:** Road networks, critical facilities (hospitals, schools), building footprints and other asset layers from the City of Toronto Open Data portal.
- **Spatial boundaries:** Neighbourhood or ward polygons used to aggregate risk scores.

## Methodology

1. **Hazard indicators:** For each hazard (heat, flood/heavy rain, freeze‑thaw), extract projection values for the Toronto area and align them to neighbourhood boundaries using GeoPandas and rasterio. Normalize these values to obtain comparable hazard scores.
2. **Exposure index:** Quantify infrastructure exposure in each area based on road length, facility counts and population or property density, then normalize to a 0‑1 scale.
3. **Composite risk index:** Combine hazard scores and exposure using a weighted sum. Weights can be equal or reflect expert judgement. The result is a final index (e.g., 0‑100) for each neighbourhood.
4. **Validation & sensitivity:** Check that known high‑risk areas (e.g. floodplains) rank high. Perform sensitivity tests on weighting schemes.
5. **Visualization:** Produce an interactive map and charts (e.g., top‑risk neighbourhoods) in Tableau or another BI tool. The dashboard allows users to filter by hazard or view different scenarios if data allow.

## Installation

1. Clone the repository and set up a Python environment:

   ```bash
   git clone https://github.com/jibrankazi/toronto-climate-risk-assessment.git
   cd toronto-climate-risk-assessment
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Download the necessary climate projection datasets and GIS layers as described in the data section. These files can be large and are not included in the repository; scripts will reference local paths.

## Usage

- Use the Python scripts (e.g. `risk_index.py` or modules under `src/`) to process raw data and compute the risk index. The main script loads climate and infrastructure datasets, computes hazard and exposure scores, and outputs a CSV of neighbourhood risk scores.
- Open the resulting dataset in Tableau or Power BI and use the provided workbook to visualize the spatial distribution of risk. You can customize filters to focus on a particular hazard.
- See the `reports/` folder (if present) for a summary PDF outlining the methodology and key findings.

## Repository Structure

- `risk_index.py` — prototype script for computing hazard and exposure scores and creating the composite risk index.
- `requirements.txt` — required Python packages (GeoPandas, rasterio, shapely, pandas, numpy, matplotlib, seaborn).
- `README.md` — project documentation (this file).
- `src/` — (optional) modular Python code for data ingestion and processing.
- `data/` — location to store raw and processed datasets (not tracked by git).
- `tableau/` — (optional) Tableau workbook for the dashboard.
- `reports/` — (optional) final report summarizing results.

## Notes

- Climate projection files can be downloaded from [ClimateData.ca](https://climatedata.ca/). See scripts or the project wiki for detailed instructions.
- Adjust the weighting of hazard components in the risk index to reflect different priorities (e.g. flood risk may warrant a higher weight).
- This project is for demonstration; no sensitive or proprietary data should be committed to the repository.

---

This project illustrates how geospatial analysis and climate science can inform climate resilience planning in urban settings. Contributions and feedback are welcome.
