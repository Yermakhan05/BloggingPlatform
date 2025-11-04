# cloud_functions/main.py

def log_new_post(request):
    """
    Cloud Function: логирует создание нового поста
    Триггер: HTTP
    """
    import json
    from datetime import datetime

    if request.method != "POST":
        return ("Only POST allowed", 405)

    data = request.get_json(silent=True)
    if not data or "title" not in data:
        return ("Missing title in request body", 400)

    title = data["title"]
    timestamp = datetime.utcnow().isoformat()

    print(f"[Cloud Function] Новый пост: {title} ({timestamp})")

    return (json.dumps({"message": f"Post '{title}' logged successfully."}), 200)
