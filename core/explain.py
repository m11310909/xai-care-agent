def get_explanation(user_id, context):
    score = trust_scores.get(user_id, 0)
    if score >= 20:
        return explain_shap_simple(context)
    elif score >= 0:
        return explain_shap_full(context)
    else:
        return explain_with_flowchart(context)


# core/explain.py


def explain_decision(context: dict) -> dict:
    fatigue = context.get("fatigue_level", 0)
    med_ok = context.get("med_adherence", True)
    task_type = context.get("care_task_type", 0)
    incident = context.get("recent_incident", 0)

    suggestion = "請持續觀察與記錄長輩狀況"
    reasons = []

    if not med_ok:
        suggestion = "提醒服藥"
        reasons.append("未依照指示服藥")
    elif fatigue >= 4:
        suggestion = "建議就醫"
        reasons.append(f"疲勞程度高（{fatigue}）")
    elif incident == 2:
        suggestion = "建議配戴定位器"
        reasons.append("近期曾發生走失事件")
    elif task_type == 1:
        suggestion = "建議安排散步活動"
        reasons.append("目前照護為戶外陪伴型")

    return {"suggestion": suggestion, "reasoning": reasons}
