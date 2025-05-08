import requests

# Optional text formatting
INFO_ADD = "[+] "
red = ""
white = ""
reset = ""
BEFORE = ""
AFTER = ""
INPUT = ""

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
    print(f"\n=== {title} ===\n")

def Error(e):
    print(f"[ERROR] {e}")

def ErrorModule(e):
    print(f"[IMPORT ERROR] {e}")

def ErrorUrl():
    print("[ERROR] Invalid or expired Discord invite.")

def Continue():
    input("\nPress Enter to continue...")

def Reset():
    print("\nResetting...\n")

# Start of script
print(BANNER)
Title("Discord Server Info Lookup")

try:
    invite = input(f"{INPUT}Server Invitation URL or Code -> {reset}")
    invite_code = invite.split("/")[-1] if "/" in invite else invite

    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

    if response.status_code == 200:
        api = response.json()
        inviter = api.get('inviter', {})
        guild = api.get('guild', {})
        channel = api.get('channel', {})

        print(f"""
Invitation Information:
{INFO_ADD} Invitation Code   : {invite_code}
{INFO_ADD} Expires At        : {api.get('expires_at', 'None')}
{INFO_ADD} Server ID         : {guild.get('id', 'None')}
{INFO_ADD} Server Name       : {guild.get('name', 'None')}
{INFO_ADD} Server Icon       : {guild.get('icon', 'None')}
{INFO_ADD} Server Features   : {' / '.join(guild.get('features', []))}
{INFO_ADD} Server Description: {guild.get('description', 'None')}
{INFO_ADD} NSFW Level        : {guild.get('nsfw_level', 'None')}
{INFO_ADD} Premium Boosts    : {guild.get('premium_subscription_count', 'None')}

Channel Information:
{INFO_ADD} Channel ID        : {channel.get('id', 'None')}
{INFO_ADD} Channel Name      : {channel.get('name', 'None')}
{INFO_ADD} Channel Type      : {channel.get('type', 'None')}

Inviter Information:
{INFO_ADD} Username          : {inviter.get('username', 'None')}
{INFO_ADD} ID                : {inviter.get('id', 'None')}
{INFO_ADD} Global Name       : {inviter.get('global_name', 'None')}
""")
    else:
        ErrorUrl()

    Continue()
    Reset()

except Exception as e:
    Error(e)

input("\nPress Enter to exit...")
