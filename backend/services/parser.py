"""
Parser Utility

Transforms raw AI text into structured Pydantic-compatible data.
"""

from models.schemas import TimelineOutcome, SimulationResult

def parse_simulation(raw: dict) -> SimulationResult:
    """
    Converts raw agent output into structured SimulationResult.

    Args:
        raw (dict): Raw AI outputs from agents.

    Returns:
        SimulationResult: Validated structured data.
    """

    # Get raw responses
    risks_text = raw.get("risks", "")
    growth_text = raw.get("growth_opportunities", "")
    future_message = raw.get("future_self_message", "")

    # Split into lists - handle both bullet points and newlines
    def clean_list(text):
        lines = text.split('\n')
        result = []
        for line in lines:
            clean = line.strip().lstrip('- •*').strip()
            if clean and len(clean) > 3:
                result.append(clean)
        return result[:10] if result else ["No data available"]

    risks = clean_list(risks_text)
    growth = clean_list(growth_text)

    return SimulationResult(
        best_case=TimelineOutcome(
            summary="Positive outcome from your decision.",
            career="Career advancement and opportunities open up.",
            health="Improved well-being and life satisfaction.",
            finance="Financial growth and stability.",
            social="Stronger relationships and social connections."
        ),
        worst_case=TimelineOutcome(
            summary="Challenging scenario from this decision.",
            career="Career setbacks or stagnation.",
            health="Health or well-being concerns.",
            finance="Financial strain or difficulties.",
            social="Relationship strain or isolation."
        ),
        realistic=TimelineOutcome(
            summary="Most likely outcome based on current factors.",
            career="Moderate career progress with mixed results.",
            health="Stable health with normal variations.",
            finance="Manageable finances with ups and downs.",
            social="Balanced relationships with expected challenges."
        ),
        risks=risks,
        growth_opportunities=growth,
        emotional_outcomes=[],
        future_self_message=future_message or "Your future self awaits..."
    )
