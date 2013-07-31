ins = open( "input.c", "r" )
array = []
for line in ins:
	if line.strip() :
		array.append( line.strip() )
print array
li=[]
sen=[]
openbraces=0
variables={}
for each in array:
	sen=each.split(';')
	for each1 in sen:
		if each1:
			lines=each1.strip()
			listlines=list(lines)
			if lines=="{":
				openbraces+=1
			if lines =="}":
				openbraces-=1
			if listlines[0]=='#':
				print	lines+" it is a preprocessor "
			if "int " in lines or "float " in lines or "char " in lines :
				if "()" in lines or "(" in lines or ")" in lines :
					print lines+" it is a function "
				else:
					
					if ',' in lines:
						variabledec=lines.split(',')
						print variabledec
						
						print lines+" it is a multiple variable declaration"
						
						
					else:
						variabledec=lines.split("=")
						print variabledec
						
						print lines+" it is a single variable declaration"
						
						for var in variabledec:
							var=var.strip()
							if "int" in var:
								print var[4:].strip()+" and the value is "+variabledec[1].strip()
								try:
									if variables[var[4:].strip()] :
										print "sorry multiple declaration"
								except :
									variables[var[4:].strip()]=variabledec[1].strip()
									print "variable inserted"
							if "float" in var:
								print var[6:]+" and the value is "+variabledec[1].strip()
								print var[6:].strip()+" and the value is "+variabledec[1].strip()
								try:
									if variables[var[6:].strip()] :
										print "sorry multiple declaration"
										
								except :
									variables[var[6:].strip()]=variabledec[1].strip()
							if "char" in var:
								print var[5:]+" and the value is "+variabledec[1].strip()
								print var[5:].strip()+" and the value is "+variabledec[1].strip()
								try:
									if variables[var[5:].strip()] :
										print "sorry multiple declaration"
								except :
									variables[var[5:].strip()]=variabledec[1].strip()
			if "return " in lines:
				print "program ends here with a return value "+lines.split(" ")[1]		
			
if openbraces == 0:
	print "proper braces are used"
else:
	print "number of open braces are "+str(openbraces)

print "*********************"
print "after lexical analysis"
print "*********************"	
print variables
	   			

