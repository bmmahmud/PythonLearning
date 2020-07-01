
# branchList = ["BOGRA","BARISAL","COMMILLA","COX BAZAR","CHITTAGONG","CTG NORTH","DINAJPUR","FENI","FARIDPUR","GAZIPUR","CHANDPUR","JESSORE","KHULNA","KERANIGANJ","KISHOREGANJ","KUSTIA","MOHAKHALI","MOULOVIBAZAR","MOTIJHEEL","MIRPUR","MYMENSIGN","NARAYANGONJ","NOAKHALI","SKF Institution","PATUAKHALI","PABNA","RAJSHAHI","RANGPUR","SAVAR","SYLHET","TANGAIL","BHAIRAB"]

def branchName(branch):
    branchList = ["BOGRA", "BARISAL", "COMMILLA", "COX BAZAR", "CHITTAGONG", "CTG NORTH", "DINAJPUR", "FENI",
                  "FARIDPUR", "GAZIPUR", "CHANDPUR", "JESSORE", "KHULNA", "KERANIGANJ", "KISHOREGANJ", "KUSTIA",
                  "MOHAKHALI", "MOULOVIBAZAR", "MOTIJHEEL", "MIRPUR", "MYMENSIGN", "NARAYANGONJ", "NOAKHALI",
                  "SKF Institution", "PATUAKHALI", "PABNA", "RAJSHAHI", "RANGPUR", "SAVAR", "SYLHET", "TANGAIL",
                  "BHAIRAB"]

    if(branch in branchList):
        return print(branch,'is in the List')
    else:
        return print(branch,'is not in the List')

branchName('BHAIRAB')