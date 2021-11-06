# производит простое сопоставление
# текста с последовательностью строк, 
# а при совпадении выдает совпавшие строки
# вместе с N предыдущими строками контекста


from collections import deque

def search(lines, pattern, history=5):
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)

# Пример использования
if __name__ == '__main__':
	with open('LICENSE') as f:
		for line, prevlines in search(f, 'copy', 3):
			for pline in prevlines:
				print(pline, end='')
			print(line, end='')
			print('-'*20)