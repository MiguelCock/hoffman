
def getprob(text):
    tabla = dict()
    for i in text:
        if  i in tabla:
            tabla[i]= tabla[i]+1
        else:
            tabla[i] = 1
    return tabla

def build_heap(A, n):
    elemento = 1
    while elemento < n:
        heapify(A, elemento)
        elemento = elemento + 1

def heapify(A, n):
    base = n
    while base > 0 and A[A[base]] < A[A[(base-1)//2]]:
        tmp = A[base]
        A[base] = A[(base-1)//2]
        A[(base-1)//2] = tmp
        base = (base-1)//2    
    
def sift(A, n):
    base = 0
    minimo = base
    while base < n: 
        if 2*base + 1 < n and A[A[2*base+1]] < A[A[minimo]]:
            minimo = 2*base+1
        if 2*base+2 < n and  A[A[2*base+2]] < A[A[minimo]]:
            minimo = 2*base+2
        if base != minimo:
            tmp =A[base]
            A[base] = A[minimo]
            A[minimo] = tmp
            base = minimo
        else:
            base = n        

def codeLengh(tabla):
    n = len(tabla)
    A = [0] * (2*n)
    u = list(tabla.keys())
    i = 0
    while i < n:
        A[i] = n + i
        A[n+i] = tabla[u[i]]
        i = i + 1
    build_heap(A, n)
    h = n-1
    while h > 0:
        m1 = A[0]
        A[0] = A[h]
        h = h - 1
        sift(A,h)
        m2 = A[0]
        A[h+1] = A[m1]+A[m2]
        A[0] = h+1
        A[m1] = h + 1
        A[m2] = h+1
        sift(A, h)
    A[1] = 0
    i = 2
    while i < 2*n:
        A[i] = A[A[i]]+1
        i = i + 1
    return A
  
def canonico(lengChar):
  chars = lengChar.keys()
  long = 0
  for c in chars:
    if lengChar[c] > long:
      long = lengChar[c]
      
  numL = [0 for n in range(long)]
  for c in chars:
    numL[lengChar[c]-1] += 1
    
  firstCode = [0 for n in range(long)]
  i = long - 2
  while i >= 0:
    firstCode[i] = (firstCode[i + 1] + numL[i + 1]) // 2
    i -= 1
  codes = {}
  for l in chars:
    codes[l] = firstCode[lengChar[l] - 1]
    firstCode[lengChar[l] - 1] += 1
  return codes

def strToNum(text):
  num = 0
  long = len(text) - 1
  pos = 0
  while long >= 0:
    num += int(text[long]) * 2**pos
    long -= 1
    pos += 1
  return num

def main():
  #aqui ponesmos el texto que queramos comprimir
  text = "acostacamachoforero asdlnfa kaslkdmfak sdlaksjdfnalkjsdfm alskdfnalskdf lkjasdnfjk"
  
  tabla = getprob(text)
  
  A = codeLengh(tabla)
  
  ln = (len(A) // 2)
  dict = {}
  for i in text:
    dict[i] = 0
    
  ltr = dict.keys()
  for l in ltr:
    dict[l] = A[ln]
    ln += 1

  cano = canonico(dict)
  
  binary = 0
  lng = 0
  for letter in text[::-1]:
    binary += cano[letter] * (2**lng)
    lng += dict[letter]
  binary += 1 * (2**lng)
    
  trueBinary = bin(binary)
  trueCopy = trueBinary[2:]
  print(len(trueCopy)%8)
  print(trueBinary)
  listHex = []
  while len(trueCopy) != 0:
    listHex.append(strToNum(trueCopy[:8]))
    trueCopy = trueCopy[8:]
  print(listHex)
  with open('text.bin', 'wb') as f:
    f.write(bytearray(listHex))

  with open('text.bin', 'rb') as f:
    x = f.read()
    print(bin(int.from_bytes(x, "big")))
  
  llavesDict = list(dict.keys())
  valuesDict = list(dict.values())
  valuesCano = list(cano.values())
  k = 4
  cosa = ""
  
  while len(trueBinary) != 3:
    w = 0
    while w < len(llavesDict):
      if len(trueBinary[3:k]) == valuesDict[w] and strToNum(trueBinary[3:k]) == valuesCano[w]:
          trueBinary = trueBinary[:3] + trueBinary[k:]
          cosa += llavesDict[w]
          k = 4
      w += 1
    k += 1
  print(cosa)
main()
