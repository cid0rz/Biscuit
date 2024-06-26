from __future__ import annotations

import tkinter as tk
import typing

from src.biscuit.common.ui import Frame, WrappingLabel

if typing.TYPE_CHECKING:
    from src.biscuit.editor import Text


class OutlineTreePlaceholder(Frame):
    """Placeholder view for the outline tree.

    The OutlineTreePlaceholder view is displayed when there is no outline information available.
    """

    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.config(padx=15, pady=10, **self.base.theme.views.sidebar.item)

        self.label = WrappingLabel(
            self,
            text="No outline information",
            font=("Segoe UI", 10),
            anchor=tk.W,
            **self.base.theme.views.sidebar.item.content,
        )
        self.label.pack(fill=tk.X)

    def show(self, tab: Text) -> None:
        self.label.config(
            text=(
                f"No outline information for {tab.filename}"
                if tab
                else "No outline information"
            )
        )
        self.grid()
