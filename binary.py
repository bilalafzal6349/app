def binary_search(student_ids, target_id):
    left = 0
    right = len(student_ids) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if student_ids[mid] == target_id:
            return True
        elif student_ids[mid] < target_id:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Example usage
student_ids = [101, 123, 145, 166, 189, 205, 234, 256, 278, 299]
target_id = 111

if binary_search(student_ids, target_id):
    print(f"Student with ID {target_id} is enrolled")
else:
    print(f"Student with ID {target_id} is not enrolled")