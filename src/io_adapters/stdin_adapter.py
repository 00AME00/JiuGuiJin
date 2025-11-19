"""
Simple CLI adapter for streaming chat messages via standard input.
Useful for manual testing of the translation pipeline.
"""
from __future__ import annotations

from typing import Any


async def run_cli(router: Any) -> None:
    """Run an interactive CLI loop for translating stdin messages.

    Parameters
    ----------
    router:
        TranslationRouter instance responsible for handling messages.

    Notes
    -----
    This function should read input lines asynchronously, pass them through the
    router, and print translated output for quick iteration.
    """

    # TODO: Implement CLI loop using asyncio for non-blocking input.
    pass
