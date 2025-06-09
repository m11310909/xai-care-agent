from apscheduler.schedulers.background import BackgroundScheduler
from line_bot import push_message_to_user

scheduler = BackgroundScheduler()
scheduler.start()


def schedule_push(user_id):
    scheduler.add_job(
        func=lambda: push_message_to_user(user_id, "記得填寫長輩狀況回報"),
        trigger="date",
        run_date=datetime.now() + timedelta(days=1),
        id=f"push_{user_id}",
    )
