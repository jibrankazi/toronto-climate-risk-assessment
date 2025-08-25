"""
risk_index.py: Compute climate risk index for Toronto infrastructure.

This script fetches climate projection data and infrastructure data, joins them spatially,
and calculates a composite risk score based on heat, flood, and freeze-thaw hazards.

Functions:
- load_climate_data: loads climate projection datasets (e.g., extreme heat days, heavy rain days, freeze-thaw cycles) from downloaded files.
- load_infrastructure_data: loads geospatial data for roads, buildings, and critical facilities (as GeoDataFrames).
- compute_hazard_scores: computes normalized hazard scores for each area or grid cell.
- compute_exposure: calculates exposure metrics (e.g., road length, facility count) for each area.
- calculate_risk_index: combines hazard scores and exposure to produce a composite risk index.
- main: orchestrates the workflow and writes results to CSV.

Note: Data files should be downloaded separately from Toronto open data and climate portals.
"""

import pandas as pd
import geopandas as gpd
import numpy as np


def load_climate_data():
    """
    Load climate projection data for heat, rainfall, and freeze‑thaw hazards.
    Return a GeoDataFrame or DataFrame with geographic coordinates and hazard metrics.
    """
    # TODO: implement data loading
    pass


def load_infrastructure_data():
    """
    Load infrastructure layers such as roads, facilities, etc., into GeoDataFrames.
    """
    # TODO: implement data loading
    pass


def compute_hazard_scores(climate_df):
    """
    Normalize climate hazard variables (e.g., using min‑max scaling).
    """
    # TODO: implement hazard scoring
    pass


def compute_exposure(infra_df):
    """
    Compute exposure metrics (e.g., total road length or facility counts per area).
    """
    # TODO: implement exposure calculation
    pass


def calculate_risk_index(hazard_scores, exposure_scores, weights=None):
    """
    Combine hazard and exposure scores into a composite risk index.
    weights: optional dict specifying weights for each hazard component.
    """
    # TODO: implement risk index calculation
    pass


def main():
    # Load data
    climate_df = load_climate_data()
    infra_df = load_infrastructure_data()

    # Compute scores
    hazard_scores = compute_hazard_scores(climate_df)
    exposure_scores = compute_exposure(infra_df)

    # Calculate risk index
    risk_index = calculate_risk_index(hazard_scores, exposure_scores)

    # TODO: join scores with spatial boundaries (e.g., neighborhoods) and export results
    # Ensure risk_index is a DataFrame before exporting
    if hasattr(risk_index, "to_csv"):
        risk_index.to_csv("risk_index.csv", index=False)


if __name__ == "__main__":
    main()
