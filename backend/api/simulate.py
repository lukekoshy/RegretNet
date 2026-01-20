"""
Simulation API route.

Handles incoming requests for decision simulation and orchestrates AI agents.
"""

from fastapi import APIRouter, HTTPException
from models.schemas import DecisionInput
from agents.outcome_agent import generate_outcomes
from agents.risk_agent import analyze_risks
from services.orchestrator import run_simulation


router = APIRouter(prefix="/api/simulate", tags=["Simulation"])

@router.post("/decision")
def simulate_decision(payload: DecisionInput):
    """
    Runs full decision simulation using all AI agents.
    """

    try:
        result = run_simulation(payload.decision, payload.context)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail="Simulation failed.")