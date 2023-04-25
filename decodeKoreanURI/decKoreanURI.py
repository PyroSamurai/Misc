#############################################################################
#    Korean URI Decoder: A tool that takes a Korean URI string and converts #
#    it to a UTF8 URI then decodes to standard text.                        #
#                                                                           #
#    Copyright (C) 2023  Sean Stafford (a.k.a. PyroSamurai)                 #
#                                                                           #
#    This program is free software: you can redistribute it and/or modify   #
#    it under the terms of the GNU General Public License as published by   #
#    the Free Software Foundation, either version 3 of the License, or      #
#    any later version.                                                     #
#                                                                           #
#    This program is distributed in the hope that it will be useful,        #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#    GNU General Public License for more details.                           #
#                                                                           #
#    You should have received a copy of the GNU General Public License      #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#                                                                           #
######################### End of copyright notice ###########################
__all__ = ['decKoreanURI']
import os
import lzma
import pickle
from urllib.parse import unquote

progDir = os.path.dirname(os.path.abspath(__file__))+os.sep
KRCHRS  = dict(pickle.load(lzma.open(progDir+"kr2utf8.dict.xz","rb")))

################# The main function ##################
def main():
    print("EUC-KR URI String: ", end='')
    euckrStr = input().strip().upper()
    n = 6 # num of str characters I want to grab per fetch
    # make an array of the EUC-KR characters
    euckrStrArr = [euckrStr[i:i + n] for i in range(0, len(euckrStr), n)]
    # then print out their UTF8 equivalents using matching dictionary
    print("Converted to UTF8: ", end='') 
    for i in euckrStrArr:
        print(unquote(KRCHRS[i]),end='')# decode URI on the fly
    print()


################# End of def main() ##################

main()
