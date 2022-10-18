# 프로그래머스 캐시
from collections import deque

cache = deque()


def cacheHit(k):
	cache.remove(k)
	cache.append(k)


def cacheMiss(k, cacheSize):
	if len(cache) < cacheSize:
		cache.append(k)
	else:
		cache.popleft()
		cache.append(k)


def solution(cacheSize, cities):
	answer = 0

	if cacheSize == 0:
		return len(cities) * 5

	for k in cities:
		k = k.lower()
		if k in cache:
			cacheHit(k)
			answer += 1
		else:
			cacheMiss(k, cacheSize)
			answer += 5

	return answer