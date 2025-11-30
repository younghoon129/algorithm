w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())
tx = x + t
ty = y + t
# print(tx, ty)
nx = ((tx - 1) // w + 1) % 2 * ((tx-1) % w + 1) + ((tx - 1) // w) % 2 * (w - ((tx-1) % w + 1))
ny = ((ty - 1) // h + 1) % 2 * ((ty-1) % h + 1) + ((ty - 1) // h) % 2 * (h - ((ty-1) % h + 1))
print(nx, ny)