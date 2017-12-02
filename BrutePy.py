#!/usr/bin/env python3

import sys
import threading
import argparse
import os

def brute_force(passwdParametersInp, charSetArgv, n):

	def next_password(passwdList, passwdCodes, charSet, passwdLen, charSetLastChar):
		passwdList[passwdLen] = charSet[passwdCodes[passwdLen]+1]
		return passwdList

	def az_to_ba(passwd, charSet, passwdCodes, passwdLen, charSetLen):
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
		passwd = charSet[0] * (passwdLen+2)

		return list(passwd)

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

	def passwd_to_codes_fake(passwdCodes, passwdLen):
		passwdCodes[passwdLen] += 1

		return passwdCodes

	def gen_chrset(opt):
		upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		lowerCase = "abcdefghijklmnopqrstuvwxyz"
		special = "~`!@#$%&(){}[]+-*/\_=^<>:;,.\"'|?"
		numaric = "0123456789"
		all = upperCase + lowerCase + special + numaric

		l_1 = ["all", "lc", "uc", "num", "sp"]
		l_2 = [all, lowerCase, upperCase, numaric, special]

		chrSet = []
		chrSetArgv = []
		num = len(opt)-1
		for o in opt:
			chrSetArgv.append(o)

			n = 0
			for a in l_1:
				chrSetArgvStr = "".join(chrSetArgv)
				if a in chrSetArgvStr:
					l = chrSetArgvStr.index(a)
					for b in range(len(a)):
						del chrSetArgv[l]

					chrSetArgvStr = "".join(chrSetArgv)
					chrSet += chrSetArgvStr
					chrSet += l_2[n]

					chrSetArgv = []

					del l_1[n]
					del l_2[n]
					break
				n += 1

			if not num:
				if chrSetArgv:
					chrSet += chrSetArgvStr
					break
			num -= 1

		return chrSet

	def bruteGen_main(passwdParametersInp, n):
		charSet = gen_chrset(charSetArgv)
		charSetLen = len(charSet)
		charSetLastChar = charSet[charSetLen-1]

		if(passwdParametersInp == ""):
			passwdFirstParameter = list(charSet[0])
			passwdBreak = ""
			n = 1

		else:
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
			for a in passwdParameters:
				for b in a:
					for char in charSet:
						if(b == char):
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
					passwdList = zz_to_aaa(charSet, passwdLen)
					passwdLen = len(passwd)
					passwdLenIncrease = charSetLastChar*(passwdLen+1)
					passwdCodes = passwd_to_codes(passwdList, charSet)
				else:
					break
			elif(passwdLastChar == charSetLastChar):
				passwdList = az_to_ba(passwdList, charSet, passwdCodes, passwdLen, charSetLen)
				passwdCodes = passwd_to_codes(passwdList, charSet)
			else:
				passwdList = next_password(passwdList, passwdCodes, charSet, passwdLen, charSetLastChar)
				passwdCodes = passwd_to_codes_fake(passwdCodes, passwdLen)

	bruteGen_main(passwdParametersInp, n)

def dict_attack(file):
	try:
		filePath = os.path.abspath(file)
		print("File Path:\t", filePath, "\n")
		r = open(filePath)
		data = r.readlines()
		for line in data:
			print(line, end="")

	except Exception as e:
		print(e)

def word_manggle(word):
	dic = {
	"a":["a", "A", "@", "4", "1"],
	"b":["b", "B", "8", "&", "2"],
	"c":["c", "C", "(", "{", "[", "<", "3"],
	"d":["d", "D", "4"],
	"e":["e", "E", "3", "5"],
	"f":["f", "F", "6"],
	"g":["g", "G", "7"],
	"h":["h", "H", "#", "8"],
	"i":["i", "I", "l", "1", "!", "|", "9"],
	"j":["j", "J", "10"],
	"k":["k", "K", "11"],
	"l":["l", "L", "!", "1", "|", "12"],
	"m":["m", "M", "13"],
	"n":["n", "N", "14"],
	"o":["o", "O", "0", "15"],
	"p":["p", "P", "16"],
	"q":["q", "Q", "17"],
	"r":["r", "R", "18"],
	"s":["s", "S", "$", "5", "19"],
	"t":["t", "T", "20"],
	"u":["u", "U", "21"],
	"v":["v", "V", "22"],
	"w":["w", "W", "23"],
	"x":["x", "X", "24"],
	"y":["y", "Y", "25"],
	"z":["z", "Z", "2", "26"],
	"0":["o", "O"],
	"1":["!", "i", "I", "|", "l"],
	"2":[""],
	"3":["e", "E"],
	"4":["a", "A", "@"],
	"5":["s", "S", "$"],
	"6":[""],
	"7":[""],
	"8":["B", "b", "&"],
	"9":[""]
	}

	def passwd_maximum_codes(w):
		passwdMaxCodes = []
		breakPasswd = ""
		for a in w:
			num = dic[a]
			n = len(num)
			breakPasswd += num[n-1]
			passwdMaxCodes.append(n)

		return(passwdMaxCodes, breakPasswd)

	def passwd_to_codes(passwdToWord, passwdList):
		passwdCodes = []
		n = 0
		num = 0
		nn = 0
		for a in passwdList:
			b = passwdToWord[nn]
			for c in dic[b]:
				if(a == c):
					passwdCodes.append(n)
					n = 0
					num = 1
					nn += 1
					break
				n += 1

		return passwdCodes

	def codes_to_word(word):
		dictionaries = "abcdefghijklmnopqrstuvwxyz0123456789"
		passwd = ""
		n = 0

		for a in word:
			for b in dictionaries:
				for c in dic[b]:
					if(c == a):
						passwd += b
						n = 1
						break
				if(n):
					n = 0
					break

		return passwd

	def next_passwd(passwdList, lastCharList, passwdCodes, passwdLen):
		passwdList[passwdLen-1] = lastCharList[passwdCodes[passwdLen-1]+1]

		return passwdList

	def az_to_ba(passwdList, passwdCodes, passwdLen, wList):
		n = 0

		for a in range(passwdLen-1, -1, -1):
			b = wList[a]
			charSet = dic[b]
			charSetLen = len(charSet)
			if(passwdList[a] == charSet[charSetLen-1]):
				passwdList[a] = charSet[0]
				n = 1
			elif(n):
				passwdList[a] = charSet[passwdCodes[a]+1]
				break
			else:
				break
		return passwdList

	def break_passwd(passwdMaxCodes):
		breakPasswd = ""
		for a in passwdMaxCodes:
			b = dic[a]
			breakPasswd += b

		return breakPasswd

	def word_mangle_main(word):
		passwdParameters = word.split("-")
		ww = passwdParameters[0]
		w = ww.casefold()
		passwdToWord = codes_to_word(w)
		wList = list(passwdToWord)
		passwdList = list(ww)
		wLen = passwdLen = len(passwdToWord)
		lastCharWord = wList[wLen-1]
		lastCharList = dic[lastCharWord]
		passwdMaxCodes, breakPasswd = passwd_maximum_codes(passwdToWord)
		passwdCodes = passwd_to_codes(passwdToWord, ww)
		n = len(ww)-1
		if(len(passwdParameters) == 2):
			if(passwdParameters[1]):
				breakPasswd = passwdParameters[1]

		passwd = ww

		while True:
			passwd = "".join(passwdList)
			print(passwd)

			if(passwd == breakPasswd):
				break

			if(passwdCodes[n]+1 == passwdMaxCodes[n]-1):
				passwdCodes = passwd_to_codes(passwdToWord, passwdList)
				passwdList = az_to_ba(passwdList, passwdCodes, wLen, wList)
			else:
				passwdCodes = passwd_to_codes(passwdToWord, passwdList)
				passwdList = next_passwd(passwdList, lastCharList, passwdCodes, passwdLen)
	word_mangle_main(word)

#def arguments():
	#parser = argparse.ArgumentParser()
	#parser.add_argument("-b", "--brute", default="a", help="Enable BruteForce attack mode")
	#parses.add_argument(
	#args = parser.parse_args()

	#return args

def main():
	#method, charSetArgv, passwdParametersInp, n = arguments()

	method = sys.argv[1]
	if(method == "--brute"):
		try:
			charSetArgv = sys.argv[2]
			passwdParametersInp = sys.argv[3]
			n = 0
			brute_force(passwdParametersInp, charSetArgv, n)
		except KeyboardInterrupt:
			sys.exit(100)
	elif(method == "--mangle"):
		word_manggle(sys.argv[2])
	elif(method == "--dict"):
		dict_attack(sys.argv[2])
	else:
		print("\033[1;31m[-] Argument Error")
		print("[*] bruteGen.py [Method Name (--brute, --mangle, --dict)] [Charset (lc, uc, sp, num, all)] [Password Parameters(aa-zz)]\033[0m")

main()
