"""
Applies glossary terms and output formatting to translated messages.
Ensures final text remains readable and consistent with player expectations.
"""
from __future__ import annotations

from typing import Dict, Optional


def apply_glossary(translated_text: str, glossary: Optional[Dict[str, str]] = None) -> str:
    """Enforce glossary translations on model output.

    Parameters
    ----------
    translated_text:
        Raw text returned by the translation model.
    glossary:
        Optional mapping of source terms to preferred translations.

    Returns
    -------
    str
        Text with glossary substitutions applied.
    """

    # TODO: Implement glossary substitution.
    return translated_text


def format_output(translated_text: str, *, preserve_emojis: bool = True) -> str:
    """Format the translated message for display.

    Parameters
    ----------
    translated_text:
        Text after glossary enforcement.
    preserve_emojis:
        Whether to preserve emoji spacing and positions from the original text.

    Returns
    -------
    str
        Formatted text ready to send back to the game client.
    """

    # TODO: Implement formatting adjustments.
    return translated_text


def postprocess_message(translated_text: str, glossary: Optional[Dict[str, str]] = None) -> str:
    """Run the full postprocessing pipeline on translated text.

    Combines glossary enforcement with formatting tweaks to produce the final
    output for display in-game.

    Parameters
    ----------
    translated_text:
        Raw translation output.
    glossary:
        Optional glossary mapping for consistent terminology.

    Returns
    -------
    str
        Finalized translation ready for rendering.
    """

    # TODO: Compose glossary application and formatting steps.
    return translated_text
