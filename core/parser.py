# core/parser.py


def parse_message_to_context(user_text: str) -> dict:
    """
    根據使用者訊息，回傳 rule-based context_dict。
    可依照需要擴充關鍵字與對應邏輯。
    """
    text = user_text.strip()

    context = {
        "fatigue_level": 0,
        "med_adherence": True,
        "care_task_type": 0,
        "recent_incident": 0,
    }

    if "忘記" in text or "沒吃藥" in text:
        context["med_adherence"] = False

    if "很累" in text or "好累" in text:
        context["fatigue_level"] = 5

    if "走失" in text or "找不到人" in text:
        context["recent_incident"] = 2

    if "陪伴" in text or "散步" in text:
        context["care_task_type"] = 1

    return context
