numbers = raw_input("Enter the numbers: ").split()
for i in range(0, len(numbers)):
	numbers[i] = float(numbers[i])
target = int(raw_input("Input the target: "))

bestSoFar = numbers[0]
bestDiffSoFar = abs(target - numbers[0])
bestOperations = str(numbers[0])

numSolutions = 0

def do_try(nums, soFar, operations, target):
	global bestDiffSoFar, bestSoFar, bestOperations
	global numSolutions

	if(soFar == target):
		print operations + " = " + str(soFar)
		numSolutions = numSolutions + 1
		return
	
	if (abs(soFar - target) < bestDiffSoFar):
		bestSoFar = soFar
		bestDiffSoFar = abs(soFar - target)
		bestOperations = operations
		#print operations + " = "+ str(soFar)
	#if(bestSoFar == target):

		#return
	#print operations + " = " + str(soFar)
	for i in range(0, len(nums)):
		do_try(nums[:i] + nums[i+1:], soFar + nums[i], "(" + operations + " + " + str(int(nums[i])) + ")", target)
		do_try(nums[:i] + nums[i+1:], soFar * nums[i], "(" + operations + " * " + str(int(nums[i])) + ")", target)
		do_try(nums[:i] + nums[i+1:], soFar / nums[i], "(" + operations + " / " + str(int(nums[i])) + ")", target)
		do_try(nums[:i] + nums[i+1:], soFar - nums[i], "(" + operations + " - " + str(int(nums[i])) + ")", target)

for i in range(0, len(numbers)):
	do_try(numbers[:i] + numbers[i+1:], numbers[i], str(int(numbers[i])), target)

#do_try(numbers, 0, "", target)

print str(int(bestSoFar)) + " " + str(int(bestDiffSoFar)) + " " + bestOperations

print numSolutions
