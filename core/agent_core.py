user_states = {}  # { user_id: current_state }


def next_action_stateful(user_id, user_input):
    state = user_states.get(user_id, "INIT")
    # 根據當前狀態 + 使用者輸入決定下一步
    if state == "INIT":
        # 呼叫推論模組 → 記錄 suggestion → 回應建議
        user_states[user_id] = "SUGGESTED"
        return {"action": "SUGGEST", "response": "建議內容"}
    elif state == "SUGGESTED" and user_input == "看解釋":
        user_states[user_id] = "EXPLAINED"
        return {"action": "EXPLAIN"}
    elif state == "EXPLAINED" and user_input == "我懂了":
        user_states[user_id] = "WAIT_PUSH"
                update_trust(user_id, +10)
                schedule_push(user_id)
                return {"action": "ACK"}
        
        def schedule_push(user_id):
            # TODO: implement push scheduling logic
            pass

trust_scores = {}  # { user_id: score }


def update_trust(user_id, delta):
    score = trust_scores.get(user_id, 0)
    trust_scores[user_id] = score + delta


# core/agent_core.py

from core.parser import parse_message_to_context
from core.decision import predict_suggestion


def next_action(user_id: str, user_text: str) -> str:
    context = parse_message_to_context(user_text)
    suggestion = predict_suggestion(context)
    return suggestion
