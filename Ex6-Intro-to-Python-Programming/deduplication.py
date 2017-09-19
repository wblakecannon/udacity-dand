'''
Quiz: Deduplication
Write a function, remove_duplicates that takes a list as its argument and returns a new list containing the unique elements of the original list. The elements in the new list without duplicates can be in any order.

Suggested test cases: Try an input list with no duplicate elements. The output list should be the same size as the original list. Try a small input list with a known number of unique entries, and some duplicates. Verify that the list without duplicates has the correct length.
'''
def remove_duplicates(original_list):
    deduplicated_list = []
    for element in original_list:
        if element not in deduplicated_list:
            deduplicated_list.append(element)
    return deduplicated_list

print(remove_duplicates(['Angola', 'Maldives', 'India', 'United States', 'India']))