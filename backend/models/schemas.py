"""
Pydantic schemas for request and response validation.

This file defines structured data models for:
- User input
- Timeline outcomes
- Risk analysis
- Emotional outcomes
- Future self narrative
"""

from pydantic import BaseModel
from typing import List

class DecisionInput(BaseModel):
    """
    Schema for user decision input.

    Attributes:
        decision (str): The user's decision to be analyzed.
        context (str | None): Optional background context.
    """
    decision: str
    context: str | None = None


class TimelineOutcome(BaseModel):
    """
    Represents a simulated future outcome.

    Attributes:
        summary (str): Description of the outcome.
        career (str): Career impact.
        health (str): Health impact.
        finance (str): Financial impact.
        social (str): Social/relationship impact.
    """
    summary: str
    career: str
    health: str
    finance: str
    social: str


class SimulationResult(BaseModel):
    """
    Full simulation result schema.

    Attributes:
        best_case (TimelineOutcome)
        worst_case (TimelineOutcome)
        realistic (TimelineOutcome)
        risks (List[str])
        growth_opportunities (List[str])
        emotional_outcomes (List[str])
        future_self_message (str)
    """
    best_case: TimelineOutcome
    worst_case: TimelineOutcome
    realistic: TimelineOutcome
    risks: List[str]
    growth_opportunities: List[str]
    emotional_outcomes: List[str]
    future_self_message: str
