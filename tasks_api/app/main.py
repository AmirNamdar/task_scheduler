#  Home Assignment for Lemonade - Timers

# This assignment is about executing delayed tasks, a common scenario you might encounter in this role.
# The challenge is designed to take 3–4 hours to complete. We don’t enforce any strict time limits, so you can choose when you prefer to dedicate time for the challenge and in how many sessions. You may add any extra functionality you want—however, this will not affect your evaluation.
# Okay, here’s your mission: We would like to create a service that allows us to easily execute scheduled tasks. For simplicity, let’s assume that tasks can be triggered by accessing a web URL. You create a task by providing a URL and the desired time to run. When the specified time arrives, the service will call the URL.

# 1. A “Set Timer” endpoint
# ○ Receives a JSON object containing hours, minutes, seconds, and a web url.
# ○ Returns a JSON object with the amount of seconds left until the timer expires and
# an id for querying the timer in the future.
# ○ The endpoint should start an internal timer, which fires a webhook to the defined
# URL when the timer expires. The webhook should be a POST HTTP call with an
# empty body.
# ○ For example, the following request:
#  POST /timers
# {
#   hours: 4,
#   minutes: 0,
#   seconds: 1,
#   url: "https://someserver.com"
# }
#  should return a response such as:
# { id: 1, time_left: 14401 }
# After 4 hours and 1 second, the server should make the following request:
#  POST https://someserver.com/1
# with an empty body. Note that the timer id should be appended to the URL:
#  https://someserver.com/<TIMER_ID>

#  2. A “Get Timer Status” endpoint
# ○ Receives the timer id in the URL, as the resource id.
# ○ Returns a JSON object with the amount of seconds left until the timer expires. If
# the timer already expired, returns 0.
# ○ For example, the following request:
# GET /timers/1
# should return a response such as:
# { id: 1, time_left: 645 } Additional requirements
# ● The code should handle invalid inputs.
# ● The firing of the webhook must not be canceled by process restarts. Any timers that
# expired while the application was down should be triggered once the application comes
# back up.
# ● The solution should support horizontal scalability (running on multiple servers) to handle
# an increasing number of timers, including their creation and webhook firing.
# ○ NOTE: For senior engineering roles, each timer must be fired only once.
# Things to keep in mind
# ● The solution will be evaluated based on correctness, craftsmanship, and horizontal scalability. You are free to use any resources, including Google, ChatGPT, and GitHub Copilot, as long as the solution meets the requirements listed.
# ● Please use Typescript, Javascript, Ruby, Python, Java, or C#. If you have a preference for a different programming language, please keep in mind that it might cause delays in the evaluation process or may not be possible at all, depending on the availability of reviewers. We strongly suggest consulting with the recruiters before proceeding with alternatives.
# ● Please ensure that the solution is easy to set up and run. Containerization is not mandatory but highly recommended, especially if you are using a language that is not on the list above.
# ● Please provide a README file that contains:
# ○ Instructions for running the solution (it will be tested in a macOS environment).
# ○ Any assumptions made. For example, “timers are never scheduled later than X days
# into the future”.
# ○ Any changes you would make (if any) in order to support a high-traffic (e.g. 100
# timer creation requests per second) production environment.
# ● Please do not hesitate to contact me if you have any questions. Good luck!


import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_layer.routes.timer_router import timer_router


logger = logging.getLogger(__name__)
SERVICE_NAME = "scheduling-service"
app = FastAPI(title=f"FastAPI {SERVICE_NAME}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routers = [timer_router]


for router in routers:
    app.include_router(router=router)
