SWISSTOPO_TRUE = {"Wahr", "wahr", "WAHR"}
SWISSTOPO_TUNNEL_TYPES = {"Tunnel", "Unterfuehrung", "Unterfuehrung mit Treppe"}
SWISSTOPO_BRIDGE_TYPES = {
    "Bruecke",
    "Bruecke mit Treppe",
    "Gedeckte Bruecke",
    "Bruecke mit Galerie",
    "Galerie",
}

# Shapefile templates
SWISSTLM3D = "2022_SWISSTLM3D_SHP_CHLV95_LN02"
RIVER_FILE_TEMPLATES = [f"{SWISSTLM3D}/TLM_GEWAESSER/swissTLM3D_TLM_FLIESSGEWAESSER"]
WATER_FILE_TEMPLATES = [
    f"{SWISSTLM3D}/TLM_BB/swissTLM3D_TLM_BODENBEDECKUNG_{direction}"
    for direction in ["OST", "WEST"]
]
PARKS_FILE_TEMPLATES = [f"{SWISSTLM3D}/TLM_AREALE/swissTLM3D_TLM_FREIZEITAREAL"]
STREETS_FILE_TEMPLATES = [f"{SWISSTLM3D}/TLM_STRASSEN/swissTLM3D_TLM_STRASSE"]
RAILWAYS_FILE_TEMPLATES = [f"{SWISSTLM3D}/TLM_OEV/swissTLM3D_TLM_EISENBAHN"]
TREES_FILE_TEMPLATES = [
    f"{SWISSTLM3D}/TLM_BB/swissTLM3D_TLM_EINZELBAUM_GEBUESCH_{direction}"
    for direction in ["OST", "WEST"]
]
FOREST_FILE_TEMPLATES = [
    f"{SWISSTLM3D}/TLM_BB/swissTLM3D_TLM_BODENBEDECKUNG_{direction}"
    for direction in ["OST", "WEST"]
]

SWISSBUILDINGS3D = "2021_SWISSBUILDINGS3D_2.0/SHP_LV95LN02/"
BUILDINGS_FILE_TEMPLATES = [
    SWISSBUILDINGS3D + "SWISSBUILDINGS3D_2_0_CHLV95LN02_{lk25}-{lk25_subindex_2}",
]
