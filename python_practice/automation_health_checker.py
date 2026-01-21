from loguru import logger


# systems = [
#     {"name": "Database", "status": "up", "errors": 0},
#     {"name": "API Server", "status": "down", "errors": 5},
#     {"name": "Auth Service", "status": "up", "errors": 2},
# ]


# def check_system(system):
#     """
#     Returns health message based on system status & errors
#     """
#     if system["status"] == "down":
#         return "Critical"
#     elif system["errors"] > 3:
#         return "Warning"
#     else:
#         return "Healthy"


# for system in systems:
#     health = check_system(system)
#     logger.info(f"{system['name']} -> {health}")

# logger.info(f"Checked: {len(system)} systems")
# summary = {"Critical": 0, "Warning": 0, "Healthy": 0}
# for system in systems:
#     health = check_system(system)
#     if health in summary:
#         summary[health] += 1
#     else:
#         summary[health] = 1
# logger.info(f"{summary}")


# Daily System Health Report Automation
# systems = [
#     {"name": "Database", "status": "up", "errors": 0},
#     {"name": "API Server", "status": "down", "errors": 5},
#     {"name": "Auth Service", "status": "up", "errors": 2},
#     {"name": "Payment Gateway", "status": "up", "errors": 6},
# ]


# def check_system(system):
#     if system["status"] == "down":
#         return "Critical"
#     elif system["errors"] > 3:
#         return "Warning"
#     else:
#         return "Healthy"


# def generate_report(systems):
#     summary = {"Critical": 0, "Warning": 0, "Healthy": 0}
#     details = []
#     for system in systems:
#         health = check_system(system)
#         summary[health] += 1
#         details.append({"name": system})
#         logger.info(f"{system['name']} -> {health}")


# logger.info(f"Checked: {len(systems)} systems")
# logger.info(f"{summary}")
