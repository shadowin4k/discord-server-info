import requests
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Mock UI styling (you can customize these if needed)
INFO_ADD = Fore.LIGHTBLACK_EX + "[+] " + Style.RESET_ALL  # Gray for [+]
red = Fore.LIGHTBLACK_EX  # Silver for the rest
white = Fore.LIGHTBLACK_EX  # Silver for text
reset = Style.RESET_ALL
BEFORE = ""
AFTER = ""
INPUT = Fore.CYAN

BANNER = r'''
 ________  _______   ________  ___      ___ _______   ________          ___  ________   ________ ________     
|\   ____\|\  ___ \ |\   __  \|\  \    /  /|\  ___ \ |\   __  \        |\  \|\   ___  \|\  _____\\   __  \    
\ \  \___|\ \   __/|\ \  \|\  \ \  \  /  / | \   __/|\ \  \|\  \       \ \  \ \  \\ \  \ \  \__/\ \  \|\  \   
 \ \_____  \ \  \_|/_\ \   _  _\ \  \/  / / \ \  \_|/_\ \   _  _\       \ \  \ \  \\ \  \ \   __\\ \  \\\  \  
  \|____|\  \ \  \_|\ \ \  \\  \\ \    / /   \ \  \_|\ \ \  \\  \|       \ \  \ \  \\ \  \ \  \_| \ \  \\\  \ 
    ____\_\  \ \_______\ \__\\ _\\ \__/ /     \ \_______\ \__\\ _\        \ \__\ \__\\ \__\ \__\   \ \_______\
   |\_________\|_______|\|__|\|__|\|__|/       \|_______|\|__|\|__|        \|__|\|__| \|__|\|__|    \|_______|
   \|_________|                                                                                               
                                                                                                              
'''

def Title(title):
    print(f"{red}\n=== {title} ===\n")

def Error(e):
    print(f"[{red}ERROR{reset}] {e}")

def ErrorModule(e):
    print(f"[{red}IMPORT ERROR{reset}] {e}")

def ErrorUrl():
    print(f"[{red}ERROR{reset}] Invalid or expired Discord invite.")

def Continue():
    input(f"\n{INPUT}Press Enter to continue...{reset}")

def Reset():
    print("\nResetting...\n")

# Start of script
print(BANNER)
Title("Discord Server Info Lookup")

try:
    invite = input(f"{BEFORE}{INPUT}Server Invitation -> {reset}")
    invite_code = invite.split("/")[-1] if "/" in invite else invite

    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

    if response.status_code == 200:
        api = response.json()

        inviter = api.get('inviter', {})
        guild = api.get('guild', {})
        channel = api.get('channel', {})

        print(f"""
{INFO_ADD}Invitation Information:
{INFO_ADD} Invitation Code   : {white}{invite_code}
{INFO_ADD} Expires At        : {white}{api.get('expires_at', 'None')}
{INFO_ADD} Server ID         : {white}{guild.get('id', 'None')}
{INFO_ADD} Server Name       : {white}{guild.get('name', 'None')}
{INFO_ADD} Server Icon       : {white}{guild.get('icon', 'None')}
{INFO_ADD} Server Description: {white}{guild.get('description', 'None')}
{INFO_ADD} NSFW Level        : {white}{guild.get('nsfw_level', 'None')}
{INFO_ADD} Premium Boosts    : {white}{guild.get('premium_subscription_count', 'None')}

{INFO_ADD}Channel Information:
{INFO_ADD} Channel ID        : {white}{channel.get('id', 'None')}
{INFO_ADD} Channel Name      : {white}{channel.get('name', 'None')}
{INFO_ADD} Channel Type      : {white}{channel.get('type', 'None')}

{INFO_ADD}Inviter Information:
{INFO_ADD} Username          : {white}{inviter.get('username', 'None')}
{INFO_ADD} ID                : {white}{inviter.get('id', 'None')}
{INFO_ADD} Global Name       : {white}{inviter.get('global_name', 'None')}
""")

    else:
        ErrorUrl()

    Continue()
    Reset()

except Exception as e:
    Error(e)

input(f"\n{INPUT}Press Enter to exit...{reset}")
