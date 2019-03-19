#This programs show that commentting should use # rather than """ """ or ''' '''
#As you can see that three quotes crash the program
#It returns an indent error to you 

def main():
    print("let's do something")
#Try using hashtag to comment this block to get code working
"""
    Note following block gives you a non-sense indent error
    The next step would be to consider how to get all the words from spam and ham
    folder from different directory. My suggestion would be do it twice and then
    concentrate two lists

    Frist think about the most efficient way
    For example, we might need to get rid off the duplicated words in the beginning

    The thoughts of writing the algorithem to create the dictionary

    Method-1:
    1. To append all the list from the email all-together
    2. Eliminate those duplicated words

    cons: the list might become super large

    I Choose method-2 to save the memory
    Method-2:
    1. kill the duplicated words in each string
    2. Only append elements that is not already in the dictionary

    Note:
    1. In this case, the length of feature actually was determined by the
    training cohorts, as we used the different English terms to decide feature

    cons: the process time might be super long
"""
    def wtf_python(var1, var2):
        var3 = var1 + var2 + (var1*var2)
        return var3

    wtfRst1 = wtf_python(1,2)
    wtfRst2 = wtf_python(3,4)

    rstAll = { "wtfRst1" : wtfRst1,
               "wtfRst2" : wtfRst2
    }
    return(rstAll)

if __name__ == "__main__":
    mainRst = main()
    print("wtfRst1 is :\n", mainRst['wtfRst1'])
    print("wtfRst2 is :\n", mainRst['wtfRst2'])




