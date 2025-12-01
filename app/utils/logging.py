from datetime import datetime

async def write_audit(db, action: str, resource_id: str):
    await db.activity_logs.insert_one({
        "action": action,
        "resource": "note",
        "resource_id": resource_id,
        "timestamp": datetime.utcnow()
    })
