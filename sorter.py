# Copyright(c) 2017 Michael Bäck

import pygame, sys, random, math

class Sorter:
	def __init__(self):
		self.array = []
		self.size = 16
		
		for i in range(self.size):
			self.array.append(i)
		
		self.newsize = self.size
		
		self.result = []
		self.result_hl = []
		self.result_index = 0
		self.result_size = 0
		self.draw_index = 0
		
		self.hl_color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]
		self.rainbow_color = []
		
		for i in range(256):
			self.rainbow_color.append((255, i, 0))
		for i in range(254, 0, -1):
			self.rainbow_color.append((i, 255, 0))
		for i in range(256):
			self.rainbow_color.append((0, 255, i))
		for i in range(254, 0, -1):
			self.rainbow_color.append((0, i, 255))
		for i in range(256):
			self.rainbow_color.append((i, 0, 255))
		for i in range(254, 0, -1):
			self.rainbow_color.append((255, 0, i))
		self.rainbow_size = len(self.rainbow_color)
		
		self.add_result()
		self.add_result()
		
		self.playing = False
		self.played = False
		self.speed = 0
		self.speed_count = 0
		
		self.sort_index = 0
		self.init_index = 0
		self.styl_index = 0
		self.shap_index = 0
		
		self.sort_list = [
							"Bubble Sort",
							"Cocktail Sort",
							"Odd-Even Sort",
							"Comb Sort",
							"Selection Sort",
							"Insertion Sort",
							"Shell Sort",
							"Gnome Sort",
							"Heap Sort",
							"Iterative Quick Sort",
							"Quick Sort LL",
							"Quick Sort LR",
							"Merge Sort",
							"Bitonic Sort",
							"Cycle Sort",
							"LSD Sort (Radix 4)",
							"Intro Sort",
							"Batcher's Odd-Even Merge Sort"
							]
		self.init_list = ["Random", "Almost Sorted", "Reversed"]
		self.styl_list = ["Default", "Negative", "Rainbow"]
		self.shap_list = ["Bar", "Dot", "Circle"]
		
		self.hl_on = False
		self.df_on = False
		self.about = False
		
	def sort_array(self):
		if self.sort_index == 0:
			sorter.bubble_sort()
		elif self.sort_index == 1:
			sorter.cocktail_sort()
		elif self.sort_index == 2:
			sorter.odd_even_sort()
		elif self.sort_index == 3:
			sorter.comb_sort()
		elif self.sort_index == 4:
			sorter.selection_sort()
		elif self.sort_index == 5:
			sorter.insertion_sort()
		elif self.sort_index == 6:
			sorter.shell_sort()
		elif self.sort_index == 7:
			sorter.gnome_sort()
		elif self.sort_index == 8:
			sorter.heap_sort()
		elif self.sort_index == 9:
			sorter.iterative_quick_sort(0, self.size-1)
		elif self.sort_index == 10:
			sorter.LL_quick_sort(0, self.size-1)
		elif self.sort_index == 11:
			sorter.LR_quick_sort(0, self.size-1)
		elif self.sort_index == 12:
			sorter.merge_sort(0, self.size-1)
		elif self.sort_index == 13:
			sorter.biotonic_sort(0, self.size, True)
		elif self.sort_index == 14:
			sorter.cycle_sort()
		elif self.sort_index == 15:
			sorter.lsd_radix_sort(4)
		elif self.sort_index == 16:
			#sorter.test_sort(0, self.size-1)
			sorter.merge_quick_sort()
		elif self.sort_index == 17:
			sorter.oddeven_merge_sort()
		sorter.add_result()
		
	def init_array(self):
		if self.init_index == 0:
			sorter.rand_array()
		if self.init_index == 1:
			sorter.gene_array()
			sorter.almo_array()
		if self.init_index == 2:
			sorter.gene_array()
			sorter.array.reverse()
		self.init_result()
	
	
	def rand_array(self):
		for i in range(self.size):
			self.r = random.randint(0, self.size-1)
			temp = self.array[i]
			self.array[i] = self.array[self.r]
			self.array[self.r] = temp
	
	def almo_array(self):
		k = int(self.size/8)
		for i in range(k):
			r1 = random.randint(0, self.size-1)
			r2 = random.randint(0, self.size-1)
			self.array[r1], self.array[r2] = self.array[r2], self.array[r1]
	
	def fewu_array(self):
		uniList = []
		self.array = []
		for i in range(4):
			uniList.append(int((self.size/4)*(i+1)))
		for j in range(self.size):
			uniIndex = j%4
			self.array.append(uniList[uniIndex])
	
	def gene_array(self):
		sorter.array = []
		for i in range(sorter.size):
			sorter.array.append(i)
	
	def bubble_sort(self):
		swapped = True
		while swapped:
			swapped = False
			for i in range(self.size-1):
				self.add_result([i])
				if self.array[i] > self.array[i+1]:
					self.add_result([i, i+1])
					self.array[i+1], self.array[i] = self.array[i], self.array[i+1]
					self.add_result([i, i+1])
					swapped = True
	
	def cocktail_sort(self):
		swapped = True
		start = 0
		end = self.size - 1
		while swapped:
			swapped = False
			for i in range (start, end):
				self.add_result([i])
				if (self.array[i] > self.array[i+1]):
					self.add_result([i, i+1])
					self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
					swapped = True
					self.add_result([i, i+1])
			if swapped == False:
				break
			swapped = False
			end = end-1
			for i in range(end-1, start-1,-1):
				self.add_result([i])
				if (self.array[i] > self.array[i+1]):
					self.add_result([i, i+1])
					self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
					swapped = True
					self.add_result([i, i+1])
			start = start+1
	
	def odd_even_sort(self):
		swapped = True
		while swapped:
			swapped = False
			for i in range(1, self.size-1, 2):
				self.add_result([i])
				if self.array[i] > self.array[i+1]:
					self.add_result([i, i+1])
					self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
					self.add_result([i, i+1])
					swapped = True
					 
			for i in range(0, self.size-1, 2):
				self.add_result([i])
				if self.array[i] > self.array[i+1]:
					self.add_result([i, i+1])
					self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
					self.add_result([i, i+1])
					swapped = True
	
	def comb_gap(self, gap):
		gap = (gap*10)//13
		if gap < 1:
			return 1
		else:
			return gap

	def comb_sort(self):
		gap = self.size
		swapped = True
		while gap !=1 or swapped == 1:
			gap = self.comb_gap(gap)
			swapped = False
			for i in range(0, self.size - gap):
				self.add_result([i])
				if self.array[i] > self.array[i+gap]:
					self.add_result([i, i+gap])
					self.array[i], self.array[i+gap] = self.array[i+ gap], self.array[i]
					self.add_result([i, i+gap])
					swapped = True
	
	def selection_sort(self):
		for i in range(self.size-1):
			minn = self.array[i]
			minindex = i
			for j in range(i+1, self.size):
				self.add_result([i, j, minindex])
				if minn > self.array[j]:
					minn = self.array[j]
					minindex = j
					self.add_result([i, j, minindex])
			self.array[minindex] = self.array[i]
			self.add_result([minindex, i])
			self.array[i] = minn
			self.add_result([i, min])
	
	def insertion_sort(self):
		for i in range(1, self.size):
			temp = self.array[i]
			j = i
			self.add_result([i, j])
			while j >= 1 and self.array[j-1] > temp:
				self.add_result([i, j, j-1])
				self.array[j] = self.array[j-1]
				j -= 1
			self.array[j] = temp
			self.add_result([i, j-1, j])
	
	def shell_sort(self):
		gap = self.size//2
		while gap > 0:
			for i in range(gap, self.size):
				temp = self.array[i]
				j = i
				self.add_result([i, j])
				while j >= gap and self.array[j-gap] > temp:
					self.add_result([i, j, j-gap])
					self.array[j] = self.array[j-gap]
					j -= gap
				self.array[j] = temp
				self.add_result([i, j-gap, j])
			gap //= 2
	
	def gnome_sort(self):
		index = 0
		while index < self.size:
			if index == 0:
				index = index + 1
			self.add_result([index])
			if self.array[index] >= self.array[index - 1]:
				self.add_result([index, index-1])
				index = index + 1
			else:
				self.add_result([index, index-1])
				self.array[index], self.array[index-1] = self.array[index-1], self.array[index]
				self.add_result([index, index-1])
				index = index - 1
	
	
	def heap(self, size, i):
		largest = i
		l = 2 * i + 1
		r = 2 * i + 2
		if l < size and self.array[i] < self.array[l]:
			largest = l
		if r < size and self.array[largest] < self.array[r]:
			largest = r
		self.add_result([i, largest])
		if largest != i:
			self.array[i], self.array[largest] = self.array[largest], self.array[i]
			self.add_result([i, largest])
			self.heap(size, largest)
			return 1
	 
	def heap_sort(self):
		for i in range(self.size, -1, -1):
			if self.heap(self.size, i) == 1:
				self.add_result()

		for i in range(self.size-1, 0, -1):
			self.add_result([i, 0])
			self.array[i], self.array[0] = self.array[0], self.array[i]
			self.add_result([i, 0])
			self.heap(i, 0)
	
	def i_q_partition(self, l, h):
		i = (l-1)
		x = self.array[h]
	 
		for j in range(l, h):
			self.add_result([h, j])
			if self.array[j] <= x:
				i += 1
				self.add_result([h, i, j])
				self.array[i], self.array[j] = self.array[j], self.array[i]
				self.add_result([h, i, j])
		self.array[i+1], self.array[h] = self.array[h], self.array[i+1]
		self.add_result([h, i+1, h])
		return (i+1)

	def iterative_quick_sort(self, l, h):
		size = h-l+1
		stack = [0]*(size)
		top = -1
		top += 1
		stack[top] = l
		top += 1
		stack[top] = h
		while top >= 0:
			h = stack[top]
			top -= 1
			l = stack[top]
			top -= 1
			p = self.i_q_partition(l, h)
			if p-1 > l:
				top += 1
				stack[top] = l
				top += 1
				stack[top] = p-1
			if p+1 < h:
				top += 1
				stack[top] = p+1
				top += 1
				stack[top] = h
	
	def LL_q_partition(self, low, high):
		i = (low-1)
		pivot = self.array[high]
		for j in range(low, high):
			self.add_result([high, i, j])
			if self.array[j] <= pivot:
				i = i+1
				self.array[i], self.array[j] = self.array[j], self.array[i]
				self.add_result([high, i, j])
		self.array[i+1], self.array[high] = self.array[high], self.array[i+1]
		self.add_result([high, i+1])
		return (i+1)

	def LL_quick_sort(self, low, high):
		if low < high:
			pi = self.LL_q_partition(low, high)
			self.LL_quick_sort(low, pi-1)
			self.LL_quick_sort(pi+1, high)
	
	def LR_quick_sort(self, low, high):
		if low < high:
			pivot = self.array[high]
			i = low - 1
			j = high
			while True:
				self.add_result([high, i, j])
				i += 1
				while self.array[i] < pivot:
					i += 1
				j -= 1
				while self.array[j] > pivot:
					j -= 1
				if i > j:
					break
				self.add_result([high, i, j])
				self.array[i], self.array[j] = self.array[j], self.array[i]
				self.add_result([high, i, j])
			self.array[high], self.array[i] = self.array[i], self.array[high]
			self.add_result([high, i, j])
			self.LR_quick_sort(low, j)
			self.LR_quick_sort(i+1, high)

				
	def merge(self, left, mid, right):
		copy_list = []
		i, j = left, mid + 1
		ind = left
		
		while ind < right+1:
			self.add_result([ind])
			if i > mid:
				copy_list.append(self.array[j])
				j +=1
			elif j > right:
				copy_list.append(self.array[i])
				i +=1
			elif self.array[j] < self.array[i]:
				copy_list.append(self.array[j])
				j +=1
			else:
				copy_list.append(self.array[i])
				i +=1
			ind +=1
			
		ind=0
		for x in (range(left,right+1)):
			self.add_result([x, left])
			self.array[x] = copy_list[ind]
			self.add_result([x, left])
			ind += 1

	def merge_sort(self, left, right):
		factor = 2
		temp_mid = 0
		while 1:
			index = 0
			left = 0
			right = self.size - (self.size % factor) - 1
			mid = (factor//2) - 1
			while index < right:
				temp_left = index
				temp_right = temp_left + factor -1
				mid2 = (temp_right +temp_left)//2
				self.merge (temp_left, mid2, temp_right)
				index = (index + factor)
			if self.size % factor and temp_mid !=0:
				self.merge(right +1, temp_mid, self.size-1)
				mid = right
			factor = factor * 2
			temp_mid = right
			if factor > self.size :
				mid = right
				right = self.size-1
				self.merge(0, mid, right)
				break
	
	def biotonic_gpotlt(self, n):
		k = 1
		while (k>0 and k<n):
			k = k<<1
		return k>>1
	
	def biotonic_merge(self, low, cnt, dire):
		if cnt > 1:
			k = self.biotonic_gpotlt(cnt)
			for i in range(low, low+cnt-k):
				self.add_result([i, i+k])
				if (dire == (self.array[i] > self.array[i+k])):
					self.array[i], self.array[i+k] = self.array[i+k], self.array[i]
					self.add_result([i, i+k])
			self.biotonic_merge(low, k, dire)
			self.biotonic_merge(low+k, cnt-k, dire)
	
	def biotonic_sort(self, low, cnt, dire):
		if cnt > 1:
			k = cnt//2
			self.biotonic_sort(low, k, not dire)
			self.biotonic_sort(low+k, cnt-k, dire)
			self.biotonic_merge(low, cnt, dire)
	
	def cycle_sort(self):
		for cycleStart in range(0, self.size - 1):
			item = self.array[cycleStart]
			pos = cycleStart
			self.add_result([pos])
			for i in range(cycleStart + 1, self.size):
				if self.array[i] < item:
					pos += 1
					self.add_result([pos])
			if pos == cycleStart:
				continue
			
			while item == self.array[pos]:
				pos += 1
				self.add_result([pos])
			self.array[pos], item = item, self.array[pos]
			self.add_result([pos])
			while pos != cycleStart:
				pos = cycleStart
				self.add_result([pos])
				for i in range(cycleStart + 1, self.size):
					if self.array[i] < item:
						pos += 1
						self.add_result([pos])
				while item == self.array[pos]:
					pos += 1
					self.add_result([pos])
				self.array[pos], item = item, self.array[pos]
				self.add_result([pos])
	
	def lsd_radix_counting_sort(self, radix, exponent, min):
		bucket_index = -1
		bucket = [0] * radix
		output = [None] * self.size
		
		for i in range(0, self.size):
			bucket_index = math.floor(((self.array[i]-min)/exponent)%radix)
			bucket[bucket_index] += 1
			self.add_result([i])
		
		for i in range(1, radix):
			bucket[i] += bucket[i-1]
			self.add_result([i])
		
		for i in range(self.size-1, -1, -1):
			bucket_index = math.floor(((self.array[i]-min)/exponent)%radix)
			bucket[bucket_index] -= 1
			output[bucket[bucket_index]] = self.array[i]
			self.add_result([i])
		
		for i in range(self.size):
			self.array[i] = output[i]
			self.add_result([i])
	
	def lsd_radix_sort(self, radix):
		min = 0
		max = self.size-1
		
		exponent = 1
		while (max-min)/exponent >= 1:
			self.lsd_radix_counting_sort(radix, exponent, min)
			exponent *= radix
	
	def merge_quick_part(self, low, high):
		if high-low > 4:
			self.merge_quick_part(low, (low+high)//2)
			self.merge_quick_part((low+high)//2+1, high)
		
		self.LR_quick_sort(low, high)
	
	def merge_quick_sort(self):
		self.merge_quick_part(0, self.size-1)
		
	def oddeven_merge(self, l, h, r):
		s = r*2
		if s<h-l:
			self.oddeven_merge(l, h, s)
			self.oddeven_merge(l+r, h, s)
			for i in range(l+r, h-r, s):
				self.oddeven_merge_sort_cnp(i, i+r)
		else:
			self.oddeven_merge_sort_cnp(l, l+r)
	
	def oddeven_merge_sort_range(self, l, h):
		if (h-l)>=1:
			m = l+((h-l)//2)
			self.oddeven_merge_sort_range(l, m)
			self.oddeven_merge_sort_range(m+1, h)
			self.oddeven_merge(l, h, 1)
	
	def oddeven_merge_sort_cnp(self, a, b):
		self.add_result([a, b])
		if self.array[a] > self.array[b]:
			self.array[a], self.array[b] = self.array[b], self.array[a]
			self.add_result([a, b])
	
	def oddeven_merge_sort(self):
		self.oddeven_merge_sort_range(0, self.size-1)
	
	def add_result(self, hl = []):
		temp = []
		for i in self.array:
			temp.append(i)
		self.result.append(temp)
		self.result_hl.append(hl)
		
	def draw(self):
		self.bar_width = (ds_X - 352)/self.size
		hl_len = len(self.result_hl[self.result_index])
		
		self.bg_size_x = ds_X - 320
		self.bg_size_y = ds_Y - 80
		
		if self.bg_size_x > self.bg_size_y:
			self.radius = self.bg_size_y*0.4375
		else:
			self.radius = self.bg_size_x*0.4375
		
		self.center_x = (self.bg_size_x//2)+304
		self.center_y = (self.bg_size_y//2)+16
		
		if self.styl_index == 0:
			pygame.draw.rect(ds, (255, 255, 255), (304, 16, self.bg_size_x, self.bg_size_y))
			
			if hl_len == 0 or self.hl_on == False:
				for self.draw_index in range(self.size):
					self.draw_select((0, 0, 0))
		
			elif hl_len >= 1:
				for self.draw_index in range(self.size):
					draw_color = (0, 0, 0)
					for hl_index in range(hl_len):
						if self.draw_index == self.result_hl[self.result_index][hl_index]:
							draw_color = self.hl_color[hl_index]
					self.draw_select(draw_color)
					
		elif self.styl_index == 1:
			pygame.draw.rect(ds, (0, 0, 0), (304, 16, self.bg_size_x, self.bg_size_y))
			
			if hl_len == 0 or self.hl_on == False:
				for self.draw_index in range(self.size):
					self.draw_select((255, 255, 255))
			
			elif hl_len >= 1:
				for self.draw_index in range(self.size):
					draw_color = (255, 255, 255)
					for hl_index in range(hl_len):
						if self.draw_index == self.result_hl[self.result_index][hl_index]:
							draw_color = self.hl_color[hl_index]
					self.draw_select(draw_color)
					
		elif self.styl_index == 2:
			pygame.draw.rect(ds, (0, 0, 0), (304, 16, self.bg_size_x, self.bg_size_y))
			
			if hl_len == 0 or self.hl_on == False:
				for self.draw_index in range(self.size):
					draw_color = self.rainbow_color[int((self.result[self.result_index][self.draw_index]/self.size)*self.rainbow_size)]
					self.draw_select(draw_color)
			
			elif hl_len >= 1:
				for self.draw_index in range(self.size):
					draw_color = self.rainbow_color[int((self.result[self.result_index][self.draw_index]/self.size)*self.rainbow_size)]
					for hl_index in range(hl_len):
						if self.draw_index == self.result_hl[self.result_index][hl_index]:
							draw_color = (255, 255, 255)
					self.draw_select(draw_color)
		
		if self.about:
			background = pygame.Surface((self.bg_size_x, self.bg_size_y))
			background.fill((0, 0, 0))
			background.set_alpha(192)
			ds.blit(background, (304, 16))
			ds.blit(self.text_render, (320, 32))
			ds.blit(self.text_2_render, (320, 96))
			ds.blit(self.text_3_render, (320, 128))
	
	def draw_select(self, color):
		
		if self.df_on:
			self.array_value = self.size-1-abs(self.draw_index-self.result[self.result_index][self.draw_index])
		else:
			self.array_value = self.result[self.result_index][self.draw_index]
		
		if self.shap_index == 0:
			self.draw_bar(color)
		elif self.shap_index == 1:
			self.draw_dot(color)
		elif self.shap_index == 2:
			self.draw_circle_dot(color)
	
	def draw_bar(self, color):
		pygame.draw.rect(ds, color, (320+(self.bar_width*self.draw_index), ds_Y - 80, self.bar_width+1, -((ds_Y - 112)/(self.size-1))*(self.array_value)))
	
	def draw_dot(self, color):
		pygame.draw.rect(ds, color, (320+(self.bar_width*self.draw_index), ds_Y - 80-((ds_Y - 112)/(self.size-1))*(self.array_value), 4, 4))
	
	def draw_circle_dot(self, color):
		self.dot_radius = self.array_value/self.size*self.radius
		self.dot_angle = math.radians(self.draw_index/self.size*360+-90)
		self.dot_x = self.center_x+(math.cos(self.dot_angle)*self.dot_radius)
		self.dot_y = self.center_y+(math.sin(self.dot_angle)*self.dot_radius)
		pygame.draw.rect(ds, color, (self.dot_x, self.dot_y, 4, 4))
	
	def draw_text(self):
		self.text = "Sorting Algorithm Visualizer 0.2 (Jan 1, 2018)"
		self.text_render = font_list[0].render(self.text, True, (255, 255, 255))
		self.text_2 = "Visualizating some sorting algrithms for integers."
		self.text_2_render = font_list[1].render(self.text_2, True, (255, 255, 255))
		self.text_3 = "Copyright(c) 2017 Michael Bäck"
		self.text_3_render = font_list[1].render(self.text_3, True, (255, 255, 255))
		
	def inplay(self):
		if self.playing:
			self.draw_index = 0
			self.result_size = len(self.result)
			if self.speed >= 0:
				if self.speed_count > self.speed:
					if self.result_index + 1 < self.result_size:
						self.result_index += 1
						self.speed_count = 0
					else:
						self.speed_count = 0
						self.playing = False
						self.played = True
				self.speed_count += 1
			else:
				if self.result_index + 1 < self.result_size:
					self.result_index += 1-self.speed
					if self.result_index >= self.result_size:
						self.result_index = self.result_size - 1
				else:
					self.playing = False
					self.played = True
			if self.played:
				self.played = False
	
	def init_result(self):
		self.result_index = 0
		self.draw_index = 0
		sorter.result = []
		sorter.result_hl = []
		sorter.add_result()
		sorter.add_result()

class Button:
	def __init__(self, pos_X, pos_Y, size_X, size_Y, index, text):
		self.pos_X = pos_X
		self.pos_Y = pos_Y
		self.size_X = size_X
		self.size_Y = size_Y
		self.clicked = -1
		self.index = index
		self.text = text
		self.text_render = font_list[0].render(self.text, True, (0, 0, 0))
		self.text_rect = self.text_render.get_rect(center=(self.pos_X + (self.size_X/2), self.pos_Y + (self.size_Y/2)))
	def update(self):
		if mouse_pos[0] >= self.pos_X and mouse_pos[0] < self.pos_X+self.size_X and mouse_pos[1] >= self.pos_Y and mouse_pos[1] < self.pos_Y+self.size_Y:
			self.color = (192, 192, 192)
			self.text_color = (64, 64, 64)
			if clicked:
				if not self.pos_out:
					self.color = (128, 128, 128)
					self.text_color = (0, 0, 0)
					self.clicked += 1
			else:
				self.pos_out = False
				self.clicked = -1
		else:
			self.color = (64, 64, 64)
			self.text_color = (255, 255, 255)
			self.clicked = -1
			if clicked:
				self.pos_out = True
			else:
				self.pos_out = False
		
		if self.clicked == 0:
			self.action()
			self.clicked = 1
	
	def draw(self):
		pygame.draw.rect(ds, self.color, (self.pos_X, self.pos_Y, self.size_X, self.size_Y))
		
		self.text_render = font_list[0].render(self.text, True, self.text_color)
		ds.blit(self.text_render, self.text_rect)
	
	def action(self):
		if self.index == 1:
			if sorter.size != sorter.newsize:
				sorter.size = sorter.newsize
				sorter.gene_array()
			sorter.init_array()
			sorter.sort_array()
			sorter.result_index = 0
			sorter.draw_index = 0
			sorter.playing = True
		elif self.index == 2:
			sorter.result_index = 0
			sorter.draw_index = 0
			sorter.playing = True

class Slider:
	def __init__(self, pos_X, pos_Y, size_X, size_Y, index, min, max, ini, text):
		self.bar_pos_X = pos_X
		self.pos_Y = pos_Y
		self.pos_X = pos_X
		self.bar_size_X = size_X
		self.size_Y = size_Y
		self.size_X = 32
		self.clicked = False
		self.bar_clicked = -1
		self.bar_input = False
		self.bar_input_end = False
		self.index = index
		self.num = ini
		self.min = min
		self.max = max
		self.text = text
		self.num_text = "%d"%ini
		self.num_pos_X = self.bar_pos_X + (self.bar_size_X/2)
		self.num_pos_Y = self.pos_Y - 24
		self.num_size_X = self.bar_pos_X + self.bar_size_X - self.num_pos_X
		self.num_size_Y = 24
		self.text_render = font_list[1].render(self.text, True, (0, 0, 0))
		self.text_color = (255, 255, 255)
		self.num_text_color = (255, 255, 255)
		
		self.pos_X = int((self.num-self.min+(self.bar_pos_X/(self.bar_size_X-self.size_X)*(self.max-self.min)))/(self.max-self.min)*(self.bar_size_X-self.size_X))
		
	def update(self):
		global key
		self.pos_in = (mouse_pos[0] >= self.pos_X and mouse_pos[0] < self.pos_X+self.size_X and mouse_pos[1] >= self.pos_Y and mouse_pos[1] < self.pos_Y+self.size_Y)
		self.bar_pos_in = (mouse_pos[0] >= self.bar_pos_X and mouse_pos[0] < self.bar_pos_X+self.bar_size_X and mouse_pos[1] >= self.pos_Y and mouse_pos[1] < self.pos_Y+self.size_Y)
		self.num_pos_in = (mouse_pos[0] >= self.num_pos_X-4 and mouse_pos[0] < self.num_pos_X+self.num_size_X+4 and mouse_pos[1] >= self.num_pos_Y and mouse_pos[1] < self.num_pos_Y+self.num_size_Y)
		if self.clicked or self.pos_in:
			self.color = (192, 192, 192)
			if clicked:
				if not self.pos_out:
					self.color = (128, 128, 128)
					self.clicked = True
			else:
				self.pos_out = False
				self.clicked = False
		else:
			self.color = (64, 64, 64)
			if clicked:
				self.pos_out = True
				self.clicked = False
			else:
				self.pos_out = False
		
		
		if (self.bar_pos_in or self.num_pos_in) and (not self.pos_in):
			if self.bar_input:
				self.bar_color = (255, 255, 255)
				self.num_text_color = (0, 0, 0)
			else:
				self.bar_color = (48, 48, 48)
				self.num_text_color = (192, 192, 192)
			if clicked:
				if not self.bar_pos_out:
					if self.bar_input:
						self.bar_color = (255, 255, 255)
						self.num_text_color = (0, 0, 0)
					else:
						self.bar_color = (16, 16, 16)
						self.num_text_color = (255, 255, 255)
					self.bar_clicked += 1
			else:
				self.bar_pos_out = False
				self.bar_clicked = -1
		else:
			if self.bar_input:
				self.bar_color = (255, 255, 255)
				self.num_text_color = (0, 0, 0)
			else:
				self.bar_color = (16, 16, 16)
				self.num_text_color = (255, 255, 255)
			if clicked:
				self.bar_pos_out = True
				self.bar_input = False
				self.bar_input_end = True
			else:
				self.bar_pos_out = False
		
		if self.clicked:
			self.pos_X = mouse_pos[0]-(self.size_X/2)
			
			self.num = int(self.pos_X/(self.bar_size_X-self.size_X)*(self.max-self.min))-int(self.bar_pos_X/(self.bar_size_X-self.size_X)*(self.max-self.min))+self.min
			self.num_text = "%d"%self.num
			self.action()
			
			if self.pos_X < self.bar_pos_X:
				self.pos_X = self.bar_pos_X
			if self.pos_X > self.bar_pos_X+self.bar_size_X-self.size_X:
				self.pos_X = self.bar_pos_X+self.bar_size_X-self.size_X
		
		if self.bar_clicked == 0:
			self.bar_color = (255, 255, 255)
			self.num_text_color = (0, 0, 0)
			if self.bar_input:
				self.bar_input = False
				self.bar_input_end = True
			else:
				self.bar_input = True
			self.bar_clicked = 1
		
		if self.bar_input:
			for kpn in ('[0]', '[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]'):
				if key == kpn:
					key = kpn[1]
					break
			for kpn in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
				if key == kpn:
					self.num_text += key
					break
			if key == '-' or key == '[-]':
				self.num_text += '-'
			if key == 'backspace':
				self.num_text = self.num_text[:len(self.num_text)-1]
			if key == 'return':
				self.bar_input = False
				self.bar_input_end = True
		
		if self.bar_input_end:
			if self.num_text == '' or self.num_text == '-':
				self.num = 0
			else:
				if (self.num_text.count('-') >= 2) or (self.num_text.count('-') == 1 and self.num_text[0] != '-'):
					self.num = 0
				else:
					self.num = int(self.num_text)
			if self.num > self.max:
				self.num = self.max
			if self.num < self.min:
				self.num = self.min
			self.num_text = "%d"%self.num
			self.pos_X = int((self.num-self.min+(self.bar_pos_X/(self.bar_size_X-self.size_X)*(self.max-self.min)))/(self.max-self.min)*(self.bar_size_X-self.size_X))
			self.action()
			
			self.bar_input_end = False
	
	def draw(self):
		pygame.draw.rect(ds, self.bar_color, (self.bar_pos_X, self.pos_Y, self.bar_size_X, self.size_Y))
		pygame.draw.rect(ds, self.color, (self.pos_X, self.pos_Y, self.size_X, self.size_Y))
		pygame.draw.rect(ds, self.bar_color, (self.num_pos_X-4, self.num_pos_Y, self.num_size_X+4, self.num_size_Y))
		
		self.text_render = font_list[1].render(self.text, True, self.text_color)
		self.num_render = font_list[1].render(self.num_text, True, self.num_text_color)
		
		ds.blit(self.text_render, (self.bar_pos_X, self.num_pos_Y))
		ds.blit(self.num_render, (self.num_pos_X, self.num_pos_Y))
		
	def action(self):
		if self.index == 1:
			sorter.newsize = self.num
		if self.index == 2:
			sorter.speed = self.num
		
class ComboBox:
	def __init__(self, pos_X, pos_Y, size_X, size_Y, index, list, text):
		self.pos_X = pos_X
		self.pos_Y = pos_Y
		self.size_X = size_X
		self.size_Y = size_Y
		
		self.list = list
		self.list_pos_Y = self.pos_Y + self.size_Y
		self.list_len = len(self.list)
		self.list_text_size_Y = 20
		self.list_size_Y = self.list_text_size_Y * self.list_len
		self.list_text_color = (0, 0, 0)
		self.list_show_index = 0
		self.list_index = self.list_show_index
		self.list_show_text_pos_Y = self.pos_Y + int((self.size_Y - self.list_text_size_Y)*(2/3))
		
		self.text = text
		self.text_color = (255, 255, 255)
		self.text_pos_Y = self.pos_Y - 20
		self.text_render = font_list[1].render(self.text, True, self.text_color)
		
		self.index = index
		
		self.clicked = -1
		self.input = False
		self.input_end = False
		self.list_pos_in = False
		
	def update(self):
		self.pos_in = (mouse_pos[0] >= self.pos_X and mouse_pos[0] < self.pos_X+self.size_X and mouse_pos[1] >= self.pos_Y and mouse_pos[1] < self.pos_Y+self.size_Y)
		
		if self.pos_in:
			if self.input:
				self.color = (16, 16, 16)
				self.bar_text_color = (255, 255, 255)
			else:
				self.color = (48, 48, 48)
				self.bar_text_color = (192, 192, 192)
			if clicked:
				if not self.pos_out:
					if self.input:
						self.color = (16, 16, 16)
						self.bar_text_color = (255, 255, 255)
					else:
						self.color = (16, 16, 16)
						self.bar_text_color = (255, 255, 255)
					self.clicked += 1
			else:
				self.pos_out = False
				self.clicked = -1
		else:
			if self.input:
				self.color = (16, 16, 16)
				self.bar_text_color = (255, 255, 255)
			else:
				self.color = (16, 16, 16)
				self.bar_text_color = (255, 255, 255)
			if clicked:
				self.pos_out = True
				self.input = False
				self.input_end = True
			else:
				self.pos_out = False
		
		if self.clicked == 0:
			self.color = (16, 16, 16)
			self.bar_text_color = (255, 255, 255)
			if self.input:
				self.input = False
				self.input_end = True
			else:
				self.input = True
			self.clicked = 1
		
		if self.input:
			self.draw_list = True
			self.list_pos_in = (mouse_pos[0] >= self.pos_X and mouse_pos[0] < self.pos_X+self.size_X and mouse_pos[1] >= self.list_pos_Y and mouse_pos[1] < self.list_pos_Y+self.list_size_Y)
			self.list_index = (mouse_pos[1] - self.list_pos_Y) // self.list_text_size_Y
			self.list_text_pos_Y = self.list_pos_Y + (self.list_index*self.list_text_size_Y)
			if self.list_pos_in:
				self.draw_select = True
			else:
				self.draw_select = False
		else:
			self.draw_list = False
		
		if self.input_end:
			if self.list_index >= 0 and self.list_index < self.list_len and self.list_pos_in:
				self.list_show_index = self.list_index
			self.action()
			self.input_end = False
	
	def draw(self):
		if self.draw_list:
			pygame.draw.rect(ds, (255, 255, 255), (self.pos_X, self.list_pos_Y, self.size_X, self.list_size_Y))
			if self.draw_select:
				pygame.draw.rect(ds, (192, 192, 192), (self.pos_X, self.list_text_pos_Y, self.size_X, self.list_text_size_Y))
			for i in range(self.list_len):
				self.list_text_render = font_list[1].render(self.list[i], True, self.list_text_color)
				ds.blit(self.list_text_render, (self.pos_X+4, self.list_pos_Y + (i*self.list_text_size_Y) + 2))
		
		pygame.draw.rect(ds, self.color, (self.pos_X, self.pos_Y, self.size_X, self.size_Y))
		
		self.list_show_text_render = font_list[1].render(self.list[self.list_show_index], True, self.bar_text_color)
		
		ds.blit(self.text_render, (self.pos_X, self.text_pos_Y))
		ds.blit(self.list_show_text_render, (self.pos_X+4, self.list_show_text_pos_Y))
		
	def action(self):
		if self.index == 1:
			sorter.sort_index = self.list_show_index
		elif self.index == 2:
			sorter.init_index = self.list_show_index
		elif self.index == 3:
			sorter.styl_index = self.list_show_index
		elif self.index == 4:
			sorter.shap_index = self.list_show_index

class CheckBox:
	def __init__(self, pos_X, pos_Y, size_X, size_Y, index, text):
		self.pos_X = pos_X
		self.pos_Y = pos_Y
		self.size_X = size_X
		self.size_Y = size_Y
		
		self.index = index
		
		self.text = text
		self.text_size_Y = 24
		self.text_pos_Y = self.pos_Y + int((self.size_Y - self.text_size_Y)*(2/3))
		
		self.clicked = -1
		
		self.checked = False
		
	def update(self):
		self.pos_in = mouse_pos[0] >= self.pos_X and mouse_pos[0] < self.pos_X+self.size_X and mouse_pos[1] >= self.pos_Y and mouse_pos[1] < self.pos_Y+self.size_Y
		if self.pos_in:
			self.color = (48, 48, 48)
			self.text_color = (192, 192, 192)
			if clicked:
				if not self.pos_out:
					self.color = (16, 16, 16)
					self.text_color = (255, 255, 255)
					self.clicked += 1
			else:
				self.pos_out = False
				self.clicked = -1
		else:
			self.color = (16, 16, 16)
			self.text_color = (255, 255, 255)
			self.clicked = -1
			if clicked:
				self.pos_out = True
			else:
				self.pos_out = False
		
		if self.clicked == 0:
			self.checked = not self.checked
			self.action()
			self.clicked = 1
		
		if self.checked:
			self.check_text = "V"
		else:
			self.check_text = " "
	
	def draw(self):
		pygame.draw.rect(ds, self.color, (self.pos_X, self.pos_Y, self.size_X, self.size_Y))
		
		self.text_render = font_list[1].render(self.text, True, self.text_color)
		self.check_text_render = font_list[1].render(self.check_text, True, self.text_color)
		
		ds.blit(self.text_render, (self.pos_X+32, self.text_pos_Y))
		ds.blit(self.check_text_render, (self.pos_X+8, self.text_pos_Y))
		
	def action(self):
		if self.index == 1:
			sorter.hl_on = self.checked
		if self.index == 2:
			sorter.df_on = self.checked
		if self.index == 3:
			sorter.about = self.checked

class Label:
	def __init__(self, pos_X, pos_Y, size_X, size_Y, text):
		self.pos_X = pos_X
		self.pos_Y = pos_Y
		self.size_X = size_X
		self.size_Y = size_Y
		
		self.text = text
		self.text_color = (255, 255, 255)
		self.text_pos_Y = self.pos_Y - 24
		self.text_render = font_list[1].render(self.text, True, self.text_color)
	
	def update(self):
		return
	
	def draw(self):
		ds.blit(self.text_render, (self.pos_X, self.text_pos_Y))

sorter = Sorter()

pygame.init()
sorter.chan = pygame.mixer.Channel(0)

ds_default_X = 1280
ds_default_Y = 720

ds_min_X = 640
ds_min_Y = 720
ds_changed = False

ds_X = ds_default_X
ds_Y = ds_default_Y

user_ds_X = pygame.display.Info().current_w
user_ds_Y = pygame.display.Info().current_h

ds = pygame.display.set_mode([ds_X, ds_Y], pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
pygame.display.set_icon(pygame.image.load('icon.png'))
pygame.display.set_caption("Sorting Algorithm Visualizer 0.2")

font_list = []

font_list.append(pygame.font.SysFont("Arial", 32, bold = True))
font_list.append(pygame.font.SysFont("Arial", 16, bold = True))

gui_list = []

gui_list.append(Button(16, 16, 128, 48, 1, "Sort"))
gui_list.append(Button(160, 16, 128, 48, 2, "Replay"))

gui_list.append(Slider(16, 128, 272, 24, 1, 2, 1024, 16, "Array Size"))
gui_list.append(Slider(16, 192, 272, 24, 2, -50, 50, 0, "Play Speed"))

gui_list.append(Label(160, 616, 128, 32, "Options"))
gui_list.append(CheckBox(160, 616, 128, 32, 1, "Highlight"))
gui_list.append(CheckBox(160, 648, 128, 32, 2, "Difference"))
gui_list.append(CheckBox(160, 680, 128, 32, 3, "About"))

gui_list.append(ComboBox(160, 496, 128, 32, 4, sorter.shap_list, "Shape"))
gui_list.append(ComboBox(160, 376, 128, 32, 3, sorter.styl_list, "Color"))
gui_list.append(ComboBox(16, 256, 128, 32, 1, sorter.sort_list, "Algorithm"))
gui_list.append(ComboBox(160, 256, 128, 32, 2, sorter.init_list, "Input Type"))

sorter.draw_text()

clicked = False
key = ""

while True:
	mouse_pos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.display.quit()
			pygame.quit()
			sys.exit()
		if event.type== pygame.VIDEORESIZE:
			ds = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
			ds_X = pygame.display.Info().current_w
			ds_Y = pygame.display.Info().current_h
			if ds_X < ds_min_X:
				ds_X = ds_min_X
				ds_changed = True
			if ds_Y < ds_min_Y:
				ds_Y = ds_min_Y
				ds_changed = True
			if ds_changed:
				ds = pygame.display.set_mode([ds_X, ds_Y], pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
				ds_changed = False
			pygame.display.flip()
		if pygame.mouse.get_pressed()[0]:
			clicked = True
		else:
			clicked = False
		if event.type == pygame.KEYDOWN:
			key = pygame.key.name(event.key)

	for gui_index in gui_list:
		gui_index.update()
		gui_index.draw()
		
	key = ""
	
	sorter.draw()
	
	sorter.inplay()
	
	pygame.display.update()
	ds.fill((32, 32, 32))
	
	pygame.time.Clock().tick(240)