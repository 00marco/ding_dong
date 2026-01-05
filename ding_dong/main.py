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

The prompt changes once per hour.
Everyone sees the same one.
There are no notifications, no feeds, and nothing to catch up on.

This is not a productivity tool.
It’s meant to be visited briefly — and left.
"""
)

st.markdown("---")

# ---------------------------
# DATA
# ---------------------------
modalities = [
    "Write about",
    "Reflect on",
    "Describe",
    "Jot down thoughts on",
    "Tell the story of",
    "Capture a moment from",
]

topics = [
    # Work / effort / cognitive load
    "your work",
    "a task you're working on",
    "something unfinished",
    "something you've been avoiding",
    "something that took more energy than expected",
    "something that felt easier than expected",
    "a recurring responsibility",
    "a small task",
    "a big task",
    "something you touched briefly",
    "something that's been on your mind",
    # Mental & emotional
    "your mental state today",
    "a thought that kept returning",
    "something that felt heavy",
    "something that felt light",
    "a moment of mental clarity",
    "a moment of mental friction",
    "something that affected your mood",
    "something you found yourself ruminating on",
    "a moment you felt present",
    "a moment you felt distracted",
    # Body / physical
    "your body today",
    "how your body feels",
    "your energy levels",
    "a moment of physical ease",
    "a moment of physical discomfort",
    "something physical you did",
    "your relationship with rest",
    "your relationship with movement",
    "something that made your body feel better",
    "something that made your body feel worse",
    "how well-rested you felt",
    "a moment you noticed your breath",
    # Social
    "an interaction you had",
    "a conversation that stayed with you",
    "a moment of connection",
    "a moment of distance",
    "someone you thought about",
    "how you felt around other people",
    "a social moment that gave you energy",
    "a social moment that drained you",
    "a relationship dynamic you noticed",
    "a small social interaction",
    # Environment
    "your home environment",
    "a space you spend a lot of time in",
    "a space that felt calm",
    "a space that felt cluttered",
    "a small area of your home",
    "something you moved or rearranged",
    "something you put away",
    "something that’s been out of place",
    "a surface you see often",
    "something in your environment that affected your mood",
    # Finances
    "something related to money that came up",
    "a financial decision you thought about",
    "a purchase you noticed yourself making",
    "a moment you felt financially at ease",
    "a moment you felt financially tense",
    "something you delayed because of money",
    "something money made easier",
    "something money complicated",
    "your relationship with spending today",
    "your relationship with financial security",
    # Time / pacing
    "how your time felt today",
    "a moment that felt rushed",
    "a moment that felt spacious",
    "something that took longer than expected",
    "something that ended sooner than expected",
    "how you transitioned between things",
    "a boundary you held",
    "a boundary you wished you’d held",
    "something that pulled at your attention",
    "something that gave you a sense of pace",
    # Integration
    "how different parts of your day connected",
    "something that surprised you",
    "a moment that felt out of sync",
    "a moment that felt aligned",
    "something that set the tone for your day",
    "something that shifted your energy",
]

timeframes = [
    "today",
    "earlier today",
    "recently",
    "over the past few hours",
    "as it is right now",
]


# ---------------------------
# HOURLY PROMPT LOGIC
# ---------------------------
def get_hourly_prompt():
    # Use UTC so everyone shares the same cadence
    now = datetime.utcnow()
    hour_key = now.strftime("%Y-%m-%d-%H")

    # Deterministic hash so the same hour always yields the same prompt
    seed = int(hashlib.sha256(hour_key.encode()).hexdigest(), 16)

    modality = modalities[seed % len(modalities)]
    topic = topics[(seed // 7) % len(topics)]
    timeframe = timeframes[(seed // 13) % len(timeframes)]

    return f"{modality} {topic} {timeframe}."


prompt = get_hourly_prompt()

# ---------------------------
# DISPLAY PROMPT
# ---------------------------
st.markdown(f"### 🍃 Prompt: {prompt}")

st.markdown("---")

st.caption(
    "The prompt will change on the next hour. "
    "You don’t need to be here when it does."
)
