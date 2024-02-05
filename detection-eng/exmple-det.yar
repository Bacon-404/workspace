rule emotet
{
	meta:
		description = "Detects Emotet malware"
		threat_level = 5
		in_the_wild = true
		
		strings:
			$s1 = "http://72.143.73.234:443/oc9MnTuEfv/ragIogg70lSJlBRz/QqA8rXWcir/x3ad24jNY/nDuZV5oyTkdoorluuUP/" fullword ascii
			$s2 = "C:\WINDOWS\12345678.EXE" fullword ascii
		condition:
			any of them

}

rule notpetya
{
	meta:
		description = "Detects NotPetya malware"
		threat_level = 5
		in_the_wild = true
		
		strings:
			$s1 = "C:\Windows\perfc" fullword ascii
			$s2 = "C:\Windows\perfc.dat" fullword ascii // NotPetya DLL
		condition:
			any of them

}