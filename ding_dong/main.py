import streamlit as st
import hashlib
from datetime import datetime

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="DING DONG",
    layout="centered",
)

# ---------------------------
# COPY
# ---------------------------
st.title("DING DONG")

st.markdown(
    """
This app shows a single shared reflection prompt.

The prompt changes slowly.
Everyone sees the same one.
There are no notifications, no feeds, and nothing to catch up on.

This is not a productivity tool.
It’s meant to be visited briefly — and left.
"""
)

st.markdown("---")

# ---------------------------
# FIXED PROMPT SET (STARTER)
# ---------------------------
PROMPTS = [
    # Work
    "Reflect on your work right now.",
    "Reflect on something unfinished.",
    "Reflect on where your effort has been going.",
    "Reflect on something you’ve been avoiding.",
    # Body
    "Reflect on how your body feels today.",
    "Reflect on your energy.",
    "Reflect on your relationship with rest.",
    "Reflect on a moment of physical ease or discomfort.",
    # Mind
    "Reflect on your mental state.",
    "Reflect on a thought that kept returning.",
    "Reflect on something that felt heavy or light.",
    "Reflect on your attention today.",
    # Social life
    "Reflect on an interaction that stayed with you.",
    "Reflect on how you felt around other people.",
    "Reflect on a moment of connection or distance.",
    # Money
    "Reflect on how money showed up today.",
    "Reflect on a choice shaped by money.",
    "Reflect on your sense of financial ease or tension.",
    # Environment
    "Reflect on the space around you.",
    "Reflect on something in your environment that affected you.",
    # Time & pacing
    "Reflect on how your time felt today.",
    "Reflect on your sense of pace.",
    "Reflect on a boundary you noticed.",
    # Social impact
    "Reflect on how your actions affected others.",
    "Reflect on how you showed up in shared space.",
    "Reflect on something you contributed or withheld.",
    # Integration
    "Reflect on how the day fit together.",
    "Reflect on what set the tone.",
    "Reflect on what shifted your energy.",
]


# ---------------------------
# PROMPT ROTATION LOGIC
# ---------------------------
def get_current_prompt():
    """
    Change cadence by modifying the key:
    - hourly: "%Y-%m-%d-%H"
    - daily:  "%Y-%m-%d"
    """
    now = datetime.utcnow()
    time_key = now.strftime("%Y-%m-%d")  # DAILY cadence

    seed = int(hashlib.sha256(time_key.encode()).hexdigest(), 16)
    index = seed % len(PROMPTS)

    return PROMPTS[index]


prompt = get_current_prompt()

# ---------------------------
# DISPLAY PROMPT
# ---------------------------
st.markdown(f"### 🍃 {prompt}")

st.markdown("---")

st.caption("You don’t need to respond. " "You don’t need to return. " "This is enough.")
