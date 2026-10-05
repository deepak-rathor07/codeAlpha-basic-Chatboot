"""Simple rule-based chatbot responses."""

import re


def is_exit_message(message: str) -> bool:
    """Return whether a message asks the chatbot to end the conversation."""
    words = set(re.findall(r"\b\w+\b", message.lower()))
    return bool(words.intersection({"bye", "goodbye", "exit", "quit", "alvida"}))


def get_response(message: str) -> str:
    """Return a reply based on a few common words and phrases."""
    normalized = re.sub(r"[^\w\s]", " ", message.lower())
    normalized = " ".join(normalized.split())
    words = set(normalized.split())

    if not normalized:
        return "Kuch type kijiye, phir main jawab dunga. / Type something and I will reply."
    if is_exit_message(normalized):
        return "Alvida! Baat karke achha laga. / Goodbye, it was nice chatting!"
    if words.intersection({"hello", "hi", "hey", "namaste", "namaskar"}):
        return "Namaste! Main InternshipBot hoon. Aap kaise hain? / Hello! How can I help?"
    if "kaise ho" in normalized or "how are you" in normalized:
        return "Main badhiya hoon aur aapki madad ke liye ready hoon! / I'm doing well and ready to help!"
    if "your name" in normalized or "tumhara naam" in normalized or "aapka naam" in normalized:
        return "Mera naam InternshipBot hai. / My name is InternshipBot."
    if "help" in words or "madad" in words:
        return "Aap hello, naam, internship, ya project ke baare mein pooch sakte hain. / Try asking about my name, an internship, or a project."
    if "internship" in words:
        return "Internship mein naye skills seekhna aur chhote goals set karna helpful hota hai. Aap kis field mein kaam kar rahe hain? / What field is your internship in?"
    if "project" in words:
        return "Project ko chhote tasks mein baant kar shuru kijiye. Aapka project kis topic par hai? / What is your project about?"
    if words.intersection({"thanks", "thank", "shukriya", "dhanyavaad"}):
        return "Aapka swagat hai! / You're welcome!"
    return "Mujhe is baare mein abhi nahi pata. Thoda aur bata sakte hain? / I am not sure about that yet. Could you tell me more?"
