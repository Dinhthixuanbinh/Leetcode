class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.get_number_from_list(l1)
        num2 = self.get_number_from_list(l2)

        total = num1 + num2

        result = ListNode(0)
        current = result

        # Convert the total to a linked list
        for digit in str(total)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next

        return result.next

    def get_number_from_list(self, lst):
        """
        Helper function to convert a linked list to an integer.
        """
        result = 0
        multiplier = 1

        while lst:
            result += lst.val * multiplier
            multiplier *= 10
            lst = lst.next

        return result
