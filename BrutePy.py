#!/usr/bin/env python3

import sys
import threading

def BruteForce(paswd, chrSet, n):
	def Password(passwd, pNo, charSet):
		l = len(pNo)
		lastCh = pNo[l-1]
		passwd[l-1] = charSet[lastCh+1]
		return passwd

	def passwd1(paswd, charSet, pNo):
		passwd = paswd
		lPasswd = len(passwd)
		lChars = len(charSet)

		n = 0
		for a in range(lPasswd-1, -1, -1):
			if(paswd[a] == charSet[lChars-1]):
				passwd[a] = charSet[0]
				n = 1
			elif(n):
				passwd[a] = charSet[pNo[a]+1]
				break
			else:
				break
		return passwd

	def passwd2(paswd, charSet):
		passwd = []
		passwd.append(charSet[0])
		for a in paswd:
			passwd.append(charSet[0])

		return passwd

	def pToNum(paswd, charSet):
		n = 0
		pNo = []
		for a in paswd:
			for b in charSet:
				if(a == b):
					pNo.append(n)
					n = 0
					break
				n += 1
		return pNo

	def GenChrset(opt):
		upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		lowerCase = "abcdefghijklmnopqrstuvwxyz"
		special = "~`!@#$%&(){}[]+-*/\_=^<>:;,.\"'|?"
		numaric = "0123456789"
		all = upperCase + lowerCase + special + numaric

		if(opt == "uc"):
			chrSet = upperCase
		elif(opt == "lc"):
			chrSet = lowerCase
		elif(opt == "sp"):
			chrSet = special
		elif(opt == "num"):
			chrSet = numaric
		elif(opt == "all"):
			chrSet = all
		else:
			chrSet = opt

		return list(chrSet)

	def bruteGen_main(paswd, n):
		charSet = GenChrset(chrSet)
		l = len(charSet)
		if(paswd == ""):
			paswd = list(charSet[0])
		p = "".join(paswd).split("-")

		paswd = list(p[0])
		if(len(p) == 1):
			bPass = len(p)*charSet[len(charSet)-1]
		elif(len(p) == 2):
			bPass = list(p[1])
			n = 1
		else:
			print("[-] Incorrect Password Parameters")
			sys.exit(100)
		no = 0
		for a in paswd:
			for b in range(l):
				char = charSet[b]
				if(a == char):
					break
				elif(a != char):
					if(no == l-1):
						print("\033[31m[-] ",end="")
						print("\033[32m{}".format("".join(paswd)),end="")
						print("\033[31m not found in {}\033[0m".format(chrSet))
						exit()
					else:
						no += 1

		pasword = paswd
		passwd = paswd
		print("".join(pasword))

		cLen = len(charSet)
		lastCh = charSet[cLen-1]

		while True:
			pNo = pToNum(pasword, charSet)
			if("".join(pasword) == len(pasword)*lastCh):
				if(n):
					passwd = passwd2(pasword, charSet)
					if(pasword == bPass):
						break
					print("".join(passwd))
				else:
					break
			else:
				if(pasword[len(pasword)-1] == charSet[len(charSet)-1]):
					passwd = passwd1(pasword, charSet, pNo)
					print("".join(passwd))

			if(pasword == bPass):
				break
			pNo = pToNum(passwd, charSet)
			pasword = Password(passwd, pNo, charSet)
			print("".join(pasword))

	bruteGen_main(paswd, n)

def arguments():
	try:
		method = sys.argv[1]
	except IndexError:
		method = "--brute"
	try:
		chrSet = sys.argv[2]
	except IndexError:
		chrSet = "all"
	try:
		paswd = list(sys.argv[3])
		n = 0
	except IndexError:
		paswd = ""
		n = 1
	return method, chrSet, paswd, n
def main():
	method, chrSet, paswd, n = arguments()

	if(method == "--brute"):
		try:
			BruteForce(paswd, chrSet, n)
		except KeyboardInterrupt:
			sys.exit(100)
	else:
		print("\033[1;31m[-] Argument Error")
		print("[*] bruteGen.py [Method Name (--brute)] [Charset (lc, uc, sp, num, all)] [Password Parameters]")

main()
