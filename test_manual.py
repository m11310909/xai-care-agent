import sys
import os

sys.path.append(os.path.abspath("."))

from core.decision import predict_suggestion

test_cases = [
    {
        "name": "忘記服藥",
        "context": {
            "fatigue_level": 2,
            "med_adherence": False,
            "care_task_type": 0,
            "recent_incident": 0,
        },
    },
    {
        "name": "疲勞指數高",
        "context": {
            "fatigue_level": 5,
            "med_adherence": True,
            "care_task_type": 0,
            "recent_incident": 0,
        },
    },
    {
        "name": "走失事件發生",
        "context": {
            "fatigue_level": 1,
            "med_adherence": True,
            "care_task_type": 0,
            "recent_incident": 2,
        },
    },
    {
        "name": "日常照護，安排散步",
        "context": {
            "fatigue_level": 1,
            "med_adherence": True,
            "care_task_type": 1,
            "recent_incident": 0,
        },
    },
]

for case in test_cases:
    result = predict_suggestion(case["context"])
    print(f"🧪 {case['name']} → 建議：{result}")
