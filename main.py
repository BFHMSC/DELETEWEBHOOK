import requests
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep

boucle1 = True

header_final = """
╔╗ ╔═╗╦ ╦╔╦╗╔═╗╦  ╔═╗╔╦╗╔═╗╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═
╠╩╗╠╣ ╠═╣ ║║║╣ ║  ║╣  ║ ║╣ ║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗
╚═╝╚  ╩ ╩═╩╝╚═╝╩═╝╚═╝ ╩ ╚═╝╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩
  𝔐𝔄𝔎𝔈 𝔅𝔜:𝔅𝔉ℌ\n\n\n\n"""

while boucle1:
    system('cls')
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.purple_to_blue, "[?] W̶e̶b̶h̶o̶o̶k̶ ̶U̶R̶L̶ ↓"))
    webhook_url = input("")
    if webhook_url.startswith("https://discord.com/api/webhooks/"):
        try:
            system('cls')
            requests.delete(webhook_url.rstrip())
            print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.purple_to_blue, "W̷e̷b̷h̷o̷o̷k̷ ̷d̷e̷l̷e̷t̷e̷d̷ !"))
            sleep(5)
        except:
            system('cls')
            print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.yellow_to_red, "[!] e̲r̲r̲o̲r̲ ̲o̲n̲ ̲d̲e̲l̲e̲t̲i̲n̲g̲ ̲t̲h̲e̲ ̲w̲e̲b̲h̲o̲o̲k̲."))
            sleep(2)
    else:
            system('cls')
            print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.yellow_to_red, "[!] P̾l̾e̾a̾s̾e̾ ̾i̾n̾s̾e̾r̾t̾ ̾a̾ ̾v̾a̾l̾i̾d̾ ̾l̾i̾n̾k̾."))
            sleep(2)