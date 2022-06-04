from lexicalAnalyser import Token,KEYWORDS,STAT,LASTSTAT,EXP,FIELDSEP,OPERATORS,BINOP,UNOP,NUMBERS
import copy

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

	"namelist -> Name NameCommaFull",
	"NameCommaFull -> # | NameCommaFull `,´ Name ",

	"explist -> expFull exp",
	"expFull -> # | expFull exp `,´ ",

	"""exp ->  `nil´ | `false´ | `true´ | Number | String | `...´ | function | prefixexp | tableconstructor | exp binop exp | unop exp """,

	"prefixexp -> `(´ exp `)´ | Name | prefixexp `[´ exp `]´ | prefixexp `.´ Name | prefixexp args | prefixexp `:´ Name args ",

	"functioncall ->  prefixexp args | prefixexp `:´ Name args ",

	"args ->  `(´ explistChoice `)´ | tableconstructor | String ",

	"function -> `function´ funcbody",

	"funcbody -> `(´ parlistChoice `)´ block `end´",
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
	
	"Name -> `NAME_LITERAL´",
	"String -> `STRING_LITERAL´",
	"Number -> `NUMBER_LITERAL´",]
	
	# 'Char -> `a´|`b´|`c´|`d´|`e´|`f´|`g´|`h´|`i´|`j´|`k´|`l´|`m´|`n´|`o´|`p´|`q´|`r´|`s´|`t´|`u´|`w´|`x´|`y´|`z´|`A´|`B´|`C´|`D´|`E´|`F´|`G´|`H´|`I´|`J´|`K´|`L´|`M´|`N´|`O´|`P´|`Q´|`R´|`S´|`T´|`U´|`W´|`X´|`Y´|`Z´|`_´',

	# # 'Digit -> `0´|`1´|`2´|`3´|`4´|`5´|`6´|`7´|`8´|`9´']
	# "Char -> `Char´",
	# "Digit -> `Digit´"]

nonTerminal = ['Number','String','Name','unop','binop','fieldsep','field','fieldsepChoice','fieldsepFull','fieldlist','fieldlistChoice','tableconstructor','commaTripleDotChoice','parlist','parlistChoice','funcbody','function','args','functioncall','prefixexp','exp','expFull','explist','NameCommaFull','namelist','var','varFull','varlist','NameColonChoice','NameDotFull','funcname','explistChoice','chunk','statFull','semicolon','laststatFull','block','stat','elseifThen','elseChoice','commaExpChoice','equalExpListChoice','laststat']
print(len(nonTerminal))
terminal = {    "do"    ,"end"      ,"while"    ,"repeat"   ,"until"    ,"if"   ,"then"     ,"elseif"   ,"else"     ,"for"    ,"in"   ,"function" ,"local",    "return","break",    "nil"   ,"false"    ,"true",    ":"     ,",",    "("     ,")"    ,"{"    ,"}"    ,"["    
    ,"]"    ,";"    ,"."    ,".."   ,"...",    "+"     ,"-"    ,"*"    ,"/"    ,"%"    ,"^"    ,"#"    ,"=="   ,"~="   ,"<="
    ,">="   ,"<"    ,">"    ,"="    ,"and"    ,"or",    '-'     ,'#'    ,"not",'NAME_LITERAL','STRING_LITERAL','NUMBER_LITERAL'}

def isTerminal(word:str)->bool:
	if ('`' in word and '´' in word):
		return True
	return False

def checkNotEmptyStrings(arr):
    if arr == '':
        return False
    return True

def first(rule,diction):
	# recursion base condition
	# (for terminal or epsilon)
	if len(rule) != 0 and (rule is not None):
		if isTerminal(rule[0]):
			return rule[0]
		elif rule[0] == '#':
			return '#'

	# condition for Non-Terminals
	if len(rule) != 0:
		if rule[0] in list(diction.keys()):
			# fres temporary list of result
			fres = []
			rhs_rules = diction[rule[0]]
			# call first on each rule of RHS
			# fetched (& take union)
			for itr in rhs_rules:
				# print(f"Entering Recursion for {itr}")
				indivRes = first(itr,diction)
				# print(f"Exited Recursion for {itr}")
				if type(indivRes) is list:
					for i in indivRes:
						fres.append(i)
				else:
					fres.append(indivRes)

			# if no epsilon in result
			# - received return fres
			# print(rule[0])
			if '#' not in fres:
				# print(fres)
				return fres
			else:
				# apply epsilon
				# rule => f(ABC)=f(A)-{e} U f(BC)
				# print(fres)
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

# follow function input is the split result on
# - Non-Terminal whose Follow we want to compute
def follow(nt,diction,memoization = {}):
	key = nt
	if(key in memoization):
		return memoization[key]
	start_symbol = "chunk"
	# for start symbol return $ (recursion base case)

	solset = set()
	if nt == start_symbol:
		# return '$'
		solset.add('$')

	# check all occurrences
	# solset - is result of computed 'follow' so far

	# For input, check in all rules
	for curNT in diction:
		rhs = diction[curNT]
		# go for all productions of NT
		# print('\n')
		# print(curNT)
		# print(rhs)
		for subrule in rhs:
			if nt in subrule:
				# call for all occurrences on
				# - non-terminal in subrule
				while nt in subrule:
					index_nt = subrule.index(nt)
					subrule = subrule[index_nt + 1:]
					# empty condition - call follow on LHS
					if len(subrule) != 0:
						# compute first if symbols on
						# - RHS of target Non-Terminal exists
						res = first(subrule,diction)
						# print(f"subrule:{subrule}")
						# print(f"res: {res}")
						# if epsilon in result apply rule
						# - (A->aBX)- follow of -
						# - follow(B)=(first(X)-{ep}) U follow(A)
						if '#' in res:
							newList = []
							res.remove('#')
							print(res)
							print(f"Entering Recursion of {curNT} on variable ansNew")
							flag = 0
							for i in diction[curNT]:
								if(curNT in i):
									flag = 1
									break
							if(flag == 1):
								continue
							ansNew = follow(curNT,diction,memoization=memoization)
							# print(f"Exiting Recursion of {curNT} on variable ansNew")
							if ansNew != None:
								if type(ansNew) is list:
									newList = res + ansNew
								else:
									newList = res + [ansNew]
							else:
								newList = res
							res = newList
					else:
						# when nothing in RHS, go circular
						# - and take follow of LHS
						# only if (NT in LHS)!=curNT
						if nt != curNT:
							# print(f"Entering Recursion of {curNT} on variable res")
							res = follow(curNT,diction,memoization=memoization)
							# print(f"Exiting Recursion of {curNT} on variable res")
					# print(f"Res is {res}")
					# add follow result in set form
					if res is not None:
						if type(res) is list:
							for g in res:
								solset.add(g)
						else:
							solset.add(res)
					# print(f"solset: {solset}")
	# print("Entered outside the loop")
	# print(f"solset outside loop: {solset}")
	memoization[key] = list(solset)
	# print("Returning ",memoization[key])
	return memoization[key]


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
			# print(f"\nsubrhs[0]: {subrhs[0]} lhs: {lhs}")
			if subrhs[0] == lhs:
				
				alphaRules.append(subrhs[1:])
				# print(f"alphaRules:{alphaRules}")
			else:
				# print(f"betaRules:{betaRules}")
				betaRules.append(subrhs)
		# alpha and beta containing subrules are separated
		# now form two new rules
		if len(alphaRules) != 0:
			# to generate new unique symbol
			# add ' till unique not generated
			lhs_ = lhs + "'"
			while (lhs_ in rulesDiction.keys()) or (lhs_ in store.keys()):
				lhs_ += "'"
			# make beta rule
			# print(f"betaRules before adding lhs: {betaRules}")
			for b in range(0, len(betaRules)):
				betaRules[b].append(lhs_)
				# print(f"lhs_ : {lhs_}")
			# print(f"betaRules after adding lhs: {betaRules}")
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

def createParseTable(diction,firsts,follows,terminals):
	print("\nFirsts and Follow Result table\n")

	# find space size
	mx_len_first = 0
	mx_len_fol = 0
	for u in diction:
		k1 = len(str(firsts[u]))
		k2 = len(str(follows[u]))
		if k1 > mx_len_first:
			mx_len_first = k1
		if k2 > mx_len_fol:
			mx_len_fol = k2

	print(f"{{:<{10}}} "
		f"{{:<{mx_len_first + 5}}} "
		f"{{:<{mx_len_fol + 5}}}"
		.format("Non-T", "FIRST", "FOLLOW"))
	for u in diction:
		print(f"{{:<{10}}} "
			f"{{:<{mx_len_first + 5}}} "
			f"{{:<{mx_len_fol + 5}}}"
			.format(u, str(firsts[u]), str(follows[u])))

	# create matrix of row(NT) x [col(T) + 1($)]
	# create list of non-terminals
	ntlist = list(diction.keys())
	terminals = copy.deepcopy(terminals)
	terminals.append('$')

	# create the initial empty state of ,matrix
	mat = []
	for x in diction:
		row = []
		for y in terminals:
			row.append('')
		# of $ append one more col
		mat.append(row)

	# Classifying grammar as LL(1) or not LL(1)
	grammar_is_LL = True

	# rules implementation
	for lhs in diction:
		rhs = diction[lhs]
		for y in rhs:
			res = first(y)
			# epsilon is present,
			# - take union with follow
			if '#' in res:
				if type(res) == str:
					firstFollow = []
					fol_op = follows[lhs]
					if fol_op is str:
						firstFollow.append(fol_op)
					else:
						for u in fol_op:
							firstFollow.append(u)
					res = firstFollow
				else:
					res.remove('#')
					res = list(res) +\
						list(follows[lhs])
			# add rules to table
			ttemp = []
			if type(res) is str:
				ttemp.append(res)
				res = copy.deepcopy(ttemp)
			for c in res:
				xnt = ntlist.index(lhs)
				yt = terminals.index(c)
				if mat[xnt][yt] == '':
					mat[xnt][yt] = mat[xnt][yt] \
								+ f"{lhs}->{' '.join(y)}"
				else:
					# if rule already present
					if f"{lhs}->{y}" in mat[xnt][yt]:
						continue
					else:
						grammar_is_LL = False
						mat[xnt][yt] = mat[xnt][yt] \
									+ f",{lhs}->{' '.join(y)}"

def syntaxAnalysis(tokenList:list[Token] = None):
    
	ruleDictionary = {}
	firstDictionary = {}
	followDictionary = {}

	for rule in Rules:
		k = rule.split("->")
		k[0] = k[0].strip()
		multiRhs = k[1].split('|')
		for i in range(len(multiRhs)):
			multiRhs[i] = multiRhs[i].split(' ')
		for i in range(len(multiRhs)):
			multiRhs[i] = list(filter(checkNotEmptyStrings,multiRhs[i]))
		ruleDictionary[k[0]] = multiRhs
	
	print("Original Grammer: ")
	for key, value in ruleDictionary.items():
		print(key, '\t:\t', value)
	print('\n')
	
	print("Grammar after removal of left recursion")
	ruleDictionary = removeLeftRecursions(ruleDictionary)
	for key, value in ruleDictionary.items():
		print(key, '\t:\t', value)
	print('\n')
	
	print("Grammar after left factoring")
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

	print("\nCalculated first Dictionary: ")
	key_list = list(firstDictionary.keys())
	index = 0
	for gg in firstDictionary:
		print(f"first({key_list[index]}) "
			f"=> {firstDictionary.get(gg)}")
		index += 1
	
	# # global start_symbol, rules, nonterm_userdef,\
	# # term_userdef, diction, firsts, follows
	for NT in ruleDictionary:
		
		print("----------------------------------------------------------------------")
		print(NT)
		solset = set()
		sol = follow(NT,ruleDictionary)
		print(f"Afterwards : {sol}")
		if sol is not None:
			for g in sol:
				solset.add(g)
		followDictionary[NT] = solset

	print("\nCalculated follow Dictionary: ")
	key_list = list(followDictionary.keys())
	index = 0
	for gg in followDictionary:
		print(f"follow({key_list[index]})"
			f" => {followDictionary[gg]}")
		index += 1
	
	createParseTable(ruleDictionary,firstDictionary,followDictionary,terminal)


# print(isTerminal('`(´'))
syntaxAnalysis()