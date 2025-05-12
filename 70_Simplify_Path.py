class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)
      
"""
Time Complexity:( O(n) ) — for splitting and processing each segment.
Space Complexity:( O(n) ) — for the stack storing directory names.
"""
