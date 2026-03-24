def simplifyPath(path: str) -> str:
    stack = []
    
    # Divide o caminho pelos '/'
    parts = path.split('/')
    
    for part in parts:
        if part == '' or part == '.':
            continue
        
        elif part == '..':
            if stack:
                stack.pop()
        
        else:
            stack.append(part)
    
    # Monta o caminho final
    return '/' + '/'.join(stack)

path = "/home//foo/../bar/"
resultado = simplifyPath(path)

print("Caminho original:", path)
print("Caminho simplificado:", resultado)