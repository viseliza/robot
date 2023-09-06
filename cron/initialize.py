import schedule
import time
import logging
import asyncio 

from tasks import clearDir

def cron_schedule_start():
    logging.info('Определение CRON задач..')

    schedule.every(1).second.do(clearDir)

    logging.info('Определение CRON закончено, перехожу к запуску..')

async def runSchedule():
    cron_schedule_start()
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    asyncio.run(runSchedule())