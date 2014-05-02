import sys

def getEditDistance(word1, word2):
  matrixTable = [[i for i in range(len(word2)+1)] for j in range(len(word1)+1)]

  for i in range(len(word1)+1):
      matrixTable[i][0] = i
  
  for i in range(1, len(word1)+1):
      for j in range(1, len(word2)+1):
          top = matrixTable[i-1][j] + 1
          left = matrixTable[i][j-1] + 1       
          if word1[i-1:i] == word2[j-1:j]:
              topLeft = matrixTable[i-1][j-1]          
          else:    
              topLeft = matrixTable[i-1][j-1] + 1
          matrixTable[i][j] = min(top, left, topLeft)

  #print matrixTable

  return matrixTable[len(word1)][len(word2)]


if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print "usage: python editdistance.py word1 word2"
        exit()

    editDistance = getEditDistance(sys.argv[1], sys.argv[2])
    print editDistance 
