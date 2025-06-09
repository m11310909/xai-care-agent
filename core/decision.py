def predict_suggestion(context: dict) -> str:
    """
    根據輸入的語境 context，回傳建議文字。
    預設使用 rule-based 規則，未來可改為 ML 模型。
    """
    fatigue = context.get("fatigue_level", 0)
    med_ok = context.get("med_adherence", True)
    task_type = context.get("care_task_type", 0)
    incident = context.get("recent_incident", 0)

    if not med_ok:
        return "提醒服藥"
    elif fatigue >= 4:
        return "建議就醫"
    elif incident == 2:
        return "建議配戴定位器"
    elif task_type == 1:
        return "建議安排散步活動"
    else:
        return "請持續觀察與記錄長輩狀況"
