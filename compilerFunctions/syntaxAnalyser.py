from lexicalAnalyser import Token,KEYWORDS,STAT,LASTSTAT,EXP,FIELDSEP,OPERATORS,BINOP,UNOP,NUMBERS

Rules = ["chunk -> { stat [ `;´ ] } [ laststat [ `;´ ] ]",

	"block -> chunk",

	"""stat ->  varlist `=´ explist | functioncall | "do" block "end" | "while" exp "do" block "end" | "repeat" block "until" exp | "if" exp "then" block {"elseif" exp "then" block} ["else" block] "end" | "for" Name `=´ exp `,´ exp [`,´ exp] "do" block "end" | "for" namelist "in" explist "do" block "end" | "function" funcname funcbody | "local" "function" Name funcbody | "local" namelist [`=´ explist] """,

	"laststat -> return [ explist ] | break",

	"funcname -> Name { `.´ Name } [ `:´ Name ]",

	"varlist -> var { `,´ var }",

	"var ->  Name | prefixexp `[´ exp `]´ | prefixexp `.´ Name ",

	"namelist -> Name { `,´ Name }",

	"explist -> { exp `,´ } exp",

	"""exp ->  "nil" | "false" | "true" | Number | String | `...´ | function | prefixexp | tableconstructor | exp binop exp | unop exp """,

	"prefixexp -> var | functioncall | `(´ exp `)´",

	"functioncall ->  prefixexp args | prefixexp `:´ Name args ",

	"args ->  `(´ [ explist ] `)´ | tableconstructor | String ",

	"function -> 'function' funcbody",

	"funcbody -> `(´ [ parlist ] `)´ block 'end'",

	"parlist -> namelist [`,´ `...´] | `...´",

	"tableconstructor -> `{´ [ fieldlist ] `}´",

	"fieldlist -> field { fieldsep field } [ fieldsep ]",

	"field -> `[´ exp `]´ `=´ exp | Name `=´ exp | exp",

	"fieldsep -> `,´ | `;´",

	"""binop -> `+´ | `-´ | `*´ | `/´ | `^´ | `%´ | `..´ | `<´ | `<=´ | `>´ | `>=´ | `==´ | `~=´ | "and" | "or""",

	"unop -> `-´ | 'not' | `#´"]

nonTerminal = ['chunk','block','stat','laststat','funcname','varlist','var','namelist','explist','exp','prefixexp','functioncall','args	','function','funcbody','parlist','tableconstructor','fieldlist','field','fieldsep','binop','unop']
terminal = {'STAT':STAT,'LASTSTAT':LASTSTAT,'EXP':EXP,'FIELDSEP':FIELDSEP,'OPERATORS':OPERATORS,'BINOP':BINOP,'UNOP':UNOP,'NUMBERS':NUMBERS}

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

def checkNotEmptyStrings(arr):
    if arr == '':
        return False
    return True

def removeLeftRecursion():
	ruleDictionary = {}
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


def syntaxAnalysis(tokenList:list[Token]):
    return False

removeLeftRecursion()
