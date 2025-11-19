"""
Handles loading glossary data sources and providing lookup helpers for terminology.
Responsible for ingesting YAML/JSON glossaries and exposing normalized entries.
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, Optional


class GlossaryLoader:
    """Load and manage game terminology glossaries.

    The loader encapsulates logic for reading glossary files, normalizing
    terminology across languages, and providing fast lookup during translation.

    Parameters
    ----------
    search_paths:
        Optional iterable of directories to search for glossary files.
    default_language_pair:
        Optional language pair (e.g., "zh-ja") used for filtering entries.
    """

    def __init__(
        self,
        search_paths: Optional[Iterable[Path]] = None,
        default_language_pair: Optional[str] = None,
    ) -> None:
        self.search_paths = list(search_paths or [])
        self.default_language_pair = default_language_pair

    def load(self) -> None:
        """Discover and parse glossary files.

        This method should iterate over configured search paths, parse supported
        glossary formats (YAML/JSON), and cache entries for quick access.
        """

        # TODO: Implement file discovery and parsing.
        pass

    def get_entry(self, term: str, language_pair: Optional[str] = None) -> Optional[Dict[str, str]]:
        """Retrieve a glossary entry for a term.

        Parameters
        ----------
        term:
            The source term to look up (case-insensitive).
        language_pair:
            Optional language pair for filtering when multiple translations
            exist for different locales.

        Returns
        -------
        Optional[Dict[str, str]]
            A normalized glossary entry mapping language codes to translations,
            or ``None`` if the term is not found.
        """

        # TODO: Implement glossary lookup.
        return None

    def reload(self) -> None:
        """Reload glossary data from disk.

        Useful when glossary files change at runtime or when switching games.
        """

        # TODO: Implement reload behavior.
        pass
