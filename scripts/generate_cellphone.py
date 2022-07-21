prefixes = ['0910', '0911', '0912', '0913', '0914', '0915', '0916', '0917', '0918', '0919', 
			'0920', '0921', '0922', '0923', '0924', '0925', '0926', '0927', '0928', '0929', 
			'0930', '0931', '0932', '0933', '0934', '0935', '0936', '0937', '0938', '0939', 
			'0952', '0953', '0954', '0955', '0956', '0958', 
			'0960', '0961', '0963', 
			'0970', '0971', '0972', '0975', '0976', '0978', 
			'0987', '0988'
			]
baseLocation = "../wordlists/Taiwan-cellphone/"

def Generate(prefix):
	print("[+] Generating Prefix " + prefix + " Wordlist ...", end = '')
	filename = baseLocation + prefix
	with open(filename, 'w') as f:
		for i in range(1000000):
			number = prefix + "%06d" % i + "\n"
			f.write(number)
		print("Done")


if __name__ == '__main__':
	prefix = input("Input the prefix: ")
	if prefix == "":
		for prefix in prefixes:
			Generate(prefix)
	else:
		Generate(prefix)
	print("[!] Complete")
