"""
Simulation API route.

Handles incoming requests for decision simulation and orchestrates AI agents.
"""

from fastapi import APIRouter, HTTPException
from models.schemas import DecisionInput
from services.orchestrator import run_simulation


router = APIRouter(prefix="/api/simulate", tags=["Simulation"])

@router.post("")
def simulate_decision(payload: DecisionInput):
    """
    Runs full decision simulation using all AI agents.
    
    Args:
        payload (DecisionInput): User's decision and context.
    
    Returns:
        dict: Simulation result with all agent outputs.
    """

    try:
        result = run_simulation(payload.decision, payload.context)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Simulation failed: {str(e)}")