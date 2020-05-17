def solution(l):
     l = sorted(l, key=lambda l:[int(i) for i in l.split('.')])
     return l