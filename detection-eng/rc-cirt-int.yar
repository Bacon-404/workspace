rule rc-scenario1
{
	meta:
		description = "Rule for detecting the first scenario of the RC-DE interview"
		threat_level = 1
		in_the_wild = false

	strings:
		$s1 = "http://bit.ly/e0Mw9w" // Wrote it this way as link is static to leeholmes.com

	condition:
		all of them
}

rule rc-scenario2
{
	meta:
		description = "Rule for detecting the second scenario of the RC-DE interview"
		threat_level = 1
		in_the_wild = false

	strings:
		$rc2 = "UI0Detect.exe" // would need more data to make this more specific to this threat.

	condition:
		all of them
}

rule rc-scenario3
{
	meta:
		description = "Rule for detecting the third scenario of the RC-DE interview"
		threat_level = 1
		in_the_wild = false

	strings:
		$rc3 = "totes-evil.sh" //
		$rc3_1 = "atomic.log" //decoded from base64
	
	condition:
		$rc3 or $rc3_1 //opted for XOR as these are fairly unique strings.
}

rule rc-scenario4
{
	meta:
		description = "Rule for detecting the fourth scenario of the RC-DE interview"
		threat_level = 1
		in_the_wild = false

	strings:
		hash.md5(0846e04c22488b04222817529f235024) 
		/*md5 of the process hash for the second process in the scenario.
		*used this one instead of the first as this is within usr/bin and is more likely to be unique.
		*/

	condition:
		all of them
}

rule rc-scenario5
{
	meta:
		description = "Rule for detecting the fifth scenario of the RC-DE interview"
		threat_level = 1
		in_the_wild = false

	strings:
		hashmd5(7ee4feeded88cb104448141ef375be8c) 
		/*
		Fairly weak detection but works for this scenario due to lack of data. As it is a known hash, it is unlikely to be used by other malware.
		*/
	condition:
		all of them
}