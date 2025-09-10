from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.data import COUNTRIES, INDUSTRIES, THREATS, THREATS_BY_ID, query_threats
from app.models import ListCountriesResponse, ListIndustriesResponse, ListThreatsResponse, QueryRequest, ThreatItem, User, UserInDB
from app.security import USER_DB, oauth2_scheme


api_router = APIRouter()

@api_router.get("/countries",
    response_model=ListCountriesResponse,
    tags=["Countries"],
    summary="Retrieve list of countries",
    description=("Retrieve a comprehensive list of countries available in the system.")
)

async def get_countries() -> ListCountriesResponse:
    """
    Get a list of countries.
    """
    return {"countries": COUNTRIES}

@api_router.get("/industries",
    response_model=ListIndustriesResponse,
    tags=["Industries"],  
    summary="Get industries list", 
    description=(
        "Retrieve a list of industries available in the system."
    )
)

async def get_industries() -> ListIndustriesResponse:
    """
    Get a list of industries.
    """
    return {"industries": INDUSTRIES}

@api_router.get("/threats",
    response_model=ListThreatsResponse,
    tags=["Threats"], 
    summary="Get threats list",  
    description="Retrieve a list of all threats.",
    responses={
        404: {"description": "Items not found"},
        } 
)

async def get_threats() -> ListThreatsResponse:
    """
    Get a list of threats.
    """
    return {"threats": THREATS}

@api_router.get("/threats/{threat_id}",
    response_model=ThreatItem,
    tags=["Threats"],  
    summary="Get a specific threat by ID",  
    description="""Get details of a specific threat using its unique ID.
    Returns the threat data if found, otherwise raises a 404 error.
    """,  
    responses={
        404: {"description": "Item not found"}  
    }
)
async def get_threat(threat_id: str) -> ThreatItem:
    """
    Get a specific threat by ID.
    """

    if threat_id not in THREATS_BY_ID:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return THREATS_BY_ID.get(threat_id)

@api_router.post("/threats/query",
    tags=["Threats"],
    summary="Query threats with filters (auth required)",
    description=("This endpoint queries threats based on filters provided in the request body. "
                "This endpoint requires authentication."
    ),
    responses={
        200: {
            "description": "Successful query response",
            "content": {
                "application/json": {
                    "example": {
                        "items": [
                            {"id": "1", "name": "Threat A", "industry": "Finance"},
                            {"id": "2", "name": "Threat B", "industry": "Technology"},
                        ]
                    }
                }
            },
        },
        401: {
            "description": "Unauthorized - Authentication required",
            "content": {
                "application/json": {
                    "example": {"detail": "Not authenticated"}
                }
            },
        },
        422: {
            "description": "Validation Error - Invalid request data",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "industry"],
                                "msg": "Field required",
                                "type": "value_error.missing"
                            },
                            {
                                "loc": ["body", "countries"],
                                "msg": "Value is not a valid list",
                                "type": "type_error.list"
                            }
                        ]
                    }
                }
            }
        }
    }
)

async def query_threats_lite(
    payload: QueryRequest,
    token: str = Depends(oauth2_scheme)
):
    """
    This endpoint queries threats based on various filters.
    Requires authentification.
    """

    industry = payload.industry
    countries: list[str] = payload.countries
    type_filter: str | None = payload.type_filter
    risk_filter: str | None = payload.risk_filter

    items = query_threats(industry, countries, type_filter, risk_filter)
    return {"items": items}


