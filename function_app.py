import logging
import azure.functions as func

app = func.FunctionApp()

@app.schedule(schedule="30 * * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False) 
def projet01(myTimer: func.TimerRequest) -> None:
    logging.info("Abhishant")