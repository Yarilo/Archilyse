from http import HTTPStatus

import pytest

from brooks.classifications import CLASSIFICATIONS
from brooks.util.projections import REGIONS_CRS
from slam_api.apis.constants import (
    area_filters,
    constants_app,
    get_classification_scheme,
    get_classification_schemes,
    get_projections,
)
from tests.flask_utils import get_address_for


def test_get_classification_schemes(client):
    response = client.get(
        get_address_for(
            blueprint=constants_app,
            use_external_address=False,
            view_function=get_classification_schemes,
        )
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json == [
        CLASSIFICATIONS.UNIFIED.name,
    ]


@pytest.mark.parametrize(
    "scheme_name,expected_code,expected_keys",
    [
        (
            "UNIFIED",
            HTTPStatus.OK,
            {
                "AreaType.ARCADE",
                "AreaType.BALCONY",
                "AreaType.BASEMENT",
                "AreaType.BASEMENT_COMPARTMENT",
                "AreaType.BATHROOM",
                "AreaType.BEDROOM",
                "AreaType.BIKE_STORAGE",
                "AreaType.CARPARK",
                "AreaType.CORRIDOR",
                "AreaType.DINING",
                "AreaType.ELEVATOR",
                "AreaType.WASTEWATER",
                "AreaType.WATER_SUPPLY",
                "AreaType.HEATING",
                "AreaType.GAS",
                "AreaType.ELECTRICAL_SUPPLY",
                "AreaType.TELECOMMUNICATIONS",
                "AreaType.AIR",
                "AreaType.ELEVATOR_FACILITIES",
                "AreaType.OPERATIONS_FACILITIES",
                "AreaType.FOYER",
                "AreaType.GARAGE",
                "AreaType.GARDEN",
                "AreaType.COMMUNITY_ROOM",
                "AreaType.BREAK_ROOM",
                "AreaType.WAITING_ROOM",
                "AreaType.CANTEEN",
                "AreaType.PRISON_CELL",
                "AreaType.OFFICE_SPACE",
                "AreaType.OPEN_PLAN_OFFICE",
                "AreaType.MEETING_ROOM",
                "AreaType.DESIGN_ROOM",
                "AreaType.COUNTER_ROOM",
                "AreaType.CONTROL_ROOM",
                "AreaType.RECEPTION_ROOM",
                "AreaType.OFFICE_TECH_ROOM",
                "AreaType.FACTORY_ROOM",
                "AreaType.WORKSHOP",
                "AreaType.TECHNICAL_LAB",
                "AreaType.PHYSICS_LAB",
                "AreaType.CHEMICAL_LAB",
                "AreaType.LIVESTOCK",
                "AreaType.PLANTS",
                "AreaType.COMMON_KITCHEN",
                "AreaType.SPECIAL_WORKSPACE",
                "AreaType.WAREHOUSE",
                "AreaType.ARCHIVE",
                "AreaType.COLD_STORAGE",
                "AreaType.LOGISTICS",
                "AreaType.SALESROOM",
                "AreaType.EXHIBITION",
                "AreaType.TEACHING_ROOM",
                "AreaType.FLEXIBLE_TEACHING_ROOM",
                "AreaType.DEDICATED_TEACHING_ROOM",
                "AreaType.LIBRARY",
                "AreaType.SPORTS_ROOMS",
                "AreaType.ASSEMBLY_HALL",
                "AreaType.STAGE_ROOM",
                "AreaType.SHOWROOM",
                "AreaType.CHAPEL",
                "AreaType.MEDICAL_ROOM",
                "AreaType.DEDICATED_MEDICAL_ROOM",
                "AreaType.SURGERY_ROOM",
                "AreaType.RADIATION_DIAGNOSIS",
                "AreaType.RADATION_THERAPY",
                "AreaType.PHYSIO_AND_REHABILITATION",
                "AreaType.MEDICAL_BEDROOM",
                "AreaType.DEDICATED_MEDICAL_BEDROOM",
                "AreaType.KITCHEN",
                "AreaType.LIGHTWELL",
                "AreaType.LIVING_DINING",
                "AreaType.LIVING_ROOM",
                "AreaType.LOBBY",
                "AreaType.LOGGIA",
                "AreaType.SANITARY_ROOMS",
                "AreaType.CLOAKROOM",
                "AreaType.PASSENGER_PLATFORM",
                "AreaType.HOUSE_TECHNICS_FACILITIES",
                "AreaType.SHELTER",
                "AreaType.MOTORCYCLE_PARKING",
                "AreaType.OFFICE",
                "AreaType.OIL_TANK",
                "AreaType.OUTDOOR_VOID",
                "AreaType.PATIO",
                "AreaType.PRAM",
                "AreaType.PRAM_AND_BIKE_STORAGE_ROOM",
                "AreaType.ROOM",
                "AreaType.SHAFT",
                "AreaType.STAIRCASE",
                "AreaType.STOREROOM",
                "AreaType.STUDIO",
                "AreaType.TECHNICAL_AREA",
                "AreaType.TERRACE",
                "AreaType.CORRIDORS_AND_HALLS",
                "AreaType.TRANSPORT_SHAFT",
                "AreaType.VEHICLE_TRAFFIC_AREA",
                "AreaType.VOID",
                "AreaType.WASH_AND_DRY_ROOM",
                "AreaType.WINTERGARTEN",
                "SIACategory.ANF",
                "SIACategory.FF",
                "SIACategory.HNF",
                "SIACategory.NNF",
                "SIACategory.VF",
            },
        ),
        ("doesnotexist", HTTPStatus.NOT_FOUND, set()),
    ],
)
def test_get_classification_scheme_area_types(
    client, scheme_name, expected_code, expected_keys
):
    response = client.get(
        get_address_for(
            blueprint=constants_app,
            use_external_address=False,
            view_function=get_classification_scheme,
            verbose_scheme_name=scheme_name,
        )
    )

    assert response.status_code == expected_code
    assert set(response.json.keys()) == expected_keys
    assert "AreaType.KITCHEN_DINING" not in response.json.get(
        "SIACategory.HNF", {}
    ).get("children", "")


def test_api_get_projections(client, login):
    projections_url = get_address_for(
        blueprint=constants_app,
        use_external_address=False,
        view_function=get_projections,
    )
    response = client.get(projections_url)
    for crs in REGIONS_CRS.values():
        assert crs.to_string() in response.json


def test_get_area_filters(client, login):
    url = get_address_for(
        blueprint=constants_app,
        use_external_address=False,
        view_function=area_filters,
        verbose_scheme_name="UNIFIED",
    )
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        "COMMERCIAL": [
            "ARCADE",
            "BALCONY",
            "BASEMENT_COMPARTMENT",
            "BASEMENT",
            "BATHROOM",
            "CARPARK",
            "ELEVATOR",
            "FOYER",
            "GARDEN",
            "LIGHTWELL",
            "LOBBY",
            "LOGGIA",
            "OFFICE",
            "OIL_TANK",
            "OUTDOOR_VOID",
            "PATIO",
            "PRAM_AND_BIKE_STORAGE_ROOM",
            "PRAM",
            "SHAFT",
            "STAIRCASE",
            "STOREROOM",
            "TERRACE",
            "VOID",
            "COMMUNITY_ROOM",
            "BREAK_ROOM",
            "WAITING_ROOM",
            "CANTEEN",
            "PRISON_CELL",
            "OFFICE_SPACE",
            "OPEN_PLAN_OFFICE",
            "MEETING_ROOM",
            "DESIGN_ROOM",
            "COUNTER_ROOM",
            "CONTROL_ROOM",
            "RECEPTION_ROOM",
            "OFFICE_TECH_ROOM",
            "FACTORY_ROOM",
            "WORKSHOP",
            "TECHNICAL_LAB",
            "PHYSICS_LAB",
            "CHEMICAL_LAB",
            "LIVESTOCK",
            "PLANTS",
            "COMMON_KITCHEN",
            "SPECIAL_WORKSPACE",
            "WAREHOUSE",
            "ARCHIVE",
            "COLD_STORAGE",
            "LOGISTICS",
            "SALESROOM",
            "EXHIBITION",
            "TEACHING_ROOM",
            "FLEXIBLE_TEACHING_ROOM",
            "DEDICATED_TEACHING_ROOM",
            "LIBRARY",
            "SPORTS_ROOMS",
            "ASSEMBLY_HALL",
            "STAGE_ROOM",
            "SHOWROOM",
            "CHAPEL",
            "MEDICAL_ROOM",
            "DEDICATED_MEDICAL_ROOM",
            "SURGERY_ROOM",
            "RADIATION_DIAGNOSIS",
            "RADATION_THERAPY",
            "PHYSIO_AND_REHABILITATION",
            "MEDICAL_BEDROOM",
            "DEDICATED_MEDICAL_BEDROOM",
            "SANITARY_ROOMS",
            "CLOAKROOM",
            "CORRIDORS_AND_HALLS",
            "TRANSPORT_SHAFT",
            "VEHICLE_TRAFFIC_AREA",
        ],
        "JANITOR": [
            "BATHROOM",
            "OFFICE",
            "STOREROOM",
            "TECHNICAL_AREA",
        ],
        "PUBLIC": [
            "BALCONY",
            "BASEMENT_COMPARTMENT",
            "BASEMENT",
            "BIKE_STORAGE",
            "CARPARK",
            "ELEVATOR",
            "FOYER",
            "GARAGE",
            "GARDEN",
            "LIGHTWELL",
            "LOGGIA",
            "OIL_TANK",
            "OUTDOOR_VOID",
            "PATIO",
            "PRAM_AND_BIKE_STORAGE_ROOM",
            "PRAM",
            "SHAFT",
            "STAIRCASE",
            "STOREROOM",
            "TECHNICAL_AREA",
            "TERRACE",
            "VOID",
            "WASH_AND_DRY_ROOM",
            "WASTEWATER",
            "WATER_SUPPLY",
            "HEATING",
            "GAS",
            "ELECTRICAL_SUPPLY",
            "TELECOMMUNICATIONS",
            "AIR",
            "ELEVATOR_FACILITIES",
            "OPERATIONS_FACILITIES",
            "SANITARY_ROOMS",
            "PASSENGER_PLATFORM",
            "HOUSE_TECHNICS_FACILITIES",
            "SHELTER",
            "CORRIDORS_AND_HALLS",
            "TRANSPORT_SHAFT",
            "VEHICLE_TRAFFIC_AREA",
        ],
        "RESIDENTIAL": [
            "BALCONY",
            "BATHROOM",
            "BEDROOM",
            "CORRIDOR",
            "DINING",
            "GARDEN",
            "KITCHEN",
            "KITCHEN_DINING",
            "LIGHTWELL",
            "LIVING_DINING",
            "LIVING_ROOM",
            "LOGGIA",
            "OUTDOOR_VOID",
            "PATIO",
            "PRAM_AND_BIKE_STORAGE_ROOM",
            "ROOM",
            "SHAFT",
            "STOREROOM",
            "STUDIO",
            "TECHNICAL_AREA",
            "TERRACE",
            "VOID",
            "WINTERGARTEN",
        ],
    }
