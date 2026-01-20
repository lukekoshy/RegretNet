"""
Agent Orchestration Service

Coordinates multiple AI agents to produce a complete simulation result.
"""

import logging
from agents.outcome_agent import generate_outcomes
from agents.risk_agent import analyze_risks
from agents.growth_agent import analyze_growth
from agents.emotion_agent import analyze_emotions
from agents.future_self_agent import generate_future_message
from services.parser import parse_simulation

logger = logging.getLogger(__name__)

def run_simulation(decision: str, context: str | None) -> dict:
    """
    Runs all AI agents and returns structured validated results.
    
    Args:
        decision (str): User's decision.
        context (str | None): Optional context.
    
    Returns:
        dict: Combined agent outputs with proper field names.
    """

    try:
        raw = {
            "outcomes": generate_outcomes(decision, context),
            "risks": analyze_risks(decision),
            "growth_opportunities": analyze_growth(decision),
            "emotional_outcomes": analyze_emotions(decision),
            "future_self_message": generate_future_message(decision)
        }

        structured = parse_simulation(raw)
        return structured.dict()

    except Exception as e:
        logger.error(f"Simulation failed: {str(e)}")
        raise
