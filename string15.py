a = list(str(input()))
result = [ ''.join(a[::-1][i:i+3])[::-1]
        for i in range(0,len(a),3)]
print(' '.join(result[::-1]))