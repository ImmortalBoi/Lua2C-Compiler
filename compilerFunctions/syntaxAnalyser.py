from lexicalAnalyser import Token,KEYWORDS,STAT,LASTSTAT,EXP,FIELDSEP,OPERATORS,BINOP,UNOP,NUMBERS

Rules = ["chunk -> statFull laststatFull",

	"statFull -> # | stat semicolon statFull",
	"semicolon -> # | `;´",
	"laststatFull -> # | laststat semicolon ",

	"block -> chunk",

	"""stat ->  varlist `=´ explist | functioncall | `do´ block `end´ | `while´ exp `do´ block `end´ | `repeat´ block `until´ exp | `if´ exp `then´ block elseifThen elseChoice `end´ | `for´ Name `=´ exp `,´ exp commaExpChoice `do´ block `end´ | `for´ namelist `in´ explist `do´ block `end´ | `function´ funcname funcbody | `local´ `function´ Name funcbody | `local´ namelist equalExpListChoice """,
	"elseifThen -> # | elseifThen `elseif´ exp `then´ block",
	"elseChoice -> # | `else´ block",
	"commaExpChoice -> # | `,´ exp",
	"equalExpListChoice -> # | `=´ explist", 

	"laststat -> `return´ explistChoice | `break´",
	"explistChoice -> # | explist",

	"funcname -> Name NameDotFull NameColonChoice",
	"NameDotFull -> # | NameDotFull `.´ Name ",
	"NameColonChoice -> # |`:´ Name ",

	"varlist -> var varFull",
	"varFull -> # | varFull `,´ var ",

	"var ->  Name | prefixexp `[´ exp `]´ | prefixexp `.´ Name ",

	"namelist -> Name NameFull",
	"NameCommaFull -> # | NameCommaFull `,´ Name ",

	"explist -> expFull exp",
	"expFull -> # | expFull exp `,´ ",

	"""exp ->  `nil´ | `false´ | `true´ | Number | String | `...´ | function | prefixexp | tableconstructor | exp binop exp | unop exp """,

	"prefixexp -> `(´ exp `)´ | Name | prefixexp `[´ exp `]´ | prefixexp `.´ Name | prefixexp args | prefixexp `:´ Name args ",

	"functioncall ->  prefixexp args | prefixexp `:´ Name args ",

	"args ->  `(´ explistChoice `)´ | tableconstructor | String ",

	"function -> 'function' funcbody",

	"funcbody -> `(´ parlistChoice `)´ block 'end'",
	"parlistChoice -> # | parlist ",

	"parlist -> namelist commaTripleDotChoice | `...´",
	"commaTripleDotChoice -> # | `,´ `...´ ",

	"tableconstructor -> `{´ fieldlistChoice `}´",
	"fieldlistChoice -> # | fieldlist ",
	"fieldlist -> field fieldsepFull fieldsepChoice",

	"fieldsepFull -> fieldsepFull fieldsep field | #",
	"fieldsepChoice -> # |fieldsep ",

	"field -> `[´ exp `]´ `=´ exp | Name `=´ exp | exp",

	"fieldsep -> `,´ | `;´",

	"""binop -> `+´ | `-´ | `*´ | `/´ | `^´ | `%´ | `..´ | `<´ | `<=´ | `>´ | `>=´ | `==´ | `~=´ | `and´ | `or´""",

	"unop -> `-´ | `not´ | `#´",
	
	'Name -> Char CharDigitFull',
	"CharDigitFull -> # | CharDigitFull Char | CharDigitFull Digit ",
	
	'Char -> `a´|`b´|`c´|`d´|`e´|`f´|`g´|`h´|`i´|`j´|`k´|`l´|`m´|`n´|`o´|`p´|`q´|`r´|`s´|`t´|`u´|`w´|`x´|`y´|`z´|`A´|`B´|`C´|`D´|`E´|`F´|`G´|`H´|`I´|`J´|`K´|`L´|`M´|`N´|`O´|`P´|`Q´|`R´|`S´|`T´|`U´|`W´|`X´|`Y´|`Z´|`_´',

	'Digit -> `0´|`1´|`2´|`3´|`4´|`5´|`6´|`7´|`8´|`9´']
	# "Char -> `Char´",
	# "Digit -> `Digit´"]

nonTerminal = ['chunk','block','stat','laststat','funcname','varlist','var','namelist','explist','exp','prefixexp','functioncall','args	','function','funcbody','parlist','tableconstructor','fieldlist','field','fieldsep','binop','unop']
terminal = {'STAT':STAT,'LASTSTAT':LASTSTAT,'EXP':EXP,'FIELDSEP':FIELDSEP,'OPERATORS':OPERATORS,'BINOP':BINOP,'UNOP':UNOP,'NUMBERS':NUMBERS}

def isTerminal(word:str)->bool:
	if ('`' in word and '´' in word):
		return True
	return False

def checkNotEmptyStrings(arr):
    if arr == '':
        return False
    return True

def first(rule,diction):
	# print("Recursion Entered")
	# global rules, nonterm_userdef, \
	# 	term_userdef, diction, firsts
	# recursion base condition
	# (for terminal or epsilon)
	# print(rule[0])
	if len(rule) != 0 and (rule is not None):
		if isTerminal(rule[0]):
			# print("Entered one")
			return rule[0]
		elif rule[0] == '#':
			return '#'

	# condition for Non-Terminals
	if len(rule) != 0:
		# print(rule[0])
		if rule[0] in list(diction.keys()):
			# print("Entered Two")
			# fres temporary list of result
			fres = []
			rhs_rules = diction[rule[0]]
			# print(rhs_rules)
			# call first on each rule of RHS
			# fetched (& take union)
			for itr in rhs_rules:
				print(f"Entering Recursion for {itr}")
				indivRes = first(itr,diction)
				print(f"Exited Recursion for {itr}")
				if type(indivRes) is list:
					for i in indivRes:
						fres.append(i)
				else:
					fres.append(indivRes)

			# if no epsilon in result
			# - received return fres
			if '#' not in fres:
				return fres
			else:
				# apply epsilon
				# rule => f(ABC)=f(A)-{e} U f(BC)
				newList = []
				fres.remove('#')
				if len(rule) > 1:
					ansNew = first(rule[1:],diction)
					if ansNew != None:
						if type(ansNew) is list:
							newList = fres + ansNew
						else:
							newList = fres + [ansNew]
					else:
						newList = fres
					return newList
				# if result is not already returned
				# - control reaches here
				# lastly if eplison still persists
				# - keep it in result of first
				fres.append('#')
				return fres


def removeLeftRecursions(rulesDiction):
	# for rule: A->Aa|b
	# result: A->bA',A'->aA'|#

	# 'store' has new rules to be added
	store = {}

	# traverse over rules
	for lhs in rulesDiction:
		# alphaRules stores subrules with left-recursion
		# betaRules stores subrules without left-recursion
		alphaRules = []
		betaRules = []
		# get rhs for current lhs
		allrhs = rulesDiction[lhs]
		for subrhs in allrhs:
			if subrhs[0] == lhs:
				alphaRules.append(subrhs[1:])
			else:
				betaRules.append(subrhs)
		# alpha and beta containing subrules are separated
		# now form two new rules
		if len(alphaRules) != 0:
			# to generate new unique symbol
			# add ' till unique not generated
			lhs_ = lhs + "'"
			while (lhs_ in rulesDiction.keys()) \
					or (lhs_ in store.keys()):
				lhs_ += "'"
			# make beta rule
			for b in range(0, len(betaRules)):
				betaRules[b].append(lhs_)
			rulesDiction[lhs] = betaRules
			# make alpha rule
			for a in range(0, len(alphaRules)):
				alphaRules[a].append(lhs_)
			alphaRules.append(['#'])
			# store in temp dict, append to
			# - rulesDiction at end of traversal
			store[lhs_] = alphaRules
	# add newly generated rules generated
	# - after removing left recursion
	for left in store:
		rulesDiction[left] = store[left]
	return rulesDiction

def LeftFactoring(rulesDiction):
	# for rule: A->aDF|aCV|k
	# result: A->aA'|k, A'->DF|CV

	# newDict stores newly generated
	# - rules after left factoring
	newDict = {}
	# iterate over all rules of dictionary
	for lhs in rulesDiction:
		# get rhs for given lhs
		allrhs = rulesDiction[lhs]
		# temp dictionary helps detect left factoring
		temp = dict()
		for subrhs in allrhs:
			if subrhs[0] not in list(temp.keys()):
				temp[subrhs[0]] = [subrhs]
			else:
				temp[subrhs[0]].append(subrhs)
		# if value list count for any key in temp is > 1,
		# - it has left factoring
		# new_rule stores new subrules for current LHS symbol
		new_rule = []
		# temp_dict stores new subrules for left factoring
		tempo_dict = {}
		for term_key in temp:
			# get value from temp for term_key
			allStartingWithTermKey = temp[term_key]
			if len(allStartingWithTermKey) > 1:
				# left factoring required
				# to generate new unique symbol
				# - add ' till unique not generated
				lhs_ = lhs + "'"
				while (lhs_ in rulesDiction.keys()) \
						or (lhs_ in tempo_dict.keys()):
					lhs_ += "'"
				# append the left factored result
				new_rule.append([term_key, lhs_])
				# add expanded rules to tempo_dict
				ex_rules = []
				for g in temp[term_key]:
					ex_rules.append(g[1:])
				tempo_dict[lhs_] = ex_rules
			else:
				# no left factoring required
				new_rule.append(allStartingWithTermKey[0])
		# add original rule
		newDict[lhs] = new_rule
		# add newly generated rules after left factoring
		for key in tempo_dict:
			newDict[key] = tempo_dict[key]
	return newDict

def syntaxAnalysis(tokenList:list[Token] = None):
    
	ruleDictionary = {}
	firstDictionary = {}

	for rule in Rules:
		k = rule.split("->")
		k[0] = k[0].strip()
		multiRhs = k[1].split('|')
		for i in range(len(multiRhs)):
			multiRhs[i] = multiRhs[i].split(' ')
		for i in range(len(multiRhs)):
			multiRhs[i] = list(filter(checkNotEmptyStrings,multiRhs[i]))
		ruleDictionary[k[0]] = multiRhs
	
	for key, value in ruleDictionary.items():
		print(key, '\t:\t', value)
	print('\n')
	
	ruleDictionary = removeLeftRecursions(ruleDictionary)
	for key, value in ruleDictionary.items():
		print(key, '\t:\t', value)
	print('\n')
	
	ruleDictionary = LeftFactoring(ruleDictionary)
	for key, value in ruleDictionary.items():
		print(key, '\t:\t', value)
	print("\n")
	
	for y in list(ruleDictionary.keys()):
		# try:
		t = set()
		for sub in ruleDictionary.get(y):
			res = first(sub,ruleDictionary)
			if res != None:
				if type(res) is list:
					for u in res:
						t.add(u)
				else:
					t.add(res)
		# except:
		# 	print(y)
		# 	continue

		# save result in 'firsts' list
		firstDictionary[y] = t

	print("\nCalculated firsts: ")
	key_list = list(firstDictionary.keys())
	index = 0
	for gg in firstDictionary:
		print(f"first({key_list[index]}) "
			f"=> {firstDictionary.get(gg)}")
		index += 1


# print(isTerminal('`(´'))
syntaxAnalysis()