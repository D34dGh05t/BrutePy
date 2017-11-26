#!/usr/bin/env python3

import sys
import threading

def BruteForce(passwdParametersInp, charSetArgv, n):

	def next_password(passwdList, passwdCodes, charSet, passwdLen, charSetLastChar):
		passwdList[passwdLen] = charSet[passwdCodes[passwdLen]+1]
		return passwdList

	def aa_to_ab(passwd, charSet, passwdCodes, passwdLen, charSetLen):
		n = 0
		for a in range(passwdLen, -1, -1):
			if(passwd[a] == charSet[charSetLen-1]):
				passwd[a] = charSet[0]
				n = 1
			elif(n):
				passwd[a] = charSet[passwdCodes[a]+1]
				break
			else:
				break
		return passwd

	def zz_to_aaa(charSet, passwdLen):
		passwd = []
		passwd.append(charSet[0])
		for a in range(passwdLen+1):
			passwd.append(charSet[0])

		return passwd

	def passwd_to_codes(passwd, charSet):
		n = 0
		passwdCodes = []
		for a in passwd:
			for b in charSet:
				if(a == b):
					passwdCodes.append(n)
					n = 0
					break
				n += 1
		return passwdCodes

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

	def bruteGen_main(passwdParametersInp, n):
		charSet = GenChrset(charSetArgv)
		charSetLen = len(charSet)
		charSetLastChar = charSet[charSetLen-1]

		if(passwdParametersInp == ""):
			passwdParametersInp = list(charSet[0])

		passwdParameters = "".join(passwdParametersInp).split("-")

		passwdFirstParameter = list(passwdParameters[0])
		passwdParametersLen = len(passwdParameters)

		if(passwdParametersLen == 1):
			passwdBreak = passwdParametersLen*charSetLastChar
		elif(passwdParametersLen == 2):
			passwdBreak = list(passwdParameters[1])
			n = 1
		else:
			print("[-] Incorrect Password Parameters")
			sys.exit(100)

		no = 0
		for a in passwdParametersInp:
			for char in charSet:
				if(a == char):
					no = 0
					break
				else:
					no = 1
			if(no):
				print("\033[31m[-] \033[32m{}\033[31m not found in {}\033[0m".format("".join(passwdFirstParameter), charSetArgv))
				exit()

		passwdCodes = passwd_to_codes(passwdFirstParameter, charSet)
		passwdLen = len(passwdFirstParameter)-1
		passwdLenIncrease = charSetLastChar*(passwdLen+1)
		passwdList = passwdFirstParameter
		while True:
			passwd = "".join(passwdList)
			passwdLastChar = passwdList[passwdLen]

			print(passwd)

			if(passwd == passwdBreak):
				break

			if(passwd == passwdLenIncrease):
				if(n):
					passwdLenIncrease = passwdLen+1*charSetLastChar
					passwdLen = len(passwd)-1
					passwdList = zz_to_aaa(charSet, passwdLen)
				else:
					break
			elif(passwdLastChar == charSetLastChar):
				passwdList = aa_to_ab(passwdList, charSet, passwdCodes, passwdLen, charSetLen)
			else:
				passwdCodes = passwd_to_codes(passwd, charSet)
				passwdList = next_password(passwdList, passwdCodes, charSet, passwdLen, charSetLastChar)

	bruteGen_main(passwdParametersInp, n)

def arguments():
	try:
		method = sys.argv[1]
	except IndexError:
		method = "--brute"
	if(method == "--brute"):
		try:
			charSetArgv = sys.argv[2]
		except IndexError:
			charSetArgv = "all"
		try:
			passwdParametersInp = list(sys.argv[3])
			n = 0
		except IndexError:
			passwdParametersInp = ""
			n = 1
	return method, charSetArgv, passwdParametersInp, n
def main():
	method, charSetArgv, passwdParametersInp, n = arguments()

	if(method == "--brute"):
		try:
			BruteForce(passwdParametersInp, charSetArgv, n)
		except KeyboardInterrupt:
			sys.exit(100)
	else:
		print("\033[1;31m[-] Argument Error")
		print("[*] bruteGen.py [Method Name (--brute)] [Charset (lc, uc, sp, num, all)] [Password Parameters(aa-zz)]")

main()
