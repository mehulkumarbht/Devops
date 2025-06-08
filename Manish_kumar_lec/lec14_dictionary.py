from loguru import logger


#Total labour cost if total working days was 50 out of which Mahesh
# was absent for 3 days and Jagmohan was absent for 7 days
# find out the total labour cost?

labour_with_cost = {"Mahesh":500,"Ramesh":400,"Mithilesh":400,"Sumesh":300,"Jagmohan":1000, "Rampyare":800}
days_worked = {"Mahesh":47,"Ramesh":50,"Mithilesh":50,"Sumesh":50,"Jagmohan":43,"Rampyare":50}
total_days = 50
total_labour_cost = 0
for i in labour_with_cost:
    if i in days_worked:
        total_labour_cost += (labour_with_cost[i]*(days_worked[i]))
logger.info(f"{total_labour_cost}")




