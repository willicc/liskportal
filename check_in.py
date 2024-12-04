import aiohttp
from colorama import Fore, Style
from config import GRAPHQL_URL

async def check_points(address):
    """Check points for an account."""
    short_address = f"{address[:8]}...{address[-4:]}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "query": """
        query PointsLeaderboard($filter: UserFilter!) {
          userdrop {
            user(filter: $filter) {
              address
              points
              pointsHistories {
                histories {
                  points
                }
              }
            }
          }
        }
        """,
        "variables": {
            "filter": {"address": address}
        }
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(GRAPHQL_URL, json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                try:
                    user_data = data["data"]["userdrop"]["user"]
                    histories = user_data["pointsHistories"]["histories"]
                    total_points = sum(history["points"] for history in histories)
                    current_points = user_data["points"]
                    pending_points = total_points - current_points
                    print(f"{Fore.GREEN}[{short_address}] Current Points: {current_points} | Pending Points: {pending_points} | Total Points: {total_points}{Style.RESET_ALL}")
                except KeyError as e:
                    print(f"{Fore.RED}Unexpected response structure. Missing key: {e}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[{short_address}] Checking Points failed: {response.status}{Style.RESET_ALL}")


async def check_in(address):
    """Perform daily check-in."""
    short_address = f"{address[:8]}...{address[-4:]}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "query": """
        mutation UpdateAirdropTaskStatus($input: UpdateTaskStatusInputData!) {
          userdrop {
            updateTaskStatus(input: $input) {
              success
              progress {
                isCompleted
                completedAt
              }
            }
          }
        }
        """,
        "variables": {
            "input": {
                "address": address,
                "taskID": 1
            }
        }
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(GRAPHQL_URL, json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                print(f"{Fore.GREEN}[{short_address}] Check-in successful: {data['data']['userdrop']['updateTaskStatus']['progress']}{Style.RESET_ALL}")
                await check_points(address)
            else:
                print(f"{Fore.RED}[{short_address}] Check-in failed: {response.status}{Style.RESET_ALL}")
