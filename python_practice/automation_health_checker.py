from loguru import logger


systems = [
    {"name": "Database", "status": "up", "errors": 0},
    {"name": "API Server", "status": "down", "errors": 5},
    {"name": "Auth Service", "status": "up", "errors": 2},
]


def check_system(system):
    """
    Returns health message based on system status & errors
    """
    if system["status"] == "down":
        return "Critical"
    elif system["errors"] > 3:
        return "Warning"
    else:
        return "Healthy"


for system in systems:
    health = check_system(system)
    logger.info(f"{system['name']} -> {health}")

logger.info(f"Checked: {len(system)} systems")
critical_count = 0
warning_count = 0
healthy_count = 0
summary = {}
for system in systems:
    health = check_system(system)
    if health == "Critical":
        critical_count += 1
    elif health == "Warning":
        warning_count += 1
    else:
        healthy_count += 1
    summary[health] = healthy_count
logger.info(f"{summary}")
logger.info(f"Critical: {critical_count}")
logger.info(f"Warning: {warning_count}")
logger.info(f"Healthy: {healthy_count}")
