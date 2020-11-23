def SetBITFunction ( VAR ,  BIT):
	result = VAR |  ( 1 <<(BIT))
	print(result)
	
def ClearBITFunction ( VAR ,  BIT):	
	result = VAR & ~( 1 <<(BIT))
	print(result)

def GetBITFunction ( VAR ,  BIT):		
	result = ((VAR  >>   BIT) & 1)
	print(result)

def ToggleBITFunction ( VAR ,  BIT):	
	result = VAR ^  ( 1 <<(BIT))
	print(result)

SetBITFunction (12,1)
ClearBITFunction (10,3)
GetBITFunction (7,2)
ToggleBITFunction(7,2)