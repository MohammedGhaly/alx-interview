#!/usr/bin/python3
'''
a module containing functions to solve "prime game problem"
'''


def isWinner(x, nums):
    '''
    a function to interpret the winner in the prime game from Maria or Ben"
    '''
    if nums is None or not len(nums) or x == 0:
        return None

    maria_score = 0
    ben_score = 0

    for round in range(x):
        marias_turn = True
        game_nums = [num for num in range(1, nums[round] + 1)]

        while True:
            least_prime = get_least_prime(game_nums)
            if least_prime is None:
                maria_score += int(not marias_turn)
                ben_score += int(marias_turn)
                break
            game_nums = update_game_nums(game_nums, least_prime)
            marias_turn = not marias_turn

    if maria_score > ben_score:
        return 'Maria'
    if maria_score < ben_score:
        return 'Ben'
    return None


def is_prime(n):
    '''
    a function that returns
    True: if n is a prime number
    False: if n is not a prime number
    '''
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_least_prime(nums):
    '''
    a helper function to get the least prime number from a list of integers
    '''
    for num in nums:
        if is_prime(num):
            return num
    return None


def update_game_nums(nums, remove_val):
    '''
    a helper function to remove a chosen number and its
    multiples, and returns a new list of the result
    '''
    new_nums = [num for num in nums if not num % remove_val == 0]
    return new_nums
