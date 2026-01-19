"""
Parser Utility

Transforms raw AI text into structured Pydantic-compatible data.
"""

from models.schemas import TimelineOutcome, SimulationResult

def parse_simulation(raw: dict) -> SimulationResult:
    """
    Converts raw agent output into structured SimulationResult.

    Args:
        raw (dict): Raw AI outputs.

    Returns:
        SimulationResult: Validated structured data.
    """

    # NOTE: For MVP, we map text into structured placeholders
    # Real parsing logic can be expanded later

    return SimulationResult(
        best_case=TimelineOutcome(
            summary="Best case outcome.",
            career="Positive career growth.",
            health="Improved health.",
            finance="Stable finances.",
            social="Stronger relationships."
        ),
        worst_case=TimelineOutcome(
            summary="Worst case outcome.",
            career="Career stagnation.",
            health="Declining health.",
            finance="Financial stress.",
            social="Weakened relationships."
        ),
        realistic=TimelineOutcome(
            summary="Realistic outcome.",
            career="Moderate growth.",
            health="Average health.",
            finance="Manageable finances.",
            social="Stable relationships."
        ),
        risks=["Burnout", "Missed opportunities"],
        growth_opportunities=["Skill development", "Discipline"],
        emotional_outcomes=["Motivated", "Occasionally stressed"],
        future_self_message=raw["future_self_message"]
    )
