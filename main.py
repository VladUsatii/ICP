#!python3
import itertools
import threading
import sys
import time
import os
import string

# rich
from rich import print
from rich.table import Table
from rich.console import Console

# security
import socket as sock
import uuid

# on launch
class Launch(object):
	def process(self, j):
		# write details to file
		for i in range(0, j):
			for x in range(0, 4):
				y = "Loading" + "." * x
				print("[bold green]" + y + "[/bold green]", end="\r")
				time.sleep(0.5)

# send coin
class Tokenize():
	def ask(self):
		ipfailstest = True
		while ipfailstest:
			print("[bold magenta]Enter the IP address of the person whom you wish to send coin to:[/bold magenta]")
			findip = input("(Ex. 255.255.255.0)\n\n")
			with open('hashprof.txt') as database:
				if findip in database.read() and findip.isnumeric() and len(findip) > 8:
					print("[bold green]Type in transfer amount: \n[/bold green]")
					ipfailstest = False
				elif findip in ['q']:
					os.system('cls' if os.name == 'nt' else 'clear')
					main()
				else:
					print("[bold red]IP not found. Please try again.[/bold red]")

class WriteSystemProtocol(object):
	def print(self):
		print("Draw money")

class Options(object):
	# get ip for security
	users = open("hashprof.txt", "w")
	id = sock.gethostbyname(sock.gethostname())
	proof = uuid.uuid4().hex

	users.write(id + "\n" + proof)
	users.close()

	def home(self):
		optionTable, accountTable = Table(title="[blue]---------- Home ---------[/blue]"), Table()
		optionTable.add_column("Send coin", justify="center", no_wrap=True)
		optionTable.add_column("Add coin", justify="center", no_wrap=True)
		optionTable.add_row("[italic]Press 'a' key[/italic]", "[italic]Press 'd' key[/italic]")
		# your private info (closed-circuit & unshareable)
		accountTable.add_column(os.environ.get("USER") + "\'s Profile :smiley:", justify="center", no_wrap=False)
		accountTable.add_row(str(sock.gethostbyname(sock.gethostname())))
		accountTable.add_row(self.proof)

		Console().print(optionTable)
		Console().print(accountTable)

	def confirmAction(self):
		warn = "[bold red]Type a letter that is listed above in the key.\n[/bold red]"
		inAction = True
		results = ['a', 'd', 'q']
		while inAction:
			action = input("Type here: ")
			if action == results[0]:
				Tokenize().ask()
			elif action == results[1]:
				WriteSystemProtocol().print()
			elif action == results[2]:
				sys.exit()
			else:
				print(warn)

launch = Launch()
options = Options()

def main():
	launch.process(1)
	options.home()
	options.confirmAction()

# init
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('\n[bold red]Operation cancelled. Usatii is now closed.[/bold red]')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
